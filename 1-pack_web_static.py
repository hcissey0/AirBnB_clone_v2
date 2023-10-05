#!/usr/bin/python3
"""This script is used as a fabfile"""

import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """This fucntion is used as the fabric command to pack the files"""
    date = datetime.now()
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            date.year, date.month, date.day,
            date.hour, date.minute, date.second)
    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed is True:
            return None
    if
