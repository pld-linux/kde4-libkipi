%define		_snap	040918
Summary:	KDE Image Plugin Interface libary
Summary(pl):	Biblioteka interfejsu przetwarzania obrazu w KDE
Name:		libkipi
Version:	0.1.0
Release:	0.%{_snap}1
License:	LGPL
Group:		Libraries
# From KDE cvs generated using
# 'cvs://pld/kde/package-kdeapp_snap.sh libkipi kdeextragear-libs-1'
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	82af5427f4a3fe5fb33b3e03ee8e9f38
URL:		http://extragear.kde.org/apps/kipi.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040805
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

%description devel
Header files for libkipi development.

%description devel -l pl
Pliki nag³ówkowe dla programistów u¿ywaj±cych libkipi.

%prep
%setup -q -n %{name}

%build
cp -f %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.?.?.?
%{_datadir}/apps/kipi
%{_datadir}/servicetypes/kipiplugin.desktop
%{_iconsdir}/hicolor/*x*/*/*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_includedir}/libkipi
