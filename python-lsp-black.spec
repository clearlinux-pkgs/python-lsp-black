#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-lsp-black
Version  : 1.0.0
Release  : 4
URL      : https://files.pythonhosted.org/packages/e9/eb/686ceb7142fb4894bdfece7db4a07a39a189f498c45c2580b19b56a22688/python-lsp-black-1.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e9/eb/686ceb7142fb4894bdfece7db4a07a39a189f498c45c2580b19b56a22688/python-lsp-black-1.0.0.tar.gz
Summary  : Black plugin for the Python LSP Server
Group    : Development/Tools
License  : MIT
Requires: python-lsp-black-python = %{version}-%{release}
Requires: python-lsp-black-python3 = %{version}-%{release}
Requires: black
Requires: python-lsp-server
Requires: toml
BuildRequires : black
BuildRequires : buildreq-distutils3
BuildRequires : python-lsp-server
BuildRequires : toml

%description
# python-lsp-black
[![PyPI](https://img.shields.io/pypi/v/pyls-black.svg)](https://pypi.org/project/python-lsp-black) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Python](https://github.com/python-lsp/python-lsp-black/actions/workflows/python.yml/badge.svg)](https://github.com/python-lsp/python-lsp-black/actions/workflows/python.yml)

%package python
Summary: python components for the python-lsp-black package.
Group: Default
Requires: python-lsp-black-python3 = %{version}-%{release}

%description python
python components for the python-lsp-black package.


%package python3
Summary: python3 components for the python-lsp-black package.
Group: Default
Requires: python3-core
Provides: pypi(python_lsp_black)
Requires: pypi(black)
Requires: pypi(python_lsp_server)
Requires: pypi(toml)

%description python3
python3 components for the python-lsp-black package.


%prep
%setup -q -n python-lsp-black-1.0.0
cd %{_builddir}/python-lsp-black-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632448693
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
