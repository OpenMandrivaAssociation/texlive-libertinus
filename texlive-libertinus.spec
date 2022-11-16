Name:		texlive-libertinus
Version:	61719
Release:	1
Summary:	Wrapper to use the correct libertinus package according to the used TeX engine
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/libertinus
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinus.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinus.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is only a wrapper for the two packages
libertinus-type1 (pdfLaTeX) and libertinus-otf
(LuaLaTeX/XeLaTeX). The Libertinus fonts are similiar to
Libertine and Biolinum, but come with math symbols.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/libertinus
%doc %{_texmfdistdir}/doc/fonts/libertinus

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
