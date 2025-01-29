#!/usr/bin/python3
"""
Module 2-do_deploy_web_static has
a function do_deploy(archive_path):
that distributes an archive to your web servers
"""
from fabric.api import run, put, env
import os.path

env.user = "ubuntu"
env.hosts = ['100.26.246.61', '54.237.93.3']

def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if os.path.isfile(archive_path) is False:
        return False
    try:
        filename = archive_path.split('/')[-1]
        without_ext = filename.split('.')[0]
        path_without_ext = "/data/web_static/releases/{}".format(without_ext)
        symlink = "/data/web_static/current"
        
        # Upload the archive
        put(archive_path, "/tmp/{}".format(filename))
        print("Archive uploaded successfully")
        
        # Create the release directory
        run("sudo mkdir -p {}".format(path_without_ext))
        print("Release directory created")
        
        # Extract archive
        run("sudo tar -xzf /tmp/{} -C {}".format(filename, path_without_ext))
        print("Archive extracted")
        
        # Clean up the uploaded archive
        run("sudo rm /tmp/{}".format(filename))
        print("Cleaned up archive")
        
        # Move contents and ensure permissions
        run("sudo chown -R ubuntu:ubuntu {}".format(path_without_ext))
        run("cd {} && cp -r web_static/* .".format(path_without_ext))
        run("sudo rm -rf {}/web_static".format(path_without_ext))
        print("Contents moved and permissions set")
        
        # Update symbolic link
        run("sudo rm -rf {}".format(symlink))
        run("sudo ln -sf {} {}".format(path_without_ext, symlink))
        print("Symbolic link updated")
        
        # Verify deployment
        run("ls -la {}".format(symlink))
        run("ls -la {}/".format(path_without_ext))
        
        return True
    except Exception as e:
        print("Deployment failed:", e)
        return False
