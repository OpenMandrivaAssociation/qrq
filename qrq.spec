%define debug_package %{nil}

Summary:	Morse telegraphy trainer
Name:		qrq
Version:	0.3.3
Release:	2
Group:		Education
License:	GPLv2+
Url:		https://fkurz.net/ham/qrq.html
Source0:	http://fkurz.net/ham/qrq/qrq-%{version}.tar.gz
Patch0:		qrq-0.2.1-makefile.patch
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(ncurses)

%description
qrq is an open source morse telegraphy trainer for Linux and Unix operating
systems, similar to the classic DOS version of Rufz by DL4MM.

It's not intended for learning telegraphy, but to improve the ability to
copy callsigns at high speeds, as needed for example for Contesting. 

%prep
%setup -q
%autopatch -p1

%build
export LDFLAGS="-lpthread"
%make

%install
make install DESTDIR=%{buildroot}%{_prefix} OSX_BUNDLE=NO

%files
%doc ChangeLog COPYING README
%{_bindir}/qrq
%{_bindir}/qrqscore
%{_mandir}/man?/*
%{_datadir}/qrq

