#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Widgets-NavMenu
Summary:	A Perl module for generating HTML navigation menus
Summary(pl):	Modu³ Perla do generowania menu nawigacyjnych w HTML-u
Name:		perl-HTML-Widgets-NavMenu
Version:	0.10.0
Release:	0.1
License:	MIT/X11	
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	431b8c1e9fe58cd772c3165e47a06503
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

%description -l pl
Modu³ Perla do generowania menu nawigacyjnych w HTML-u.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL 

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
