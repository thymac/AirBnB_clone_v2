#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static

# Update and install Nginx
sudo apt-get update
sudo apt-get install -y nginx
sudo service nginx start

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "Test File" | sudo tee /data/web_static/releases/test/index.html

# Create or update symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership of directories to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/^http {/a\    location /hbnb_static/ {\n        alias /data/web_static/current/;\n    }' /etc/nginx/nginx.conf

# Restart Nginx
sudo service nginx restart

