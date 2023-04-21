#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.04.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kreversi
Summary:	kreversi
Name:		ka5-%{kaname}
Version:	23.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	7fdbac2f264123ee6ceb9ecbfc1ae923
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
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdeclarative-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
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

%description -l pl.UTF-8
Kreversi jest prostą grą strategiczną. Gracz gra przeciwko komputerowi.
Jeśli pionek gracza jest zdobyty przez oponenta, to zmienia swój kolor
na kolor przeciwnika. Zwycięzcą jest ten z graczy, który ma więcej
pionków w swoim kolorze, gdy na planszy nie można już wykonać ruchu.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

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
