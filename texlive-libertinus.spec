%global tl_name libertinus
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.02
Release:	%{tl_revision}.1
Summary:	Wrapper to use the correct libertinus package according to the used TeX engine
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/libertinus
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinus.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinus.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is only a wrapper for the two packages libertinus-type1
(pdfLaTeX) and libertinus-otf (LuaLaTeX/XeLaTeX). The Libertinus fonts
are similar to Libertine and Biolinum, but come with math symbols.

