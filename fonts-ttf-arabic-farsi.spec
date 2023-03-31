%define oname farsifonts
%define fontdir	fonts/TTF/arabic/farsi

Summary:	Arabic TrueType fonts
Name:		fonts-ttf-arabic-farsi
Version:	0.4
Release:	25
License:	GPLv2
Group:		System/Fonts/True type
Url:		http://www.farsiweb.info
Source0:	http://www.farsiweb.info/font/%{oname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	mkfontscale
Provides:	fonts-ttf-arabic

%description
This Package provides Free Arabic TrueType fonts donated under the GPL license
by farsiweb.info.

%prep
%setup -qn %oname-%{version}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/%fontdir
cp *.ttf %{buildroot}/%{_datadir}/%fontdir

pushd %{buildroot}/%{_datadir}/%fontdir
mkfontscale
cp fonts.scale fonts.dir
popd

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/%fontdir \
    %{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-arabic-farsi:pri=50

%files
%doc COPYING NEWS *.txt
%dir %{_datadir}/%{fontdir}
%{_datadir}/%{fontdir}/*
%{_sysconfdir}/X11/fontpath.d/ttf-arabic-farsi:pri=50

