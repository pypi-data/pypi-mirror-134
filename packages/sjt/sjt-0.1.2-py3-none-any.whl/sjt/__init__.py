from sjt.config import SJTConfig, validate_config
from sjt.utils import handle_args, to_path
from sjt.sjt import Render
import dataclasses

def run():
    args = handle_args()

    config = None
    if args.config_file is not None:
        print(f"Config File: {args.config_file}")
        if not args.config_file.exists() or not args.config_file.exists():
            print(f"Specified config file {args.config_file} does not exist, fallback to default.")
        else:
            config = SJTConfig.from_file(args.config_file)
    else:
        print("No config file found, using defaults.")

    if config is None:
        config = SJTConfig()


    if args.log_level is not None:
        config.LOG_LEVEL = args.log_level

    validate_config(config=config)
    # print(config)
    r = Render(config=config)
    r.run(data_file=args.data_file, template_name=args.template_name)