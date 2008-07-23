%define	module	File-NFSLock
%define	name	perl-%{module}
%define	version	1.20
%define	release	%mkrel 4

Name:		%{name}
Summary:	%{module} module for perl
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/~bbb/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/B/BB/BBB/%{module}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
%{module} perl module

%prep
%setup -q -n %{module}-%{version}

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

