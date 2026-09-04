#define name 	        ncmpc

Summary:		Ncurses client for MPD
Name:	ncmpc
Version:		0.54
Release:		2
License:		GPLv2+
Group:	Sound
Url:	https://www.musicpd.org/clients/ncmpc/
Source0:	https://www.musicpd.org/download/ncmpc/0/%{name}-%{version}.tar.xz
BuildRequires:		meson >= 1.2
BuildRequires:		ninja
BuildRequires:		python-sphinx
BuildRequires:		boost-devel
BuildRequires:		pkgconfig(fmt)
BuildRequires:		pkgconfig(glib-2.0)
BuildRequires:		pkgconfig(libmpdclient)
BuildRequires:		pkgconfig(libpcre2-8)
BuildRequires:		pkgconfig(lirc)
BuildRequires:		pkgconfig(ncurses)

%description
This is a ncurses client for the Music Player Daemon (MPD). It connects to a
MPD running on a machine on the local network, and controls this with an
interface inspired by cplay. If it is used with lirc and irpty it can be
used to manage playlists and control MPD with a remote control.

%files 
#-f %%{name}.lang
%license COPYING
%doc README.rst AUTHORS NEWS doc/config.sample doc/keys.sample doc/ncmpc.lirc
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1

# Fix FSF address
sed -i 's/51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA/31 Milk Street, # 960789, Boston, MA 02196, USA/g' COPYING


%build
%meson
%meson_build


%install
%meson_install

rm -rf %{buildroot}%{_docdir}/%{name}/

#find_lang %%{name}


