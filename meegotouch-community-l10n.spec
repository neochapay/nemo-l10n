Name:           meegotouch-community-l10n
Version:        0.2.4
Release:        1%{?dist}
Summary:        Translations made by community for the meegotouch.
Group:          User Interface/Desktops
License:        GPL v2
URL:            https://gitorious.org/meego-developer-edition-for-n900/meegotouch-community-l10n
Source0:        file://meegotouch-community-l10n-0.2.4.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:	gettext, qt-devel

%description
English (Great Britain) translation for all those MeeGo Touch apps on CE, like SystemUI, Home, Settings and applets.

%prep
%setup -q

%build
lrelease *.ts

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/l10n/meegotouch/
install -m 644 *_en.qm %{buildroot}/usr/share/l10n/meegotouch/

%files
%defattr(-,root,root,-)
%{_datadir}/l10n/meegotouch/*_en.qm

