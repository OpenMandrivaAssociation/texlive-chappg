Name:		texlive-chappg
Version:	2.1b
Release:	1
Summary:	Page numbering by chapter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chappg
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chappg.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chappg.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chappg.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides for 'chapterno-pageno' or 'chaptername-
pageno' page numbering. Provision is made for front- and
backmatter in book class.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
