import pathlib
import jinja2
import yaml
from sjt.config import SJTConfig
from sjt.utils import get_logger
import dataclasses


class Render:

    def __init__(self, config: SJTConfig = None):
        self.config = config or SJTConfig()
        self.logger = get_logger(name="SJT", level=config.LOG_LEVEL)
        self.logger.debug(msg=f"Initializing Renderer with config: {dataclasses.asdict(self.config)}")
        self.env: jinja2.Environment = None
        self.data: dict = None


    def get_jinja_env(self) -> jinja2.Environment:
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(
                searchpath=self.config.TEMPLATE_DIR
            ),
            autoescape=True,
            trim_blocks=True,
            lstrip_blocks=True,
            undefined=jinja2.runtime.StrictUndefined,
            newline_sequence='\n'
        )
        self.env = env

    def get_template(self, template_name: str) -> jinja2.Template:

        template = self.env.get_template(name=template_name)
        return template

    def load_data(self, filename: str):
        self.logger.info(msg=f"Loading data from {filename}")
        raw_data = None
        data = list()
        with self.config.DATA_DIR.joinpath(filename).open() as f:
            raw_data = yaml.safe_load(stream=f)
        # Extend Host Data with common_config
        for host in raw_data['hosts']:
            host_data = dict(raw_data['common_config'])
            host_data.update(host)
            data.append(host_data)
        return data


    def render(self, template_name: str, data: dict) -> str:
        template = self.get_template(template_name=template_name)
        output = template.render(**dataclasses.asdict(self.config), **data)
        return output

    def store_output(self, output: str, filename: str) -> None:
        with self.config.OUTPUT_DIR.joinpath(filename).open(mode='w') as f:
            f.write(output)

    def run(self, data_file: str, template_name: str) -> None:
        self.get_jinja_env()
        if self.data is None:
            self.data = self.load_data(filename=data_file)
        for host in self.data:
            output = self.render(template_name=template_name, data=host)
            self.store_output(output=output, filename=host['name'])



