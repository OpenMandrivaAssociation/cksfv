%define name	cksfv
%define version 1.3.11
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Simple File Verification program
License:	GPL
Group:		File tools
Source0:	http://zakalwe.virtuaalipalvelin.net/~shd/foss/cksfv/files/%{name}-%{version}.tar.bz2
Source1:	cksfv.bash-completion.bz2
URL:		http://zakalwe.virtuaalipalvelin.net/~shd/foss/cksfv/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
cksfv (Check SFV) can create sfv (Simple File Verification) listings and test
already created sfv files.  Uses the crc32 checksum.
This format is common in the Windows world.

%prep
%setup -q
bzcat %{SOURCE1} > %{name}.bash-completion
chmod 644 COPYING ChangeLog README TODO INSTALL

%build

%configure

%make

%install
rm -rf %buildroot

install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
install -m 644 %{name}.bash-completion $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/%{name}
# this prepare directory for man page. bug in Makefile..
install -d -m 755 $RPM_BUILD_ROOT%_mandir/man1

%makeinstall BINDIR=%buildroot%_bindir MANDIR=%buildroot%_mandir

%clean
rm -rf %buildroot

%files
%defattr(-, root, root)
%doc ChangeLog README TODO INSTALL
%doc scripts/
%{_bindir}/cksfv
%_mandir/man1/*
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}


