%define oname	osmgpsmap

Name:		python-%{oname}
Version:	0.7.3
Release:	2
Summary:	Python bindings for osm-gps-map GTK+ widget
Group:		Development/Python
License:	GPLv2
URL:		https://nzjrs.github.com/osm-gps-map/
Source0:	http://www.johnstowers.co.nz/files/osm-gps-map/%{name}-%{version}.tar.gz
BuildRequires:	osm-gps-map-devel
BuildRequires:	python-gobject-devel
BuildRequires:	pygtk2.0-devel

%description
Python bindings for a GTK+ widget that when given GPS co-ordinates,
draws a GPS track, and points of interest on a moving map
display. Downloads map data from a number of websites, including
openstreetmap.org.

%prep
%setup -q

%build
CFLAGS="%{optflags}" python setup.py build

%install
rm -rf %{buildroot}
python setup.py install \
	-O1 \
	--skip-build \
	--root %{buildroot}
 
%clean
rm -rf %{buildroot}

%files
%doc AUTHORS
%{python_sitearch}/%{oname}.so
%{python_sitearch}/python_%{oname}-%{version}-py%{py_ver}.egg-info



%changelog
* Mon Oct 31 2011 Andrey Bondrov <abondrov@mandriva.org> 0.7.3-1
+ Revision: 708036
- imported package python-osmgpsmap

