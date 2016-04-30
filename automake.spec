Name     : automake
Version  : 1.15
Release  : 15
URL      : http://mirrors.kernel.org/gnu/automake/automake-1.15.tar.xz
Source0  : http://mirrors.kernel.org/gnu/automake/automake-1.15.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: automake-bin
Requires: automake-data
Requires: automake-doc
BuildRequires : bison
BuildRequires : flex
BuildRequires : gfortran
Patch1: automake-1.15-perl-escape-curly-bracket.patch

%description
This is Automake, a Makefile generator.  It aims to be portable and
to conform to the GNU Coding Standards for Makefile variables and
targets.

%package bin
Summary: bin components for the automake package.
Group: Binaries
Requires: automake-data

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
Requires: automake-bin
Requires: automake-data

%description dev
dev components for the automake package.


%package doc
Summary: doc components for the automake package.
Group: Documentation

%description doc
doc components for the automake package.


%prep
%setup -q -n automake-1.15
%patch1 -p1 

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make V=1 %{?_smp_mflags} check ||:

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/aclocal
/usr/bin/aclocal-1.15
/usr/bin/automake
/usr/bin/automake-1.15

%files data
%defattr(-,root,root,-)
/usr/share/aclocal-1.15/internal/ac-config-macro-dirs.m4
/usr/share/aclocal/README
/usr/share/automake-1.15/Automake/ChannelDefs.pm
/usr/share/automake-1.15/Automake/Channels.pm
/usr/share/automake-1.15/Automake/Condition.pm
/usr/share/automake-1.15/Automake/Config.pm
/usr/share/automake-1.15/Automake/Configure_ac.pm
/usr/share/automake-1.15/Automake/DisjConditions.pm
/usr/share/automake-1.15/Automake/FileUtils.pm
/usr/share/automake-1.15/Automake/General.pm
/usr/share/automake-1.15/Automake/Getopt.pm
/usr/share/automake-1.15/Automake/Item.pm
/usr/share/automake-1.15/Automake/ItemDef.pm
/usr/share/automake-1.15/Automake/Language.pm
/usr/share/automake-1.15/Automake/Location.pm
/usr/share/automake-1.15/Automake/Options.pm
/usr/share/automake-1.15/Automake/Rule.pm
/usr/share/automake-1.15/Automake/RuleDef.pm
/usr/share/automake-1.15/Automake/VarDef.pm
/usr/share/automake-1.15/Automake/Variable.pm
/usr/share/automake-1.15/Automake/Version.pm
/usr/share/automake-1.15/Automake/Wrap.pm
/usr/share/automake-1.15/Automake/XFile.pm
/usr/share/automake-1.15/COPYING
/usr/share/automake-1.15/INSTALL
/usr/share/automake-1.15/am/check.am
/usr/share/automake-1.15/am/check2.am
/usr/share/automake-1.15/am/clean-hdr.am
/usr/share/automake-1.15/am/clean.am
/usr/share/automake-1.15/am/compile.am
/usr/share/automake-1.15/am/configure.am
/usr/share/automake-1.15/am/data.am
/usr/share/automake-1.15/am/dejagnu.am
/usr/share/automake-1.15/am/depend.am
/usr/share/automake-1.15/am/depend2.am
/usr/share/automake-1.15/am/distdir.am
/usr/share/automake-1.15/am/footer.am
/usr/share/automake-1.15/am/header-vars.am
/usr/share/automake-1.15/am/header.am
/usr/share/automake-1.15/am/inst-vars.am
/usr/share/automake-1.15/am/install.am
/usr/share/automake-1.15/am/java.am
/usr/share/automake-1.15/am/lang-compile.am
/usr/share/automake-1.15/am/lex.am
/usr/share/automake-1.15/am/library.am
/usr/share/automake-1.15/am/libs.am
/usr/share/automake-1.15/am/libtool.am
/usr/share/automake-1.15/am/lisp.am
/usr/share/automake-1.15/am/ltlib.am
/usr/share/automake-1.15/am/ltlibrary.am
/usr/share/automake-1.15/am/mans-vars.am
/usr/share/automake-1.15/am/mans.am
/usr/share/automake-1.15/am/program.am
/usr/share/automake-1.15/am/progs.am
/usr/share/automake-1.15/am/python.am
/usr/share/automake-1.15/am/remake-hdr.am
/usr/share/automake-1.15/am/scripts.am
/usr/share/automake-1.15/am/subdirs.am
/usr/share/automake-1.15/am/tags.am
/usr/share/automake-1.15/am/texi-vers.am
/usr/share/automake-1.15/am/texibuild.am
/usr/share/automake-1.15/am/texinfos.am
/usr/share/automake-1.15/am/vala.am
/usr/share/automake-1.15/am/yacc.am
/usr/share/automake-1.15/ar-lib
/usr/share/automake-1.15/compile
/usr/share/automake-1.15/config.guess
/usr/share/automake-1.15/config.sub
/usr/share/automake-1.15/depcomp
/usr/share/automake-1.15/install-sh
/usr/share/automake-1.15/mdate-sh
/usr/share/automake-1.15/missing
/usr/share/automake-1.15/mkinstalldirs
/usr/share/automake-1.15/py-compile
/usr/share/automake-1.15/tap-driver.sh
/usr/share/automake-1.15/test-driver
/usr/share/automake-1.15/texinfo.tex
/usr/share/automake-1.15/ylwrap

%files dev
%defattr(-,root,root,-)
/usr/share/aclocal-1.*/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/automake/*
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
