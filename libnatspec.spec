Summary:	Library for national and language-specific issues
Name:		libnatspec
Version:	0.2.6
Release:	1%{?dist}

License:	LGPLv2
Group:		Development/Libraries
Url:		http://sourceforge.net/projects/natspec
Source:		https://downloads.sourceforge.net/project/natspec/natspec/%{version}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	popt-devel
BuildRequires:	autoconf, automake, libtool


%description
Library for national and language-specific issues.
This library provides userful functions for
mount, submount, mkisofs, multimedia players.
This library try to help resolve charset hell (encoding problem)
in a various programs depends on locale and messages.
See detailed description at %url.


%package	devel
Summary:	Development package of library for national and language-specific issues
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}


%description devel
The %{name}-devel package contains libraries and header files for
developing extensions for %{name}.


%prep
%setup -q


%build
autoreconf -fiv
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%makeinstall
rm -f %{buildroot}%{_libdir}/*.la


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS README ChangeLog NEWS TODO README-ru.html
%doc examples profile
%{_libdir}/*.so.*
%{_bindir}/*
%{_mandir}/man?/*


%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*


%changelog
* Sat Feb  6 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.2.6-1
- initial build for Fedora
