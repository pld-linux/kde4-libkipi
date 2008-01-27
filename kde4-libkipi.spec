Summary:	KDE Image Plugin Interface libary
Summary(pl.UTF-8):	Biblioteka interfejsu przetwarzania obrazu w KDE
Name:		libkipi
Version:	0.1.5
Release:	3
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/kipi/%{name}-%{version}.tar.bz2
# Source0-md5:	aef790871583444cd81bd9dea9c3fd0b
Patch0:		kde-ac260-lt.patch
URL:		http://extragear.kde.org/apps/kipi/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6.1
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kipi (KDE Image Plugin Interface) is an effort to develop a common
plugin structure for Digikam, KimDaBa, Showimg, and GwenView.

%description -l pl.UTF-8
Kipi to próba stworzenia wspólnego modelu wtyczek dla aplikacji
graficznych KDE takich jak Digikam, KimDaBa, Showimg and Gwenview.

%package devel
Summary:	Header files for libkipi development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających libkipi
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kdelibs-devel >= 9:3.2.0

%description devel
Header files for libkipi development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających libkipi.

%package static
Summary:	Static libkipi library
Summary(pl.UTF-8):	Biblioteka statyczna libkipi
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libkipi library.

%description static -l pl.UTF-8
Biblioteka statyczna libkipi.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--enable-shared \
	--enable-static \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

# empty
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/is

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.?.?.?
%{_datadir}/apps/kipi
%{_datadir}/servicetypes/kipiplugin.desktop
%{_iconsdir}/hicolor/*x*/*/*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/libkipi

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
