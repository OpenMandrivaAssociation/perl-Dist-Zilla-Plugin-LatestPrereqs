%define upstream_name    Dist-Zilla-Plugin-LatestPrereqs
%define upstream_version 0.3

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Adjust prereqs to use latest version available
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CPAN)
BuildRequires:	perl(Dist::Zilla)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

