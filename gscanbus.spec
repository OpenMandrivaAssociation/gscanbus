%define name gscanbus
%define version 0.7.1
%define release %mkrel 8

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


