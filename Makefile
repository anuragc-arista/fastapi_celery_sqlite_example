PYTHONVER = python3.9
PYTHONPATH = $(PWD)/.venv/lib/$(PYTHONVER)/site-packages:$(PWD)/.venv/lib64/$(PYTHONVER)/site-packages:/usr/lib/$(PYTHONVER)/site-packages
.venv:
	PIPENV_VENV_IN_PROJECT=1  pipenv install

server : .venv
	PYTHONPATH=$(PYTHONPATH)  python3 main.py

worker: .venv
	echo $(PYTHONPATH)
	PYTHONPATH=$(PYTHONPATH)  python3 .venv/bin/celery -A main.celery worker --loglevel=info -Q fibonacci --concurrency=3
clean : 
	rm -rf *.sqlite
	rm -rf .venv
