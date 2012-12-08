%define major 1
%define libname %mklibname xscrnsaver %{major}
%define develname %mklibname xscrnsaver -d

Name:		libxscrnsaver
Summary:	The XScrnSaver Library
Version:	1.2.2
Release:	2
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXScrnSaver-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	x11-proto-devel >= 7.4-25
BuildRequires:	x11-util-macros >= 1.0.1

%description
The XScrnSaver Library.

%package -n %{libname}
Summary:	The XScrnSaver Library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}

%description -n %{libname}
The XScrnSaver Library.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	libxscrnsaver-devel = %{version}-%{release}
Obsoletes:	%{_lib}xscrnsaver1-devel < 1.2.2
Obsoletes:	%{_lib}xscrnsaver-static-devel < 1.2.2
Conflicts:	libxorg-x11-devel < 7.0

%description -n %{develname}
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


%changelog
* Sat Mar 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.2-1
+ Revision: 783940
- version update 1.2.2

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.2.1-4
+ Revision: 745757
- rebuild
- disabled static build
- removed .la files
- cleaned up spec
- employed major macro

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-3
+ Revision: 662429
- mass rebuild

* Sat Feb 19 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.2.1-2
+ Revision: 638671
- remove typos
- dropped major from devel and static pkgs
- added proper provides and obsoletes

* Sat Oct 30 2010 Thierry Vignaud <tv@mandriva.org> 1.2.1-1mdv2011.0
+ Revision: 590418
- new release

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-3mdv2010.1
+ Revision: 520972
- rebuilt for 2010.1

* Thu Sep 17 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.2.0-2mdv2010.0
+ Revision: 444039
- Require x11-proto-devel >= 7.4-25mdv because /usr/include/X11/xscrnsaver.h moved
  from x11-proto-devel to libxscrnsaver-devel (to avoid 2 packages owning the same
  file)

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.2.0-1mdv2010.0
+ Revision: 424584
- adjust file list
- new release

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.1.3-2mdv2009.0
+ Revision: 265005
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Apr 14 2008 Thierry Vignaud <tv@mandriva.org> 1.1.3-1mdv2009.0
+ Revision: 192990
- new release

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.2-2mdv2008.1
+ Revision: 154202
- Updated BuildRequires and resubmit package.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

