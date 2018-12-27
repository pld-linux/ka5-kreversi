%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kreversi
Summary:	kreversi
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	bd77a8ac7f869052773672235f99fd7e
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= 18.12.0
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.30.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.30.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.30.0
BuildRequires:	kf5-kcrash-devel >= 5.30.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.30.0
BuildRequires:	kf5-kdeclarative-devel >= 5.30.0
BuildRequires:	kf5-ki18n-devel >= 5.30.0
BuildRequires:	kf5-kiconthemes-devel >= 5.30.0
BuildRequires:	kf5-kio-devel >= 5.30.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KReversi is a simple one player strategy game played against the
computer. If a player's piece is captured by an opposing player, that
piece is turned over to reveal the color of that player. A winner is
declared when one player has more pieces of his own color on the board
and there are no more possible moves.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kreversi
%{_desktopdir}/org.kde.kreversi.desktop
%{_iconsdir}/hicolor/128x128/apps/kreversi.png
%{_iconsdir}/hicolor/16x16/actions/lastmoves.png
%{_iconsdir}/hicolor/16x16/actions/legalmoves.png
%{_iconsdir}/hicolor/16x16/apps/kreversi.png
%{_iconsdir}/hicolor/22x22/actions/lastmoves.png
%{_iconsdir}/hicolor/22x22/actions/legalmoves.png
%{_iconsdir}/hicolor/22x22/apps/kreversi.png
%{_iconsdir}/hicolor/32x32/actions/lastmoves.png
%{_iconsdir}/hicolor/32x32/actions/legalmoves.png
%{_iconsdir}/hicolor/32x32/apps/kreversi.png
%{_iconsdir}/hicolor/48x48/actions/lastmoves.png
%{_iconsdir}/hicolor/48x48/actions/legalmoves.png
%{_iconsdir}/hicolor/48x48/apps/kreversi.png
%{_iconsdir}/hicolor/64x64/apps/kreversi.png
%{_iconsdir}/hicolor/scalable/actions/lastmoves.svgz
%{_iconsdir}/hicolor/scalable/actions/legalmoves.svgz
%{_datadir}/knotifications5/kreversi.notifyrc
%{_datadir}/kreversi
%{_datadir}/metainfo/org.kde.kreversi.appdata.xml
