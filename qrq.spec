Name:           qrq
Version:        0.3.0
Release:        4
Summary:        Morse telegraphy trainer
Group:          Education
License:        GPLv2+
URL:            http://fkurz.net/ham/qrq.html
Source0:        http://fkurz.net/ham/qrq/qrq-%{version}.tar.gz
Patch0:         qrq-0.2.1-makefile.patch

BuildRequires:  ncurses-devel
BuildRequires:  pulseaudio-devel

%define debug_package %{nil}

%description
qrq is an open source morse telegraphy trainer for Linux and Unix operating
systems, similar to the classic DOS version of Rufz by DL4MM.

It's not intended for learning telegraphy, but to improve the ability to
copy callsigns at high speeds, as needed for example for Contesting. 

%prep
%setup -q
%patch0 -p1

%build
export LDFLAGS="-lpthread"
%make

%install
make install DESTDIR=%{buildroot}%{_prefix} OSX_BUNDLE=NO

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING README
%{_bindir}/qrq
%{_bindir}/qrqscore
%{_mandir}/man?/*
%{_datadir}/qrq


%changelog
* Sat Dec 24 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.3.0-1
+ Revision: 745112
- version update 0.3.0

* Wed Nov 30 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.2.1-1
+ Revision: 735806
- imported package qrq

