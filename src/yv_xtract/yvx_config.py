import os
import json
from yv_xtract.terminal_utils import print_info, print_processing


class YVXConfig:
    def __init__(self) -> None:
        self.CONFIG_FILE = "yvx_config.json"

    def check_if_config_exists(self) -> bool:
        return os.path.exists(self.CONFIG_FILE)

    def create_config_file(self) -> None:
        print_info("Set a default path to store the downloaded files:")
        path = input()
        print_processing("Creating config file...")
        with open(self.CONFIG_FILE, "w") as f:
            path_to_assign = self.check_path(path)
            json.dump({"default_path": path_to_assign}, f)
        cwd = os.getcwd()
        print_info(f"'{self.CONFIG_FILE}' created successfully at '{cwd}'.")

    def get_default_path(self) -> str:
        with open(self.CONFIG_FILE, "r") as f:
            return json.load(f)["default_path"]

    def update_default_path(self, path: str) -> None:
        print_processing(f"Updating default path to '{path}'...")
        with open(self.CONFIG_FILE, "w") as f:
            json.dump({"default_path": path}, f)
        print_info("Default path updated successfully.")

    def check_path(self, path: str) -> str | None:
        if path is None:
            return None
        path = path.strip()
        if path[0] == '"' and path[-1] == '"':
            path = path[1:-1]
        if path[-1] != "/":
            path += "/"
        return path
