import sys
import pathlib
import logging
import argparse

CWD = pathlib.Path.cwd()

def get_logger(name='SJT', level=logging.INFO, handle=["stderr"]) -> logging.Logger:
    # formatter_string = '[%(asctime)s] [%(levelname)s]\t[%(name)s][%(module)s][%(funcName)s]\t%(message)s'
    formatter_string = '[%(asctime)s] [%(levelname)s]\t%(message)s'


    logfile_path = CWD.joinpath('sjt.log')
    formatter = logging.Formatter(formatter_string)
    stdout_handler = logging.StreamHandler(sys.stdout)
    stderr_handler = logging.StreamHandler(sys.stderr)
    file_handler = logging.FileHandler(logfile_path, delay=True)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    handlers = []
    if "stderr" in handle:
        handlers.append(stderr_handler)
    if "stdout" in handle:
        handlers.append(stdout_handler)


    for handler in handlers:
        handler.setFormatter(formatter)
        try:
            handler.setLevel(level)
        except KeyError:
            handler.setLevel(logging.INFO)

    root = logging.getLogger(name)
    root.propagate = 0
    root.setLevel(logging.DEBUG)
    has_handler = {"file_handler": False, "stderr_handler": False, "stdout_handler": False}
    for handler in root.handlers:
        if isinstance(handler, logging.FileHandler):
            has_handler["file_handler"] = True
        if isinstance(handler, logging.StreamHandler):
            has_handler["stderr_handler"] = True
    if not has_handler["file_handler"]:
        root.addHandler(file_handler)
    if not has_handler["stderr_handler"]:
        root.addHandler(stderr_handler)
    return root

def list_str(values):
    return [x.strip() for x in values.split(',')]

def get_cwd():
    path = pathlib.Path.cwd().joinpath('.sjt.yml')
    if path.exists() and path.is_file():
        return path
    else:
        return pathlib.Path.cwd()

def to_path(path_str: str):
    print(path_str)
    path = None
    path_candidate = pathlib.Path(path_str).resolve()
    print(path_candidate)
    if path_candidate.exists():
        path = path_candidate
    else:
        path_candidate = CWD.joinpath(path_str)
        if path_candidate.exists():
            path = path_candidate
    return path


def handle_args():
    global log
    parser = argparse.ArgumentParser(
        formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=50)
    )
    parser.add_argument(
        '--config-file',
        help="Path to the config file",
        dest='config_file',
        default='.sjt.yml',
        type=to_path
    )
    parser.add_argument(
        '-d',
        '--data-file',
        help="Name of the data file inside ./data/ directory",
        dest='data_file',
        required=True
    )
    parser.add_argument(
        '-D',
        '--include-defaults',
        help="When specified, template render will include default config lines (not visible in show running-config)",
        dest='include_defaults',
        action='store_true',
        default=False
    )
    parser.add_argument(
        '--omit-sections',
        help="When specified, template render will not include section desctiptions",
        dest='omit_sections',
        action='store_true',
        default=False
    )
    parser.add_argument(
        '-l',
        '--limit',
        help="Limit Config Rendering only to these comma-separated hosts",
        dest='limit',
        type=list_str,
        default=None
    )
    parser.add_argument(
        '-v',
        '--log-level',
        dest='log_level',
        type=str,
        choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'],
        default=None
    )
    parser.add_argument(
        '-t',
        '--template-name',
        dest='template_name',
        type=str,
        required=True
    )
    args = parser.parse_args()
    return args
