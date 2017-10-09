# This file is autogenerated by running
#  ./dhs/precheckin.sh 
# Please edit droid-src-syspart-f5121.spec.tmpl and re-run that command to modify

# device is the codename for the device
%define device suzu

%define ha_device_override f5121

# repo service performed : %%include define-trees
%define dhs_trees art development prebuilts/qemu-kernel sdk abi bionic bootable build device external frameworks hardware kernel libcore libnativehelper prebuilts/clang/linux-x86 prebuilts/gcc/linux-x86 prebuilts/misc prebuilts/ndk prebuilts/sdk prebuilts/tools system vendor

%define device_variant -userdebug
%define lunch_device aosp_f5121
%define pre_actions sudo update-java-alternatives -s java-1.7.0-openjdk-amd64

%define dhs_flavour syspart

# Our promotions fail, because rpm v4.9 can't handle conditional macros well, see JB#33275
# Let's work around it for now:
#define dhs_name_hardcoded droid-src-%{ha_device_override}
# If dhs_flavour is set to e.g. syspart, then the hardcoded name should be:
%define dhs_name_hardcoded droid-src-%{dhs_flavour}-%{ha_device_override}

%define dhs_sources \
Source52: %{dhs_name_hardcoded}.spec.tmpl\
Source53: additional-source.paths\
%{nil}

# repo service performed : %%include dhs/droid-hal-source.inc
# This file should be %%included into a device specific spec file
# where macros are defined:
# device:            should be the CM codename or the AOSP TARGET_PRODUCT
# hadk_make_target:  the target used when running make in the HABUILD_SDK on the
#                      OBS. Defaults to "hybris-hal"
# device_variant:    for AOSP this is used as the TARGET_BUILD_VARIANT for lunch
# lunch_device:      cases where the lunch combo is different from device name.
#                      For example, it's "aosp_f5121" for the "suzu" device
# have_vendor_src_for_obs:
#                    include a separately packaged vendor source for OBS builds

%define __provides_exclude_from ^%{_libexecdir}/droid-hybris/.*$
%define android_root .

%define __find_provides %{nil}
%define __find_requires %{nil}
%define __strip /bin/true
%define __provides_exclude_from ^/system/.*$
%define __requires_exclude ^.*$
%global debug_package %{nil}

# Support build info extracted from OBS builds too
%if 0%{?_obs_build_project:1}
%define _build_flavour %(echo %{_obs_build_project} | awk -F : '{if ($NF == "testing" || $NF == "release") print $NF; else if ($NF ~ /[0-9]\.[0-9]\.[0-9]/ && NF == 3) print strdevel; else if (NF == 2) print strdevel; else print strunknown}' strdevel=devel strunknown=unknown)
%else
%define _build_flavour unknown
%endif

%define _obs_build_count %(echo %{release} | awk -F . '{if (NF >= 3) print $3; else print $1 }')
%define _obs_commit_count %(echo %{release} | awk -F . '{if (NF >= 2) print $2; else print $1 }')

%if "%{_build_flavour}" == "release"
%define _version_appendix (%{_target_cpu})
%else
%define _version_appendix (%{_target_cpu},%{_build_flavour})
%endif

%if 0%{?ha_device_override:1}
%define ha_device %{ha_device_override}
%else
%define ha_device %{device}
%endif

%if 0%{?dhs_flavour:1}
%define dhs_feature droid-src-%{dhs_flavour}
%else
%define dhs_feature droid-src
%endif

%define dhs_name %{dhs_feature}-%{ha_device}

# if dhs_flavour is not defined, means we're building a generic droid-src, and
# for backwards compatibility we'll need to provide droid-bin and others
%if 0%{?dhs_flavour:1}
%define dhs_legacy 0
%else
%define dhs_legacy 1
%endif

# Don't run strip
%define __strip /bin/true

