#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yum-utils
Version  : 1.1.31
Release  : 8
URL      : http://yum.baseurl.org/download/yum-utils/yum-utils-1.1.31.tar.gz
Source0  : http://yum.baseurl.org/download/yum-utils/yum-utils-1.1.31.tar.gz
Summary  : Utilities based around the yum package manager
Group    : Development/Tools
License  : GPL-2.0+ GPL-2.0
Requires: yum-utils-config
Requires: yum-utils-bin
Requires: yum-utils-python
Requires: yum-utils-locales
Requires: yum-utils-doc
BuildRequires : python-dev

%description
yum-utils is a collection of utilities and examples for the yum package
manager. It includes utilities by different authors that make yum easier and
more powerful to use. These tools include: debuginfo-install, 
find-repos-of-install, needs-restarting, package-cleanup, repoclosure, 
repodiff, repo-graph, repomanage, repoquery, repo-rss, reposync,
repotrack, show-installed, show-changed-rco, verifytree, yumdownloader,
yum-builddep, yum-complete-transaction, yum-config-manager, yum-debug-dump,
yum-debug-restore and yum-groups-manager.

%package bin
Summary: bin components for the yum-utils package.
Group: Binaries
Requires: yum-utils-config

%description bin
bin components for the yum-utils package.


%package config
Summary: config components for the yum-utils package.
Group: Default

%description config
config components for the yum-utils package.


%package doc
Summary: doc components for the yum-utils package.
Group: Documentation

%description doc
doc components for the yum-utils package.


%package locales
Summary: locales components for the yum-utils package.
Group: Default

%description locales
locales components for the yum-utils package.


%package python
Summary: python components for the yum-utils package.
Group: Default

%description python
python components for the yum-utils package.


%prep
%setup -q -n yum-utils-1.1.31

%build
make V=1 %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
%find_lang yum-utils

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/debuginfo-install
/usr/bin/find-repos-of-install
/usr/bin/needs-restarting
/usr/bin/package-cleanup
/usr/bin/repo-graph
/usr/bin/repo-rss
/usr/bin/repoclosure
/usr/bin/repodiff
/usr/bin/repomanage
/usr/bin/repoquery
/usr/bin/reposync
/usr/bin/repotrack
/usr/bin/show-changed-rco
/usr/bin/show-installed
/usr/bin/verifytree
/usr/bin/yum-builddep
/usr/bin/yum-complete-transaction
/usr/bin/yum-config-manager
/usr/bin/yum-debug-dump
/usr/bin/yum-debug-restore
/usr/bin/yum-groups-manager
/usr/bin/yumdb
/usr/bin/yumdownloader

%files config
%defattr(-,root,root,-)
%exclude /etc/NetworkManager/dispatcher.d/yum-NetworkManager-dispatcher
%exclude /etc/bash_completion.d/yum-utils.bash

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

%files locales -f yum-utils.lang 
%defattr(-,root,root,-)

