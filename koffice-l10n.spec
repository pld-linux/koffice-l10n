# NOTE
# - easy way to update all sources with new/old locales:
#   lynx -dump ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n | awk '/.tar.bz2$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   and then ':r out' in vim and ./builder -a5 the spec
#   and ':%s#koffice-1.6.3#koffice-%{version}#g'
# - ISO 639-1 language codes maybe be looked up from http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
#
%define	koffice_epoch	5
Summary:	KOffice suite - international support
Summary(pl.UTF-8):	KOffice - wsparcie dla wielu języków
Name:		koffice-l10n
Version:	1.6.3
Release:	3
License:	GPL
Group:		I18n
Source0:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-bg-%{version}.tar.bz2
# Source0-md5:	da3167fc536f51d8e32998ae203cd4b9
Source1:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-ca-%{version}.tar.bz2
# Source1-md5:	5ec6aa3c1c613466a545e26bdb9dfd72
Source2:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-cs-%{version}.tar.bz2
# Source2-md5:	d893774830fa05b2450018ae70fcd267
Source3:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-cy-%{version}.tar.bz2
# Source3-md5:	6a100e050c3e6ae95733b24ce4d4f4cf
Source4:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-da-%{version}.tar.bz2
# Source4-md5:	fa9c878f7672d1b9881722f93a1dc1ce
Source5:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-de-%{version}.tar.bz2
# Source5-md5:	9153728550bc6101094bac42aefb7663
Source6:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-el-%{version}.tar.bz2
# Source6-md5:	be97b80ccaa0da028d8d04f263be5fed
Source7:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-en_GB-%{version}.tar.bz2
# Source7-md5:	468c3ac77b57de10e1cb7c99d184a443
Source8:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-es-%{version}.tar.bz2
# Source8-md5:	23f246f5bc86f8831e595f98c24c154e
Source9:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-et-%{version}.tar.bz2
# Source9-md5:	fdc1c81ae65bec5f7e56d76bcdbaa1af
Source10:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-eu-%{version}.tar.bz2
# Source10-md5:	3ca81163f7242bcad450342e1105ad89
Source11:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-fa-%{version}.tar.bz2
# Source11-md5:	63f5d0570660e47455e8ccd1a8c4bf02
Source12:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-fi-%{version}.tar.bz2
# Source12-md5:	98b3b306061c127b92d9e73d3641f687
Source13:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-fr-%{version}.tar.bz2
# Source13-md5:	01219310196ac9c8325c3d8c7456bcb3
Source14:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-ga-%{version}.tar.bz2
# Source14-md5:	80f28f345dbae9b108b97701ab2a3b7b
Source15:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-gl-%{version}.tar.bz2
# Source15-md5:	84b9c65886a99599d99c7ea077875a88
Source16:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-hu-%{version}.tar.bz2
# Source16-md5:	088e5c503a9dedfa8d23a3fa11f596ca
Source17:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-it-%{version}.tar.bz2
# Source17-md5:	1aa3d67279e63f7c7919908c686f2281
Source18:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-ja-%{version}.tar.bz2
# Source18-md5:	b0d886c7504a8b0bafb5095835e78c8a
Source19:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-km-%{version}.tar.bz2
# Source19-md5:	527e698b2907f90712239681f0ae0a9e
Source20:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-lv-%{version}.tar.bz2
# Source20-md5:	62386e1713216bd2709e1ce3fd150c8e
Source21:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-ms-%{version}.tar.bz2
# Source21-md5:	1bf2fcf2c82464e038eed026eaa13fca
Source22:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-nb-%{version}.tar.bz2
# Source22-md5:	462ecb27a008482801ca3bd9e803b2d1
Source23:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-nds-%{version}.tar.bz2
# Source23-md5:	50702ef6c8d586e89280a2b42d2c5225
Source24:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-ne-%{version}.tar.bz2
# Source24-md5:	bd95494b15f647dfcbe39d514811504a
Source25:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-nl-%{version}.tar.bz2
# Source25-md5:	a63c40510c0bb322dc1f6bb057759772
Source26:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-pl-%{version}.tar.bz2
# Source26-md5:	a174b73f3e2c0e579bf3775e481958dd
Source27:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-pt-%{version}.tar.bz2
# Source27-md5:	e74540534eae3d0b1cb4bbabf3da0ed0
Source28:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-pt_BR-%{version}.tar.bz2
# Source28-md5:	fe49fa2405b44044b69b5d1e2bcb15cf
Source29:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-ru-%{version}.tar.bz2
# Source29-md5:	e6be9bcea5e2b6e6aa4662f1530841ef
Source30:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-sk-%{version}.tar.bz2
# Source30-md5:	aa49a6c5497dc201359c577ab77c8361
Source31:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-sl-%{version}.tar.bz2
# Source31-md5:	18e3f2e81be91170fe551e4b47c2f907
Source32:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-sr-%{version}.tar.bz2
# Source32-md5:	3eb97f2ef5f65b3637af397dca0d8fcb
Source33:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-sr@Latn-%{version}.tar.bz2
# Source33-md5:	217064c12d6efe969a1bbdac2ef8aef0
Source34:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-sv-%{version}.tar.bz2
# Source34-md5:	c6c530010a64fb9e2880a3f33bb9276e
Source35:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-tr-%{version}.tar.bz2
# Source35-md5:	301f3a665f12d1b7f56fe9be93403812
Source36:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-uk-%{version}.tar.bz2
# Source36-md5:	f8a50375d4f280131a27e0bdfb0deb83
Source37:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-zh_CN-%{version}.tar.bz2
# Source37-md5:	a21490ebc1d0beedc565c070d4bdad25
Source38:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-zh_TW-%{version}.tar.bz2
# Source38-md5:	7c7c3787a45743ae9d06938829381d2e
Patch0:		koffice-module-l10n-locale-names.patch
BuildRequires:	gettext-devel
# It creates symlinks to some not-translated files.
BuildRequires:	kdelibs-devel >= 9:3.2
BuildRequires:	libxml2-progs >= 2.4.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KOffice suite - international support.

