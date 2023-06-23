#!/usr/bin/env bash
# setting up server for deployment of web_static

# install Nginx if not installed
if [ -x "$(command -v nginx)" ]
then
	echo "Nginx is already installed"
else
	echo "Installing Nginx..."
	sudo apt-get update
	sudo apt-get install nginx -y
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
		sudo mkdir "$folder"
		echo "created $folder"
	else
		echo "$folder already exists"
	fi
done

# create fake HTML file to test Nginx configuration
echo "Nginx test page" > sudo tee /data/web_static/releases/test/index.html

# create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# change ownership of the /data/ folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Add an alias to serve the content of /data/web_static/current/ to hbnb_static
nginx_config_path="/etc/nginx/sites-available/default"
sudo sed -i '/listen 80 default_server;/a \ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' "$nginx_config_path"

# restart nginx to apply changes
sudo service nginx restart
