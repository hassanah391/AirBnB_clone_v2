#!/usr/bin/python3
"""
Module 2-do_deploy_web_static has
a function do_deploy(archive_path):
that distributes an archive to your web servers
The script should take the following steps:
- Upload the archive to the /tmp/ directory of the web server
- Uncompress the archive to the folder
 /data/web_static/releases/<archive filename without extension>
 on the web server
- Delete the archive from the web server
- Delete the symbolic link /data/web_static/current from the web server
- Create a new the symbolic link /data/web_static/current on the web server,
 linked to the new version of your code
 (/data/web_static/releases/<archive filename without extension>)
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
        sylink = "/data/web_static/current"
        put(archive_path, "/tmp/", mirror_local_mode=True)
        run("mkdir -p {}".format(path_without_ext))
        run("tar -xzf /tmp/{} -C {}".format(filename, path_without_ext))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(path_without_ext, path_whitout_ext))
        run("rm -rf {}web_static".format(path_whitout_ext))
        run("rm -rf {}".format(sylink))
        run("ln -s {} {}".format(path_without_ext, sylink))
        return True

    except Exception:
        return False