%description -l pl.UTF-8
KOffice - wsparcie dla wielu języków.

%package base
Summary:	Empty metapackage to handle obsoletes
Summary(pl.UTF-8):	Pusty metapakiet z obsoletes
Group:		I18n
Requires:	kde-i18n-base
Obsoletes:	koffice-common-i18n
Obsoletes:	koffice-i18n-base
Obsoletes:	koffice-karbon-i18n
Obsoletes:	koffice-kchart-i18n
Obsoletes:	koffice-kformula-i18n
Obsoletes:	koffice-kivio-i18n
Obsoletes:	koffice-kpresenter-i18n
Obsoletes:	koffice-kspread-i18n
Obsoletes:	koffice-kugar-i18n
Obsoletes:	koffice-kword-i18n
# Languages that didn't make it or are dropped
Obsoletes:	koffice-l10n-Afrikaans
Obsoletes:	koffice-l10n-Breton
Obsoletes:	koffice-l10n-Esperanto
Obsoletes:	koffice-l10n-Hebrew
Obsoletes:	koffice-l10n-Lao
Obsoletes:	koffice-l10n-Maltese
Obsoletes:	koffice-l10n-Northern_Sami
Obsoletes:	koffice-l10n-Norwegian_Nynorsk
Obsoletes:	koffice-l10n-Spanish
Obsoletes:	koffice-l10n-Tajik
Obsoletes:	koffice-l10n-Tamil
Obsoletes:	koffice-l10n-Thai
Obsoletes:	koffice-l10n-Upper_Sorbian
Obsoletes:	koffice-l10n-Xhosa
Obsoletes:	koffice-l10n-Zulu
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7

%description base
Empty metapackage to handle obsoletes for individual i18n subpackages.

%description base -l pl.UTF-8
Pusty metapakiet z Obsoletes dla oddzielnych podpakietów i18n.

%package Afrikaans
Summary:	KOffice suite - Afrikaans language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka afrykanerskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Afrikaans

%description Afrikaans
KOffice suite - Afrikaans language support.

%description Afrikaans -l pl.UTF-8
KOffice - wsparcie dla języka afrykanerskiego.

%package Arabic
Summary:	KOffice suite - Arabic language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka arabskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Arabic

%description Arabic
KOffice suite - Arabic language support.

%description Arabic -l pl.UTF-8
KOffice - wsparcie dla języka arabskiego.

%package Azerbaijani
Summary:	KOffice suite - Azerbaijani language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka azerskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Azerbaijani

%description Azerbaijani
KOffice suite - Azerbaijani language support.

%description Azerbaijani -l pl.UTF-8
KOffice - wsparcie dla języka azerskiego.

%package Bulgarian
Summary:	KOffice suite - Bulgarian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka bułgarskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Bulgarian

%description Bulgarian
KOffice suite - Bulgarian language support.

%description Bulgarian -l pl.UTF-8
KOffice - wsparcie dla języka bułgarskiego.

%package Breton
Summary:	KOffice suite - Breton language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka bretońskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Breton

%description Breton
KOffice suite - Breton language support.

%description Breton -l pl.UTF-8
KOffice - wsparcie dla języka bretońskiego.

%package Bosnian
Summary:	KOffice suite - Bosnian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka bośniackiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Bosnian

%description Bosnian
KOffice suite - Bosnian language support.

%description Bosnian -l pl.UTF-8
KOffice - wsparcie dla języka bośniackiego.

%package Catalan
Summary:	KOffice suite - Catalan language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka katalońskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Catalan

