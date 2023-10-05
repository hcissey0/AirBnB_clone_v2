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

defsite="/etc/nginx/sites-available/default"

# serving to hbnb_static
if ! grep -q "location /hbnb_static" "$defsite";
then
	sudo sed -i '/server {/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
fi

# now restart the server
sudo service nginx restart
