Summary:	Game similar to the original game Super Mario Bros
Summary(pl.UTF-8):   Gra podobna do oryginalnej gry Super Mario Bros
Name:		supertux
Version:	0.3.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.berlios.de/supertux/%{name}-%{version}.tar.bz2
# Source0-md5:	454760a0a1d3f8ea6e54829e838cd94d
Patch0:		%{name}-desktop.patch
URL:		http://supertux.berlios.de/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	SDL_image-devel >= 1.2.1
BuildRequires:	autoconf >= 2.54
BuildRequires:	jam
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
%attr(755,root,root) %{_bindir}/supertux
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/images
%{_datadir}/%{name}/levels
%dir %{_datadir}/%{name}/locale
%lang(cs) %{_datadir}/%{name}/locale/cs.po
%lang(da) %{_datadir}/%{name}/locale/da.po
%lang(de) %{_datadir}/%{name}/locale/de.po
%lang(es) %{_datadir}/%{name}/locale/es.po
%lang(hu) %{_datadir}/%{name}/locale/hu.po
%lang(nn) %{_datadir}/%{name}/locale/nn.po
%lang(pt_BR) %{_datadir}/%{name}/locale/pt_BR.po
%lang(sl) %{_datadir}/%{name}/locale/sl.po
%lang(sv) %{_datadir}/%{name}/locale/sv.po
%{_datadir}/%{name}/music
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/sounds
%{_datadir}/%{name}/credits.txt
%{_desktopdir}/supertux.desktop
%{_pixmapsdir}/supertux.png
