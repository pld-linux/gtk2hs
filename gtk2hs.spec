#
# Conditional build:
%bcond_without	doc		# don't build html documentation
#
%define ghc_version %(LC_ALL="C" ghc -V | sed 's/.*version //')

%define ghclibdir %{_libdir}/ghc-%{ghc_version}

Summary:	A Haskell GUI library based on the GTK+ GUI toolkit
Summary(pl.UTF-8):	Biblioteka GUI dla Haskella oparta na GTK+
Name:		gtk2hs
Version:	0.9.12
Release:	1
License:	LGPL
Group:		Development/Libraries
#Group:		Development/Languages/Haskell
Source0:	http://downloads.sourceforge.net/gtk2hs/%{name}-%{version}.tar.gz
# Source0-md5:	32752a42c225f55b0280151f8e19a3ed
Patch0:		%{name}-CUInt.patch
URL:		http://haskell.org/gtk2hs/
BuildRequires:	GConf2-devel
BuildRequires:	cairo-devel >= 1.0.0
BuildRequires:	ghc >= 6.0
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtkglext-devel >= 1.0.5
BuildRequires:	gtksourceview-devel
%{?with_doc:BuildRequires:	haddock}
BuildRequires:	libglade2-devel
BuildRequires:	librsvg-devel >= 1:2.16.0
BuildRequires:	libsvg-cairo-devel >= 0.1.6
BuildRequires:	xulrunner-devel
Requires(post,preun):	%{_bindir}/ghc-pkg
%requires_eq	ghc
Requires:	cairo-devel >= 1.0.0
Requires:	glib2-devel
Requires:	gtk+2-devel
Obsoletes:	gtk2hs-cairo
Obsoletes:	gtk2hs-glib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GTK+ binding for the functional language Haskell featuring automatic
memory management, unicode support, and wide coverage of widgets up to
GTK+ 2.2 as well as some 2.4 widgets such as the new file chooser
dialog.

%description -l pl.UTF-8
Dowiązanie GTK+ dla języka funkcyjnego Haskell z automatycznym
zarządzeniem pamięcią, obsługą unikodu i szerokim pokryciem widgetów
do wersji GTK+ 2.2, a także częścią widgetów 2.4, takich jak nowe okno
dialogowe wyboru plików.

%package svgcairo
Summary:	Haskell SVG cairo binding for gtk2hs
Summary(pl.UTF-8):	Dowiązanie SVG cairo do Haskella dla gtk2hs
Group:		Development/Libraries
#Group:		Development/Languages/Haskell
Requires(post,preun):	%{_bindir}/ghc-pkg
Requires:	librsvg-devel >= 1:2.16.0
Requires:	libsvg-cairo-devel >= 0.1.6
Requires:	%{name} = %{version}-%{release}
%requires_eq	ghc

%description svgcairo
Haskell SVG cairo binding for gtk2hs.

%description svgcairo -l pl.UTF-8
Dowiązanie SVG cairo do Haskella dla gtk2hs.

%package gconf
Summary:	Haskell GConf binding for gtk2hs
Summary(pl.UTF-8):	Dowiązanie GConfa do Haskella dla gtk2hs
Group:		Development/Libraries
#Group:		Development/Languages/Haskell
Requires(post,preun):	%{_bindir}/ghc-pkg
Requires:	GConf2-devel
Requires:	%{name} = %{version}-%{release}
%requires_eq	ghc

%description gconf
Haskell GConf binding for gtk2hs.

%description gconf -l pl.UTF-8
Dowiązanie GConfa do Haskella dla gtk2hs.

%package glade
Summary:	Haskell Glade binding for gtk2hs
Summary(pl.UTF-8):	Dowiązanie Glade do Haskella dla gtk2hs
Group:		Development/Libraries
#Group:		Development/Languages/Haskell
Requires(post,preun):	%{_bindir}/ghc-pkg
Requires:	libglade2-devel
Requires:	%{name} = %{version}-%{release}
%requires_eq	ghc

%description glade
Haskell Glade2 binding for gtk2hs.

%description glade -l pl.UTF-8
Dowiązanie Glade2 do Haskella dla gtk2hs.

