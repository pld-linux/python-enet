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
BuildRequires:	python-Cython >= 0.13
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyenet is a Python wrapper for the ENet library by Lee Salzman,
<http://enet.bespin.org/>.

%description -l pl.UTF-8
pyenet to pythonowe obudowanie biblioteki ENet autorstwa Lee Salzmana
<http://enet.bespin.org/>.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README.rst
%attr(755,root,root) %{py_sitedir}/enet.so
%{py_sitedir}/pyenet-%{version}-py*.egg-info
