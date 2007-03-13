#
# TODO: SVG
#
# Conditional build:
%bcond_without	docs		# don't build html documentation
#
%define ghc_version %(LC_ALL="C" ghc -V | sed 's/.*version //')

%define ghclibdir %{_libdir}/ghc-%{ghc_version}

Summary:	A Haskell GUI library based on the Gtk+ GUI toolkit
Summary(pl.UTF-8):	Biblioteka GUI dla Haskella oparta na Gtk+
Name:		gtk2hs
Version:	0.9.11
Release:	0.2
License:	LGPL
Group:		Development/Libraries
#Group:		Development/Languages/Haskell
Source0:	http://downloads.sourceforge.net/gtk2hs/%{name}-%{version}.tar.gz
# Source0-md5:	a59f19d15ae0cab976722dbf3a09fc14
URL:		http://haskell.org/gtk2hs/
BuildRequires:	GConf2-devel
BuildRequires:	cairo-devel >= 1.0.0
BuildRequires:	ghc >= 6.0
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtkglext-devel >= 1.0.5
BuildRequires:	gtksourceview-devel
%{?with_docs:BuildRequires:	haddock}
BuildRequires:	libglade2-devel
BuildRequires:	librsvg-devel >= 1:2.16.0
BuildRequires:	xulrunner-devel
Requires(post,preun):	%{_bindir}/ghc-pkg
%requires_eq	ghc
Requires:	gtk+2-devel
Requires:	gtk2hs-cairo = %{version}-%{release}
Requires:	gtk2hs-glib = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Gtk+ binding for the functional language Haskell featuring automatic
memory management, unicode support, and wide coverage of widgets up to
Gtk+ 2.2 as well as some 2.4 widgets such as the new file chooser
dialog.

%package cairo
Summary:	Haskell binding for cairo
Group:		Development/Libraries
#Group:		Development/Languages/Haskell
Requires(post,preun):	%{_bindir}/ghc-pkg
Requires:	cairo-devel >= 1.0.0
%requires_eq	ghc

%description cairo
A cairo binding for gtk2hs.

%package gconf
Summary:	Haskell binding for GConf
Group:		Development/Libraries
#Group:		Development/Languages/Haskell
Requires(post,preun):	%{_bindir}/ghc-pkg
Requires:	GConf2-devel
%requires_eq	ghc
Requires:	gtk2hs-glib = %{version}-%{release}

%description gconf
A GConf binding for gtk2hs.

%package glade
Summary:	Haskell binding of glade for gtk2hs
Group:		Development/Libraries
#Group:		Development/Languages/Haskell
Requires(post,preun):	%{_bindir}/ghc-pkg
%requires_eq	ghc
Requires:	libglade2-devel
Requires:	gtk2hs = %{version}-%{release}

%description glade
A Glade2 binding for gtk2hs.

%package glib
Summary:	Haskell binding for glib
Group:		Development/Libraries
#Group:		Development/Languages/Haskell
Requires(post,preun):	%{_bindir}/ghc-pkg
%requires_eq	ghc
Requires:	glib2-devel

%description glib
A glib binding for gtk2hs.

%package mozembed
Summary:	Haskell binding for gtkembedmoz
Group:		Development/Libraries
#Group:		Development/Languages/Haskell
Requires(post,preun):	%{_bindir}/ghc-pkg
%requires_eq	ghc
Requires:	gtk2hs = %{version}-%{release}
Requires:	xulrunner-devel

%description mozembed
A GtkEmbedMoz binding for gtk2hs.

%package sourceview
Summary:	Haskell binding for gtksourceview
Group:		Development/Libraries
#Group:		Development/Languages/Haskell
Requires(post,preun):	%{_bindir}/ghc-pkg
%requires_eq	ghc
Requires:	gtk2hs = %{version}-%{release}
Requires:	gtksourceview-devel

%description sourceview
A GtkSourceView binding for gtk2hs.

%package gtkglext
Summary:	Haskell binding for gtkglext
Group:		Development/Libraries
#Group:		Development/Languages/Haskell
Requires(post,preun):	%{_bindir}/ghc-pkg
%requires_eq	ghc
Requires:	gtk2hs = %{version}-%{release}
Requires:	gtkglext-devel >= 1.0.5

%description gtkglext
A GtkGLExt binding for gtk2hs.

%prep
%setup -q

%build
%configure \
	--with-hcflags="-O"  \
	--libdir=%{ghclibdir} \
	%{?with_docs:--enable-docs} \
	--enable-libglade \
	--enable-gconf \
	--enable-sourceview \
	--enable-cairo \
	--enable-opengl \
	--enable-svg \
	--enable-xulrunner \
	--disable-firefox \
	--disable-seamonkey \
	--disable-mozilla \
	--disable-deprecated \
	--without-pkgreg

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
ghc-pkg register %{ghclibdir}/gtk2hs/gtk.package.conf
ghc-pkg register %{ghclibdir}/gtk2hs/soegtk.package.conf

