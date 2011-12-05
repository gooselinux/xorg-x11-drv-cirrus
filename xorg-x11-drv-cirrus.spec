%define tarball xf86-video-cirrus
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:   Xorg X11 cirrus video driver
Name:      xorg-x11-drv-cirrus
Version:   1.3.2
Release:   1.1%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

ExcludeArch: s390 s390x

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
Source1:   cirrus.xinf

Patch0:	    cirrus-1.2.0-qemu.patch

BuildRequires: xorg-x11-server-sdk >= 1.5.99.902
BuildRequires: xorg-x11-util-macros >= 1.1.5

Requires:  hwdata
Requires:  xorg-x11-server-Xorg >= 1.5.99.902

%description 
X.Org X11 cirrus video driver.

%prep
%setup -q -n %{tarball}-%{version}
%patch0 -p1 -b .qemu

%build
%configure --disable-static
make -s %{_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases/

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/cirrus_drv.so
%{driverdir}/cirrus_alpine.so
%{driverdir}/cirrus_laguna.so
%{_datadir}/hwdata/videoaliases/cirrus.xinf
%{_mandir}/man4/cirrus.4*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.3.2-1.1
- Rebuilt for RHEL 6

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 1.3.2-1
- cirrus 1.3.2

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 1.3.1-1.1
- ABI bump

* Thu Jul 02 2009 Adam Jackson <ajax@redhat.com> 1.3.1-1
- cirrus 1.3.1

* Mon Jun 22 2009 Adam Jackson <ajax@redhat.com> 1.3.0-2
- Fix ABI for new server

* Mon May 18 2009 Adam Jackson <ajax@redhat.com> 1.3.0-1
- cirrus 1.3.0

* Fri Feb 27 2009 Adam Jackson <ajax@redhat.com> 1.2.0-6
- Fix the qemu patch to, uh, work.

* Fri Feb 27 2009 Adam Jackson <ajax@redhat.com> 1.2.0-5
- cirrus-1.2.0-qemu.patch: Detect qemu virtual video when we can, and default
  to 1024x768 in that case. (#251264)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 08 2009 Adam Jackson <ajax@redhat.com> 1.2.0-3
- Re-bump, previous build didn't get the right buildroot.

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 1.2.0-2
- bump for server API

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 1.2.0-1
- Latest upstream release

* Thu Mar 13 2008 Dave Airlie <airlied@redhat.com> 1.1.0-9
- fix cirrus with no xorg.conf in qemu

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.0-8
- Autorebuild for GCC 4.3

* Mon Jan 21 2008 Dave Airlie <airlied@redhat.com> - 1.1.0-7
- make cirrus work with pciaccess in qemu

* Thu Jan 17 2008 Dave Airlie <airlied@redhat.com> - 1.1.0-6
- update for new server build and pciaccess

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 1.1.0-5
- Rebuild for PPC toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 1.1.0-4
- Update Requires and BuildRequires.  Disown the module directories.  Add
  Requires: hwdata.

* Thu Feb 15 2007 Adam Jackson <ajax@redhat.com> 1.1.0-3
- ExclusiveArch -> ExcludeArch

* Mon Aug 21 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-2.fc6
- Un-ExclusiveArch x86, as it should work everywhere and makes qemu much
  happier.  (#203373)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 1.1.0-1.1
- rebuild

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-1
- Update to 1.1.0 from 7.1RC1.

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0.5-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.0.5-1
- Updated xorg-x11-drv-cirrus to version 1.0.0.5 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.4-1
- Updated xorg-x11-drv-cirrus to version 1.0.0.4 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.
- Added cirrus_alpine.so, cirrus_laguna.so to the file manifest.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.2-1
- Updated xorg-x11-drv-cirrus to version 1.0.0.2 from X11R7 RC2

* Fri Nov 4 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.1-1
- Updated xorg-x11-drv-cirrus to version 1.0.0.1 from X11R7 RC1
- Fix *.la file removal.

* Mon Oct 3 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Update BuildRoot to use Fedora Packaging Guidelines.
- Deglob file manifest.
- Set "ExclusiveArch: %{ix86}"

* Fri Sep 2 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-0
- Initial spec file for cirrus video driver generated automatically
  by my xorg-driverspecgen script.
