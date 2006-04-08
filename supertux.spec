Summary:	Game similar to the original game Super Mario Bros
Summary(pl):	Gra podobna do oryginalnej gry Super Mario Bros
Name:		supertux
Version:	0.1.3
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.berlios.de/supertux/%{name}-%{version}.tar.bz2
# Source0-md5:	f2fc288459f33d5cd8f645fbca737a63
#Source0:	http://pingus.seul.org/~grumbel/tmp/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-gcc4.patch
URL:		http://super-tux.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Super Mario Bros style game starring Tux the penguin.

%description -l pl
Gra w stylu Super Mario Bros z pingwinem Tuksem w roli g³ównej.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I mk/autoconf
%{__autoconf}
%{__automake}
%configure \
	%{?debug:--enable-debug}%{!?debug:--disable-debug}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install data/images/icon.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LEVELDESIGN README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.xpm
