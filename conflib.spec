Summary:	Configuration file library
Summary(pl.UTF-8):	Biblioteka plików konfiguracyjnych
Summary(de.UTF-8):	Library zum Lesen von Konfigurationsdateien
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

%description -l pl.UTF-8
Biblioteka C służąca do odczytywania plików konfiguracyjnych.

%package devel
Summary:	Files for developing programs that use the conflib library
Summary(pl.UTF-8):	Pliki do tworzenia programów wykorzystujących bibliotekę conflib
Summary(de.UTF-8):	Dateien zum Entwickeln von Programmen mit der conflib-Library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This library makes it relativly easy to read configuration files (one
or more), or parts of them. It supports a lot of different data types
and some types of text interpretations, including \-escapes, ~user,
$HOME and conditional expansions.

%description devel -l pl.UTF-8
Ta biblioteka pozwala na stosunkowo proste czytanie plików
konfiguracyjnych lub ich części. Wspiera wiele różnych typów danych
oraz niektóre typy interpretacji tekstu, np. \-escapes, ~user, $HOME
oraz warunkowe rozwijanie.

%package static
Summary:	Files for developing programs that use the conflib library
Summary(pl.UTF-8):	Statyczne pliki do tworzenia programów wykorzystujących bibliotekę conflib
Summary(de.UTF-8):	Dateien zum Entwickeln von Programmen mit der conflib-Library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This library makes it relativly easy to read configuration files (one
or more), or parts of them. It supports a lot of different data types
and some types of text interpretations, including \-escapes, ~user,
$HOME and conditional expansions.

%description static -l pl.UTF-8
Ta biblioteka pozwala na stosunkowo proste czytanie plików
konfiguracyjnych lub ich części. Wspiera wiele różnych typów danych
oraz niektóre typy interpretacji tekstu, np. \-escapes, ~user, $HOME
oraz warunkowe rozwijanie. Ten pakiet zawiera pliki statyczne.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

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

%post devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

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
