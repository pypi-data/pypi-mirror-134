import argparse
import configparser
import re
from ast import literal_eval


class ConfigArgumentParser:
    """Wrapper combining ConfigParser and ArgumentParser.

    Attributes:
        config: A configparser.ConfigParser.
        parser: A argparse.ArgumentParser.
        defaults: A dict contains the default arguments.
        namespace: An object returned by `parser.parse_args`.
        args: A dict contains the parsed arguments.
        help: A dict contains the help messages.
    """

    def __init__(self):
        self._init_config()
        self._init_parser()
        self.defaults = dict()
        self.namespace = object()
        self.args = dict()
        self.help = dict()
        self._comment_prefix = "#"
        self._sect_header_default = self.config.SECTCRE
        self._sect_header_py = re.compile(r"# \[(?P<header>.+)\]")

    def _init_config(self):
        self.config = configparser.ConfigParser(
            allow_no_value=True, delimiters="=", comment_prefixes=";", strict=False
        )
        self.config.optionxform = lambda x: x  # override the default

    def _convert_defaults(self):
        """Convert configuration to `self.defaults` and parse the comments into `self.help`."""
        msg_lst = []
        for key, value in self.config.defaults().items():
            if key.startswith(self._comment_prefix):
                msg = key.lstrip(self._comment_prefix)
                msg = msg.strip()
                msg_lst.append(msg)
            else:
                self.defaults[key] = literal_eval(value)
                self.help[key] = " ".join(msg_lst) if msg_lst else " "
                msg_lst = []

    def read(self, filenames):
        """Read and parse a filename or an iterable of filenames.

        Return list of successfully read files.
        """
        f_lst = self.config.read(filenames)
        self._convert_defaults()
        return f_lst

    def read_string(self, string):
        """Read configuration from a given string."""
        self.config.read_string(string)
        self._convert_defaults()

    def read_py(self, filename):
        """Read and parse a filename of Python script."""
        self.config.SECTCRE = self._sect_header_py
        self.config.read(filename)
        self._convert_defaults()
        self.config.SECTCRE = self._sect_header_default

    def add_arguments(self, shorts=""):
        """Add arguments to parser according to the configuration.

        Args:
            shorts: A sequence of short option letters for the leading options.
        """
        for i, (option, value) in enumerate(self.defaults.items()):
            if i < len(shorts):
                flags = [f"-{shorts[i]}", f"--{option}"]
            else:
                flags = [f"--{option}"]
            if isinstance(value, bool):
                self.parser.add_argument(
                    *flags,
                    action="store_false" if value else "store_true",
                    help=self.help[option],
                )
            else:
                self.parser.add_argument(
                    *flags, default=value, type=type(value), help=self.help[option]
                )

    def _init_parser(self):
        self.parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )

    def parse_args(self, args=None):
        """Convert argument strings to dictionary `self.args`.

        Return a dictionary containing arguments.
        """
        self.namespace = self.parser.parse_args(args)
        self.args = vars(self.namespace)
        return self.args
