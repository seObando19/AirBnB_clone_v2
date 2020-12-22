#!/usr/bin/env bash
#0-setup_web_static

sudo apt update
sudo apt install nginx

sudo mkdir -p /data/ /data/web_static/ /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/
echo "dios bendiga el reaggueton, Amen" | sudo tee -a /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/

config_file=/etc/nginx/sites-available/default
sed -i '29a \ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $config_file
service nginx restart