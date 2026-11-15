#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	Params
%define	pnam	SomeUtil
Summary:	Params::SomeUtil - Simple, compact and correct param-checking functions
Summary(pl.UTF-8):	Params::SomeUtil - proste, zwięzłe i poprawne funkcje do sprawdzania parametrów
Name:		perl-Params-SomeUtil
Version:	1.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/P/PL/PLICEASE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	39d44b84911aea9aa41579f5c70d3693
URL:		https://metacpan.org/dist/Params-SomeUtil
BuildRequires:	perl-ExtUtils-CBuilder >= 0.27
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.52
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.80
BuildRequires:	perl-Scalar-List-Utils >= 1.18
BuildRequires:	perl-Test-Simple >= 0.87
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Params::SomeUtil provides a basic set of importable functions that
makes checking parameters a hell of a lot easier.

The functions provided by Params::SomeUtil check in the most strictly
correct manner, and should not be fooled by odd cases.

This module is a fork of version 1.07 of Params::Util with some
additional bug fixes.

%description -l pl.UTF-8
Params::SomeUtil udostępnia podstawowy zestaw importowalnych funkcji
znacznie ułatwiających sprawdzanie parametrów.

Funkcje dostarczane przez Params::SomeUtil sprawdzają poprawność w
najbardziej ścisły sposób i nie powinny dać się ogłupić przez
nietypowe przypadki.

Ten moduł jest odgałęzieniem wersji 1.07 modułu Params::Util z
dodatkowymi poprawkami błędów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README.md
%{perl_vendorarch}/Params/SomeUtil.pm
%dir %{perl_vendorarch}/auto/Params/SomeUtil
%attr(755,root,root) %{perl_vendorarch}/auto/Params/SomeUtil/SomeUtil.so
%{_mandir}/man3/Params::SomeUtil.3pm*
