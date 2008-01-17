%define libxscrnsaver %mklibname xscrnsaver 1 
Name: libxscrnsaver
Summary:  The XScrnSaver Library
Version: 1.1.2
Release: %mkrel 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXScrnSaver-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: x11-proto-devel	>= 7.3
BuildRequires: libxext-devel	>= 1.0.3

%description
The XScrnSaver Library

#-----------------------------------------------------------

%package -n %{libxscrnsaver}
Summary:  The XScrnSaver Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxscrnsaver}
 The XScrnSaver Library

#-----------------------------------------------------------

%package -n %{libxscrnsaver}-devel
Summary: Development files for %{name}
Group: Development/X11


Requires: %{libxscrnsaver} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxscrnsaver-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxscrnsaver}-devel
Development files for %{name}

%files -n %{libxscrnsaver}-devel
%defattr(-,root,root)
%{_libdir}/libXss.so
%{_libdir}/libXss.la
%{_libdir}/pkgconfig/xscrnsaver.pc
%{_mandir}/man3/XScreenSaver*
%{_mandir}/man3/Xss*

#-----------------------------------------------------------

%package -n %{libxscrnsaver}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxscrnsaver}-devel = %{version}
Provides: libxscrnsaver-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxscrnsaver}-static-devel
Static development files for %{name}

%files -n %{libxscrnsaver}-static-devel
%defattr(-,root,root)
%{_libdir}/libXss.a

#-----------------------------------------------------------

%prep
%setup -q -n libXScrnSaver-%{version}

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxscrnsaver}
%defattr(-,root,root)
%{_libdir}/libXss.so.1
%{_libdir}/libXss.so.1.0.0
