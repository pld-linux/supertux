Summary:	Game similar to the original game Super Mario Bros
Summary(pl):	Gra podobna do oryginalnej gry Super Mario Bros
Name:		supertux
Version:	0.1.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://pingus.seul.org/~grumbel/tmp/%{name}-%{version}.tar.bz2
# Source0-md5:	c867f5444b93bf66044b4dc087be2298
#Source0:	http://dl.sourceforge.net/super-tux/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
URL:		http://super-tux.sourceforge.net/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Super Mario Bros style game starring Tux the penguin.

%description -l pl
Gra w stylu Super Mario Bros z pingwinem Tuksem w roli g��wnej.

%prep
%setup -q

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
install data/images/icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LEVELDESIGN README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
