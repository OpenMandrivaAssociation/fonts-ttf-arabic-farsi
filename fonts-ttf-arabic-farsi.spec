%define name fonts-ttf-arabic-farsi
%define name_orig farsifonts
%define version 0.4
%define release %mkrel 14
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
BuildRequires: fontconfig
BuildRoot:	%_tmppath/%name-%version-%release-buildroot
BuildRequires:	mkfontscale
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
mkfontscale
cp fonts.scale fonts.dir
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




%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 0.4-13mdv2011.0
+ Revision: 675407
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 0.4-12
+ Revision: 675171
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4-11
+ Revision: 664320
- mass rebuild

* Fri Dec 03 2010 Funda Wang <fwang@mandriva.org> 0.4-10mdv2011.0
+ Revision: 605816
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Wed Feb 17 2010 Frederic Crozat <fcrozat@mandriva.com> 0.4-9mdv2010.1
+ Revision: 507147
- force rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.4-8mdv2010.1
+ Revision: 494118
- fc-cache is now called by an rpm filetrigger

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.4-7mdv2009.1
+ Revision: 351037
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.4-6mdv2009.0
+ Revision: 220856
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.4-5mdv2008.1
+ Revision: 170832
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.4-4mdv2008.1
+ Revision: 149732
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- buildrequires obsoletes buildprereq

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.4-3mdv2008.0
+ Revision: 48736
- fontpath.d conversion (#31756)
- minor cleanups


* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 23:10:13 (52882)
- Normalize fonts with new paths

* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 21:03:06 (52803)
- import fonts-ttf-arabic-farsi-0.4-2mdk

* Fri Feb 03 2006 Frederic Crozat <fcrozat@mandriva.com> 0.4-2mdk
- Don't package fonts.cache-2 file
- Fix prereq
- touch parent directory to workaround rpm changing directory last modification
  time (breaking fontconfig cache consistency detection)
- Remove dependency on freetype, this is old stuff

* Thu Aug 05 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.4-1mdk
- fix rpmlint warnings
- do not use subsheels b/c they hide errors
- initial build (Munzir Taha <munzirtaha@newhorizons.com.sa>)

