#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yum-utils
Version  : 1.1.31
Release  : 17
URL      : http://yum.baseurl.org/download/yum-utils/yum-utils-1.1.31.tar.gz
Source0  : http://yum.baseurl.org/download/yum-utils/yum-utils-1.1.31.tar.gz
Summary  : Utilities based around the yum package manager
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: yum-utils-bin
Requires: yum-utils-legacypython
Requires: yum-utils-locales
Requires: yum-utils-doc
BuildRequires : python-dev
Patch1: 0001-Add-ovl-plugin.patch

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

%description bin
bin components for the yum-utils package.


%package doc
Summary: doc components for the yum-utils package.
Group: Documentation

%description doc
doc components for the yum-utils package.


%package legacypython
Summary: legacypython components for the yum-utils package.
Group: Default

%description legacypython
legacypython components for the yum-utils package.


%package locales
Summary: locales components for the yum-utils package.
Group: Default

%description locales
locales components for the yum-utils package.


%prep
%setup -q -n yum-utils-1.1.31
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505074392
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1505074392
rm -rf %{buildroot}
%make_install
%find_lang yum-utils
## make_install_append content
install -D -m 644 plugins/ovl/ovl.py %{buildroot}/usr/lib/yum-plugins/ovl.py
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib/yum-plugins/ovl.py
/usr/lib/yum-plugins/ovl.pyc
/usr/lib/yum-plugins/ovl.pyo

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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files locales -f yum-utils.lang
%defattr(-,root,root,-)

