Summary:	configuration file library
Summary(de):	Library zum Lesen von Konfigurationsdateien
Name:		conflib
Version:	0.4.5
Release:	1
Copyright:	GPL
Group:		Libraries
Source:		ftp://ftp.ohse.de/uwe/releases/%{name}-%{version}.tar.gz
Patch:		conflib-info.patch
Prereq:		/sbin/install-info
Buildroot:	/tmp/%{name}-%{version}-root

%description 
A C language library for reading configuration files.

%package devel
Summary:	file for developing programs that use the conflib library
Summary(de):	Dateien zum Entwickeln von Programmen mit der conflib-Library
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This library makes it relativly easy to read configuration files (one or
more), or parts of them. It supports a lot of different data types and
some types of text interpretations, including \-escapes, ~user, $HOME
and conditional expansions.

%package static
Summary:	file for developing programs that use the conflib library
Summary(de):	Dateien zum Entwickeln von Programmen mit der conflib-Library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This library makes it relativly easy to read configuration files (one or
more), or parts of them. It supports a lot of different data types and
some types of text interpretations, including \-escapes, ~user, $HOME
and conditional expansions.

%prep
%setup -q
%patch -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*info* \
	README NEWS ChangeLog

%post
/sbin/ldconfig
/sbin/install-info %{_infodir}/conflib.info.gz /etc/info-dir

%postun -p /sbin/ldconfig

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/conflib.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc README.gz NEWS.gz ChangeLog.gz
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_infodir}/*info*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