%description Catalan
KOffice suite - Catalan language support.

%description Catalan -l pl.UTF-8
KOffice - wsparcie dla języka katalońskiego.

%package Czech
Summary:	KOffice suite - Czech language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka czeskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Czech

%description Czech
KOffice suite - Czech language support.

%description Czech -l pl.UTF-8
KOffice - wsparcie dla języka czeskiego.

%package Cymraeg
Summary:	KOffice suite - Cymraeg language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka walijskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Cymraeg

%description Cymraeg
KOffice suite - Cymraeg language support.

%description Cymraeg -l pl.UTF-8
KOffice - wsparcie dla języka walijskiego.

%package Danish
Summary:	KOffice suite - Danish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka duńskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Danish

%description Danish
KOffice suite - Danish language support.

%description Danish -l pl.UTF-8
KOffice - wsparcie dla języka duńskiego.

%package German
Summary:	KOffice suite - German language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka niemieckiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-German

%description German
KOffice suite - German language support.

%description German -l pl.UTF-8
KOffice - wsparcie dla języka niemieckiego.

%package Greek
Summary:	KOffice suite - Greek language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka greckiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Greek

%description Greek
KOffice suite - Greek language support.

%description Greek -l pl.UTF-8
KOffice - wsparcie dla języka greckiego.

%package English
Summary:	KOffice suite - English language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka angielskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-English

%description English
KOffice suite - English language support.

%description English -l pl.UTF-8
KOffice - wsparcie dla języka angielskiego.

%package English_UK
Summary:	KOffice suite - KOffice suite - English (UK) language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka angielskiego (odmiany brytyjskiej)
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-English_UK

%description English_UK
KOffice suite - English (UK) language support.

%description English_UK -l pl.UTF-8
KOffice - wsparcie dla języka angielskiego (odmiany brytyjskiej).

%package Esperanto
Summary:	KOffice suite - Esperanto language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka esperanto
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Esperanto

%description Esperanto
KOffice suite - Esperanto language support.

%description Esperanto -l pl.UTF-8
KOffice - wsparcie dla języka esperanto.

%package Spanish
Summary:	KOffice suite - Spanish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka hiszpańskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Spanish

%description Spanish
KOffice suite - Spanish language support.

%description Spanish -l pl.UTF-8
KOffice - wsparcie dla języka hiszpańskiego.

%package Estonian
Summary:	KOffice suite - Estonian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka estońskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Estonian

%description Estonian
KOffice suite - Estonian language support.

%description Estonian -l pl.UTF-8
KOffice - wsparcie dla języka estońskiego.

%package Basque
Summary:	KOffice suite - Basque language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka baskijskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Basque

%description Basque
KOffice suite - Basque language support.

%description Basque -l pl.UTF-8
KOffice - wsparcie dla języka baskijskiego.

%package Farsi
Summary:	KOffice suite - Farsi language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka perskiego (farsi)
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Farsi

%description Farsi
KOffice suite - Farsi language support.

%description Farsi -l pl.UTF-8
KOffice - wsparcie dla języka perskiego (farsi).

%package Finnish
Summary:	KOffice suite - Finnish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka fińskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Finnish

%description Finnish
KOffice suite - Finnish language support.

%description Finnish -l pl.UTF-8
KOffice - wsparcie dla języka fińskiego.

%package French
Summary:	KOffice suite - French language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka francuskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-French

%description French
KOffice suite - French language support.

%description French -l pl.UTF-8
KOffice - wsparcie dla języka francuskiego.

%package Irish
Summary:	KOffice suite - Irish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka irlandzkiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Irish

%description Irish
KOffice suite - Irish language support.

%description Irish -l pl.UTF-8
KOffice - wsparcie dla języka irlandzkiego.

%package Galician
Summary:	KOffice suite - Galician language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka galicyjskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Galician

%description Galician
KOffice suite - Galician language support.

%description Galician -l pl.UTF-8
KOffice - wsparcie dla języka galicyjskiego.

%package Hindi
Summary:	KOffice suite - Hindi language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka hindi
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Hindi

%description Hindi
KOffice suite - Hindi language support.

%description Hindi -l pl.UTF-8
KOffice - wsparcie dla języka hindi.

%package Hebrew
Summary:	KOffice suite - Hebrew language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka hebrajskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Hebrew

%description Hebrew
KOffice suite - Hebrew language support.

%description Hebrew -l pl.UTF-8
KOffice - wsparcie dla języka hebrajskiego.

%package Croatian
Summary:	KOffice suite - Croatian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka chorwackiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Croatian

%description Croatian
KOffice suite - Croatian language support.

%description Croatian -l pl.UTF-8
KOffice - wsparcie dla języka chorwackiego.

