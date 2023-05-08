#!/usr/bin/env bash
# setting up server for deployment of web_static

# install Nginx if not installed
if [ -x "$(command -v nginx)" ]
then
	echo "Nginx is already installed"
else
	echo "Installing Nginx..."
	sudo apt-get update
	sudo apt-get install nginx
	echo "Nginx has been successfully installed"
fi

# create necessary folders if they dont exist
keyFolders=("/data/"
			"/data/web_static/"
			"/data/web_static/releases/"
			"/data/web_static/shared/"
			"/data/web_static/releases/test/")

for folder in "${keyFolders[@]}"
do
	if [ ! -d "$folder" ]
	then
		mkdir "$folder"
		echo "created $folder"
	else
		echo "$folder already exists"
	fi
done

# create fake HTML file to test Nginx configuration
echo "Nginx test page" > /data/web_static/releases/test/index.html

# create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current
