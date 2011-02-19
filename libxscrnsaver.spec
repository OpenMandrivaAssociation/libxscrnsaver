%define libname %mklibname xscrnsaver 1 
%define develname %mklibname xscrnsaver -d
%define staticname %mklibname xscrnsaver -s -d

Name: libxscrnsaver
Summary:  The XScrnSaver Library
Version: 1.2.1
Release: %mkrel 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXScrnSaver-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 7.4-25mdv
BuildRequires: x11-util-macros >= 1.0.1

%description
The XScrnSaver Library

#-----------------------------------------------------------

%package -n %{libname}
Summary:  The XScrnSaver Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
 The XScrnSaver Library

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11


Requires: %{libname} = %{version}-%{release}
Requires: x11-proto-devel >= 7.4-25
Provides: libxscrnsaver-devel = %{version}-%{release}
Provides: libxscrnsaver1-devel = %{version}-%{release}
Obsoletes: %{mklibname xscrnsaver -1 -d}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXss.so
%{_libdir}/libXss.la
%{_libdir}/pkgconfig/xscrnsaver.pc
%{_mandir}/man3/XScreenSaver*
%{_mandir}/man3/Xss*
%{_includedir}/X11/extensions/scrnsaver.h

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}-%{release}
Provides: libxscrnsaver-static-devel = %{version}-%{release}
Provides: libxscrnsaver1-static-devel = %{version}-%{release}
Obsoletes: %{mklibname xscrnsaver -1 -s -d}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libXss.a

#-----------------------------------------------------------

%prep
%setup -q -n libXScrnSaver-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXss.so.1
%{_libdir}/libXss.so.1.0.0
