## Process this file with automake to produce Makefile.in
## Created by Anjuta


uidir = $(datadir)/greaver/ui
ui_DATA = greaver2.ui


## The main script
bin_SCRIPTS = greaver.py

## Directory where .class files will be installed
greaverdir = $(pythondir)/greaver


greaver_PYTHON = \
	greaver.py \
	interfaces.py


EXTRA_DIST = $(ui_DATA)


# Remove ui directory on uninstall
uninstall-local:

	-rm -r $(uidir)

	-rm -r $(datadir)/greaver
