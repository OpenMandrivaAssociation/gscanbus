%define name gscanbus
%define version 0.7.1
%define release %mkrel 9

Summary: A tool to scan IEEE1394 (firewire/i.link) bus
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0: gscanbus-add-destdir.patch
Patch1: gscanbus-0.7.1-fix-unterminated-strings.patch
License: GPL
URL: http://gscanbus.berlios.de/
Group: System/Kernel and hardware
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libraw1394-devel
BuildRequires: automake1.4
BuildRequires: gtk-devel

%description
gscanbus is a little bus scanning, testing and topology visualizing tool
for the Linux IEEE1394 subsystem, with some AV/C support, especially for
controlling Camcorders and VCRs. It is intended as a debugging tool for
IEEE1394 development, but can also be used to simply check your IEEE1394
setup on Linux.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
automake-1.4      # patched Makefile.am

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-9mdv2011.0
+ Revision: 619257
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.7.1-8mdv2010.0
+ Revision: 437819
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.7.1-7mdv2009.0
+ Revision: 246651
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.7.1-5mdv2008.1
+ Revision: 140742
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Jan 16 2007 Stefan van der Eijk <stefan@mandriva.org> 0.7.1-5mdv2007.0
+ Revision: 109644
- Import gscanbus

* Mon Apr 24 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.7.1-5mdk
- Add BuildRequires
- use mkrel

* Fri Mar 18 2005 Olivier Blin <oblin@mandrakesoft.com> 0.7.1-4mdk
- use automake1.4
- rebuild for libraw1394

* Sat Mar 13 2004 Guillaume Cottenceau <gc@mandrakesoft.com> 0.7.1-3mdk
- rebuild per request of Warly's bot