Summary: 	Droid SRC package for %{ha_device}%{?dhs_flavour:, %{dhs_flavour} flavour}
License: 	BSD-3-Clause
Name: 		%{dhs_name_hardcoded}
Version: 	0.0.0.1
# timestamped releases are used only for HADK (mb2) builds
%if 0%{?_obs_build_project:1}
Release:	1
%else
Release:	%(date +'%%Y%%m%%d%%H%%M')
%endif
Provides:	%{dhs_feature}
%if %{dhs_legacy}
Provides:	droid-bin
%endif
# The repo sync service on OBS prepares a 'source tarball' of the rpm
# dir since we currently have a complex setup with subdirs which OBS
# doesn't like. This is not a problem for local builds.
Source0: 	rpm.tar.bzip2
# Ths actual droid source from the repo service when run on OBS.
# local builds don't mind if this is missing
Source40:       repo.tar.bzip2
# Reserve Source50 onwards
# Allow device specific sources to be defined using dhs_sources
%{?dhs_sources}

Group:		System

# droid-src does not build any binaries, just bundles sources
BuildArch:      noarch

%if 0%{?_obs_build_project:1}
%if 0%{?have_vendor_src_for_obs:1}
BuildRequires:  droid-system-vendor-obsbuild
%endif
%endif

# Ignore the rpmlint-* to avoid long RPMLINT reporting
#!BuildIgnore: rpmlint-mini
#!BuildIgnore: rpmlint-MeeGo
# Don't run any of the MeeGo brp-strip-* or other install_post validation commands
%define __os_install_post %{nil}

%description
%{summary}.

%if 0%{?dhs_trees:1}
# repo service performed : %%include package-section
%package dhs-full
Provides: %{dhs_feature}-full
%if %{dhs_legacy}
Provides: droid-bin-src-full
%endif
Group:  System
AutoReqProv: no
Requires(post): /bin/sh
Requires: %{dhs_feature}-dhs-rootdir %{dhs_feature}-art %{dhs_feature}-development %{dhs_feature}-prebuilts-qemu-kernel %{dhs_feature}-sdk %{dhs_feature}-abi %{dhs_feature}-bionic %{dhs_feature}-bootable %{dhs_feature}-build %{dhs_feature}-device %{dhs_feature}-external %{dhs_feature}-frameworks %{dhs_feature}-hardware %{dhs_feature}-kernel %{dhs_feature}-libcore %{dhs_feature}-libnativehelper %{dhs_feature}-prebuilts-clang-linux-x86 %{dhs_feature}-prebuilts-gcc-linux-x86 %{dhs_feature}-prebuilts-misc %{dhs_feature}-prebuilts-ndk %{dhs_feature}-prebuilts-sdk %{dhs_feature}-prebuilts-tools %{dhs_feature}-system %{dhs_feature}-vendor
Summary: Syspart source for all the src trees to be used for droid-side code building
%description dhs-full
This is the full src tree for the %{dhs_name} manifest.
It is only meant for use in the OBS.

%package dhs-utils
Provides: %{dhs_feature}-dhs-utils
Group:  System
AutoReqProv: no
Requires(post): /bin/sh
Summary: Utilities for droid-side code building for %{device}%{?device_variant}
%description dhs-utils
Summary: Utilities for using the syspart source for droid-side code building.
This package is hardcoded for %{device}%{?device_variant}
It is only meant for use in the OBS.

%package dhs-makefile
Provides: %{dhs_feature}-dhs-makefile
Group:  System
AutoReqProv: no
Requires(post): /bin/sh
Summary: Top level makefile to be used for droid-side code building
%description dhs-makefile
Top level makefile to be used for droid-side code building
It is only meant for use in the OBS.

%package dhs-rootdir
Provides: %{dhs_feature}-dhs-rootdir
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Top level source files for the device src tree to be used for droid-side code building
%description dhs-rootdir
This is the src tree for the files in the root directory from the %device manifest.
It is only meant for use in the OBS.

