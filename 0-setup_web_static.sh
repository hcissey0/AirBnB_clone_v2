#!/usr/bin/env bash
# This script is used to set up the airbnb clone static page

# check if nginx is installed
if which nginx > /dev/null 2>&1;
then
	echo "nginx installed"
else
	echo "nginx not install"
	sudo apt-get update -y
	sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared

# add hello world to the index.html file
index="/data/web_static/releases/test/index.html"
sudo touch $index
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# now create a symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# giving ownership of /data folder to ubuntu user
sudo chown -R ubuntu:ubuntu /data/

# serving to hbnb_static
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html;
    
    location /hbnb_static {
        alias /data/web_static/current;
	autoindex off;
    }
    location /redirect_me {
        return 301 https://youtube.com;
    }
    error_page 404 /custom_404.html;
    location /404 {
        root /var/www/html;
	internal;
    }
}" | sudo tee /etc/nginx/sites-available/default

# now restart the server
sudo service nginx restart
