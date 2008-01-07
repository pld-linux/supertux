# TODO
# - check locale names
# - is it debug bcond missing?
Summary:	Game similar to the original game Super Mario Bros
Summary(pl.UTF-8):   Gra podobna do oryginalnej gry Super Mario Bros
Name:		supertux
Version:	0.3.1
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://download.berlios.de/supertux/%{name}-%{version}d.tar.bz2
# Source0-md5:	6741f3874f64bc5371d72d664a6424bc
Patch0:		%{name}-desktop.patch
URL:		http://supertux.berlios.de/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	SDL_image-devel >= 1.2.1
BuildRequires:	autoconf >= 2.54
BuildRequires:	jam >= 2.5
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
%{__aclocal} -I mk/autoconf
%{__autoheader}
%{__autoconf}
%configure \
	%{?debug:--enable-debug}%{!?debug:--disable-debug}
jam

%install
rm -rf $RPM_BUILD_ROOT

jam -s DESTDIR=$RPM_BUILD_ROOT install

# the same as supertux.png
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/supertux.xpm

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/locale/messages.pot
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README WHATSNEW.txt
%attr(755,root,root) %{_bindir}/supertux2
%dir %{_datadir}/%{name}2
%{_datadir}/%{name}2/camera.cfg
%{_datadir}/%{name}2/images
%{_datadir}/%{name}2/levels
%dir %{_datadir}/%{name}2/locale
%lang(ca) %{_datadir}/%{name}2/locale/ca.po
%lang(cs) %{_datadir}/%{name}2/locale/cs.po
%lang(da) %{_datadir}/%{name}2/locale/da.po
%lang(de) %{_datadir}/%{name}2/locale/de.po
%lang(es) %{_datadir}/%{name}2/locale/es.po
%lang(fi) %{_datadir}/%{name}2/locale/fi.po
%lang(fr) %{_datadir}/%{name}2/locale/fr.po
%lang(hu) %{_datadir}/%{name}2/locale/hu.po
%lang(it) %{_datadir}/%{name}2/locale/it.po
%lang(lt) %{_datadir}/%{name}2/locale/lt.po
%lang(nb) %{_datadir}/%{name}2/locale/nb.po
%lang(nl) %{_datadir}/%{name}2/locale/nl.po
%lang(nn) %{_datadir}/%{name}2/locale/nn.po
%lang(pt) %{_datadir}/%{name}2/locale/pt.po
%lang(pt_BR) %{_datadir}/%{name}2/locale/pt_BR.po
%lang(ro) %{_datadir}/%{name}2/locale/ro.po
%lang(sl) %{_datadir}/%{name}2/locale/sl.po
%lang(sv) %{_datadir}/%{name}2/locale/sv.po
%{_datadir}/%{name}2/music
%{_datadir}/%{name}2/scripts
%{_datadir}/%{name}2/sounds
%{_datadir}/%{name}2/credits.txt
%{_desktopdir}/supertux2.desktop
%{_pixmapsdir}/supertux.png