%package art
Provides: %{dhs_feature}-art
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the art src tree to be used for droid-side code building
%description art
This is the src tree for the art subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package development
Provides: %{dhs_feature}-development
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the development src tree to be used for droid-side code building
%description development
This is the src tree for the development subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package prebuilts-qemu-kernel
Provides: %{dhs_feature}-prebuilts-qemu-kernel
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the prebuilts-qemu-kernel src tree to be used for droid-side code building
%description prebuilts-qemu-kernel
This is the src tree for the prebuilts-qemu-kernel subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package sdk
Provides: %{dhs_feature}-sdk
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the sdk src tree to be used for droid-side code building
%description sdk
This is the src tree for the sdk subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package abi
Provides: %{dhs_feature}-abi
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the abi src tree to be used for droid-side code building
%description abi
This is the src tree for the abi subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package bionic
Provides: %{dhs_feature}-bionic
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the bionic src tree to be used for droid-side code building
%description bionic
This is the src tree for the bionic subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package bootable
Provides: %{dhs_feature}-bootable
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the bootable src tree to be used for droid-side code building
%description bootable
This is the src tree for the bootable subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package build
Provides: %{dhs_feature}-build
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the build src tree to be used for droid-side code building
%description build
This is the src tree for the build subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package device
Provides: %{dhs_feature}-device
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the device src tree to be used for droid-side code building
%description device
This is the src tree for the device subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package external
Provides: %{dhs_feature}-external
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the external src tree to be used for droid-side code building
%description external
This is the src tree for the external subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package frameworks
Provides: %{dhs_feature}-frameworks
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the frameworks src tree to be used for droid-side code building
%description frameworks
This is the src tree for the frameworks subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package hardware
Provides: %{dhs_feature}-hardware
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the hardware src tree to be used for droid-side code building
%description hardware
This is the src tree for the hardware subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package kernel
Provides: %{dhs_feature}-kernel
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the kernel src tree to be used for droid-side code building
%description kernel
This is the src tree for the kernel subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package libcore
Provides: %{dhs_feature}-libcore
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the libcore src tree to be used for droid-side code building
%description libcore
This is the src tree for the libcore subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package libnativehelper
Provides: %{dhs_feature}-libnativehelper
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the libnativehelper src tree to be used for droid-side code building
%description libnativehelper
This is the src tree for the libnativehelper subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package prebuilts-clang-linux-x86
Provides: %{dhs_feature}-prebuilts-clang-linux-x86
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the prebuilts-clang-linux-x86 src tree to be used for droid-side code building
%description prebuilts-clang-linux-x86
This is the src tree for the prebuilts-clang-linux-x86 subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package prebuilts-gcc-linux-x86
Provides: %{dhs_feature}-prebuilts-gcc-linux-x86
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the prebuilts-gcc-linux-x86 src tree to be used for droid-side code building
%description prebuilts-gcc-linux-x86
This is the src tree for the prebuilts-gcc-linux-x86 subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package prebuilts-misc
Provides: %{dhs_feature}-prebuilts-misc
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the prebuilts-misc src tree to be used for droid-side code building
%description prebuilts-misc
This is the src tree for the prebuilts-misc subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package prebuilts-ndk
Provides: %{dhs_feature}-prebuilts-ndk
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the prebuilts-ndk src tree to be used for droid-side code building
%description prebuilts-ndk
This is the src tree for the prebuilts-ndk subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package prebuilts-sdk
Provides: %{dhs_feature}-prebuilts-sdk
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the prebuilts-sdk src tree to be used for droid-side code building
%description prebuilts-sdk
This is the src tree for the prebuilts-sdk subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package prebuilts-tools
Provides: %{dhs_feature}-prebuilts-tools
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the prebuilts-tools src tree to be used for droid-side code building
%description prebuilts-tools
This is the src tree for the prebuilts-tools subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package system
Provides: %{dhs_feature}-system
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the system src tree to be used for droid-side code building
%description system
This is the src tree for the system subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%package vendor
Provides: %{dhs_feature}-vendor
Group:  System
AutoReqProv: no
Requires: %{dhs_feature}-dhs-utils %{dhs_feature}-dhs-makefile
Requires(post): /bin/sh
Summary: Source for the vendor src tree to be used for droid-side code building
%description vendor
This is the src tree for the vendor subdirectory from the %{device} manifest.
It is only meant for use in the OBS.

