Summary:	configuration file library
Summary(de):	Library zum Lesen von Konfigurationsdateien
Name:		conflib
Version:	0.4.5
Release:	1
Copyright:	GPL
Group:		Libraries
Source:		ftp://ftp.ohse.de/uwe/releases/conflib-0.4.5.tar.gz
Buildroot:	/tmp/%{name}-%{version}-root
Prereq:		/sbin/install-info /sbin/ldconfig

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
%setup -q

%build
%GNUconfigure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*info* \
	README NEWS ChangeLog

#	$RPM_BUILD_ROOT%{_mandir}/man*/* \

%post
/sbin/ldconfig
/sbin/install-info %{_infodir}/conflib.info.gz %{_infodir}/dir --entry="* Conflib: (conflib.info).         Configuration File Handling."

%postun -p /sbin/ldconfig

%preun
if [ $1 = 0 ]; then
   /sbin/install-info --delete %{_infodir}/history.info.gz %{_infodir}/dir --entry="* Conflib: (conflib.info).         Configuration File Handling."
readline."
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%{_mandir}/*/*
%{_infodir}/*info*
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%doc README.gz NEWS.gz ChangeLog.gz
%{_includedir}/*.h
%{_libdir}/lib*.a
%{_libdir}/lib*.so
