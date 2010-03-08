# TODO
# - check locale names
# - check if it works
# - rename it to supertux2?
Summary:	Game similar to the original game Super Mario Bros
Summary(pl.UTF-8):	Gra podobna do oryginalnej gry Super Mario Bros
Name:		supertux
Version:	0.3.3
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://download.berlios.de/supertux/%{name}-%{version}.tar.bz2
# Source0-md5:	f3f803e629ee51a9de0b366a036e393d
Patch0:		%{name}-desktop.patch
URL:		http://supertux.berlios.de/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	SDL_image-devel >= 1.2.1
BuildRequires:	cmake >= 2.6
BuildRequires:	libstdc++-devel >= 5:3.2
BuildRequires:	libvorbis-devel
BuildRequires:	physfs-devel >= 1.0.0
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Super Mario Bros style game starring Tux the penguin.

%description -l pl.UTF-8
Gra w stylu Super Mario Bros z pingwinem Tuksem w roli głównej.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DINSTALL_SUBDIR_BIN="bin"
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# the same as supertux.png
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/supertux.xpm

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/locale/messages.pot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README WHATSNEW.txt
%attr(755,root,root) %{_bindir}/supertux2
%dir %{_datadir}/games/%{name}2
%{_datadir}/games/%{name}2/fonts
%{_datadir}/games/%{name}2/images
%{_datadir}/games/%{name}2/levels
%{_datadir}/games/%{name}2/music
%{_datadir}/games/%{name}2/scripts
%{_datadir}/games/%{name}2/sounds
%{_datadir}/games/%{name}2/speech
%dir %{_datadir}/games/%{name}2/locale
%lang(ca) %{_datadir}/games/%{name}2/locale/ca.po
%lang(cs) %{_datadir}/games/%{name}2/locale/cs.po
%lang(da) %{_datadir}/games/%{name}2/locale/da.po
%lang(de) %{_datadir}/games/%{name}2/locale/de.po
%lang(es) %{_datadir}/games/%{name}2/locale/es.po
%lang(fi) %{_datadir}/games/%{name}2/locale/fi.po
%lang(fr) %{_datadir}/games/%{name}2/locale/fr.po
%lang(hu) %{_datadir}/games/%{name}2/locale/hu.po
%lang(it) %{_datadir}/games/%{name}2/locale/it.po
%lang(lt) %{_datadir}/games/%{name}2/locale/lt.po
%lang(nb) %{_datadir}/games/%{name}2/locale/nb.po
%lang(ne) %{_datadir}/games/%{name}2/locale/ne.po
%lang(nl) %{_datadir}/games/%{name}2/locale/nl.po
%lang(nn) %{_datadir}/games/%{name}2/locale/nn.po
%lang(pl) %{_datadir}/games/%{name}2/locale/pl.po
%lang(pt) %{_datadir}/games/%{name}2/locale/pt.po
%lang(pt_BR) %{_datadir}/games/%{name}2/locale/pt_BR.po
%lang(ro) %{_datadir}/games/%{name}2/locale/ro.po
%lang(ru) %{_datadir}/games/%{name}2/locale/ru.po
%lang(sl) %{_datadir}/games/%{name}2/locale/sl.po
%lang(sv) %{_datadir}/games/%{name}2/locale/sv.po
%lang(tr) %{_datadir}/games/%{name}2/locale/tr.po
%lang(uk) %{_datadir}/games/%{name}2/locale/uk.po
%lang(zh_CN) %{_datadir}/games/%{name}2/locale/zh_CN.po
%{_desktopdir}/supertux2.desktop
%{_pixmapsdir}/supertux.png
