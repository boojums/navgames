#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    # Add apps/ to path
    sys.path[0:0] = [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "apps")
    ]


    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "navgames.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
