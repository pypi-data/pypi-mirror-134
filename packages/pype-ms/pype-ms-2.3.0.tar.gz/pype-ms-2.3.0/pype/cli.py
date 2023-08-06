import importlib
import inspect
import os
import pprint
import shutil
import socket

import click
import yaml
from pype import utils
from pype.log import get_logger
from pype.status import Status


@click.group()
def cli():
    pass


@cli.command()
@click.option("--tag", "-t", default="", help="only run configs with the tag")
@click.option("--force", "-f", default=False, is_flag=True)
@click.option("--scratch", "-f", default=None)
@click.argument("config")
def run(config, tag, force, scratch):
    run_(config, tag, force=force, scratch=scratch)


def run_(config, tag, force=False, scratch=None):
    if isinstance(config, str):
        assert config.endswith("yaml"), "Configuration file must be YAML"
        config = yaml.load(open(config, "r"), Loader=yaml.FullLoader)

    if isinstance(config, list):
        for config_ in config:
            run_(config_, tag, force=force, scratch=scratch)

    else:
        status = Status(config["job_dir"])
        if tag:
            if not tag in config.get("tag", ""):
                return

        if force:
            pass

        elif status.status == "Running" or status.status == "Done":
            print(
                f"{config['job_id']} was skipped because status is {status.status} ... "
            )
            return


        output_dir = os.path.join(config["job_dir"], "output")
        if os.path.islink(output_dir):
            os.remove(output_dir)
            os.makedirs(output_dir)

        if scratch:
            scratch_output_dir = os.path.join(scratch, config["job_id"])
            os.makedirs(scratch_output_dir, exist_ok=True)
            shutil.rmtree(output_dir)
            os.symlink(scratch_output_dir, output_dir)

        print(f"{config['job_id']} is running")
        run_job(config)

        if scratch:
            os.remove(output_dir)
            shutil.copytree(scratch_output_dir, output_dir)
            shutil.rmtree(scratch_output_dir)


def run_job(config):
    job_dir = config["job_dir"]
    log_file = os.path.join(job_dir, "file.log")
    logger = get_logger(config["job_id"], log_file)
    status = Status(job_dir)

    msg = running_job_msg(config)
    logger.info(msg)
    utils.save_git_sha(job_dir)

    status.running()

    try:
        module = _import_module(config["script_path"])
        if not hasattr(module, "main"):
            raise RuntimeError(f"{config['script_path']} has no main function.")

        if (
            "logger" in inspect.getargspec(module.main).args
        ):  # pylint: disable=deprecated-method
            module.main(config, logger)
        else:
            module.main(config)
        status.done()
        logger.info("job terminated succesfully.\n\n-\n")

    except Exception:  # pylint: disable=broad-except
        status.failed()
        logger.exception("Exception occurred: \n\n")


def running_job_msg(config):
    space = 4 * " "

    msg = f"Running job {config['job_id']}"
    hashs = (2 * len(space) + len(msg)) * "#" + ""

    full_msg = f"\n{hashs}\n{'    '+msg}\n{hashs}\n\n"
    full_msg += "Host: " + socket.gethostname() + "\n"
    full_msg += "PID: " + str(os.getpid()) + "\n"
    full_msg += "gitsha: " + str(utils.get_git_sha()) + 2 * "\n"
    full_msg += "Configuration:\n"

    full_msg += pprint.pformat(config)
    length = max([len(l) for l in pprint.pformat(config).split("\n")])
    full_msg += 2 * "\n" + length * "_" + "\n"

    return full_msg


def permission_to_continue(msg):
    return input(msg + "Type 'y' or 'yes' to continue anyways\n").lower() in [
        "y",
        "yes",
    ]


def _import_module(path):
    spec = importlib.util.spec_from_file_location("module.name", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def _uncomitted():
    if not utils.GIT_CONTROL:
        return False

    cmd = r"git status | grep -q '\smodified:\s'"
    code = os.system(cmd)
    return code == 0
