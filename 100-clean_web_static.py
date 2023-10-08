#!/usr/bin/python3
"""This is used to clean up the fabric mess"""

from fabric.api import *
import os


env.hosts = ["54.160.68.240", "34.232.71.122"]
env.user = 'ubuntu'


def do_clean(number=0):
    """This is the fabric clean up function"""
    number = 1 if int(number) == 0 else int(number)

    archives_list = os.listdir("versions").sort()
    [archives_list.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(i)) for i in archives_list]

    with cd("/data/web_static/releases"):
        archives_list = run("ls -tr").split()
        archives_list = [a for a in archives_list if "web_static_" in a]
        [archives_list.pop() for i in range(number)]
        [run("rm -fr ./{}".format(i)) for i in archives_list]
