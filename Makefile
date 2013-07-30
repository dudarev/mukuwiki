PROJECT_NAME=mukuwiki
PYTHONPATH=$(CURDIR):$(CURDIR)/$(PROJECT_NAME)

MANAGE= PYTHONPATH=$(PYTHONPATH) python $(PROJECT_NAME)/manage.py

runserver:
	$(MANAGE) runserver --settings=mukuwiki.settings.local

syncdb:
	$(MANAGE) syncdb --settings=mukuwiki.settings.local
