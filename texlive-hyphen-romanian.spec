# revision 23092
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-romanian
Version:	20120124
Release:	1
Summary:	Romanian hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-romanian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Romanian in T1/EC and UTF-8 encodings.
The UTF-8 patterns use U+0219 for the character 's with comma
accent' and U+021B for 't with comma accent', but we may
consider using U+015F and U+0163 as well in the future.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-romanian
%_texmf_language_def_d/hyphen-romanian
%_texmf_language_lua_d/hyphen-romanian

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-romanian <<EOF
\%% from hyphen-romanian:
romanian loadhyph-ro.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-romanian
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-romanian <<EOF
\%% from hyphen-romanian:
\addlanguage{romanian}{loadhyph-ro.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-romanian
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-romanian <<EOF
-- from hyphen-romanian:
	['romanian'] = {
		loader = 'loadhyph-ro.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-ro.pat.txt',
		hyphenation = '',
	},
EOF
