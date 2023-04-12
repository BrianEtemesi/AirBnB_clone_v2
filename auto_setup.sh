#!/usr/bin/env bash
# creates necessary folders if they dont exist

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