%package Hungarian
Summary:	KOffice suite - Hungarian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka węgierskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Hungarian

%description Hungarian
KOffice suite - Hungarian language support.

%description Hungarian -l pl.UTF-8
KOffice - wsparcie dla języka węgierskiego.

%package Upper_Sorbian
Summary:	KOffice suite - Upper Sorbian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka górnołużyckiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Upper_Sorbian

%description Upper_Sorbian
KOffice suite - Upper Sorbian language support.

%description Upper_Sorbian  -l pl.UTF-8
KOffice - wsparcie dla języka górnołużyckiego.

%package Indonesian
Summary:	KOffice suite - Indonesian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka indonezyjskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Indonesian

%description Indonesian
KOffice suite - Indonesian language support.

%description Indonesian -l pl.UTF-8
KOffice - wsparcie dla języka indonezyjskiego.

%package Icelandic
Summary:	KOffice suite - Icelandic language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka islandzkiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Icelandic

%description Icelandic
KOffice suite - Icelandic language support.

%description Icelandic -l pl.UTF-8
KOffice - wsparcie dla języka islandzkiego.

%package Italian
Summary:	KOffice suite - Italian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka włoskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Italian

%description Italian
KOffice suite - Italian language support.

%description Italian -l pl.UTF-8
KOffice - wsparcie dla języka włoskiego.

%package Japanese
Summary:	KOffice suite - Japanese language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka japońskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Japanese

%description Japanese
KOffice suite - Japanese language support.

%description Japanese -l pl.UTF-8
KOffice - wsparcie dla języka japońskiego.

%package Khmer
Summary:	KOffice suite - Khmer language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka khmerskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Khmer
KOffice Suite - Khmer language support.

%description Khmer -l pl.UTF-8
KOffice - wsparcie dla języka khmerskiego.

%package Korean
Summary:	KOffice suite - Korean language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka koreańskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Korean

%description Korean
KOffice suite - Korean language support.

%description Korean -l pl.UTF-8
KOffice - wsparcie dla języka koreańskiego.

%package Lithuanian
Summary:	KOffice suite - Lithuanian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka litewskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Lithuanian

%description Lithuanian
KOffice suite - Lithuanian language support.

%description Lithuanian -l pl.UTF-8
KOffice - Wsparcie dla języka litewskiego.

%package Lao
Summary:	KOffice suite - Lao language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka laotańskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Lao

%description Lao
KOffice suite - lao language support.

%description Lao -l pl.UTF-8
KOffice - wsparcie dla języka laotańskiego.

%package Latvian
Summary:	KOffice suite - Latvian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka łotewskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Latvian

%description Latvian
KOffice suite - Latvian language support.

%description Latvian -l pl.UTF-8
KOffice - wsparcie dla języka łotewskiego.

%package Maori
Summary:	KOffice suite - Maori language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka maoryjskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Maori

%description Maori
KOffice suite - Maori language support.

%description Maori -l pl.UTF-8
KOffice - wsparcie dla języka maoryjskiego.

%package Macedonian
Summary:	KOffice suite - Macedonian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka macedońskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Macedonian

%description Macedonian
KOffice suite - Macedonian language support.

%description Macedonian -l pl.UTF-8
KOffice - wsparcie dla języka macedońskiego.

%package Malay
Summary:	KOffice suite - Malay language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka malajskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Malay

%description Malay
KOffice suite - Malay language support.

%description Malay -l pl.UTF-8
KOffice - wsparcie dla języka malajskiego.

%package Maltese
Summary:	KOffice suite - Maltese language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka maltańskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Maltese

%description Maltese
KOffice suite - Maltese language support.

%description Maltese -l pl.UTF-8
KOffice - wsparcie dla języka maltańskiego.

%package Mongolian
Summary:	KOffice suite - Mongolian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka mongolskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Mongolian

%description Mongolian
KOffice suite - Mongolian language support.

%description Mongolian -l pl.UTF-8
KOffice - wsparcie dla języka mongolskiego.

%package Dutch
Summary:	KOffice suite - Dutch language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka holenderskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Dutch

%description Dutch
KOffice suite - Dutch language support.

%description Dutch -l pl.UTF-8
KOffice - wsparcie dla języka holenderskiego.

%package Low_Saxon
Summary:	KOffice suite - Low Saxon language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka dolnosaksońskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Low_Saxon
KOffice suite - Low_Saxon language support.

%description Low_Saxon -l pl.UTF-8
KOffice - wsparcie dla języka dolnosaksońskiego.

%package Nepali
Summary:	KOffice suite - Nepali language support
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}

%description Nepali
KOffice suite - Nepali language support.

%description Low_Saxon -l pl.UTF-8
KOffice - wsparcie dla języka dolnosaksońskiego.

