#!/usr/bin/env bash
# This script is used to set up the airbnb clone static page

# check if nginx is installed
if which nginx > /dev/null 2>&1;
then
	echo "nginx installed"
else
	echo "nginx not install"
fi

dataf="/data/"
web_staticf="/data/web_static/"
releasesf="/data/web_static/releases/"
sharedf="/data/web_static/shared/"
testf="/data/web_static/releases/test/"

# create array of folders
folders=("$dataf" "$web_staticf" "$releasesf" "$sharedf" "$testf")

# loop through and check if not available then create
for folder in "${folders[@]}";
do
	if [ -d "$folder" ];
	then
		echo "The folder $folder exists"
	else
		echo "The folder $folder does not exist"
		echo "Creating the $folder folder"
		sudo mkdir -p "$folder"
		echo "$folder created successfully"
	fi
done

# add hello world to the index.html file
index="/data/web_static/releases/test/index.html"
sudo touch $index
echo "Holberton School" | sudo tee $index

# now create a symbolic link
sudo ln -sf "$testf" "/data/web_static/current"

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
