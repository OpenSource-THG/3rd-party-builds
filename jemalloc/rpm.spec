Name:           jemalloc
Version:        5.3.0

Release:        3%{?dist}
Summary:        General-purpose scalable concurrent malloc implementation

Group:          System Environment/Libraries
License:        BSD
URL:            http://www.canonware.com/jemalloc/
Source0:        https://github.com/jemalloc/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  perl-generators
%ifnarch s390 %{mips}
BuildRequires:  valgrind-devel
%endif

%description
General-purpose scalable concurrent malloc(3) implementation.
This distribution is the stand-alone "portable" implementation of %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

# Override PAGESIZE, bz #1545539
%ifarch %ix86 %arm x86_64 s390x
%define lg_page --with-lg-page=12
%endif

%ifarch ppc64 ppc64le aarch64
%define lg_page --with-lg-page=16
%endif

# Disable thp on systems not supporting this for now
%ifarch %ix86 %arm aarch64 s390x
%define disable_thp --disable-thp
%endif


%build
%ifarch %ix86
%if 0%{?fedora} >= 21
CFLAGS="%{optflags} -msse2"
%endif
%endif

%if 0%{?rhel} && 0%{?rhel} < 7
export LDFLAGS="%{?__global_ldflags} -lrt"
%endif

echo "For debugging package builders"
echo "What is the pagesize?"
getconf PAGESIZE

echo "What mm features are available?"
ls /sys/kernel/mm
ls /sys/kernel/mm/transparent_hugepage || true
cat /sys/kernel/mm/transparent_hugepage/enabled || true

echo "What kernel version and config is this?"
uname -a

%configure %{?disable_thp} %{?lg_page}
make %{?_smp_mflags}


%check
make check


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
# Install this with doc macro instead
rm %{buildroot}%{_datadir}/doc/%{name}/jemalloc.html

# None of these in fedora
find %{buildroot}%{_libdir}/ -name '*.a' -exec rm -vf {} ';'



%files
%{_libdir}/libjemalloc.so.*
%{_bindir}/jemalloc.sh
%doc COPYING README VERSION
%doc doc/jemalloc.html

%files devel
%{_includedir}/jemalloc
%{_bindir}/jemalloc-config
%{_libdir}/pkgconfig/jemalloc.pc
%{_bindir}/jeprof
%{_libdir}/libjemalloc.so
%{_mandir}/man3/jemalloc.3*

#%ldconfig_scriptlets