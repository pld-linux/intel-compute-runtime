
# versions listed on
# https://github.com/intel/compute-runtime/releases
%define	gmmlib_version	19.2.1
%define	igc_version 1.0.8

Summary:	Intel Graphics Compute Runtime for OpenCL
Name:		intel-compute-runtime
Version:	19.24.13171
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://github.com/intel/compute-runtime/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c827cb2987d11e65a0f25befee0bbcb1
URL:		https://01.org/compute-runtime
BuildRequires:	cmake >= 3.2.0
BuildRequires:	intel-gmmlib >= %{gmmlib_version}
BuildRequires:	intel-graphics-compiler >= %{igc_version}
BuildRequires:	libdrm-devel
BuildRequires:	libva-devel
BuildRequires:	pkgconfig
Provides:	ocl-icd(intel)
Provides:	ocl-icd-driver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Intel(R) Graphics Compute Runtime for OpenCL(TM) is an open source
project to converge Intel's development efforts on OpenCL(TM) compute
stacks supporting the GEN graphics hardware architecture.

%prep
%setup -qn compute-runtime-%{version}

%build
install -d build
cd build
%cmake \
		../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ocloc
%{_sysconfdir}/OpenCL/vendors/intel.icd
%dir %{_libdir}/intel-opencl
%attr(755,root,root) %{_libdir}/intel-opencl/libigdrcl.so
