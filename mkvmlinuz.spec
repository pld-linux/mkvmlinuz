Summary:	Script for creating bootable kernel with included initrd for PowerPCs
Name:		mkvmlinuz
Version:	1.1
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	%{name}
Source1:	%{name}.sysconfig
Requires:	binutils
Requires:	gzip
Requires:	mktemp
ExclusiveArch:	ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Script for creating bootable kernel with included initrd for PowerPCs.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/sysconfig}

install %{SOURCE0} $RPM_BUILD_ROOT%{_sbindir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
