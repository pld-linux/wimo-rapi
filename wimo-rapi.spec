Summary:	WiMo-RAPI
Summary(pl.UTF-8):	WiMo-RAPI
Name:		wimo-rapi
Version:	0.5.0
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/wimo/%{name}-%{version}.tar.bz2
# Source0-md5:	985c6fc69cd1f9e1dfb51c36862204a9
URL:		http://www.wimol.org/
BuildRequires:	nant
BuildRequires:	mono-csharp
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Windows Mobile devices support for Linux desktop.
WiMo-RAPI is free Windows Mobile RAPI and RAPI2 implementation written
in managed C# 2.0.

%prep
%setup -q

%build
nant -D:PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
nant install \
	-D:DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/mono/gac/%{name}
%{_libdir}/mono/%{name}
%{_pkgconfigdir}/%{name}.pc
