#!/usr/bin/env bash
# Installation
if ! which nginx > /dev/null 2>&1; then
sudo apt-get -y update
sudo apt-get -y install nginx
sudo servce nginx start
fi
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo -e "<html>\n<head></head>\n<body>\nHolberton School\n</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
if [ -e "/data/web_static/current" ]; then
	sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
old_config="server {"
new_config="\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/\;\n\t}\n"
sudo sed -i "s/^$old_config/$old_config$new_config/" /etc/nginx/sites-enabled/default
sudo service nginx restart
