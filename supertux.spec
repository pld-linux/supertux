#
# Conditional build:
%bcond_with discord	# Discord integration
#
Summary:	Game similar to the original game Super Mario Bros
Summary(pl.UTF-8):	Gra podobna do oryginalnej gry Super Mario Bros
Name:		supertux
Version:	0.6.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	https://github.com/SuperTux/supertux/releases/download/v%{version}/SuperTux-v%{version}-Source.tar.gz
# Source0-md5:	798d5518d3f4672ee0bac92693063c2f
Patch0:		%{name}-0.6.3-missing-headers.patch
URL:		https://www.supertux.org
BuildRequires:	GLM-devel
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL2-devel >= 2.0.1
BuildRequires:	SDL2_image-devel >= 2.0.0
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	doxygen
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
BuildRequires:	glew-devel
BuildRequires:	graphviz
BuildRequires:	harfbuzz-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libraqm-devel
BuildRequires:	libvorbis-devel
BuildRequires:	physfs-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.742
BuildRequires:	zlib-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Super Mario Bros style game starring Tux the penguin.

%description -l pl.UTF-8
Gra w stylu Super Mario Bros z pingwinem Tuksem w roli głównej.

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%prep
%setup -q -n SuperTux-v%{version}-Source
%patch0 -p1

%build
mkdir -p build
cd build
%cmake .. \
	-DINSTALL_SUBDIR_BIN=bin \
	%{cmake_on_off discord ENABLE_DISCORD} \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/supertux2

%if %{with discord}
%{__rm} $RPM_BUILD_ROOT%{_includedir}/discord_*.h
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CODINGSTYLE.md CONTRIBUTING.md NEWS.md README.md
%attr(755,root,root) %{_bindir}/supertux2
%{_datadir}/games/supertux2
%{_desktopdir}/supertux2.desktop
%{_iconsdir}/hicolor/scalable/apps/supertux2.svg
%{_datadir}/metainfo/supertux2.appdata.xml
%{_pixmapsdir}/supertux.png
%{_pixmapsdir}/supertux.xpm
%if %{with discord}
%{_libdir}/libdiscord-rpc.so
%endif
