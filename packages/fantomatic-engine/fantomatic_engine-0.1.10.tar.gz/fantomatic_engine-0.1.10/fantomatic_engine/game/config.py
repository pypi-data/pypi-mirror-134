import os
from pathlib import Path
from typing import Optional
from getopt import getopt
import json
import sys


class GameConfig:
    def __init__(self, argv):
        self.app_dir = Path(os.path.abspath(os.path.dirname(__file__))).parent

        self.data_dir = self.make_data_dir()

        opts, _args = getopt(
            argv, "hn:r:", ["game_name=", "resources_dir=", "help"])

        self.arg_opts = opts

        if self.get_opt("h", "help"):
            self.print_help_and_exit()

        conf = self.get_conf()

        self.window_frame = conf.get("window_frame", True)
        self.window_fullscreen = conf.get("window_fullscreen", False)
        self.default_small_window_size = (1000, 600)
        self.window_size = tuple(
            conf.get("window_size", self.default_small_window_size))

        self.lang = conf.get("lang", "en")

        self.game_name = (self.get_opt("n", "game_name")
                          or conf.get("game_name", "Fantomatic Engine"))

        self.resources_dir = (self.get_opt("r", "resources_dir")
                              or conf.get("resources_dir")
                              or self.get_maybe_resources_in_data_dir()
                              or "")

        if self.resources_dir:
            assert os.path.isdir(self.resources_dir), \
                "A valid resources directory path is required. Got: " + \
                str(self.resources_dir)

        self.no_resources = not self.resources_dir

        if self.no_resources:
            print("[WARNING] No game resources were found")

        home_dir = os.path.abspath(Path.home())
        self.save_file = os.path.join(home_dir, ".fantom_quest.save.json")

        self.translations_file = os.path.join(self.data_dir,
                                              "translations.json")

        self.disable_change_resources_dir = conf.get(
            "disable_change_resources_dir", False)

        self.disable_light = conf.get("disable_light", False)

        self.create_default_config_file()

    def get_maybe_resources_in_data_dir(self) -> Optional[str]:
        resources_in_data_dir_path = os.path.join(self.data_dir,
                                                  "resources")
        if os.path.isdir(resources_in_data_dir_path):
            return str(resources_in_data_dir_path)
        return None

    def print_help_and_exit(self):
        lines = [
            " _____",
            "|   __|",
            "|  |_           _____            _____     _",
            "|   _|  /\\  |\\ |  |  /\\ |\\/|  /\\   |   |  /",
            "|__|   /  \\ | \\|  |  \\/ |  | /  \\  |   |  \\_",
            "",
            "FANTOMATIC ENGINE  - Help",
            "Syntax:",
            "python -m fantomatic_engine -r [RESOURCES_DIRECTORY]"
        ]

        for l in lines:
            print(l)

        sys.exit()

    def make_data_dir(self):
        def find_data_dir(root) -> (str, bool):
            data_dir = os.path.join(root, "fantomatic_data")
            return (data_dir, os.path.isdir(data_dir))

        sys_root = os.path.abspath(os.sep)
        exec_env = os.getenv("EXEC_DIR")

        data_dir_path = ""

        for pth in (exec_env, sys_root, self.app_dir):
            if pth:
                (data_dir, exists) = find_data_dir(pth)
                if exists:
                    data_dir_path = data_dir
                    break

        if not data_dir_path:
            data_dir_path = os.path.join(
                exec_env or self.app_dir, "fantomatic_data")

        if not os.path.isdir(data_dir_path):
            os.mkdir(data_dir_path)

        return data_dir_path

    def create_default_config_file(self):
        conf_path = os.path.join(self.data_dir, "config.json")
        if not self.conf_exists():
            default_conf_data = {
                "window_fullscreen": self.window_fullscreen,
                "window_frame": self.window_frame,
                "window_size": self.window_size,
                "resources_dir": self.resources_dir,
                "game_name": self.game_name,
                "lang": self.lang
            }
            self.write_conf(default_conf_data)  # Installation

    def get_conf(self):
        conf_path = os.path.join(self.data_dir, "config.json")
        return json.load(open(conf_path)) if os.path.isfile(conf_path) else dict()

    def conf_exists(self):
        return os.path.isfile(os.path.join(self.data_dir, "config.json"))

    def translations_available(self):
        return os.path.isfile(self.translations_file)

    def write_conf(self, data: dict):
        f = open(os.path.join(self.data_dir, "config.json"), "w")
        f.write(json.dumps(data))

    def write_conf_key(self, key, value):
        conf = self.get_conf()
        conf[key] = value
        self.write_conf(conf)

    def get_opt(self, shortopt, longopt):
        for opt, arg in self.arg_opts:
            if opt in {"-"+shortopt, "--"+longopt}:
                return arg or True
        return None
