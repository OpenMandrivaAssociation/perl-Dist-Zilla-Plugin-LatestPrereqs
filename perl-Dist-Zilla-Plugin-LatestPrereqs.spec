%define upstream_name    Dist-Zilla-Plugin-LatestPrereqs
%define upstream_version 0.2

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Adjust prereqs to use latest version available
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CPAN)
BuildRequires: perl(Dist::Zilla)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This plugin will filter over all your declared or discovered prerequisites,
contact CPAN, and adjust the version to the latest one available.

This will make sure that your module will be installed with the latest
version available on CPAN at the time you built your package.

The most common use for this techinique is for the Task manpage modules.
You can rebuild your Task module on a regular basis to make sure it has the
latest versions of your dependencies.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


