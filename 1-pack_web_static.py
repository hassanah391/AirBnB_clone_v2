#!/usr/bin/python3
"""
Module 1-pack_web_static is fabric script that generates a .tgz archive
from the contents of the web_static folder of your AirBnB Clone repo
using the function:
def do_pack():
- All files in the folder web_static must be added to the final archive
- All archives must be stored in the folder versions
  (your function should create this folder if it doesn’t exist)
- The name of the archive created must be
  web_static_<year><month><day><hour><minute><second>.tgz
- The function do_pack must return the archive path
  if the archive has been correctly generated.
  Otherwise, it should return None
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions/")
        filename = "versions/web_static_{}.tgz".format(time)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except Exception:
        return None
