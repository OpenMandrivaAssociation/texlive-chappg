Name:		texlive-chappg
Version:	15878
Release:	1
Summary:	Page numbering by chapter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chappg
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chappg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chappg.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chappg.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
