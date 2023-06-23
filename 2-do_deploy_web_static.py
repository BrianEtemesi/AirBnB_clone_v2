#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""
from fabric.api import env, put, run
from os.path import exists
import os


env.hosts = ['100.25.137.152', '35.168.1.108']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False

    compressed = archive_path.split("/")[-1]
    uncompressed = compressed.split(".")[0]

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/<file>
        remote_folder = "/data/web_static/releases/{}/".format(uncompressed)
        symbolic_conn = "/data/web_static/current"

        run("mkdir -p {}".format(remote_folder))
        run("tar -xvzf /tmp/{} -C {}".format(compressed, remote_folder))
        run("rm /tmp/{}".format(compressed))
        run("mv {}/web_static/* {}".format(remote_folder, remote_folder))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf {}/web_static".format(remote_folder))
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current
        run("ln -sf {} {}".format(remote_folder, symbolic_conn))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed:", str(e))
        return False
