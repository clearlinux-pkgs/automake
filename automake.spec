#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7FD9FCCB000BEEEE (meyering@fb.com)
#
Name     : automake
Version  : 1.16.3
Release  : 26
URL      : https://mirrors.kernel.org/gnu/automake/automake-1.16.3.tar.xz
Source0  : https://mirrors.kernel.org/gnu/automake/automake-1.16.3.tar.xz
Source1  : https://mirrors.kernel.org/gnu/automake/automake-1.16.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: automake-bin = %{version}-%{release}
Requires: automake-data = %{version}-%{release}
Requires: automake-info = %{version}-%{release}
Requires: automake-license = %{version}-%{release}
Requires: automake-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : cscope
BuildRequires : ctags
BuildRequires : docutils
BuildRequires : expect
BuildRequires : flex
BuildRequires : gfortran

%description
This is Automake, a Makefile generator.  It aims to be portable and
to conform to the GNU Coding Standards for Makefile variables and
targets.

%package bin
Summary: bin components for the automake package.
Group: Binaries
Requires: automake-data = %{version}-%{release}
Requires: automake-license = %{version}-%{release}

%description bin
bin components for the automake package.


%package data
Summary: data components for the automake package.
Group: Data

%description data
data components for the automake package.


%package dev
Summary: dev components for the automake package.
Group: Development
Requires: automake-bin = %{version}-%{release}
Requires: automake-data = %{version}-%{release}
Provides: automake-devel = %{version}-%{release}
Requires: automake = %{version}-%{release}

%description dev
dev components for the automake package.


%package doc
Summary: doc components for the automake package.
Group: Documentation
Requires: automake-man = %{version}-%{release}
Requires: automake-info = %{version}-%{release}

%description doc
doc components for the automake package.


%package info
Summary: info components for the automake package.
Group: Default

%description info
info components for the automake package.


%package license
Summary: license components for the automake package.
Group: Default

%description license
license components for the automake package.


%package man
Summary: man components for the automake package.
Group: Default

%description man
man components for the automake package.


%prep
%setup -q -n automake-1.16.3
cd %{_builddir}/automake-1.16.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605803835
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1605803835
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/automake
cp %{_builddir}/automake-1.16.3/COPYING %{buildroot}/usr/share/package-licenses/automake/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/automake-1.16.3/lib/COPYING %{buildroot}/usr/share/package-licenses/automake/31a3d460bb3c7d98845187c716a30db81c44b615
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/aclocal
/usr/bin/aclocal-1.16
/usr/bin/automake
/usr/bin/automake-1.16

%files data
%defattr(-,root,root,-)
/usr/share/aclocal-1.16/internal/ac-config-macro-dirs.m4
/usr/share/aclocal/README
/usr/share/automake-1.16/Automake/ChannelDefs.pm
/usr/share/automake-1.16/Automake/Channels.pm
/usr/share/automake-1.16/Automake/Condition.pm
/usr/share/automake-1.16/Automake/Config.pm
/usr/share/automake-1.16/Automake/Configure_ac.pm
/usr/share/automake-1.16/Automake/DisjConditions.pm
/usr/share/automake-1.16/Automake/FileUtils.pm
/usr/share/automake-1.16/Automake/General.pm
/usr/share/automake-1.16/Automake/Getopt.pm
/usr/share/automake-1.16/Automake/Item.pm
/usr/share/automake-1.16/Automake/ItemDef.pm
/usr/share/automake-1.16/Automake/Language.pm
/usr/share/automake-1.16/Automake/Location.pm
/usr/share/automake-1.16/Automake/Options.pm
/usr/share/automake-1.16/Automake/Rule.pm
/usr/share/automake-1.16/Automake/RuleDef.pm
/usr/share/automake-1.16/Automake/VarDef.pm
/usr/share/automake-1.16/Automake/Variable.pm
/usr/share/automake-1.16/Automake/Version.pm
/usr/share/automake-1.16/Automake/Wrap.pm
/usr/share/automake-1.16/Automake/XFile.pm
/usr/share/automake-1.16/COPYING
/usr/share/automake-1.16/INSTALL
/usr/share/automake-1.16/am/check.am
/usr/share/automake-1.16/am/check2.am
/usr/share/automake-1.16/am/clean-hdr.am
/usr/share/automake-1.16/am/clean.am
/usr/share/automake-1.16/am/compile.am
/usr/share/automake-1.16/am/configure.am
/usr/share/automake-1.16/am/data.am
/usr/share/automake-1.16/am/dejagnu.am
/usr/share/automake-1.16/am/depend.am
/usr/share/automake-1.16/am/depend2.am
/usr/share/automake-1.16/am/distdir.am
/usr/share/automake-1.16/am/footer.am
/usr/share/automake-1.16/am/header-vars.am
/usr/share/automake-1.16/am/header.am
/usr/share/automake-1.16/am/inst-vars.am
/usr/share/automake-1.16/am/install.am
/usr/share/automake-1.16/am/java.am
/usr/share/automake-1.16/am/lang-compile.am
/usr/share/automake-1.16/am/lex.am
/usr/share/automake-1.16/am/library.am
/usr/share/automake-1.16/am/libs.am
/usr/share/automake-1.16/am/libtool.am
/usr/share/automake-1.16/am/lisp.am
/usr/share/automake-1.16/am/ltlib.am
/usr/share/automake-1.16/am/ltlibrary.am
/usr/share/automake-1.16/am/mans-vars.am
/usr/share/automake-1.16/am/mans.am
/usr/share/automake-1.16/am/program.am
/usr/share/automake-1.16/am/progs.am
/usr/share/automake-1.16/am/python.am
/usr/share/automake-1.16/am/remake-hdr.am
/usr/share/automake-1.16/am/scripts.am
/usr/share/automake-1.16/am/subdirs.am
/usr/share/automake-1.16/am/tags.am
/usr/share/automake-1.16/am/texi-vers.am
/usr/share/automake-1.16/am/texibuild.am
/usr/share/automake-1.16/am/texinfos.am
/usr/share/automake-1.16/am/vala.am
/usr/share/automake-1.16/am/yacc.am
/usr/share/automake-1.16/ar-lib
/usr/share/automake-1.16/compile
/usr/share/automake-1.16/config.guess
/usr/share/automake-1.16/config.sub
/usr/share/automake-1.16/depcomp
/usr/share/automake-1.16/install-sh
/usr/share/automake-1.16/mdate-sh
/usr/share/automake-1.16/missing
/usr/share/automake-1.16/mkinstalldirs
/usr/share/automake-1.16/py-compile
/usr/share/automake-1.16/tap-driver.sh
/usr/share/automake-1.16/test-driver
/usr/share/automake-1.16/texinfo.tex
/usr/share/automake-1.16/ylwrap

%files dev
%defattr(-,root,root,-)
/usr/share/aclocal-1.*/*.m4

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/automake/*

%files info
%defattr(0644,root,root,0755)
/usr/share/info/automake-history.info
/usr/share/info/automake.info
/usr/share/info/automake.info-1
/usr/share/info/automake.info-2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/automake/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/automake/31a3d460bb3c7d98845187c716a30db81c44b615

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/aclocal-1.16.1
/usr/share/man/man1/aclocal.1
/usr/share/man/man1/automake-1.16.1
/usr/share/man/man1/automake.1
