#
# Conditional build:
%bcond_with	tests	# unit tests (test_hostname can fail on host vs FQDN mismatch)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	pyenet
Summary:	Python bindings for ENet
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki ENet
Name:		python-enet
Version:	1.3.17
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyenet/
Source0:	https://files.pythonhosted.org/packages/source/p/pyenet/%{module}-%{version}.tar.gz
# Source0-md5:	baecbf35aa9365fac5172ff29abe8d84
Patch0:		pyenet-build-against-system-enet.patch
URL:		https://pypi.org/project/pyenet/
BuildRequires:	enet-devel >= 1.3.3
%if %{with python2}
BuildRequires:	python-Cython >= 0.13
BuildRequires:	python-devel >= 1:2.5
%endif
%if %{with python3}
BuildRequires:	python3-Cython >= 0.13
BuildRequires:	python3-devel >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyenet is a Python wrapper for the ENet library by Lee Salzman,
<http://enet.bespin.org/>.

%description -l pl.UTF-8
pyenet to pythonowe obudowanie biblioteki ENet autorstwa Lee Salzmana
<http://enet.bespin.org/>.

%package -n python3-enet
Summary:	Python bindings for ENet
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki ENet
Group:		Libraries/Python

%description -n python3-enet
pyenet is a Python wrapper for the ENet library by Lee Salzman,
<http://enet.bespin.org/>.

%description -n python3-enet -l pl.UTF-8
pyenet to pythonowe obudowanie biblioteki ENet autorstwa Lee Salzmana
<http://enet.bespin.org/>.

%prep
%setup -q -n %{module}-%{version}
%patch -P 0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(echo $(pwd)/build-2/lib.linux-*) \
%{__python} test_enet.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(echo $(pwd)/build-3/lib.linux-*) \
%{__python3} test_enet.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README.rst
%attr(755,root,root) %{py_sitedir}/enet.so
%{py_sitedir}/pyenet-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-enet
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README.rst
%attr(755,root,root) %{py3_sitedir}/enet.cpython-*.so
%{py3_sitedir}/pyenet-%{version}-py*.egg-info
%endif
