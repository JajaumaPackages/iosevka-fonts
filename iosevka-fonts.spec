%global fontname iosevka
%global fontconf 62-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        1.9.5
Release:        1%{?dist}
Summary:        A programmer's typeface (sans-serif variant)

License:        SIL OFL 1.1
URL:            http://be5invis.github.io/Iosevka/
Source0:        https://github.com/be5invis/Iosevka/releases/download/v%{version}/01.%{fontname}-%{version}.zip
Source1:        %{name}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Iosevka is a monospace coding typeface inspired by Pragmata Pro, M+ and PF DIN
Mono. It is designed to have a narrow shape to be space efficient and
compatible to CJK characters.

This package contains the default Iosevka, sans-serif variant.


%prep
%setup -q -c
cp %{SOURCE1} .


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%clean
rm -fr %{buildroot}


%_font_pkg -f %{fontconf} *.ttf


%changelog
* Sun Nov 06 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.9.5-1
- Public release
