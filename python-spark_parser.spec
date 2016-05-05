#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	spark_parser
Summary:	An Early-Algorithm LR Parser
Name:		python-%{module}
Version:	1.1.1
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/ff/13/752712a1bf51a76eedfcfc1d6d06b48388fbe0194722b736190ccea57c3a/%{module}-%{version}.tar.gz
# Source0-md5:	2fdfb3e8e82a79ca1d58b31c8562df1c
URL:		https://github.com/rocky/python-spark/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-nose >= 1.0
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-nose >= 1.0
BuildRequires:	python3-setuptools
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SPARK stands for Scanning, Parsing, and Rewriting Kit. It uses Jay
Early's algorithm for LR parsing and comes with some generic Abstract
Syntax Tree routines. There is also a prototype scanner which does its
job by combining Python regular expressions.

%package -n python3-%{module}
Summary:	An Early-Algorithm LR Parser
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
SPARK stands for Scanning, Parsing, and Rewriting Kit. It uses Jay
Early's algorithm for LR parsing and comes with some generic Abstract
Syntax Tree routines. There is also a prototype scanner which does its
job by combining Python regular expressions.

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
%{__rm} -r %{module}.egg-info

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%files
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
