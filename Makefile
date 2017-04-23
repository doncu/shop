BUILDDIR = /tmp/venv_shop
VENVNAME = venv_shop.tar.gz
VENVPATH = $(shell pwd)/$(VENVNAME)

GITVERSION = $(shell git rev-parse HEAD)

REMOTE_SSH = branch@92.53.97.207


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
	scp -P 18206 $(VENVPATH) $(REMOTE_SSH):/tmp/
	ssh $(REMOTE_SSH) -p 18206 "sudo mkdir -p /root/venv_shop-$(GITVERSION); sudo tar -zxvf /tmp/$(VENVNAME) -C /root/venv_shop-$(GITVERSION); sudo ln -s /root/venv_shop-$(GITVERSION) /root/venv_shop; sudo supervisorctl reread; sudo supervisorctl update; sudo supervisorctl restart shop"