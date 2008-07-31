%define name 	xstroke
%define version 0.6.cvs20040921
%define release %mkrel 3

Summary: 	Fullscreen gesture and alphabet recognition
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://www.xstroke.org/
License: 	GPL
Group: 		Accessibility
Source: 	%{name}-%{version}.tar.bz2

Buildroot: 	%_tmppath/%name-%version-buildroot
BuildRequires:	X11-devel ImageMagick

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
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%name.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%name
Name=XStroke
Comment=Fullscreen gesture recognition
Icon=%name
Categories=Utility;Accessibility;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 xstroke_inactive.xpm $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 xstroke_inactive.xpm $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 xstroke_inactive.xpm $RPM_BUILD_ROOT/%_miconsdir/%name.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%update_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/%name
%config(noreplace) %_sysconfdir/%name
%{_datadir}/applications/mandriva-%name.desktop
%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png

