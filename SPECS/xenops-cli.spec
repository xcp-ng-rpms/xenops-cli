Name:           xenops-cli
Version:        1.1.0
Release:        5%{?dist}
Summary:        CLI for xenopsd, the xapi toolstack domain manager
License:        LGPL
URL:            https://github.com/xapi-project/xenops-cli
Source0:        https://code.citrite.net/rest/archive/latest/projects/XSU/repos/%{name}/archive?at=v%{version}&format=tar.gz&prefix=%{name}-%{version}#/%{name}-%{version}.tar.gz
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xenops-cli/archive?at=v1.1.0&format=tar.gz&prefix=xenops-cli-1.1.0#/xenops-cli-1.1.0.tar.gz) = 90dd0a6d38d8ac6163155141041572808cb6ea4c
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  opam
BuildRequires:  xs-opam-repo
BuildRequires:  ocaml-xcp-idl-devel

%description
Command-line interface for xenopsd, the xapi toolstack domain manager.

%prep
%autosetup -p1

%build
make
./main.native --help=groff > xenops-cli.1 && gzip xenops-cli.1

%install
%{__install} -D -m 0755 main.native %{buildroot}%{_sbindir}/xenops-cli
%{__install} -D -m 0644 xenops-cli.1.gz %{buildroot}%{_mandir}/man1/xenops-cli.1.gz

%files
%doc README.md LICENSE MAINTAINERS
%{_sbindir}/xenops-cli
%{_mandir}/man1/xenops-cli.1.gz

%changelog
* Wed Nov 01 2017 Rob Hoes <rob.hoes@citrix.com> - 1.1.0-1
- Update VM.migrate with vgpu map

* Mon Mar 13 2017 Marcello Seri <marcello.seri@citrix.com> - 1.0.3-2
- Update OCaml dependencies and build/install script after xs-opam-repo split

* Tue Jan 10 2017 Rob Hoes <rob.hoes@citrix.com> - 1.0.3-1
- git: Add metadata to the result of `git archive`

* Mon Sep 12 2016 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.0.2-1
- Update to 1.0.2

* Thu May 12 2016 Si Beaumont <simon.beaumont@citrix.com> - 1.0.1-1
- Update to 1.0.1
- New build dependency on oasis
- Install man page

* Thu Apr 21 2016 Euan Harris <euan.harris@citrix.com> - 1.0.0-1
- Update to 1.0.0

* Wed Sep 9 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.10.0-2
- Bump release

* Thu Aug 20 2015 David Scott <dave.scott@citrix.com> - 0.10.0-1
- Update to 0.10.0

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-2
- Initial package

