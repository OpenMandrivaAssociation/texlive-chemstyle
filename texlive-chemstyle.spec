# revision 20996
# category Package
# catalog-ctan /macros/latex/contrib/chemstyle
# catalog-date 2011-01-05 22:49:37 +0100
# catalog-license lppl1.3
# catalog-version 2.0k
Name:		texlive-chemstyle
Version:	2.0k
Release:	1
Summary:	Writing chemistry with style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chemstyle
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemstyle.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemstyle.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemstyle.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
