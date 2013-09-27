Summary:	Simple theme for the Xfce window manager
Name:		xfwm4-theme-axis
Version:	1
Release:	1
License:	GPL
Group:		Themes
Source0:	http://xfce-look.org/CONTENT/content-files/95158-axis-xfwm.tar.gz
# Source0-md5:	db4246e83ccb04c93437fa27ba9c11c8
URL:		http://www.xfce.org/
BuildArch:	noarch
Requires:	xfwm4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minimal, squared theme for the Xfce window manager.

%prep
%setup -qn axis

%build

%install
install -d $RPM_BUILD_ROOT%{_datadir}/themes/axis

cp -ar xfwm4 $RPM_BUILD_ROOT%{_datadir}/themes/axis

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/themes/axis