%endif

%prep
# No %%setup macro !!

%if 0%{?_obs_build_project:1}
# The OBS does not have access to 'repo' so a service does the repo init/sync
# and provides a (huge) tarball with the checked-out tree in it.
# So now drop to android_root and pretend to do a repo sync
tar xf %{SOURCE40} -C %android_root
# Clean up the repo tarball to save space
rm -f %{SOURCE40}
# Make a dummy tarball for rpm checks
mkdir dummy;(cd dummy; touch dummy; tar cvf - . | bzip2 > %{SOURCE40}); rm -rf dummy
# unpack the directories to SOURCES ... this needs to change
tar xf %{SOURCE0} -C ../SOURCES
# Clean up the rpm tarball too
rm -f %{SOURCE0}
cp %{SOURCE40} %{SOURCE0}

%if 0%{?have_vendor_src_for_obs:1}
# Copy SW binaries to the build dir (provided by droid-system-vendor-obsbuild)
cp -ar /vendor .
%endif

# In OBS the repo service leaves the rpm/* files for OBS and they just ^^
# got unpacked to ../SOURCES ... but we're used to having an rpm/ dir
# So if rpm/ is missing then we use ../SOURCES :
[ -d rpm ] || ln -s ../SOURCES rpm
%endif

%build

# We'll hardcode the device/variant information into the droid-make
# script This isn't trivially installable into the ubu-chroot so
# include the ubu-chroot command within it
cat <<"EOF" > droid-make
#!/bin/bash

# This command runs a hardware-specific 'make' command inside the
# ubu-chroot with the correct lunch setup
# It is only intended to run in the OBS builders

exec ubu-chroot -r /srv/mer/sdks/ubu "%{?pre_actions}; source build/envsetup.sh; lunch %{?lunch_device}%{!?lunch_device:%{device}}%{?device_variant}; make $*"
EOF

################
%install
rm -rf $RPM_BUILD_ROOT

# Support the building of src-* rpms and srcutils if they're wanted
%if 0%{?dhs_trees:1}
# To create a set of rpms that hold the *source* we move the subset of
# src to the buildroot for packaging
# These will be used to create buildroots for packages like droidmedia
mkdir -p $RPM_BUILD_ROOT/home/abuild/src/droid
for tree in %dhs_trees ; do
   d=$(dirname $tree)
   mkdir -p $RPM_BUILD_ROOT/home/abuild/src/droid/$d
   mv %android_root/$tree $RPM_BUILD_ROOT/home/abuild/src/droid/$d
done

# Top level makefile
mv %android_root/Makefile $RPM_BUILD_ROOT/home/abuild/src/droid/

# Install the droid-make helper
mkdir -p $RPM_BUILD_ROOT/usr/bin
cp droid-make $RPM_BUILD_ROOT/usr/bin

rm -rf tmp/
mkdir tmp/

find %android_root -maxdepth 1 \( -type f -or -type l \) -print -exec mv {} $RPM_BUILD_ROOT/home/abuild/src/droid/ \; | sed 's ^%android_root /home/abuild/src/droid ' >> tmp/rootdir.files

%endif

################################################################
# Begin files section

#files
#defattr(-,root,root,-)

%if 0%{?dhs_trees:1}
# repo service performed : %%include files-section
%files dhs-full
# Deliberately empty

