Summary:	KDE Image Plugin Interface libary
Summary(pl):	Biblioteka interfejsu przetwarzania obrazu w KDE
Name:		libkipi
Version:	0.1.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/kipi/%{name}-%{version}.tar.bz2
# Source0-md5:	2d8b8da064b85b0e53a98b4a7510392e
Patch0:		kde-ac260.patch
Patch1:		kde-common-LD_quote.patch
URL:		http://extragear.kde.org/apps/kipi/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kipi (KDE Image Plugin Interface) is an effort to develop a common
plugin structure for Digikam, KimDaBa, Showimg, and GwenView.

%description -l pl
Kipi to próba stworzenia wspólnego modelu wtyczek dla aplikacji
graficznych KDE takich jak Digikam, KimDaBa, Showimg and Gwenview.

%package devel
Summary:	Header files for libkipi development
Summary(pl):	Pliki nag³ówkowe dla programistów u¿ywaj±cych libkipi
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdelibs-devel >= 9:3.2.0

%description devel
Header files for libkipi development.

%description devel -l pl
Pliki nag³ówkowe dla programistów u¿ywaj±cych libkipi.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
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

rm -rf $RPM_BUILD_ROOT/usr/share/locale/is

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

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
