SHELL:=/bin/bash
PYTHON=$(shell [ -z "`which python3`" ] && echo "python" || echo "python3")
.PHONY: build deploy clean serve

venv:
	$(PYTHON) -m venv venv && source venv/bin/activate && pip install -r REQUIREMENTS.txt 

build: venv
	( \
		source venv/bin/activate; \
		git pull; \
		pip install -r REQUIREMENTS.txt; \
		mkdocs build; \
	)

serve: build
	(\
	source venv/bin/activate; \
	mkdocs serve; \
	)

deploy: build
	(\
		source venv/bin/activate; \
		mkdocs build; \
		mkdocs gh-deploy; \
		git add site; \
		git commit -m 'auto-committing from Makefile'; \
		git push origin main; \
	)

clean: 
	(\
		rm *.html; \
		rm *.xml; \
		rm -rf blog; \
		rm sitemap.xml.gz; \
		rm src/posts/*~; \
	)

post:
	source venv/bin/activate && python scripts/make_post.py
