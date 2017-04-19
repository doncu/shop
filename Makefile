BUILDDIR = /tmp/venv_shop
VENVPATH = $(shell pwd)/venv_shop.tar.gz

GITVERSION = $(shell git rev-parse HEAD)


make-venv:
	echo Create venv at $(BUILDDIR)
	virtualenv $(BUILDDIR) -p $(python)
	$(BUILDDIR)/bin/pip install -U pip==9.0.1
	$(BUILDDIR)/bin/pip install --upgrade -r requirements.txt
	echo Build date: $(shell date) > $(BUILDDIR)/INFO
	echo Builder: $(shell hostname -f) >> $(BUILDDIR)/INFO
	echo Git revision: $(GITVERSION) >> $(BUILDDIR)/INFO

	mkdir -p $(BUILDDIR)/configs
	mkdir -p $(BUILDDIR)/app
	cp etc/uwsgi.ini $(BUILDDIR)/configs
	git ls-files | tar -T - -cf - | tar -C "$(BUILDDIR)/app" -xf -

pack-venv: make-venv
	virtualenv --relocatable $(BUILDDIR)
	tar -C $(BUILDDIR) -czf $(VENVPATH) .

clean:
	rm -rf $(BUILDDIR)

create-venv: pack-venv clean