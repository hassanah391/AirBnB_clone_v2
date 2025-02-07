#!/usr/bin/python3
"""
Module 2-do_deploy_web_static has
a function do_deploy(archive_path):
that distributes an archive to your web servers
"""
from fabric.api import put, env, sudo, run
import os.path


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

        # Copy files to proper location with sudo
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

        # Set proper permissions
        if sudo("chown -R ubuntu:ubuntu /data/web_static/releases/{}".format(
                name)).failed:
            return False

        # Add Nginx configuration
        nginx_conf = (
            "server {\n"
            "    listen 80 default_server;\n"
            "    listen [::]:80 default_server;\n"
            "    add_header X-Served-By $hostname;\n"
            "    root /var/www/html;\n"
            "    index index.html index.htm;\n\n"
            "    location /hbnb_static/ {\n"
            "        alias /data/web_static/current/;\n"
            "        index index.html index.htm;\n"
            "    }\n"
            "    location /redirect_me {\n"
            "        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n"
            "    }\n"
            "    error_page 404 /404.html;\n"
            "    location = /404.html {\n"
            "        root /var/www/html;\n"
            "        internal;\n"
            "    }\n"
            "}\n"
        )

        # Write the complete Nginx configuration
        if sudo("echo '{}' > /etc/nginx/sites-available/default".format(
                nginx_conf)).failed:
            return False

        # Test Nginx configuration
        if sudo("nginx -t").failed:
            return False

        # Restart Nginx
        if sudo("service nginx restart").failed:
            return False

        print("New version deployed!")
        return True

    except Exception:
        return False
