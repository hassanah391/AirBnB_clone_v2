#!/usr/bin/env bash
# Sets up web servers for web_static deployment:
# - Installs Nginx if not installed
# - Creates folders:
#   * /data/
#   * /data/web_static/
#   * /data/web_static/releases/
#   * /data/web_static/shared/
#   * /data/web_static/releases/test/
# - Creates test index.html file
# - Creates symbolic link /data/web_static/current -> /data/web_static/releases/test/
# - Sets ownership of /data/ folder to ubuntu user and group recursively
# - Updates Nginx config to serve /data/web_static/current/ at /hbnb_static/
# Usage: sudo ./0-setup_web_static.sh
SOURCE="/data/web_static/releases/test/"
TARGET="/data/web_static/current"
ADD_WEBSTATIC="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"

# Install nginx if not installed
if ! command -v nginx &> /dev/null
then
    sudo apt-get update -y
    sudo apt-get install nginx -y
fi

sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo sh -c 'cat > /data/web_static/releases/test/index.html << EOF
<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>
EOF'

# Check if the symbolic link already exists
if [ -L "$TARGET" ];
then
    sudo rm -f "$TARGET" # Remove the symbolic link
fi

# Create the new symbolic link
sudo ln -sf "$SOURCE" "$TARGET"

# Change owner and group of folder /data/ to ubuntu user/group
sudo chown -hR ubuntu:ubuntu /data/

sudo sed -i "/server_name _;/a $ADD_WEBSTATIC" /etc/nginx/sites-available/default
sudo nginx -t && sudo service nginx reload
