%define	upstream_name	 File-NFSLock
%define	upstream_version 1.21

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	%{upstream_name} module for perl
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/~bbb/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/B/BB/BBB/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
%{upstream_name} perl module

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/File/NFSLock.pm
%{_mandir}/man3/*
