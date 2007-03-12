#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	docs		# don't build html documentation
#
Summary:	A GUI Library for Haskell based on Gtk+
Summary(pl.UTF-8):	Biblioteka GUI dla Haskella oparta na Gtk+
Name:		gtk2hs
Version:	0.9.11
Release:	0.1
License:	LGPL
Group:		Applications
Source0:	http://downloads.sourceforge.net/gtk2hs/%{name}-%{version}.tar.gz
# Source0-md5:	a59f19d15ae0cab976722dbf3a09fc14
URL:		http://haskell.org/gtk2hs/
BuildRequires:	ghc >= 6.0
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libglade2-devel
BuildRequires:	GConf2-devel
BuildRequires:	gtksourceview-devel
BuildRequires:	xulrunner-devel
BuildRequires:	librsvg-devel >= 2.16.0
BuildRequires:	cairo-devel >= 1.0.0
BuildRequires:	gtkglext-devel >= 1.0.5
%{?with_docs:BuildRequires:	haddock}
Requires:	ghc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GUI Library for Haskell based on Gtk+.

%description -l pl.UTF-8
Biblioteka GUI dla Haskella oparta na Gtk+.

%prep
%setup -q

%build
%configure \
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

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%{?with_docs:%doc docs/reference}
%{_libdir}/%{name}
