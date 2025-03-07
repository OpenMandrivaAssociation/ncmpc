%define name 	        ncmpc

Name:			ncmpc
Version:		0.52
Release:		1
Summary:		Ncurses client for MPD
License:		GPL
Group:			Sound
URL:			https://mpd.wikia.com/wiki/Client:Ncmpc
Source0:	https://www.musicpd.org/download/ncmpc/0/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:	pkgconfig(lirc)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:	ninja
BuildRequires:	boost-devel
BuildRequires:	python-sphinx
BuildRequires:  meson

%description
ncmpc is a curses client for the Music Player Daemon (MPD). ncmpc connects to a
MPD running on a machine on the local network, and controls this with an
interface inspired by cplay. If ncmpc is used with lirc and irpty it can be
used to manage playlists and control MPD with a remote control.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

rm -rf $RPM_BUILD_ROOT/%{_docdir}/%{name}/

#find_lang %name

%files 
#-f %name.lang
%doc README.rst AUTHORS NEWS COPYING doc/config.sample doc/keys.sample doc/ncmpc.lirc
%{_bindir}/%name
%{_mandir}/man1/*
