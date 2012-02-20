%define name 	        ncmpc
%define version         0.20
%define release	        1

Name:			%name
Version:		%version
Release:		%release

Summary:		Ncurses client for MPD
License:		GPL
Group:			Sound
URL:			http://mpd.wikia.com/wiki/Client:Ncmpc
Source0:        http://downloads.sourceforge.net/musicpd/%{name}-%{version}.tar.bz2

BuildRequires:  glib2-devel
BuildRequires:  libmpdclient-devel
BuildRequires:  ncursesw-devel

%description
ncmpc is a curses client for the Music Player Daemon (MPD). ncmpc connects to a
MPD running on a machine on the local network, and controls this with an
interface inspired by cplay. If ncmpc is used with lirc and irpty it can be
used to manage playlists and control MPD with a remote control.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

rm -rf $RPM_BUILD_ROOT/%{_docdir}/%{name}/

%find_lang %name

%files -f %name.lang
%doc README AUTHORS NEWS COPYING doc/config.sample doc/keys.sample doc/ncmpc.lirc
%{_bindir}/%name
%{_mandir}/man1/*
