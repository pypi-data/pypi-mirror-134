#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file sets up and configures Django. It's used by scripts that need to
execute as if running in a Django server.
"""


import subprocess

import django
from django.conf import settings


def test():
    # print(dir(BASE_DIR))
    # print("Yo")
    p = subprocess.run(["pwd"], capture_output=True, text=True)
    return(p.stdout.strip())


# def boot_django(installed_apps: list):
#
#     settings.configure(
#         BASE_DIR=BASE_DIR,
#         DEBUG=True,
#         DATABASES={
#             "default": {
#                 "ENGINE": "django.db.backends.sqlite3",
#                 "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#             }
#         },
#         INSTALLED_APPS=installed_apps,
#         TIME_ZONE="UTC",
#         USE_TZ=True,
#     )
#
#     django.setup()
#     print(BASE_DIR)

if __name__ == "__main__":
    # boot_django()
    test()
