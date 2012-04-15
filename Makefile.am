## Process this file with automake to produce Makefile.in
## Created by Anjuta

SUBDIRS = src 

greaverdocdir = ${prefix}/doc/greaver
greaverdoc_DATA = \
	README\
	COPYING\
	AUTHORS\
	ChangeLog\
	INSTALL\
	NEWS


EXTRA_DIST = $(greaverdoc_DATA)


# Remove doc directory on uninstall
uninstall-local:
	-rm -r $(greaverdocdir)
