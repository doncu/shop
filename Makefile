BUILDDIR = /tmp/venv_shop
VENVNAME = venv_shop.tar.gz
VENVPATH = $(shell pwd)/$(VENVNAME)

GITVERSION = $(shell git rev-parse HEAD)

REMOTE_SSH = root@mzhv.ru


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

upload-venv: create-venv
	scp $(VENVPATH) $(REMOTE_SSH):/tmp/
	ssh $(REMOTE_SSH) "tar -zxvf /tmp/$(VENVNAME) -C /root/venv_shop-$(GITVERSION); ln -s /root/venv_shop /root/venv_shop-$(GITVERSION); supervisorctl reread; supervisorctl update; supervisorctl restart shop"