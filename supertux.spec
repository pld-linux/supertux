Summary:	Game similar to the original game Super Mario Bros
Summary(pl):	Gra podobna do oryginalnej gry Super Mario Bros
Name:		supertux
Version:	0.0.4
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	ftp://ftp.sonic.net/pub/users/nbs/unix/x/%{name}/src/%{name}-%{version}.tar.gz
# Source0-md5:	54f95a7fe1133587ac56c6980c2a79df
Source1:	%{name}.desktop
URL:		http://www.newbreedsoftware.com/supertux/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define tuxdir	%{_datadir}/games/%{name}

%description
Super Mario Bros style game starring Tux the penguin.

%description -l pl
Gra w stylu Super Mario Bros z pingwinek Tuksem w roli g³ównej.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags} `sdl-config --cflags` -DDATA_PREFIX=\\\"%{tuxdir}/data/\\\" -D__SOUND -DLINUX"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{tuxdir},%{_desktopdir},%{_pixmapsdir}}

cp -R data $RPM_BUILD_ROOT%{tuxdir}
install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install data/images/icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGES.txt README.txt TODO.txt
%attr(755,root,root) %{_bindir}/*
%{tuxdir}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
