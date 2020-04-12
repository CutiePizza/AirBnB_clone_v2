#!/usr/bin/env bash
# Instalation
sudo apt-get -y update
sudo apt-get -y install nginx
sudo servce nginx start
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo -e "<html>\n<head></head>\n<body>\nHolberton School\n</body>\n</html>" >> /data/web_static/releases/test/index.html
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
config="\\\nlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}"
sudo sed -i "20i $config" /etc/nginx/sites-enabled/default
sudo service nginx restart