%package Norwegian_Bokmaal
Summary:	KOffice suite - Norwegian (Bokmaal) language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka norweskiego (odmiany bokmaal)
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Norwegian_Bokmaal

%description Norwegian_Bokmaal
KOffice suite - Norwegian (Bokmaal) language support.

%description Norwegian_Bokmaal -l pl.UTF-8
KOffice - wsparcie dla języka norweskiego (odmiany bokmaal).

%package Norwegian_Nynorsk
Summary:	KOffice suite - Norwegian (Nynorsk) language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka norweskiego (odmiany nynorsk)
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Norwegian_Nynorsk

%description Norwegian_Nynorsk
KOffice suite - Norwegian (Nynorsk) language support.

%description Norwegian_Nynorsk -l pl.UTF-8
KOffice - wsparcie dla języka norweskiego (odmiany nynorsk).

%package Northern_Sotho
Summary:	KOffice suite - Northern Sotho language support
Summary(pl.UTF-8):	KOffice - wsparcie dla północnej odmiany języka ludu Soto
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Northern_Sotho

%description Northern_Sotho
KOffice suite - Northern Sotho language support.

%description Northern_Sotho -l pl.UTF-8
KOffice - wsparcie dla północnej odmiany języka ludu Soto.

%package Gascon_occitan
Summary:	KOffice suite - Occitan (Gascon) language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka oksytańskiego (dialektu gaskońskiego)
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Gascon_occitan

%description Gascon_occitan
KOffice suite - Occitan (Gascon) language support.

%description Gascon_occitan -l pl.UTF-8
KOffice - wsparcie dla języka oksytańskiego (dialektu gaskońskiego).

%package Polish
Summary:	KOffice suite - Polish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka polskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Polish

%description Polish
KOffice suite - Polish language support.

%description Polish -l pl.UTF-8
KOffice - wsparcie dla języka polskiego.

%package Portuguese
Summary:	KOffice suite - Portuguese language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka portugalskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Portuguese

%description Portuguese
KOffice suite - Portuguese language support.

%description Portuguese -l pl.UTF-8
KOffice - wsparcie dla języka portugalskiego.

%package Brazil_Portuguese
Summary:	KOffice suite - Portuguese (Brazil) language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka portugalskiego (odmiany brazylijskiej)
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Brazil_Portuguese

%description Brazil_Portuguese
KOffice suite - Portuguese (Brazil) language support.

%description Brazil_Portuguese -l pl.UTF-8
KOffice - wsparcie dla języka portugalskiego (odmiany brazylijskiej).

%package Romanian
Summary:	KOffice suite - Romanian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka rumuńskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Romanian

%description Romanian
KOffice suite - Romanian language support.

%description Romanian -l pl.UTF-8
KOffice - wsparcie dla języka rumuńskiego.

%package Russian
Summary:	KOffice suite - Russian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka rosyjskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Russian

%description Russian
KOffice suite - Russian language support.

%description Russian -l pl.UTF-8
KOffice - wsparcie dla języka rosyjskiego.

%package Swati
Summary:	KOffice suite - Swati language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka swati
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Swati

%description Swati
KOffice suite - Swati language support.

%description Swati -l pl.UTF-8
KOffice - wsparcie dla języka swati.

%package Northern_Sami
Summary:	KOffice suite - Northern Sami language support
Summary(pl.UTF-8):	KOffice - wsparcie dla północnego języka saami (lapońskiego)
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Northern_Sami

%description Northern_Sami
KOffice suite - Northern Sami language support.

%description Northern_Sami -l pl.UTF-8
KOffice - wsparcie dla północnego języka saami (lapońskiego).

%package Slovak
Summary:	KOffice suite - Slovak language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka słowackiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Slovak

%description Slovak
KOffice suite - Slovak language support.

%description Slovak -l pl.UTF-8
KOffice - wsparcie dla języka słowackiego.

%package Slovenian
Summary:	KOffice suite - Slovenian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka słoweńskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Slovenian

%description Slovenian
KOffice suite - Slovenian language support.

%description Slovenian -l pl.UTF-8
KOffice - wsparcie dla języka słoweńskiego.

%package Serbian
Summary:	KOffice suite - Serbian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka serbskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Serbian

%description Serbian
KOffice suite - Serbian language support.

%description Serbian -l pl.UTF-8
KOffice - wsparcie dla języka serbskiego.

%package Swedish
Summary:	KOffice suite - Swedish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka szwedzkiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Swedish

%description Swedish
KOffice suite - Swedish language support.

%description Swedish -l pl.UTF-8
KOffice - wsparcie dla języka szwedzkiego.

%package Tamil
Summary:	KOffice suite - Tamil language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka tamilskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Tamil

%description Tamil
KOffice suite - Tamil language support.

