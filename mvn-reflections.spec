#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-reflections
Version  : 0.9.11
Release  : 2
URL      : https://github.com/ronmamo/reflections/archive/0.9.11.tar.gz
Source0  : https://github.com/ronmamo/reflections/archive/0.9.11.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/reflections/reflections/0.9.10/reflections-0.9.10.jar
Source2  : https://repo.maven.apache.org/maven2/org/reflections/reflections/0.9.10/reflections-0.9.10.pom
Source3  : https://repo.maven.apache.org/maven2/org/reflections/reflections/0.9.11/reflections-0.9.11.jar
Source4  : https://repo.maven.apache.org/maven2/org/reflections/reflections/0.9.11/reflections-0.9.11.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : WTFPL
Requires: mvn-reflections-data = %{version}-%{release}
Requires: mvn-reflections-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
##Java runtime metadata analysis, in the spirit of [Scannotations](http://bill.burkecentral.com/2008/01/14/scanning-java-annotations-at-runtime/)

%package data
Summary: data components for the mvn-reflections package.
Group: Data

%description data
data components for the mvn-reflections package.


%package license
Summary: license components for the mvn-reflections package.
Group: Default

%description license
license components for the mvn-reflections package.


%prep
%setup -q -n reflections-0.9.11

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-reflections
cp COPYING.txt %{buildroot}/usr/share/package-licenses/mvn-reflections/COPYING.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/reflections/reflections/0.9.10
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/reflections/reflections/0.9.10/reflections-0.9.10.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/reflections/reflections/0.9.10
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/reflections/reflections/0.9.10/reflections-0.9.10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/reflections/reflections/0.9.11
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/reflections/reflections/0.9.11/reflections-0.9.11.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/reflections/reflections/0.9.11
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/reflections/reflections/0.9.11/reflections-0.9.11.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/reflections/reflections/0.9.10/reflections-0.9.10.jar
/usr/share/java/.m2/repository/org/reflections/reflections/0.9.10/reflections-0.9.10.pom
/usr/share/java/.m2/repository/org/reflections/reflections/0.9.11/reflections-0.9.11.jar
/usr/share/java/.m2/repository/org/reflections/reflections/0.9.11/reflections-0.9.11.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-reflections/COPYING.txt
