# libxscrnsaver is used by sdl2 and steam
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define major 1
%define libname %mklibname xscrnsaver %{major}
%define devname %mklibname xscrnsaver -d
%define lib32name libxscrnsaver%{major}
%define dev32name libxscrnsaver-devel

Summary:	The XScrnSaver Library
Name:		libxscrnsaver
Version:	1.2.4
Release:	2
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXScrnSaver-%{version}.tar.xz
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xextproto)
BuildRequires:	pkgconfig(scrnsaverproto)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
%if %{with compat32}
BuildRequires:	libc6
BuildRequires:	devel(libX11)
BuildRequires:	devel(libXext)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
%endif

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

%if %{with compat32}
%package -n %{lib32name}
Summary:	The XScrnSaver Library (32-bit)
Group:		Development/X11

%description -n %{lib32name}
The XScrnSaver Library.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n %{dev32name}
Development files for %{name}.
%endif

%prep
%setup -qn libXScrnSaver-%{version}
%autopatch -p1

export CONFIGURE_TOP="$(pwd)"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libXss.so.%{major}*

%files -n %{devname}
%{_libdir}/libXss.so
%{_libdir}/pkgconfig/xscrnsaver.pc
%doc %{_mandir}/man3/XScreenSaver*
%doc %{_mandir}/man3/Xss*
%{_includedir}/X11/extensions/scrnsaver.h

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libXss.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libXss.so
%{_prefix}/lib/pkgconfig/xscrnsaver.pc
%endif
