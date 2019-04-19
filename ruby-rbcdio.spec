Summary:	Ruby bindings for libcdio
Summary(pl.UTF-8):	Wiązania języka Ruby do libcdio
Name:		ruby-rbcdio
Version:	0.05
Release:	2
License:	GPL v3+
Group:		Development/Languages
#Source0:	http://ftp.gnu.org/gnu/libcdio/rbcdio-%{version}.tgz
#Source0Download: https://rubygems.org/gems/rbcdio/
Source0:	https://rubygems.org/downloads/rbcdio-%{version}.gem
# Source0-md5:	6bf56a8cb590c4d00b972239ece0ac65
Patch0:		%{name}-libcdio.patch
URL:		http://www.gnu.org/software/libcdio/
BuildRequires:	libcdio-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1:1.8
BuildRequires:	swig-ruby
Requires:	libcdio >= 2.0.0
Requires:	ruby >= 1:1.8
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby bindings for libcdio.

%description -l pl.UTF-8
Wiązania języka Ruby do libcdio.

%prep
%setup -q -n rbcdio-%{version}
%patch0 -p1

# force regeneration
%{__rm} ext/cdio/*_wrap.c ext/iso9660/*_wrap.c

%build
%configure \
	--with-ruby=%{__ruby}

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
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{ruby_archdir}/rubycdio.so
%attr(755,root,root) %{ruby_archdir}/rubyiso9660.so
%{ruby_rubylibdir}/cdio.rb
%{ruby_rubylibdir}/iso9660.rb
%{_examplesdir}/%{name}-%{version}
