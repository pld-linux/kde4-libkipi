%define         _state          stable
%define		orgname		libkipi
%define         qtver           4.8.3

Summary:	Kipi library
Summary(pl.UTF-8):	Biblioteka kipi
Name:		kde4-libkipi
Version:	4.14.3
Release:	4
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	4dd3c5e16297983bfa462d9ddc793dbb
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	rpmbuild(macros) >= 1.164
Obsoletes:	libkipi <= 4.8.0
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
Obsoletes:	kde4-kdegraphics-devel < 4.6.99
Obsoletes:	libkipi-devel <= 4.8.0

%description devel
Header files for libkipi development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających libkipi.

%prep
%setup -q -n %{orgname}-%{version}

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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kxmlkipicmd
%attr(755,root,root) %ghost %{_libdir}/libkipi.so.??
%attr(755,root,root) %{_libdir}/libkipi.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_kxmlhelloworld.so
%{_datadir}/apps/kipi
%{_datadir}/apps/kxmlkipicmd
%{_iconsdir}/hicolor/*x*/apps/*.png
%{_datadir}/kde4/services/kipiplugin_kxmlhelloworld.desktop
%{_datadir}/kde4/servicetypes/kipiplugin.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkipi.so
%{_includedir}/libkipi
%{_pkgconfigdir}/libkipi.pc
