Summary: configuration file library
Name: conflib
Version: 0.4.5
Release: 0
Copyright: GPL
Group: Libraries
Source: ftp://ftp.ohse.de/uwe/releases/conflib-0.4.5.tar.gz
Buildroot: /tmp/conflib-buildroot
Prereq: /sbin/install-info /sbin/ldconfig
Summary(de): Library zum Lesen von Konfigurationsdateien

%description 
A C language library for reading configuration files.

%package devel
Summary: file for developing programs that use the conflib library
Group: Development/Libraries
Requires: conflib = %{PACKAGE_VERSION}
Summary(de): Dateien zum Entwickeln von Programmen mit der conflib-Library

%description devel
This library makes it relativly easy to read configuration files (one or
more), or parts of them. It supports a lot of different data types and
some types of text interpretations, including \-escapes, ~user, $HOME
and conditional expansions.

%prep
%setup 

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr
# Uh ... too ugly to describe? Do the people at redhat _really_
# update the specs files manually? Every time?
# ln -sf libconf.so.5.0.1 $RPM_BUILD_ROOT/usr/lib/libconf.so
(cd $RPM_BUILD_ROOT/usr/lib/ ; ln -fs `echo libconf.*.*.*` libconf.so )

gzip -nf9 $RPM_BUILD_ROOT/usr/info/*info*

%post
/sbin/ldconfig
/sbin/install-info /usr/info/conflib.info.gz /usr/info/dir --entry="* Conflib: (conflib.info).         Configuration File Handling."

%postun -p /sbin/ldconfig

%preun
if [ $1 = 0 ]; then
   /sbin/install-info --delete /usr/info/history.info.gz /usr/info/dir --entry="* Conflib: (conflib.info).         Configuration File Handling."
readline."
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
#/usr/man/*/*
/usr/info/*info*
/usr/lib/lib*.so.*

%files devel
%doc README NEWS ChangeLog
/usr/include/*.h
/usr/lib/lib*.a
/usr/lib/lib*.so
