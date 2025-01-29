#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

# Define variables
SOURCE="/data/web_static/releases/test"
TARGET="/data/web_static/current"
NGINX_CONFIG="/etc/nginx/sites-available/default"
ADD_WEBSTATIC="\\\tlocation /hbnb_static {\n\t\talias $SOURCE/;\n\t}\n"

# Install nginx if not installed
if ! command -v nginx &> /dev/null
then
    sudo apt-get update -y
    sudo apt-get install nginx -y
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create test HTML file
sudo bash -c 'cat > /data/web_static/releases/test/index.html << EOF
<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>
EOF'

# Remove symbolic link if it exists and create new one
if [ -L "$TARGET" ]
then
    sudo rm -f "$TARGET"
fi
sudo ln -sf "$SOURCE" "$TARGET"

# Set ownership
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration if location block doesn't exist
if ! grep -q "location /hbnb_static" "$NGINX_CONFIG"; then
    sudo sed -i "/server_name _;/a $ADD_WEBSTATIC" "$NGINX_CONFIG"
fi

# Test Nginx configuration and restart
sudo nginx -t && sudo service nginx restart

exit 0
