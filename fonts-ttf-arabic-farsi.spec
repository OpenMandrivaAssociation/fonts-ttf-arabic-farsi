%define name fonts-ttf-arabic-farsi
%define name_orig farsifonts
%define version 0.4
%define release %mkrel 8
%define fontdir	fonts/TTF/arabic/farsi

Name:		%{name}
Summary:	Arabic TrueType fonts
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Fonts/True type
Source:		http://www.farsiweb.info/font/%{name_orig}-%{version}.tar.bz2
URL:		http://www.farsiweb.info
BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-%release-buildroot
BuildRequires: 	freetype-tools
Provides:	fonts-ttf-arabic

%description
This Package provides Free Arabic TrueType fonts donated under the GPL license
by farsiweb.info.

%prep
%setup -n %name_orig-%version -q

%build

%install
rm -rf %buildroot

mkdir -p %buildroot/%_datadir/%fontdir
cp *.ttf %buildroot/%_datadir/%fontdir

pushd %buildroot/%_datadir/%fontdir
%_sbindir/ttmkfdir -u > fonts.scale
cp fonts.scale fonts.dir
%if %mdkversion < 20070
%_bindir/fc-cache . 
%endif
popd

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/%fontdir \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-arabic-farsi:pri=50

%clean
rm -rf %buildroot

%files
%defattr(0644,root,root,0755)
%doc COPYING NEWS *.txt
%dir %_datadir/%{fontdir}
%_datadir/%{fontdir}/*
%_sysconfdir/X11/fontpath.d/ttf-arabic-farsi:pri=50


