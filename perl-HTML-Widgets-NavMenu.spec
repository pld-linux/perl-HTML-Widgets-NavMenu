#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Widgets-NavMenu
Summary:	A Perl module for generating HTML navigation menus
Summary(pl.UTF-8):	Moduł Perla do generowania menu nawigacyjnych w HTML-u
Name:		perl-HTML-Widgets-NavMenu
Version:	1.0001
Release:	0.1
License:	MIT/X11
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6cace7ae837780c51a5d2bea44b1d874
URL:		http://search.cpan.org/dist/HTML-Widgets-NavMenu/
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Error
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
#BuildRequires:	a lot, give me a hint how to find them
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Perl module for generating HTML navigation menus.

%description -l pl.UTF-8
Moduł Perla do generowania menu nawigacyjnych w HTML-u.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO TODO-Rejects
%dir %{perl_vendorlib}/HTML/Widgets
%{perl_vendorlib}/HTML/Widgets/*
%{_mandir}/man3/*
