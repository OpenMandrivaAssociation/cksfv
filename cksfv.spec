Name:		cksfv
Version:	1.3.12
Release:	%mkrel 1
Summary:	Simple File Verification program
License:	GPL
Group:		File tools
Source0:	http://zakalwe.virtuaalipalvelin.net/~shd/foss/cksfv/files/%{name}-%{version}.tar.bz2
Source1:	cksfv.bash-completion
URL:		http://zakalwe.virtuaalipalvelin.net/~shd/foss/cksfv/

%description
cksfv (Check SFV) can create sfv (Simple File Verification) listings and test
already created sfv files.  Uses the crc32 checksum.
This format is common in the Windows world.

%prep
%setup -q

%build
%{configure}
%{make}

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
