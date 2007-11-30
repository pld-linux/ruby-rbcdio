Summary:	Ruby bindings for libcdio
Summary(pl.UTF-8):	Wiązania języka Ruby do libcdio
Name:		ruby-rbcdio
Version:	0.02
Release:	1
License:	GPL v2+
Group:		Development/Languages
Source0:	http://ftp.gnu.org/gnu/libcdio/rbcdio-%{version}.tgz
# Source0-md5:	8f408cb726fcf64aaed17a6ca75c7227
URL:		http://www.gnu.org/software/libcdio/
BuildRequires:	libcdio-devel >= 0.76
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1:1.8
BuildRequires:	swig-ruby
Requires:	libcdio >= 0.76
Requires:	ruby >= 1:1.8
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby bindings for libcdio.

%description -l pl.UTF-8
Wiązania języka Ruby do libcdio.

%prep
%setup -q -n rbcdio-%{version}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

for d in ext/* ; do
%{__make} -C $d install \
	RUBYARCHDIR=$RPM_BUILD_ROOT%{ruby_archdir}
done

install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}
install lib/*.rb $RPM_BUILD_ROOT%{ruby_rubylibdir}

install example/{*.rb,README} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS doc/*
%attr(755,root,root) %{ruby_archdir}/rubycdio.so
%attr(755,root,root) %{ruby_archdir}/rubyiso9660.so
%{ruby_rubylibdir}/cdio.rb
%{ruby_rubylibdir}/iso9660.rb
%{_examplesdir}/%{name}-%{version}
