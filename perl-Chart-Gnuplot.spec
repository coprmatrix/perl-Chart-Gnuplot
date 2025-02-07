#
# spec file for package perl-perl-Chart-Gnuplot
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define cpan_name Chart-Gnuplot
Name:           perl-Chart-Gnuplot
Version:        0
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Plot graph using Gnuplot in Perl on the fly
URL:            https://github.com/huakim/Chart-Gnuplot
Source0:        perl-Chart-Gnuplot.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Requires: gnuplot
%{perl_requires}

%description
Plot graph using Gnuplot in Perl on the fly

%prep
%autosetup  -n %{name}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes doc README

%changelog