%description Tamil -l pl.UTF-8
KOffice - wsparcie dla języka tamilskiego.

%package Tajik
Summary:	KOffice - Tajik language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka tadżyckiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Tajik

%description Tajik
KOffice - Tajik language support.

%description Tajik -l pl.UTF-8
KOffice - wsparcie dla języka tadżyckiego.

%package Thai
Summary:	KOffice suite - Thai language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka tajlandzkiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Thai

%description Thai
KOffice suite - Thai language support.

%description Thai -l pl.UTF-8
KOffice - wsparcie dla języka tajlandzkiego.

%package Turkish
Summary:	KOffice suite - Turkish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka tureckiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Turkish

%description Turkish
KOffice suite - Turkish language support.

%description Turkish -l pl.UTF-8
KOffice - wsparcie dla języka tureckiego.

%package Ukrainian
Summary:	KOffice suite - Ukrainian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka ukraińskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Ukrainian

%description Ukrainian
KOffice suite - Ukrainian language support.

%description Ukrainian -l pl.UTF-8
KOffice - wsparcie dla języka ukraińskiego.

%package Uzbek
Summary:	KOffice suite - Uzbek language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka uzbeckiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Uzbek

%description Uzbek
KOffice suite - Uzbek language support.

%description Uzbek -l pl.UTF-8
KOffice - wsparcie dla języka uzbeckiego.

%package Venda
Summary:	KOffice suite - Venda language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka venda
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Venda

%description Venda
KOffice suite - Venda language support.

%description Venda -l pl.UTF-8
KOffice - wsparcie dla języka venda.

%package Vietnamese
Summary:	KOffice suite - Vietnamese language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka wietnamskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Vietnamese

%description Vietnamese
KOffice suite - Vietnamese language support.

%description Vietnamese -l pl.UTF-8
KOffice - wsparcie dla języka wietnamskiego.

%package Walloon
Summary:	KOffice suite - Walloon language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka walońskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Walloon

%description Walloon
KOffice suite - Walloon language support.

%description Walloon -l pl.UTF-8
KOffice - wsparcie dla języka walońskiego.

%package Xhosa
Summary:	KOffice suite - Xhosa language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka khosa
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Xhosa

%description Xhosa
KOffice suite - Xhosa language support.

%description Xhosa -l pl.UTF-8
KOffice - wsparcie dla języka khosa.

%package Simplified_Chinese
Summary:	KOffice suite - simplified Chinese language support
Summary(pl.UTF-8):	KOffice - wsparcie dla uproszczonego języka chińskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Simplified_Chinese

%description Simplified_Chinese
KOffice suite - simplified Chinese language support.

%description Simplified_Chinese -l pl.UTF-8
KOffice - wsparcie dla uproszczonego języka chińskiego.

%package Chinese
Summary:	KOffice suite - Chinese language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka chińskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Chinese

%description Chinese
KOffice suite - Chinese language support.

%description Chinese -l pl.UTF-8
KOffice - wsparcie dla języka chińskiego.

%package Zulu
Summary:	KOffice suite - Zulu language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka zuluskiego
Group:		I18n
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Zulu

%description Zulu
KOffice suite - Zulu language support.

%description Zulu -l pl.UTF-8
KOffice - wsparcie dla języka zuluskiego.

%prep
%setup -q -c -T %(seq -f '-a %g' 0 38 | xargs)
%patch0 -p1

%build
for dir in %{name}-*-%{version}; do
	cd "$dir"
	%configure
	%{__make} \
		RPM_OPT_FLAGS="%{rpmcflags}" \
		kde_htmldir="%{_kdedocdir}" \
		kde_libs_htmldir="%{_kdedocdir}"
	cd ..
done

