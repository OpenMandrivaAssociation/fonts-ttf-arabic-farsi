%define name fonts-ttf-arabic-farsi
%define name_orig farsifonts
%define version 0.4
%define release %mkrel 3
%define fontdir	fonts/TTF/arabic/farsi

Name:		%{name}
Summary:	Free Arabic TrueType fonts
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Fonts/True type
Source:		http://www.farsiweb.info/font/%{name_orig}-%{version}.tar.bz2
URL:		http://www.farsiweb.info
BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-%release-buildroot
BuildPrereq: 	freetype-tools
Requires(post):		chkfontpath
Requires(postun):	chkfontpath
Requires(post):		fontconfig
Requires(postun):	fontconfig
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

%post
[ -x %_sbindir/chkfontpath ] && %_sbindir/chkfontpath -q -a %_datadir/%{fontdir}
touch %{_datadir}/fonts/TTF
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 

%postun
# 0 means a real uninstall
if [ "$1" = "0" ]; then
   [ -x %_sbindir/chkfontpath ] && \
   %_sbindir/chkfontpath -q -r %_datadir/%{fontdir}
   [ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 
fi

%clean
rm -rf %buildroot

%files
%defattr(0644,root,root,0755)
%doc COPYING NEWS *.txt
%dir %_datadir/fonts/TTF/
%dir %_datadir/%{fontdir}
%_datadir/%{fontdir}/*



