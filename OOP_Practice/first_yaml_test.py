import yaml
from pathlib import Path


def load_and_parse_yaml():
    config_path = Path(__file__).parent / "first_yaml_test.yaml"
    if not config_path.exists():
        print(f"File not found: {config_path}")
        print("Create first_yaml_test.yaml in folder")
        return None
    print(f"=== Reading YAML: {config_path.name} ===\n")

    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    print("File loaded")
    print(f"Data type: {type(config)}")
    print(f"Keys of upper level: {list(config.keys())}\n")
    print(f"Full config list: {list(config.items())}")

    return config


load_and_parse_yaml()
