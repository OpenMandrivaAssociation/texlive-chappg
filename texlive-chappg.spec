# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/chappg
# catalog-date 2009-05-30 13:37:26 +0200
# catalog-license lppl
# catalog-version 2.1b
Name:		texlive-chappg
Version:	2.1b
Release:	3
Summary:	Page numbering by chapter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chappg
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chappg.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chappg.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chappg.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides for 'chapterno-pageno' or 'chaptername-
pageno' page numbering. Provision is made for front- and
backmatter in book class.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chappg/chappg.sty
%doc %{_texmfdistdir}/doc/latex/chappg/chappg.pdf
#- source
%doc %{_texmfdistdir}/source/latex/chappg/chappg.dtx
%doc %{_texmfdistdir}/source/latex/chappg/chappg.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1b-2
+ Revision: 750101
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.1b-1
+ Revision: 718033
- texlive-chappg
- texlive-chappg
- texlive-chappg
- texlive-chappg
- texlive-chappg

