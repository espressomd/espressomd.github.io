%.html: %.md template.html metadata.yml assets/css/style.css
	pandoc "$<" --template "$<" --metadata-file=metadata.yml | pandoc --template "template.html" --metadata-file=metadata.yml -c "assets/css/style.css" --write=html5 -o "$@"
	@sed -i 's/<\/a> | <a href/<\/a> |\n<a href/g' "$@"

tutorials.md: tutorials.py tutorials_header.md build/doc/tutorials/Readme.md
	python3 "$<"
