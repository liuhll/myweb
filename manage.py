#!/usr/bin/env python
import os
import sys
from settings.common import CONFIG_FILE
import ConfigParser

if __name__ == "__main__":

    config = ConfigParser.ConfigParser()
    config.read(CONFIG_FILE)

    current_env = config.get('env','current_env')

    if current_env == "dev":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
