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

# create folder /data/ if it doesnt already exist
if [ ! -d "/data/" ]
then
	mkdir /data/
	echo "Created /data/ folder"
else
	echo "/data/ folder already exists"
fi

# create folder /data/web_static/ if doesnt exist
if [ ! -d "/data/web_static/" ]
then
	mkdir /data/web_static/
	echo "created /data/web_static/ folder"
else
	echo "/data/web_static/ folder already exists"
fi

# create folder /data/web_static/releases/ if it doesnt exist
if [ ! -d "/data/web_static/releases/" ]
then
	mkdir /data/web_static/releases/
	echo "created /data/web_static/releases/ folder"
else
	echo "/data/web_static/releases/ folder already exists"
fi

# create folder /data/web_static/shared/ if it doesnt exist
if [ ! -d "/data/web_static/shared/" ]
then
	mkdir /data/web_static/shared/
	echo "/data/web_static/shared/ folder created"
else
	echo "/data/web_static/shared/ already exists"
fi
