%preun
if [ "$1" = 0 ]; then
  ghc-pkg unregister soegtk
  ghc-pkg unregister gtk
fi

%post cairo
ghc-pkg register %{ghclibdir}/gtk2hs/cairo.package.conf

%preun cairo
if [ "$1" = 0 ]; then
  ghc-pkg unregister cairo
fi

%post gconf
ghc-pkg register %{ghclibdir}/gtk2hs/gconf.package.conf

%preun gconf
if [ "$1" = 0 ]; then
  ghc-pkg unregister gconf
fi

%post glade
ghc-pkg register %{ghclibdir}/gtk2hs/glade.package.conf

%preun glade
if [ "$1" = 0 ]; then
  ghc-pkg unregister glade
fi

%post glib
ghc-pkg register %{ghclibdir}/gtk2hs/glib.package.conf

%preun glib
if [ "$1" = 0 ]; then
  ghc-pkg unregister glib
fi

%post mozembed
ghc-pkg register %{ghclibdir}/gtk2hs/mozembed.package.conf

%preun mozembed
if [ "$1" = 0 ]; then
  ghc-pkg unregister mozembed
fi

%post sourceview
ghc-pkg register %{ghclibdir}/gtk2hs/sourceview.package.conf

%preun sourceview
if [ "$1" = 0 ]; then
  ghc-pkg unregister sourceview
fi

%post gtkglext
ghc-pkg register %{ghclibdir}/gtk2hs/gtkglext.package.conf

%preun gtkglext
if [ "$1" = 0 ]; then
  ghc-pkg unregister gtkglext
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%{?with_docs:%doc docs/reference}
%{ghclibdir}/gtk2hs/gtk.package.conf
%{ghclibdir}/gtk2hs/soegtk.package.conf
%{ghclibdir}/gtk2hs/HSgtk.o
%{ghclibdir}/gtk2hs/HSsoegtk.o
%{ghclibdir}/gtk2hs/libHSgtk.a
%{ghclibdir}/gtk2hs/libHSsoegtk.a
%{ghclibdir}/gtk2hs/include/gtk2hs-config.h
%{ghclibdir}/gtk2hs/imports/gtk
%{ghclibdir}/gtk2hs/imports/soegtk

%files cairo
%defattr(644,root,root,755)
%{ghclibdir}/gtk2hs/cairo.package.conf
%{ghclibdir}/gtk2hs/HScairo.o
%{ghclibdir}/gtk2hs/libHScairo.a
%{ghclibdir}/gtk2hs/imports/cairo

%files gconf
%defattr(644,root,root,755)
%{ghclibdir}/gtk2hs/gconf.package.conf
%{ghclibdir}/gtk2hs/HSgconf.o
%{ghclibdir}/gtk2hs/libHSgconf.a
%{ghclibdir}/gtk2hs/imports/gconf

%files glade
%defattr(644,root,root,755)
%{ghclibdir}/gtk2hs/glade.package.conf
%{ghclibdir}/gtk2hs/HSglade.o
%{ghclibdir}/gtk2hs/libHSglade.a
%{ghclibdir}/gtk2hs/imports/glade

%files glib
%defattr(644,root,root,755)
%dir %{ghclibdir}/gtk2hs
%dir %{ghclibdir}/gtk2hs/imports
%{ghclibdir}/gtk2hs/glib.package.conf
%{ghclibdir}/gtk2hs/HSglib.o
%{ghclibdir}/gtk2hs/libHSglib.a
%{ghclibdir}/gtk2hs/imports/glib

%files mozembed
%defattr(644,root,root,755)
%{ghclibdir}/gtk2hs/mozembed.package.conf
%{ghclibdir}/gtk2hs/HSmozembed.o
%{ghclibdir}/gtk2hs/libHSmozembed.a
%{ghclibdir}/gtk2hs/imports/mozembed

%files sourceview
%defattr(644,root,root,755)
%{ghclibdir}/gtk2hs/sourceview.package.conf
%{ghclibdir}/gtk2hs/HSsourceview.o
%{ghclibdir}/gtk2hs/libHSsourceview.a
%{ghclibdir}/gtk2hs/imports/sourceview

%files gtkglext
%defattr(644,root,root,755)
%{ghclibdir}/gtk2hs/gtkglext.package.conf
%{ghclibdir}/gtk2hs/HSgtkglext.o
%{ghclibdir}/gtk2hs/libHSgtkglext.a
%{ghclibdir}/gtk2hs/imports/gtkglext
