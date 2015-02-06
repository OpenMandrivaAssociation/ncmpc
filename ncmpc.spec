%define name 	        ncmpc
%define version         0.20
%define release	        2

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


%changelog
* Mon Feb 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.20-1
+ Revision: 778139
- version update 0.20

* Thu Sep 29 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 0.19-1
+ Revision: 702013
- new version 0.19

* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.18-1
+ Revision: 645330
- update to new version 0.18

* Wed Feb 02 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.17-3
+ Revision: 635344
- Build with unicode support.

* Sun Aug 08 2010 Rémy Clouard <shikamaru@mandriva.org> 0.17-2mdv2011.0
+ Revision: 567659
- rebuild for new libmpdclient

* Sat Aug 07 2010 Jérôme Quelin <jquelin@mandriva.org> 0.17-1mdv2011.0
+ Revision: 567361
- update to new version 0.17

* Thu Feb 04 2010 Jérôme Quelin <jquelin@mandriva.org> 0.16.1-1mdv2010.1
+ Revision: 500673
- update to new version 0.16.1

* Sat Jan 02 2010 Jérôme Quelin <jquelin@mandriva.org> 0.16-1mdv2010.1
+ Revision: 485064
- update buildrequires:
- update buildrequires:
- update buildrequires:
- update buildrequires:
- update buildrequires:
- update buildrequires:
- update buildrequires:
- update buildrequires:
- adding missing buildrequires:
- fix buildrequires:
- adding missing buildrequires:
- update to new version 0.16

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.15-1mdv2010.1
+ Revision: 460704
- update to new version 0.15

* Sun May 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.14-1mdv2010.0
+ Revision: 379285
- update to new version 0.14

* Sat Jan 10 2009 Jérôme Quelin <jquelin@mandriva.org> 0.13-1mdv2009.1
+ Revision: 327934
- update to new version 0.13

* Mon Dec 08 2008 Jérôme Quelin <jquelin@mandriva.org> 0.12-5mdv2009.1
+ Revision: 311727
- update to 0.12
- fix spec file to allow for easy update with mdvsys

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.11.1-5mdv2009.0
+ Revision: 241055
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Jul 20 2007 Gaëtan Lehmann <glehmann@mandriva.org> 0.11.1-3mdv2008.0
+ Revision: 53833
- build requires libglib2-devel
- rebuild
- Import ncmpc

