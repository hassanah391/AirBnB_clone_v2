#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to the web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
import os

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with your server IPs


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        # Create the versions directory if it doesn't exist
        local("mkdir -p versions")
        
        # Create the archive name using the current timestamp
        now = datetime.now()
        archive_name = "versions/web_static_{}.tgz".format(
            now.strftime("%Y%m%d%H%M%S"))
        
        # Create the archive
        local("tar -cvzf {} web_static".format(archive_name))
        
        # Return the archive path if successful
        if os.path.exists(archive_name):
            return archive_name
    except:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Get the filename and folder name from the archive path
        file_name = archive_path.split("/")[-1]
        folder_name = file_name.replace(".tgz", "")
        folder_path = "/data/web_static/releases/{}".format(folder_name)
        
        # Upload the archive to /tmp/ directory
        put(archive_path, "/tmp/{}".format(file_name))
        
        # Create the folder to store the new version
        run("mkdir -p {}".format(folder_path))
        
        # Extract the archive
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        
        # Remove the archive
        run("rm /tmp/{}".format(file_name))
        
        # Move the files from web_static to the new folder
        run("mv {}/web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}/web_static".format(folder_path))
        
        # Remove current symbolic link and create new one
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """
    Creates and distributes an archive to the web servers
    """
    # Create the archive
    archive_path = do_pack()
    if not archive_path:
        return False
        
    # Deploy the archive
    return do_deploy(archive_path)