%package mozembed
Summary:	Haskell gtkembedmoz binding for gtk2hs
Summary(pl.UTF-8):	Dowiązanie gtkembedmoz do Haskella dla gtk2hs
Group:		Development/Libraries
#Group:		Development/Languages/Haskell
Requires(post,preun):	%{_bindir}/ghc-pkg
Requires:	xulrunner-devel
Requires:	%{name} = %{version}-%{release}
%requires_eq	ghc

%description mozembed
Haskell GtkEmbedMoz binding for gtk2hs.

%description mozembed -l pl.UTF-8
Dowiązanie gtkembedmoz do Haskella dla gtk2hs.

%package sourceview
Summary:	Haskell gtksourceview binding for gtk2hs
Summary(pl.UTF-8):	Dowiązanie gtksourceview do Haskella dla gtk2hs
Group:		Development/Libraries
#Group:		Development/Languages/Haskell
Requires(post,preun):	%{_bindir}/ghc-pkg
Requires:	gtksourceview-devel
Requires:	%{name} = %{version}-%{release}
%requires_eq	ghc

%description sourceview
Haskell GtkSourceView binding for gtk2hs.

%description sourceview -l pl.UTF-8
Dowiązanie gtksourceview do Haskella dla gtk2hs.

%package gtkglext
Summary:	Haskell gtkglext binding for gtk2hs
Summary(pl.UTF-8):	Dowiązanie gtkglext do Haskella dla gtk2hs
Group:		Development/Libraries
#Group:		Development/Languages/Haskell
Requires(post,preun):	%{_bindir}/ghc-pkg
Requires:	gtkglext-devel >= 1.0.5
Requires:	%{name} = %{version}-%{release}
%requires_eq	ghc

%description gtkglext
Haskell GtkGLExt binding for gtk2hs.

%description gtkglext -l pl.UTF-8
Dowiązanie gtkglext do Haskella dla gtk2hs.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--with-hcflags="-O"  \
	--libdir=%{ghclibdir} \
	%{?with_doc:--enable-docs} \
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
ghc-pkg register %{ghclibdir}/gtk2hs/glib.package.conf
ghc-pkg register %{ghclibdir}/gtk2hs/cairo.package.conf
ghc-pkg register %{ghclibdir}/gtk2hs/gtk.package.conf
ghc-pkg register %{ghclibdir}/gtk2hs/soegtk.package.conf

%preun
if [ "$1" = 0 ]; then
  ghc-pkg unregister soegtk
  ghc-pkg unregister gtk
  ghc-pkg unregister cairo
  ghc-pkg unregister glib
fi

%post svgcairo
ghc-pkg register %{ghclibdir}/gtk2hs/svgcairo.package.conf

%preun svgcairo
if [ "$1" = 0 ]; then
  ghc-pkg unregister svgcairo
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
%{?with_doc:%doc docs/reference}
%dir %{ghclibdir}/gtk2hs
%dir %{ghclibdir}/gtk2hs/imports
%dir %{ghclibdir}/gtk2hs/include
%{ghclibdir}/gtk2hs/include/gtk2hs-config.h
%{ghclibdir}/gtk2hs/gtk.package.conf
%{ghclibdir}/gtk2hs/soegtk.package.conf
%{ghclibdir}/gtk2hs/HSgtk.o
%{ghclibdir}/gtk2hs/HSsoegtk.o
%{ghclibdir}/gtk2hs/libHSgtk.a
%{ghclibdir}/gtk2hs/libHSsoegtk.a
%{ghclibdir}/gtk2hs/imports/gtk
%{ghclibdir}/gtk2hs/imports/soegtk

%{ghclibdir}/gtk2hs/cairo.package.conf
%{ghclibdir}/gtk2hs/HScairo.o
%{ghclibdir}/gtk2hs/libHScairo.a
%{ghclibdir}/gtk2hs/imports/cairo

%{ghclibdir}/gtk2hs/glib.package.conf
%{ghclibdir}/gtk2hs/HSglib.o
%{ghclibdir}/gtk2hs/libHSglib.a
%{ghclibdir}/gtk2hs/imports/glib

%files svgcairo
%defattr(644,root,root,755)
%{ghclibdir}/gtk2hs/svgcairo.package.conf
%{ghclibdir}/gtk2hs/HSsvgcairo.o
%{ghclibdir}/gtk2hs/libHSsvgcairo.a
%{ghclibdir}/gtk2hs/imports/svgcairo

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
