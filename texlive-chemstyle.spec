%global tl_name chemstyle
%global tl_revision 31096

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0m
Release:	%{tl_revision}.1
Summary:	Writing chemistry with style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chemstyle
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemstyle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemstyle.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemstyle.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Chemstyle has been developed as a successor to the LaTeX package
provided by the rsc bundle. The package provides an extensible system
for formatting chemistry documents according to the conventions of a
number of leading journals. It also provides some handy chemistry-
related macros. Chemstyle is much enhanced compared to its predecessor,
and users of rsc are strongly encouraged to migrate (all of the
additional macros in the rsc LaTeX package are present in chemstyle).
The package chemscheme is distributed with chemstyle; chemstyle itself
incorporates ideas that come from the trivfloat package; the
documentation uses the auto-pst-pdf package.

