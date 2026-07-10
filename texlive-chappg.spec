%global tl_name chappg
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1b
Release:	%{tl_revision}.1
Summary:	Page numbering by chapter
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chappg
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chappg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chappg.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chappg.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides for 'chapterno-pageno' or 'chaptername-pageno' page
numbering. Provision is made for front- and backmatter in book class.