%files dhs-utils
%defattr(755,root,root,-)
/usr/bin/droid-make

%post dhs-makefile
# The abuild user is not setup at post time so we use the numeric id
chown 399:399 /home/abuild/src
chown 399:399 /home/abuild/src/droid
chown 399:399 /home/abuild/src/droid/Makefile

%files dhs-makefile
%defattr(-,root,root,-)
/home/abuild/src/droid/Makefile

%post dhs-rootdir
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/

%files dhs-rootdir -f tmp/rootdir.files
%defattr(-,root,root,-)

%post art
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/art
%files art
%defattr(-,root,root,-)
/home/abuild/src/droid/art

%post development
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/development
%files development
%defattr(-,root,root,-)
/home/abuild/src/droid/development

%post prebuilts-qemu-kernel
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/prebuilts/qemu-kernel
%files prebuilts-qemu-kernel
%defattr(-,root,root,-)
/home/abuild/src/droid/prebuilts/qemu-kernel

%post sdk
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/sdk
%files sdk
%defattr(-,root,root,-)
/home/abuild/src/droid/sdk

%post abi
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/abi
%files abi
%defattr(-,root,root,-)
/home/abuild/src/droid/abi

%post bionic
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/bionic
%files bionic
%defattr(-,root,root,-)
/home/abuild/src/droid/bionic

%post bootable
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/bootable
%files bootable
%defattr(-,root,root,-)
/home/abuild/src/droid/bootable

%post build
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/build
%files build
%defattr(-,root,root,-)
/home/abuild/src/droid/build

%post device
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/device
%files device
%defattr(-,root,root,-)
/home/abuild/src/droid/device

%post external
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/external
%files external
%defattr(-,root,root,-)
/home/abuild/src/droid/external

%post frameworks
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/frameworks
%files frameworks
%defattr(-,root,root,-)
/home/abuild/src/droid/frameworks

%post hardware
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/hardware
%files hardware
%defattr(-,root,root,-)
/home/abuild/src/droid/hardware

%post kernel
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/kernel
%files kernel
%defattr(-,root,root,-)
/home/abuild/src/droid/kernel

%post libcore
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/libcore
%files libcore
%defattr(-,root,root,-)
/home/abuild/src/droid/libcore

%post libnativehelper
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/libnativehelper
%files libnativehelper
%defattr(-,root,root,-)
/home/abuild/src/droid/libnativehelper

%post prebuilts-clang-linux-x86
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/prebuilts/clang/linux-x86
%files prebuilts-clang-linux-x86
%defattr(-,root,root,-)
/home/abuild/src/droid/prebuilts/clang/linux-x86

%post prebuilts-gcc-linux-x86
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/prebuilts/gcc/linux-x86
%files prebuilts-gcc-linux-x86
%defattr(-,root,root,-)
/home/abuild/src/droid/prebuilts/gcc/linux-x86

%post prebuilts-misc
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/prebuilts/misc
%files prebuilts-misc
%defattr(-,root,root,-)
/home/abuild/src/droid/prebuilts/misc

%post prebuilts-ndk
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/prebuilts/ndk
%files prebuilts-ndk
%defattr(-,root,root,-)
/home/abuild/src/droid/prebuilts/ndk

%post prebuilts-sdk
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/prebuilts/sdk
%files prebuilts-sdk
%defattr(-,root,root,-)
/home/abuild/src/droid/prebuilts/sdk

%post prebuilts-tools
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/prebuilts/tools
%files prebuilts-tools
%defattr(-,root,root,-)
/home/abuild/src/droid/prebuilts/tools

%post system
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/system
%files system
%defattr(-,root,root,-)
/home/abuild/src/droid/system

%post vendor
# The abuild user is not setup at post time so we use the numeric id
chown -R 399:399 /home/abuild/src/droid/vendor
%files vendor
%defattr(-,root,root,-)
/home/abuild/src/droid/vendor

%endif

