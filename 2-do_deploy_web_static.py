#!/usr/bin/python3
"""
Module 2-do_deploy_web_static has
a function do_deploy(archive_path):
that distributes an archive to your web servers
"""
from fabric.api import put, env, sudo
import os.path

# Define the list of host servers
env.hosts = ['100.26.246.61', '54.237.93.3']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    Args:
        archive_path: path to the archive to deploy
    Returns:
        True if all operations have been done correctly, False otherwise
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Get filename without path
        filename = os.path.basename(archive_path)
        # Get name without extension
        name = filename.split('.')[0]

        # Upload archive to /tmp/ directory
        if put(archive_path, "/tmp/{}".format(filename)).failed:
            return False

        # Create release directory using sudo
        if sudo("mkdir -p /data/web_static/releases/{}/".format(name)).failed:
            return False

        # Uncompress archive with sudo
        if sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
                filename, name)).failed:
            return False

        # Remove archive
        if sudo("rm /tmp/{}".format(filename)).failed:
            return False

        # Copy files to proper location with sudo (using cp -r instead of mv)
        if sudo("cp -r /data/web_static/releases/{}/web_static/* "
               "/data/web_static/releases/{}/".format(name, name)).failed:
            return False

        # Remove the web_static directory
        if sudo("rm -rf /data/web_static/releases/{}/web_static".format(
                name)).failed:
            return False

        # Remove symbolic link
        if sudo("rm -rf /data/web_static/current").failed:
            return False

        # Create new symbolic link
        if sudo("ln -s /data/web_static/releases/{}/ /data/web_static/current"
               .format(name)).failed:
            return False

        print("New version deployed!")
        return True

    except Exception:
        return False
