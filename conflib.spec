Summary:	Configuration file library
Summary(pl):	Biblioteka plików konfiguracyjnych
Summary(de):	Library zum Lesen von Konfigurationsdateien
Name:		conflib
Version:	0.4.5
Release:	7
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.ohse.de/uwe/releases/%{name}-%{version}.tar.gz
# Source0-md5:	301f140d0fbd0b5a225419c101c4c9d1
Patch0:		%{name}-info.patch
Patch1:		%{name}-cl_build_stanza_array-fix.patch
Patch2:		%{name}-ac25x.patch
Patch3:		%{name}-locale.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A C language library for reading configuration files.

%description -l pl
Biblioteka C s³u¿±ca do odczytywania plików konfiguracyjnych.

%package devel
Summary:	Files for developing programs that use the conflib library
Summary(pl):	Pliki do tworzenia programów wykorzystuj±cych bibliotekê conflib
Summary(de):	Dateien zum Entwickeln von Programmen mit der conflib-Library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This library makes it relativly easy to read configuration files (one
or more), or parts of them. It supports a lot of different data types
and some types of text interpretations, including \-escapes, ~user,
$HOME and conditional expansions.

%description devel -l pl
Ta biblioteka pozwala na stosunkowo proste czytanie plików
konfiguracyjnych lub ich czê¶ci. Wspiera wiele ró¿nych typów danych
oraz niektóre typy interpretacji tekstu, np. \-escapes, ~user, $HOME
oraz warunkowe rozwijanie.

%package static
Summary:	Files for developing programs that use the conflib library
Summary(pl):	Statyczne pliki do tworzenia programów wykorzystuj±cych bibliotekê conflib
Summary(de):	Dateien zum Entwickeln von Programmen mit der conflib-Library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This library makes it relativly easy to read configuration files (one
or more), or parts of them. It supports a lot of different data types
and some types of text interpretations, including \-escapes, ~user,
$HOME and conditional expansions.

%description static -l pl
Ta biblioteka pozwala na stosunkowo proste czytanie plików
konfiguracyjnych lub ich czê¶ci. Wspiera wiele ró¿nych typów danych
oraz niektóre typy interpretacji tekstu, np. \-escapes, ~user, $HOME
oraz warunkowe rozwijanie. Ten pakiet zawiera pliki statyczne.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_infodir}/*info*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
