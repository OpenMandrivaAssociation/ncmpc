%define name 	        ncmpc
%define version         0.16
%define release	        %mkrel 1

Name:			%name
Version:		%version
Release:		%release

Summary:		Ncurses client for MPD
License:		GPL
Group:			Sound
URL:			http://mpd.wikia.com/wiki/Client:Ncmpc
Source0:        http://downloads.sourceforge.net/musicpd/%{name}-%{version}.tar.bz2

BuildRequires:  libmpdclient

BuildRoot:		%{_tmppath}/%{name}-%{version}

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
rm -rf $RPM_BUILD_ROOT
%makeinstall

rm -rf $RPM_BUILD_ROOT/%{_docdir}/%{name}/

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS NEWS COPYING doc/config.sample doc/keys.sample doc/ncmpc.lirc
%{_bindir}/%name
%{_mandir}/man1/*
