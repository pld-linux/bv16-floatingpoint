#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	BroadVoice16 floating point codec
Summary(pl.UTF-8):	Kodek BroadVoice16 z arytmetyką zmiennoprzecinkową
Name:		bv16-floatingpoint
Version:	2.1
Release:	1
License:	BSD
Group:		Libraries
# original sources: https://docs.broadcom.com/docs/12358447 (found via https://www.broadcom.com/site-search?q=broadvoice)
# linphone added cmake build
#Source0Download: https://gitlab.linphone.org/BC/public/external/bv16-floatingpoint/-/tags
Source0:	https://gitlab.linphone.org/BC/public/external/bv16-floatingpoint/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	b28dd02e633cd71136c32cacc2797566
URL:		https://gitlab.linphone.org/BC/public/external/bv16-floatingpoint
BuildRequires:	cmake >= 3.0
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BroadVoice16 floating point codec.

%description -l pl.UTF-8
Kodek BroadVoice16 z arytmetyką zmiennoprzecinkową.

%package devel
Summary:	Header files for bv16 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki bv16
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for bv16 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki bv16.

%package static
Summary:	Static bv16 library
Summary(pl.UTF-8):	Statyczna biblioteka bv16
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static bv16 library.

%description static -l pl.UTF-8
Statyczna biblioteka bv16.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	%{!?with_static_libs:-DENABLE_STATIC=OFF} \
	-DENABLE_TOOLS=ON \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/BroadVoice16
%attr(755,root,root) %{_libdir}/libbv16.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/bv16-floatingpoint

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libbv16.a
%endif
