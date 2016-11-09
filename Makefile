check:
	appstreamcli validate org.kde.development.appdata.xml

arch: archlinux/PKGBUILD.in ./archlinux/genpkgbuild.py
	mkdir -p archlinux-output/
	./archlinux/genpkgbuild.py
