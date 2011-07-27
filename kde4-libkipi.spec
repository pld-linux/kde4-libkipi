%define         _state          stable
%define		orgname		libkipi
%define         qtver           4.7.3

Summary:	Kipi library
Summary(pl.UTF-8):	Biblioteka kipi
Name:		libkipi
Version:	4.7.0
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	7c512e305dac78bbaadff24d8d3f4742
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.164
Obsoletes:	kde4-libkipi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kipi library.

%description -l pl.UTF-8
Biblioteka kipi.

%package devel
Summary:	Header files for libkipi development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających libkipi
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kde4-libkipi-devel

%description devel
Header files for libkipi development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających libkipi.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libkipi.so.?
%attr(755,root,root) %{_libdir}/libkipi.so.*.*.*
%{_datadir}/apps/kipi
%{_iconsdir}/hicolor/*x*/apps/*.png
%{_datadir}/kde4/servicetypes/kipiplugin.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkipi.so
%{_includedir}/libkipi
%{_pkgconfigdir}/libkipi.pc
