Summary:	Game similar to the original game Super Mario Bros
Summary(pl):	Gra podobna do oryginalnej gry Super Mario Bros
Name:		supertux
Version:	0.0.6
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/super-tux/%{name}-%{version}.tar.bz2
# Source0-md5:	c5763a70bc397653f051953cd0ec1b44
Source1:	%{name}.desktop
URL:		http://www.newbreedsoftware.com/supertux/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Super Mario Bros style game starring Tux the penguin.

%description -l pl
Gra w stylu Super Mario Bros z pingwinem Tuksem w roli g³ównej.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
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
%doc AUTHORS ChangeLog LEVELDESIGN README TODO.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
