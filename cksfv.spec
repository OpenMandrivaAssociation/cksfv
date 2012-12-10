Name:		cksfv
Version:	1.3.14
Release:	%mkrel 2
Summary:	Simple File Verification program
License:	GPLv2+
Group:		File tools
Source0:	http://zakalwe.virtuaalipalvelin.net/~shd/foss/cksfv/files/%{name}-%{version}.tar.bz2
Source1:	cksfv.bash-completion
URL:		http://zakalwe.virtuaalipalvelin.net/~shd/foss/cksfv/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
cksfv (Check SFV) can create sfv (Simple File Verification) listings and test
already created sfv files.  Uses the crc32 checksum.
This format is common in the Windows world.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_sysconfdir}/bash_completion.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}
# this prepare directory for man page. bug in Makefile..
install -d -m 755 %{buildroot}%{_mandir}/man1

%{makeinstall} BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir}

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc ChangeLog README TODO INSTALL
%doc scripts/
%attr(0755,root,root) %{_bindir}/cksfv
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}


%changelog
* Wed Jul 13 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.3.14-2mdv2011
+ Revision: 689834
- rebuild

* Mon Jun 08 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.3.14-1mdv2011.0
+ Revision: 383894
- new version
- fix build

* Mon Aug 25 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.3.13-1mdv2009.0
+ Revision: 275668
- new version
- update license

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.3.12-3mdv2009.0
+ Revision: 240503
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Aug 12 2007 David Walluck <walluck@mandriva.org> 1.3.12-1mdv2008.0
+ Revision: 62360
- 1.3.12
- bunzip2 cksfv.bash-completion
- consistent use of tabs
- consistent use of macros
- set correct doc file permissions in %%files

* Wed Jul 11 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.3.11-1mdv2008.0
+ Revision: 51280
- new version
- add nautilus script to docs


* Wed Mar 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.3.10-1mdv2007.1
+ Revision: 149086
- new version
- Import cksfv

* Fri Jul 21 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.3.9-1mdv2007.0
- Rebuild

* Tue Mar 07 2006 Götz Waschk <waschk@mandriva.org> 1.3.9-1mdk
- fix for rpmlint
- New release 1.3.9

* Sun Jan 01 2006 David Walluck <walluck@mandriva.org> 1.3.8-1mdk
- 1.3.8

* Tue Oct 25 2005 Götz Waschk <waschk@mandriva.org> 1.3.7-1mdk
- new version
- URL

* Tue Aug 09 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.3.6-1mdk
- New release 1.3.6

* Wed Jun 08 2005 Götz Waschk <waschk@mandriva.org> 1.3.5-1mdk
- New release 1.3.5

* Tue Apr 05 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 1.3.4-1mdk
- New release 1.3.4

* Fri Apr 01 2005 Tibor Pittich <Tibor.Pittich@mandrake.org> 1.3.3-1mdk
- 1.3.3
- fix for creation and installation man page

* Thu Feb 03 2005 Götz Waschk <waschk@linux-mandrake.com> 1.3.2-2mdk
- add missing man page

* Thu Feb 03 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.3.2-1mdk
- 1.3.2

* Tue Jan 25 2005 Götz Waschk <waschk@linux-mandrake.com> 1.3.1-2mdk
- fix bash-completion

* Tue Jan 25 2005 Götz Waschk <waschk@linux-mandrake.com> 1.3.1-1mdk
- fix URL
- New release 1.3.1

* Sat Jan 08 2005 Götz Waschk <waschk@linux-mandrake.com> 1.3-5mdk
- rebuild

