# $Id$
# Authority: dag

%{?el4: %define _without_gettextdevel 1}
%{?el3: %define _without_gettextdevel 1}
%{?el2: %define _without_gettextdevel 1}

Summary: Converts text files to HTML, XHTML, sgml, LaTeX, man...
Name: txt2tags
Version: 2.6
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://txt2tags.org/

Source: http://txt2tags.googlecode.com/files/txt2tags-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
%{!?_without_gettextdevel:BuildRequires: gettext-devel}
BuildRequires: python >= 2.2
Requires: python >= 2.2

%description
Txt2tags is a generic text converter. From a simple text file with minimal
markup, it generates documents on the following formats: HTML, XHTML, sgml,
LaTeX, Lout, man, Magic Point (mgp), MoinMoin and Adobe PageMaker. Supports
heading, font beautifiers, verbatim, quote, link, lists, table and image.
There are GUI, Web and cmdline interfaces. It's a single Python script and
no external commands or libraries are needed.

%prep
%setup

### Create locale files
for file in $(ls -1 po/*.po); do
    msgfmt -o ${file//.po/.mo} $file
done

find . -type d -exec chmod a+x {} \;

%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m0755 txt2tags %{buildroot}%{_bindir}/txt2tags

### Install translated manpages
%{__install} -Dp -m0644 doc/manpage.man %{buildroot}%{_mandir}/man1/txt2tags.1
for file in $(ls -1 doc/manpage-*.man); do
    lang="${file##doc/manpage-}"
    lang="${lang%%.man}"
    %{__install} -Dp -m0644 $file %{buildroot}%{_mandir}/$lang/man1/txt2tags.1
done

### Install locale files
for file in $(ls -1 po/*.mo); do
    basename="${file##po/}"
    lang="${basename%%.mo}"
    %{__install} -Dp -m0644 $file %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/txt2tags.mo
done

%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README doc/*.pdf extras/ samples/
%doc %{_mandir}/man1/txt2tags.1*
%doc %{_mandir}/*/man1/txt2tags.1*
%{_bindir}/txt2tags

%changelog
* Mon Nov 08 2010 Dag Wieers <dag@wieers.com> - 2.6-1
- Updated to release 2.6.

* Sun Jul 27 2008 Dag Wieers <dag@wieers.com> - 2.5-1
- Updated to release 2.5.

* Mon Jan 29 2007 Dag Wieers <dag@wieers.com> - 2.4-1
- Initial package. (using DAR)
