from dataclasses import dataclass
import yaml, os


@dataclass
class DBConfig:
    db_name: str

@dataclass
class Config:
    db_config: DBConfig
    static_file_dir: str

    @classmethod
    def init_from_yaml(cls, path: str):
        try:
            with open(path, 'r') as file:
                config = yaml.safe_load(file)

                db_config = DBConfig(
                    db_name=config["database"]["db_name"],
                )
                static_dir = config["static_dir"]

            return cls(
                db_config=db_config,
                static_file_dir=static_dir
            )
        except Exception as e:
            raise Exception(f'Unable to load config from yaml: {e}')


current_dir = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(current_dir, "config.yaml")

app_config = Config.init_from_yaml(config_path)
