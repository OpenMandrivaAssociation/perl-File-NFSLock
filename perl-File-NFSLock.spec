%define	upstream_name	 File-NFSLock
%define	upstream_version 1.21

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	%{upstream_name} module for perl
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/~bbb/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/B/BB/BBB/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

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
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/File/NFSLock.pm
%{_mandir}/man3/*


%changelog
* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.210.0-1mdv2011
+ Revision: 690260
- update to new version 1.21

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2011.0
+ Revision: 409017
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.20-4mdv2009.0
+ Revision: 241219
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-2mdv2008.0
+ Revision: 86401
- rebuild


* Fri Jan 06 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.20-1mdk
- initial Mandriva release

