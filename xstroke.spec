%define name 	xstroke
%define version 0.6.cvs20040921
%define release 9

Summary: 	Fullscreen gesture and alphabet recognition
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://cworth.org/~cworth/papers/xstroke/	
License: 	GPLv2+
Group: 		Accessibility
Source: 	%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xft)
BuildRequires:	xpm-devel
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(xi)
BuildRequires:	imagemagick

%description
XStroke is a full-screen gesture recognition program for the X Window
System. It captures gestures performed with a pointer device, (such as a
mouse, a stylus, or a pen/tablet), recognizes the gestures and performs
actions based on the gestures. xstroke has been developed on Linux systems,
(i386 and StrongARM), but should be quite portable to any reasonable
system with X.

%prep
%setup -q -n %name-0.6

%build
export LDFLAGS="-lXrender -lX11 -ldl -lXext -lXtst -lXi"
%configure2_5x
%make

%install
%makeinstall_std

#menu
mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%name.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%name
Name=XStroke
Comment=Fullscreen gesture recognition
Icon=%name
Categories=Utility;Accessibility;
EOF

#icons
mkdir -p %{buildroot}/%_liconsdir
convert -size 48x48 xstroke_inactive.xpm %{buildroot}/%_liconsdir/%name.png
mkdir -p %{buildroot}/%_iconsdir
convert -size 32x32 xstroke_inactive.xpm %{buildroot}/%_iconsdir/%name.png
mkdir -p %{buildroot}/%_miconsdir
convert -size 16x16 xstroke_inactive.xpm %{buildroot}/%_miconsdir/%name.png

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/%name
%config(noreplace) %_sysconfdir/%name
%{_datadir}/applications/mandriva-%name.desktop
%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png



%changelog
* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 0.6.cvs20040921-6mdv2011.0
+ Revision: 634970
- simplify BR

* Sat May 16 2009 Samuel Verschelde <stormi@mandriva.org> 0.6.cvs20040921-5mdv2010.0
+ Revision: 376497
- fix URL
- fix license

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 0.6.cvs20040921-4mdv2009.0
+ Revision: 262733
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.6.cvs20040921-3mdv2009.0
+ Revision: 257781
- rebuild
- fix 'error: for key "Icon" in group "Desktop Entry" is an icon name with an
  extension, but there should be no extension as described in the Icon Theme
  Specification if the value is not an absolute path'
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 14 2007 Thierry Vignaud <tv@mandriva.org> 0.6.cvs20040921-1mdv2008.1
+ Revision: 120014
- auto convert menu to XDG
- buildrequires X11-devel instead of XFree86-devel
- use %%mkrel
- import xstroke


* Tue Sep 21 2004 Austin Acton <austin@mandrake.org> 0.6.cvs20040921-1mdk
- initial build

