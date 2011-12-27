%define major 1
%define libname %mklibname xscrnsaver %{major}
%define develname %mklibname xscrnsaver -d

Name: libxscrnsaver
Summary:  The XScrnSaver Library
Version: 1.2.1
Release: 4
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXScrnSaver-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 7.4-25
BuildRequires: x11-util-macros >= 1.0.1

%description
The XScrnSaver Library

%package -n %{libname}
Summary:  The XScrnSaver Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
 The XScrnSaver Library

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}-%{release}
Provides: libxscrnsaver-devel = %{version}-%{release}
Obsoletes: %{_lib}xscrnsaver1-devel
Obsoletes: %{_lib}xscrnsaver-static-devel
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXScrnSaver-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXss.so.%{major}*

%files -n %{develname}
%{_libdir}/libXss.so
%{_libdir}/pkgconfig/xscrnsaver.pc
%{_mandir}/man3/XScreenSaver*
%{_mandir}/man3/Xss*
%{_includedir}/X11/extensions/scrnsaver.h

