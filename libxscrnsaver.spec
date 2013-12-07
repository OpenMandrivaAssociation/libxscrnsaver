%define major 1
%define libname %mklibname xscrnsaver %{major}
%define devname %mklibname xscrnsaver -d

Summary:	The XScrnSaver Library
Name:		libxscrnsaver
Version:	1.2.2
Release:	5
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXScrnSaver-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
The XScrnSaver Library.

%package -n %{libname}
Summary:	The XScrnSaver Library
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
The XScrnSaver Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	libxscrnsaver-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%prep
%setup -qn libXScrnSaver-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXss.so.%{major}*

%files -n %{devname}
%{_libdir}/libXss.so
%{_libdir}/pkgconfig/xscrnsaver.pc
%{_mandir}/man3/XScreenSaver*
%{_mandir}/man3/Xss*
%{_includedir}/X11/extensions/scrnsaver.h