%install
if [ ! -f installed.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf $RPM_BUILD_ROOT

	for dir in %{name}-*-%{version}; do
		cd "$dir"
		%{__make} install \
			DESTDIR=$RPM_BUILD_ROOT \
			kde_htmldir="%{_kdedocdir}" \
			kde_libs_htmldir="%{_kdedocdir}"
		cd ..
	done
	touch installed.stamp
fi

rm -f *.lang

FindLang() {
	#    $1 - short language name
	local lang="$1"

	# share/doc/kde/HTML/(%%lang)
    if [ -d "$RPM_BUILD_ROOT%{_kdedocdir}/$lang" ]; then
		echo "%lang($lang) %{_kdedocdir}/$lang"
    fi

	# share/locale/(%%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/locale/$lang" ]; then
		echo "%lang($lang) %{_datadir}/locale/$lang/LC_MESSAGES/*.mo"
	fi

	# share/apps/koffice/autocorrect/*.xml
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/koffice/autocorrect/$lang.xml" ]; then
		echo "%lang($lang) %{_datadir}/apps/koffice/autocorrect/$lang.xml"
	fi

	touch $lang.ok
}

files="\
example \
graphite \
kdatabase \
kdgantt \
kexi \
kformdesigner \
kontour \
kplato \
krita \
"

for i in $files; do
	rm -rf $(find $RPM_BUILD_ROOT -name "$i*.mo")
	rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/$i
done

#FindLang af > Afrikaans.lang
#FindLang ar > Arabic.lang
#FindLang az > Azerbaijani.lang
FindLang bg > Bulgarian.lang
#FindLang br > Breton.lang
#FindLang bs > Bosnian.lang
FindLang ca > Catalan.lang
FindLang cs > Czech.lang
FindLang cy > Cymraeg.lang
FindLang da > Danish.lang
FindLang de > German.lang
FindLang el > Greek.lang
#FindLang en > English.lang
FindLang en_GB > English_UK.lang
#FindLang eo > Esperanto.lang
FindLang es > Spanish.lang
FindLang et > Estonian.lang
FindLang eu > Basque.lang
FindLang fa > Farsi.lang
FindLang fi > Finnish.lang
FindLang fr > French.lang
FindLang ga > Irish.lang
FindLang gl > Galician.lang
#FindLang he > Hebrew.lang
#FindLang hsb > Upper_Sorbian.lang
#FindLang hi > Hindi.lang
#FindLang hr > Croatian.lang
FindLang hu > Hungarian.lang
#FindLang id > Indonesian.lang
#FindLang is > Icelandic.lang
FindLang it > Italian.lang
FindLang ja > Japanese.lang
FindLang km > Khmer.lang
#FindLang ko > Korean.lang
#FindLang lt > Lithuanian.lang
#FindLang lo > Lao.lang
FindLang lv > Latvian.lang
#FindLang mi > Maori.lang
#FindLang mk > Macedonian.lang
#FindLang mn > Mongolian.lang
FindLang ms > Malay.lang
#FindLang mt > Maltese.lang
FindLang nds > Low_Saxon.lang
FindLang ne > Nepali.lang
FindLang nb > Norwegian_Bokmaal.lang
FindLang nl > Dutch.lang
#FindLang nn > Norwegian_Nynorsk.lang
#FindLang nso > Northern_Sotho.lang
#FindLang oc > Gascon_occitan.lang
FindLang pl > Polish.lang
FindLang pt > Portuguese.lang
FindLang pt_BR > Brazil_Portuguese.lang
#FindLang ro > Romanian.alng
FindLang ru > Russian.lang
#FindLang ss > Swati.lang
#FindLang se > Northern_Sami.lang
FindLang sk > Slovak.lang
FindLang sl > Slovenian.lang
FindLang sr > Serbian.lang
FindLang sr@latin > Serbian_Latin.lang
cat Serbian_Latin.lang >> Serbian.lang
rm -f Serbian_Latin.lang
FindLang sv > Swedish.lang
#FindLang ta > Tamil.lang
#FindLang tg > Tajik.lang
#FindLang th > Thai.lang
FindLang tr > Turkish.lang
FindLang uk > Ukrainian.lang
#FindLang uz > Uzbek.lang
#FindLang ve > Venda.lang
#FindLang vi > Vietnamese.lang
#FindLang wa > Walloon.lang
#FindLang xh > Xhosa.lang
FindLang zh_CN > Simplified_Chinese.lang
FindLang zh_TW > Chinese.lang
#FindLang zu > Zulu.lang

check_installed_languages() {
	err=0
	# we ignore dialects (currently sr@latin is the only case)
	for a in $(ls -1d %{name}-*-%{version} | %{__sed} '/@/d'); do
		l=${a#%{name}-}
		l=${l%%-%{version}}
		if [ ! -f $l.ok ]; then
			echo >&2 "language $l not processed"
			err=1
		fi
	done
	if [ "$err" = 1 ]; then
		exit 1
	fi
}
check_installed_languages

%clean
check_installed_files() {
	for a in *.lang; do
		lang=${a%%.lang}

		rpmfile=%{_rpmdir}/%{name}-$lang-%{version}-%{release}.%{_target_cpu}.rpm
		if [ ! -f $rpmfile ]; then
			echo >&2 "Missing %%files section for $lang"
			exit 1
		fi
	done
}
check_installed_files
%{!?debug:rm -rf $RPM_BUILD_ROOT}

%files base
%defattr(644,root,root,755)

#%files -f Afrikaans.lang Afrikaans
#%defattr(644,root,root,755)

#%%files -f Arabic.lang Arabic
##%files -f Azerbaijani.lang Azerbaijani

%files -f Bulgarian.lang Bulgarian
%defattr(644,root,root,755)

#%files -f Breton.lang Breton
#%defattr(644,root,root,755)

##%files -f Bosnian.lang Bosnian

%files -f Catalan.lang Catalan
%defattr(644,root,root,755)

%files -f Czech.lang Czech
%defattr(644,root,root,755)

%files -f Cymraeg.lang Cymraeg
%defattr(644,root,root,755)

%files -f Danish.lang Danish
%defattr(644,root,root,755)

%files -f German.lang German
%defattr(644,root,root,755)

%files -f Greek.lang Greek
%defattr(644,root,root,755)

# %files -f English.lang English

%files -f English_UK.lang English_UK
%defattr(644,root,root,755)

#%files -f Esperanto.lang Esperanto
#%defattr(644,root,root,755)

%files -f Spanish.lang Spanish
%defattr(644,root,root,755)

%files -f Estonian.lang Estonian
%defattr(644,root,root,755)

%files -f Basque.lang Basque
%defattr(644,root,root,755)

%files -f Farsi.lang Farsi
%defattr(644,root,root,755)

%files -f Finnish.lang Finnish
%defattr(644,root,root,755)

%files -f French.lang French
%defattr(644,root,root,755)

%files -f Irish.lang Irish
%defattr(644,root,root,755)

%files -f Galician.lang Galician
%defattr(644,root,root,755)

##%files -f Hindi.lang Hindi

#%files -f Hebrew.lang Hebrew
#%defattr(644,root,root,755)

#%files -f Upper_Sorbian.lang Upper_Sorbian
#%defattr(644,root,root,755)

#%%files -f Croatian.lang Croatian

%files -f Hungarian.lang Hungarian
%defattr(644,root,root,755)

##%files -f Indonesian.lang Indonesian
#%%files -f Icelandic.lang Icelandic

%files -f Italian.lang Italian
%defattr(644,root,root,755)

%files -f Japanese.lang Japanese
%defattr(644,root,root,755)

%files -f Khmer.lang Khmer
%defattr(644,root,root,755)

##%files -f Korean.lang Korean

#%files -f Lao.lang Lao
#%defattr(644,root,root,755)

#%%files -f Lithuanian.lang Lithuanian

%files -f Latvian.lang Latvian
%defattr(644,root,root,755)

#%files -f Maltese.lang Maltese
#%defattr(644,root,root,755)

%files -f Malay.lang Malay
%defattr(644,root,root,755)

##%files -f Mongolian.lang Mongolian
# %files -f Maori.lang Maori
#%%files -f Macedonian.lang Macedonian

%files -f Dutch.lang Dutch
%defattr(644,root,root,755)

%files -f Low_Saxon.lang Low_Saxon
%defattr(644,root,root,755)

%files -f Nepali.lang Nepali
%defattr(644,root,root,755)

%files -f Norwegian_Bokmaal.lang Norwegian_Bokmaal
%defattr(644,root,root,755)

#%files -f Norwegian_Nynorsk.lang Norwegian_Nynorsk
#%defattr(644,root,root,755)

#%%files -f Northern_Sotho.lang Northern_Sotho
# %files -f Gascon_occitan.lang Gascon_occitan

%files -f Polish.lang Polish
%defattr(644,root,root,755)

%files -f Portuguese.lang Portuguese
%defattr(644,root,root,755)

%files -f Brazil_Portuguese.lang Brazil_Portuguese
%defattr(644,root,root,755)

##%files -f Romanian.lang Romanian

%files -f Russian.lang Russian
%defattr(644,root,root,755)

#%files -f Northern_Sami.lang Northern_Sami
#%defattr(644,root,root,755)

#%%files -f Swati.lang Swati

%files -f Slovak.lang Slovak
%defattr(644,root,root,755)

%files -f Slovenian.lang Slovenian
%defattr(644,root,root,755)

%files -f Serbian.lang Serbian
%defattr(644,root,root,755)

%files -f Swedish.lang Swedish
%defattr(644,root,root,755)

#%files -f Tamil.lang Tamil
#%defattr(644,root,root,755)

#%files -f Tajik.lang Tajik
#%defattr(644,root,root,755)

#%files -f Thai.lang Thai
#%defattr(644,root,root,755)

%files -f Turkish.lang Turkish
%defattr(644,root,root,755)

%files -f Ukrainian.lang Ukrainian
%defattr(644,root,root,755)
##%files -f Uzbek.lang Uzbek

#%files -f Venda.lang Venda
#%defattr(644,root,root,755)

#%%files -f Vietnamese.lang Vietnamese
# %files -f Walloon.lang Walloon

#%files -f Xhosa.lang Xhosa
#%defattr(644,root,root,755)

%files -f Simplified_Chinese.lang Simplified_Chinese
%defattr(644,root,root,755)

%files -f Chinese.lang Chinese
%defattr(644,root,root,755)

#%files -f Zulu.lang Zulu
#%defattr(644,root,root,755)
