#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""
from fabric.api import env, put, run
from os.path import exists
import os


env.hosts = ['100.25.137.152', '35.168.1.108']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/<archive filename without extension>
        archive_filename = os.path.basename(archive_path)
        folder_name = '/data/web_static/releases/' + os.path.splitext(archive_filename)[0]
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, folder_name))
        run('rm /tmp/{}'.format(archive_filename))

        # Delete the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current linked to the new version
        run('ln -s {} /data/web_static/current'.format(folder_name))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed:", str(e))
        return False
