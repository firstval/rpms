# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Hook-LexWrap

Summary: Lexically scoped subroutine wrappers
Name: perl-Hook-LexWrap
Version: 0.20
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Hook-LexWrap/

Source: http://www.cpan.org/modules/by-module/Hook/Hook-LexWrap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Lexically scoped subroutine wrappers

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Hook::LexWrap.3pm*
%dir %{perl_vendorlib}/Hook/
#%{perl_vendorlib}/Hook/LexWrap/
%{perl_vendorlib}/Hook/LexWrap.pm

%changelog
* Mon Jun 05 2006 Dag Wieers <dag@wieers.com> - 0.20-1
Initial package. (using DAR)
