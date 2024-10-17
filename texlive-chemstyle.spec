Name:		texlive-chemstyle
Version:	31096
Release:	2
Summary:	Writing chemistry with style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chemstyle
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemstyle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemstyle.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemstyle.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Chemstyle has been developed as a successor to the LaTeX
package provided by the rsc bundle. The package provides an
extensible system for formatting chemistry documents according
to the conventions of a number of leading journals. It also
provides some handy chemistry-related macros. Chemstyle is much
enhanced compared to its predecessor, and users of rsc are
strongly encouraged to migrate (all of the additional macros in
the rsc LaTeX package are present in chemstyle). The package
chemscheme is distributed with chemstyle; chemstyle itself
incorporates ideas that come from the trivfloat package; the
documentation uses the auto-pst-pdf package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chemstyle/chemscheme.sty
%{_texmfdistdir}/tex/latex/chemstyle/chemstyle.sty
%{_texmfdistdir}/tex/latex/chemstyle/config/angew.chemstyle.cfg
%{_texmfdistdir}/tex/latex/chemstyle/config/ic.chemstyle.cfg
%{_texmfdistdir}/tex/latex/chemstyle/config/jacs.chemstyle.cfg
%{_texmfdistdir}/tex/latex/chemstyle/config/jomc.chemstyle.cfg
%{_texmfdistdir}/tex/latex/chemstyle/config/orglett.chemstyle.cfg
%{_texmfdistdir}/tex/latex/chemstyle/config/rsc.chemstyle.cfg
%{_texmfdistdir}/tex/latex/chemstyle/config/tetlett.chemstyle.cfg
%doc %{_texmfdistdir}/doc/latex/chemstyle/README
%doc %{_texmfdistdir}/doc/latex/chemstyle/chemscheme.cdx
%doc %{_texmfdistdir}/doc/latex/chemstyle/chemstyle-demo.tex
%doc %{_texmfdistdir}/doc/latex/chemstyle/chemstyle.pdf
#- source
%doc %{_texmfdistdir}/source/latex/chemstyle/chemstyle.dtx
%doc %{_texmfdistdir}/source/latex/chemstyle/chemstyle.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
