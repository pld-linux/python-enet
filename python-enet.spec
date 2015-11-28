# No releases, source only available through svn.
# svn co http://pyenet.googlecode.com/svn/trunk/ pyenet-trunk-svn24
%define		module	pyenet
%define		svnrev	svn24
%define		rel		1
Summary:	Python bindings for ENet
Name:		python-enet
Version:	0.0.0
Release:	0.%{svnrev}.%{rel}
License:	MIT
Group:		Libraries/Python
URL:		http://code.google.com/p/pyenet
Source0:	%{module}-trunk-%{svnrev}.tar.bz2
# Source0-md5:	1fa3e0ff41974fee2defc88d03a1c293
Patch0:		pyenet-build-against-system-enet.patch
BuildRequires:	enet-devel >= 1.3.3
BuildRequires:	python-Cython >= 0.13
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyenet was written originally by Scott Robinson <scott@tranzoa.com>.

It's currently maintained by Andrew Resch <andrewresch@gmail.com> and
provides the Python bindings for ENet.

%prep
%setup -q -n %{module}-trunk-%{svnrev}
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
%doc LICENSE README ChangeLog
%attr(755,root,root) %{py_sitedir}/enet.so
%{py_sitedir}/enet-%{version}-py*.egg-info
