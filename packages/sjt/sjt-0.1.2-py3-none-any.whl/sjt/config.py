import dataclasses
import pathlib
import yaml

from sjt.utils import to_path, get_logger

CWD = pathlib.Path.cwd()

LOGGER = get_logger(name="SJT_Init", level='DEBUG')

@dataclasses.dataclass
class SJTConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    INCLUDE_DEFAULTS: bool = False
    LOG_LEVEL: str = 'INFO'
    OMIT_SECTIONS: bool = False
    DATA_DIR: pathlib.Path = CWD.joinpath('data')
    TEMPLATE_DIR: pathlib.Path = CWD.joinpath('templates')
    OUTPUT_DIR: pathlib.Path = CWD.joinpath('output')

    @classmethod
    def from_file(cls, path: pathlib.Path):
        data = None
        with path.open(mode='r') as f:
            data = yaml.safe_load(f)
        instance = SJTConfig()
        if 'config' in data.keys():
            for key, value in data['config'].items():
                if hasattr(instance, key):
                    setattr(instance, key, value)
        return instance


def validate_config(config: SJTConfig):
    print(config)
    LOGGER.info(msg="Validating config...")
    valid = True
    # Resolve paths
    for a in ['DATA_DIR', 'TEMPLATE_DIR']:
        value = getattr(config, a)
        if not isinstance(value, pathlib.Path):
            path = to_path(value)
            if path is not None:
                LOGGER.debug(msg=f"Resolved path for {a}: {value} -> {str(path)}")
                setattr(config, a, path)
            else:
                LOGGER.error(msg=f"Could not resolve path for {a}: {value}. Make sure it is a valid and existing path")

    # Resolve paths and create if necessary
    for a in ['OUTPUT_DIR']:
        value = getattr(config, a)
        if not isinstance(value, pathlib.Path):
            path = to_path(value)
            if path is not None:
                LOGGER.debug(msg=f"Resolved path for {a}: {value} -> {str(path)}")
                setattr(config, a, path)
            else:
                LOGGER.error(msg=f"Value for {a}={value}")
        if isinstance(value, pathlib.Path):
            if not value.exists():
                LOGGER.info(msg=f"Creating output directory: {str(value)}")
                value.mkdir(exist_ok=True)
    return valid
