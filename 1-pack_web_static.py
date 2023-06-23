#!/usr/bin/python3
"""
fabric script to generate a .tgz archive
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Create a .tgz archive from the contents of the web_static folder.
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}".format(archive_name)

    local("mkdir -p versions")

    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.succedded:
        return archive_path
    else:
        return None
