Summary:	Configuration file library
Summary(pl):	Biblioteka plik�w konfiguracyjnych
Summary(de):	Library zum Lesen von Konfigurationsdateien
Name:		conflib
Version:	0.4.5
Release:	5
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	����������
Group(uk):	��̦�����
Source0:	ftp://ftp.ohse.de/uwe/releases/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-cl_build_stanza_array-fix.patch
Patch2:		%{name}-ac25x.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
A C language library for reading configuration files.

%description -l pl
Biblioteka C s�u��ca do odczytywania plik�w konfiguracyjnych.

%package devel
Summary:	Files for developing programs that use the conflib library
Summary(pl):	Pliki do tworzenia program�w wykorzystuj�cych bibliotek� conflib
Summary(de):	Dateien zum Entwickeln von Programmen mit der conflib-Library
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name} = %{version}

%description devel
This library makes it relativly easy to read configuration files (one
or more), or parts of them. It supports a lot of different data types
and some types of text interpretations, including \-escapes, ~user,
$HOME and conditional expansions.

%description -l pl devel
Ta biblioteka pozwala na stosunkowo proste czytanie plik�w
konfiguracyjnych lub ich cz�ci. Wspiera wiele r�nych typ�w danych
oraz niekt�re typy interpretacji tekstu, np. \-escapes, ~user, $HOME
oraz warunkowe rozwijanie.

%package static
Summary:	Files for developing programs that use the conflib library
Summary(pl):	Statyczne pliki do tworzenia program�w wykorzystuj�cych bibliotek� conflib
Summary(de):	Dateien zum Entwickeln von Programmen mit der conflib-Library
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name}-devel = %{version}

%description static
This library makes it relativly easy to read configuration files (one
or more), or parts of them. It supports a lot of different data types
and some types of text interpretations, including \-escapes, ~user,
$HOME and conditional expansions.

%description -l pl static
Ta biblioteka pozwala na stosunkowo proste czytanie plik�w
konfiguracyjnych lub ich cz�ci. Wspiera wiele r�nych typ�w danych
oraz niekt�re typy interpretacji tekstu, np. \-escapes, ~user, $HOME
oraz warunkowe rozwijanie. Ten pakiet zawiera pliki statyczne.

%prep
%setup -q
%patch0 -p1
%patch1 -p1	
%patch2 -p1	

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README NEWS ChangeLog

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

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
