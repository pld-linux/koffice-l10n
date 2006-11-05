# TODO
# - missing:
# - koffice-bg-1.6.0.tar.bz2
# - koffice-nn-1.6.0.tar.bz2
# - koffice-ta-1.6.0.tar.bz2
# - koffice-tg-1.6.0.tar.bz2
# - broken: es
%define	koffice_epoch	5
Summary:	KOffice suite - international support
Summary(pl):	KOffice - wsparcie dla wielu jêzyków
Name:		koffice-l10n
Version:	1.6.0
Release:	0.1
License:	GPL
Group:		X11/Applications
#Source0:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-bg-%{version}.tar.bz2
##Source0-md5:	8daaeb614b3439490c2dd64a5ca6a90d
Source1:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-ca-%{version}.tar.bz2
# Source1-md5:	b90e14bd3508bcc030096496ea87683a
Source2:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-cs-%{version}.tar.bz2
# Source2-md5:	21f9a7c3daf57aabf70111dded8a26a6
Source3:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-cy-%{version}.tar.bz2
# Source3-md5:	b1d03624474b91becd3ff64647f45087
Source4:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-da-%{version}.tar.bz2
# Source4-md5:	d1532dc1107f01752a9eeeb362666289
Source5:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-de-%{version}.tar.bz2
# Source5-md5:	21344257dcd9b418898fb5e348918171
Source6:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-el-%{version}.tar.bz2
# Source6-md5:	c00bbbf55de2d5d8aa68916ef6618ee3
Source7:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-en_GB-%{version}.tar.bz2
# Source7-md5:	eb4582f359eaada24a1dd96443636219
Source8:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-es-%{version}.tar.bz2
# Source8-md5:	81db059841e59cfee6371d10b12e82d7
Source9:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-et-%{version}.tar.bz2
# Source9-md5:	64b4dd81d61362599af0882d695dd175
Source28:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-eu-%{version}.tar.bz2
# Source28-md5:	c3c5dbfe0135896c41f749ff79c6744e
Source10:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-fi-%{version}.tar.bz2
# Source10-md5:	738bf409e16c08018b75f672abcb94a4
Source11:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-fr-%{version}.tar.bz2
# Source11-md5:	96a5871374f69c694be87e621f04f39e
Source12:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-hu-%{version}.tar.bz2
# Source12-md5:	01ea831cfbd136fecb1c7de8826e97b9
Source13:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-it-%{version}.tar.bz2
# Source13-md5:	73f17287697e54e61237a8cf7f6fc75f
Source29:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-ja-%{version}.tar.bz2
# Source29-md5:	dd3f979c03f9bc4ae6393a54766b4a84
Source30:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-lv-%{version}.tar.bz2
# Source30-md5:	af51669631e18feef464e8d6778a41ad
Source31:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-ms-%{version}.tar.bz2
# Source31-md5:	259be59d9bfe0e7fba7d96c1b5740614
Source14:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-nb-%{version}.tar.bz2
# Source14-md5:	ef631712fe58e8129823b0f53253e153
Source15:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-nl-%{version}.tar.bz2
# Source15-md5:	b9c572b04701226fdce5e9ae5817177c
#Source16:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-nn-%{version}.tar.bz2
##Source16-md5:	12a451ca1384c776045a86aa3f0fecb5
Source17:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-pl-%{version}.tar.bz2
# Source17-md5:	aaa167a7881f383b88696d34fd1903a5
Source18:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-pt-%{version}.tar.bz2
# Source18-md5:	c907923d13d2e2d15e09ac5be9259c96
Source19:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-pt_BR-%{version}.tar.bz2
# Source19-md5:	8d1be2180acdba3287c2936cc379b4c6
Source20:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-ru-%{version}.tar.bz2
# Source20-md5:	0b895c8a86f0b3c6f31903c906e0dd08
Source32:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-sk-%{version}.tar.bz2
# Source32-md5:	3bdbfb8532c3a3422345ff8693544b29
Source21:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-sl-%{version}.tar.bz2
# Source21-md5:	6dfa4b30a8d246a46dddef1e3933cf36
Source22:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-sr-%{version}.tar.bz2
# Source22-md5:	69681fe0a95a61b88aa5b9ee226fc320
Source23:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-sr@Latn-%{version}.tar.bz2
# Source23-md5:	8ce2f6edd23a43b079fbec9c20cfe516
Source24:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-sv-%{version}.tar.bz2
# Source24-md5:	774efb0a9c02776c58ca6cfe1930d327
#Source25:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-ta-%{version}.tar.bz2
##Source25-md5:	536e66f3b85923771f2af964b51a465e
#Source26:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-tg-%{version}.tar.bz2
##Source26-md5:	a38ec98b0f6437ddb93196f369a09485
Source33:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-tr-%{version}.tar.bz2
# Source33-md5:	d941eddab83cc8991d4f218854d25f64
Source27:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-zh_CN-%{version}.tar.bz2
# Source27-md5:	a3fda356e170368d7fd88d0ce892307b
Source34:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-zh_TW-%{version}.tar.bz2
# Source34-md5:	17ec8363abee3dd45c1a4c103b023ff3
BuildRequires:	gettext-devel
# It creates symlinks to some not-translated files.
BuildRequires:	kdelibs-devel >= 9:3.2
BuildRequires:	libxml2-progs >= 2.4.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KOffice suite - international support.

%description -l pl
KOffice - wsparcie dla wielu jêzyków.

%package base
Summary:	Empty metapackage to handle obsoletes
Summary(pl):	Pusty metapakiet z obsoletes
Group:		X11/Applications
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
Obsoletes:	koffice-l10n-Bulgarian
Obsoletes:	koffice-l10n-Norwegian_Nynorsk
Obsoletes:	koffice-l10n-Tajik
Obsoletes:	koffice-l10n-Tamil

%description base
Empty metapackage to handle obsoletes for individual i18n subpackages.

%description base -l pl
Pusty metapakiet z Obsoletes dla oddzielnych podpakietów i18n.

%package Afrikaans
Summary:	KOffice suite - Afrikaans language support
Summary(pl):	KOffice - wsparcie dla jêzyka afrykanerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Afrikaans

%description Afrikaans
KOffice suite - Afrikaans language support.

%description Afrikaans -l pl
KOffice - wsparcie dla jêzyka afrykanerskiego.

%package Arabic
Summary:	KOffice suite - Arabic language support
Summary(pl):	KOffice - wsparcie dla jêzyka arabskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Arabic

%description Arabic
KOffice suite - Arabic language support.

%description Arabic -l pl
KOffice - wsparcie dla jêzyka arabskiego.

%package Azerbaijani
Summary:	KOffice suite - Azerbaijani language support
Summary(pl):	KOffice - wsparcie dla jêzyka azerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Azerbaijani

%description Azerbaijani
KOffice suite - Azerbaijani language support.

%description Azerbaijani -l pl
KOffice - wsparcie dla jêzyka azerskiego.

%package Bulgarian
Summary:	KOffice suite - Bulgarian language support
Summary(pl):	KOffice - wsparcie dla jêzyka bu³garskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Bulgarian

%description Bulgarian
KOffice suite - Bulgarian language support.

%description Bulgarian -l pl
KOffice - wsparcie dla jêzyka bu³garskiego.

%package Breton
Summary:	KOffice suite - Breton language support
Summary(pl):	KOffice - wsparcie dla jêzyka bretoñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Breton

%description Breton
KOffice suite - Breton language support.

%description Breton -l pl
KOffice - wsparcie dla jêzyka bretoñskiego.

%package Bosnian
Summary:	KOffice suite - Bosnian language support
Summary(pl):	KOffice - wsparcie dla jêzyka bo¶niackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Bosnian

%description Bosnian
KOffice suite - Bosnian language support.

%description Bosnian -l pl
KOffice - wsparcie dla jêzyka bo¶niackiego.

%package Catalan
Summary:	KOffice suite - Catalan language support
Summary(pl):	KOffice - wsparcie dla jêzyka kataloñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Catalan

%description Catalan
KOffice suite - Catalan language support.

%description Catalan -l pl
KOffice - wsparcie dla jêzyka kataloñskiego.

%package Czech
Summary:	KOffice suite - Czech language support
Summary(pl):	KOffice - wsparcie dla jêzyka czeskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Czech

%description Czech
KOffice suite - Czech language support.

%description Czech -l pl
KOffice - wsparcie dla jêzyka czeskiego.

%package Cymraeg
Summary:	KOffice suite - Cymraeg language support
Summary(pl):	KOffice - wsparcie dla jêzyka walijskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Cymraeg

%description Cymraeg
KOffice suite - Cymraeg language support.

%description Cymraeg -l pl
KOffice - wsparcie dla jêzyka walijskiego.

%package Danish
Summary:	KOffice suite - Danish language support
Summary(pl):	KOffice - wsparcie dla jêzyka duñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Danish

%description Danish
KOffice suite - Danish language support.

%description Danish -l pl
KOffice - wsparcie dla jêzyka duñskiego.

%package German
Summary:	KOffice suite - German language support
Summary(pl):	KOffice - wsparcie dla jêzyka niemieckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-German

%description German
KOffice suite - German language support.

%description German -l pl
KOffice - wsparcie dla jêzyka niemieckiego.

%package Greek
Summary:	KOffice suite - Greek language support
Summary(pl):	KOffice - wsparcie dla jêzyka greckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Greek

%description Greek
KOffice suite - Greek language support.

%description Greek -l pl
KOffice - wsparcie dla jêzyka greckiego.

%package English
Summary:	KOffice suite - English language support
Summary(pl):	KOffice - wsparcie dla jêzyka angielskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-English

%description English
KOffice suite - English language support.

%description English -l pl
KOffice - wsparcie dla jêzyka angielskiego.

%package English_UK
Summary:	KOffice suite - KOffice suite - English (UK) language support
Summary(pl):	KOffice - wsparcie dla jêzyka angielskiego (odmiany brytyjskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-English_UK

%description English_UK
KOffice suite - English (UK) language support.

%description English_UK -l pl
KOffice - wsparcie dla jêzyka angielskiego (odmiany brytyjskiej).

%package Esperanto
Summary:	KOffice suite - Esperanto language support
Summary(pl):	KOffice - wsparcie dla jêzyka esperanto
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Esperanto

%description Esperanto
KOffice suite - Esperanto language support.

%description Esperanto -l pl
KOffice - wsparcie dla jêzyka esperanto.

%package Spanish
Summary:	KOffice suite - Spanish language support
Summary(pl):	KOffice - wsparcie dla jêzyka hiszpañskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Spanish

%description Spanish
KOffice suite - Spanish language support.

%description Spanish -l pl
KOffice - wsparcie dla jêzyka hiszpañskiego.

%package Estonian
Summary:	KOffice suite - Estonian language support
Summary(pl):	KOffice - wsparcie dla jêzyka estoñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Estonian

%description Estonian
KOffice suite - Estonian language support.

%description Estonian -l pl
KOffice - wsparcie dla jêzyka estoñskiego.

%package Basque
Summary:	KOffice suite - Basque language support
Summary(pl):	KOffice - wsparcie dla jêzyka baskijskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Basque

%description Basque
KOffice suite - Basque language support.

%description Basque -l pl
KOffice - wsparcie dla jêzyka baskijskiego.

%package Farsi
Summary:	KOffice suite - Farsi language support
Summary(pl):	KOffice - wsparcie dla jêzyka perskiego (farsi)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Farsi

%description Farsi
KOffice suite - Farsi language support.

%description Farsi -l pl
KOffice - wsparcie dla jêzyka perskiego (farsi).

%package Finnish
Summary:	KOffice suite - Finnish language support
Summary(pl):	KOffice - wsparcie dla jêzyka fiñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Finnish

%description Finnish
KOffice suite - Finnish language support.

%description Finnish -l pl
KOffice - wsparcie dla jêzyka fiñskiego.

%package French
Summary:	KOffice suite - French language support
Summary(pl):	KOffice - wsparcie dla jêzyka francuskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-French

%description French
KOffice suite - French language support.

%description French -l pl
KOffice - wsparcie dla jêzyka francuskiego.

%package Irish
Summary:	KOffice suite - Irish language support
Summary(pl):	KOffice - wsparcie dla jêzyka irlandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Irish

%description Irish
KOffice suite - Irish language support.

%description Irish -l pl
KOffice - wsparcie dla jêzyka irlandzkiego.

%package Galician
Summary:	KOffice suite - Galician language support
Summary(pl):	KOffice - wsparcie dla jêzyka galicyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Galician

%description Galician
KOffice suite - Galician language support.

%description Galician -l pl
KOffice - wsparcie dla jêzyka galicyjskiego.

%package Hindi
Summary:	KOffice suite - Hindi language support
Summary(pl):	KOffice - wsparcie dla jêzyka hindi
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Hindi

%description Hindi
KOffice suite - Hindi language support.

%description Hindi -l pl
KOffice - wsparcie dla jêzyka hindi.

%package Hebrew
Summary:	KOffice suite - Hebrew language support
Summary(pl):	KOffice - wsparcie dla jêzyka hebrajskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Hebrew

%description Hebrew
KOffice suite - Hebrew language support.

%description Hebrew -l pl
KOffice - wsparcie dla jêzyka hebrajskiego.

%package Croatian
Summary:	KOffice suite - Croatian language support
Summary(pl):	KOffice - wsparcie dla jêzyka chorwackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Croatian

%description Croatian
KOffice suite - Croatian language support.

%description Croatian -l pl
KOffice - wsparcie dla jêzyka chorwackiego.

%package Hungarian
Summary:	KOffice suite - Hungarian language support
Summary(pl):	KOffice - wsparcie dla jêzyka wêgierskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Hungarian

%description Hungarian
KOffice suite - Hungarian language support.

%description Hungarian -l pl
KOffice - wsparcie dla jêzyka wêgierskiego.

%package Upper_Sorbian
Summary:	KOffice suite - Upper Sorbian language support
Summary(pl):	KOffice - wsparcie dla jêzyka górno³u¿yckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Upper_Sorbian

%description Upper_Sorbian
KOffice suite - Upper Sorbian language support.

%description Upper_Sorbian  -l pl
KOffice - wsparcie dla jêzyka górno³u¿yckiego.

%package Indonesian
Summary:	KOffice suite - Indonesian language support
Summary(pl):	KOffice - wsparcie dla jêzyka indonezyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Indonesian

%description Indonesian
KOffice suite - Indonesian language support.

%description Indonesian -l pl
KOffice - wsparcie dla jêzyka indonezyjskiego.

%package Icelandic
Summary:	KOffice suite - Icelandic language support
Summary(pl):	KOffice - wsparcie dla jêzyka islandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Icelandic

%description Icelandic
KOffice suite - Icelandic language support.

%description Icelandic -l pl
KOffice - wsparcie dla jêzyka islandzkiego.

%package Italian
Summary:	KOffice suite - Italian language support
Summary(pl):	KOffice - wsparcie dla jêzyka w³oskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Italian

%description Italian
KOffice suite - Italian language support.

%description Italian -l pl
KOffice - wsparcie dla jêzyka w³oskiego.

%package Japanese
Summary:	KOffice suite - Japanese language support
Summary(pl):	KOffice - wsparcie dla jêzyka japoñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Japanese

%description Japanese
KOffice suite - Japanese language support.

%description Japanese -l pl
KOffice - wsparcie dla jêzyka japoñskiego.

%package Korean
Summary:	KOffice suite - Korean language support
Summary(pl):	KOffice - wsparcie dla jêzyka koreañskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Korean

%description Korean
KOffice suite - Korean language support.

%description Korean -l pl
KOffice - wsparcie dla jêzyka koreañskiego.

%package Lithuanian
Summary:	KOffice suite - Lithuanian language support
Summary(pl):	KOffice - wsparcie dla jêzyka litewskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Lithuanian

%description Lithuanian
KOffice suite - Lithuanian language support.

%description Lithuanian -l pl
KOffice - Wsparcie dla jêzyka litewskiego.

%package Lao
Summary:	KOffice suite - Lao language support
Summary(pl):	KOffice - wsparcie dla jêzyka laotañskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Lao

%description Lao
KOffice suite - lao language support.

%description Lao -l pl
KOffice - wsparcie dla jêzyka laotañskiego.

%package Latvian
Summary:	KOffice suite - Latvian language support
Summary(pl):	KOffice - wsparcie dla jêzyka ³otewskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Latvian

%description Latvian
KOffice suite - Latvian language support.

%description Latvian -l pl
KOffice - wsparcie dla jêzyka ³otewskiego.

%package Maori
Summary:	KOffice suite - Maori language support
Summary(pl):	KOffice - wsparcie dla jêzyka maoryjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Maori

%description Maori
KOffice suite - Maori language support.

%description Maori -l pl
KOffice - wsparcie dla jêzyka maoryjskiego.

%package Macedonian
Summary:	KOffice suite - Macedonian language support
Summary(pl):	KOffice - wsparcie dla jêzyka macedoñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Macedonian

%description Macedonian
KOffice suite - Macedonian language support.

%description Macedonian -l pl
KOffice - wsparcie dla jêzyka macedoñskiego.

%package Malay
Summary:	KOffice suite - Malay language support
Summary(pl):	KOffice - wsparcie dla jêzyka malajskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Malay

%description Malay
KOffice suite - Malay language support.

%description Malay -l pl
KOffice - wsparcie dla jêzyka malajskiego.

%package Maltese
Summary:	KOffice suite - Maltese language support
Summary(pl):	KOffice - wsparcie dla jêzyka maltañskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Maltese

%description Maltese
KOffice suite - Maltese language support.

%description Maltese -l pl
KOffice - wsparcie dla jêzyka maltañskiego.

%package Mongolian
Summary:	KOffice suite - Mongolian language support
Summary(pl):	KOffice - wsparcie dla jêzyka mongolskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Mongolian

%description Mongolian
KOffice suite - Mongolian language support.

%description Mongolian -l pl
KOffice - wsparcie dla jêzyka mongolskiego.

%package Dutch
Summary:	KOffice suite - Dutch language support
Summary(pl):	KOffice - wsparcie dla jêzyka holenderskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Dutch

%description Dutch
KOffice suite - Dutch language support.

%description Dutch -l pl
KOffice - wsparcie dla jêzyka holenderskiego.

%package Norwegian_Bokmaal
Summary:	KOffice suite - Norwegian (Bokmaal) language support
Summary(pl):	KOffice - wsparcie dla jêzyka norweskiego (odmiany bokmaal)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Norwegian_Bokmaal

%description Norwegian_Bokmaal
KOffice suite - Norwegian (Bokmaal) language support.

%description Norwegian_Bokmaal -l pl
KOffice - wsparcie dla jêzyka norweskiego (odmiany bokmaal).

%package Norwegian_Nynorsk
Summary:	KOffice suite - Norwegian (Nynorsk) language support
Summary(pl):	KOffice - wsparcie dla jêzyka norweskiego (odmiany nynorsk)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Norwegian_Nynorsk

%description Norwegian_Nynorsk
KOffice suite - Norwegian (Nynorsk) language support.

%description Norwegian_Nynorsk -l pl
KOffice - wsparcie dla jêzyka norweskiego (odmiany nynorsk).

%package Northern_Sotho
Summary:	KOffice suite - Northern Sotho language support
Summary(pl):	KOffice - wsparcie dla pó³nocnej odmiany jêzyka ludu Soto
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Northern_Sotho

%description Northern_Sotho
KOffice suite - Northern Sotho language support.

%description Northern_Sotho -l pl
KOffice - wsparcie dla pó³nocnej odmiany jêzyka ludu Soto.

%package Gascon_occitan
Summary:	KOffice suite - Occitan (Gascon) language support
Summary(pl):	KOffice - wsparcie dla jêzyka oksytañskiego (dialektu gaskoñskiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Gascon_occitan

%description Gascon_occitan
KOffice suite - Occitan (Gascon) language support.

%description Gascon_occitan -l pl
KOffice - wsparcie dla jêzyka oksytañskiego (dialektu gaskoñskiego).

%package Polish
Summary:	KOffice suite - Polish language support
Summary(pl):	KOffice - wsparcie dla jêzyka polskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Polish

%description Polish
KOffice suite - Polish language support.

%description Polish -l pl
KOffice - wsparcie dla jêzyka polskiego.

%package Portuguese
Summary:	KOffice suite - Portuguese language support
Summary(pl):	KOffice - wsparcie dla jêzyka portugalskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Portuguese

%description Portuguese
KOffice suite - Portuguese language support.

%description Portuguese -l pl
KOffice - wsparcie dla jêzyka portugalskiego.

%package Brazil_Portuguese
Summary:	KOffice suite - Portuguese (Brazil) language support
Summary(pl):	KOffice - wsparcie dla jêzyka portugalskiego (odmiany brazylijskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Brazil_Portuguese

%description Brazil_Portuguese
KOffice suite - Portuguese (Brazil) language support.

%description Brazil_Portuguese -l pl
KOffice - wsparcie dla jêzyka portugalskiego (odmiany brazylijskiej).

%package Romanian
Summary:	KOffice suite - Romanian language support
Summary(pl):	KOffice - wsparcie dla jêzyka rumuñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Romanian

%description Romanian
KOffice suite - Romanian language support.

%description Romanian -l pl
KOffice - wsparcie dla jêzyka rumuñskiego.

%package Russian
Summary:	KOffice suite - Russian language support
Summary(pl):	KOffice - wsparcie dla jêzyka rosyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Russian

%description Russian
KOffice suite - Russian language support.

%description Russian -l pl
KOffice - wsparcie dla jêzyka rosyjskiego.

%package Swati
Summary:	KOffice suite - Swati language support
Summary(pl):	KOffice - wsparcie dla jêzyka swati
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Swati

%description Swati
KOffice suite - Swati language support.

%description Swati -l pl
KOffice - wsparcie dla jêzyka swati.

%package Northern_Sami
Summary:	KOffice suite - Northern Sami language support
Summary(pl):	KOffice - wsparcie dla pó³nocnego jêzyka saami (lapoñskiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Northern_Sami

%description Northern_Sami
KOffice suite - Northern Sami language support.

%description Northern_Sami -l pl
KOffice - wsparcie dla pó³nocnego jêzyka saami (lapoñskiego).

%package Slovak
Summary:	KOffice suite - Slovak language support
Summary(pl):	KOffice - wsparcie dla jêzyka s³owackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Slovak

%description Slovak
KOffice suite - Slovak language support.

%description Slovak -l pl
KOffice - wsparcie dla jêzyka s³owackiego.

%package Slovenian
Summary:	KOffice suite - Slovenian language support
Summary(pl):	KOffice - wsparcie dla jêzyka s³oweñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Slovenian

%description Slovenian
KOffice suite - Slovenian language support.

%description Slovenian -l pl
KOffice - wsparcie dla jêzyka s³oweñskiego.

%package Serbian
Summary:	KOffice suite - Serbian language support
Summary(pl):	KOffice - wsparcie dla jêzyka serbskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Serbian

%description Serbian
KOffice suite - Serbian language support.

%description Serbian -l pl
KOffice - wsparcie dla jêzyka serbskiego.

%package Swedish
Summary:	KOffice suite - Swedish language support
Summary(pl):	KOffice - wsparcie dla jêzyka szwedzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Swedish

%description Swedish
KOffice suite - Swedish language support.

%description Swedish -l pl
KOffice - wsparcie dla jêzyka szwedzkiego.

%package Tamil
Summary:	KOffice suite - Tamil language support
Summary(pl):	KOffice - wsparcie dla jêzyka tamilskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Tamil

%description Tamil
KOffice suite - Tamil language support.

%description Tamil -l pl
KOffice - wsparcie dla jêzyka tamilskiego.

%package Tajik
Summary:	KOffice - Tajik language support
Summary(pl):	KOffice - wsparcie dla jêzyka tad¿yckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Tajik

%description Tajik
KOffice - Tajik language support.

%description Tajik -l pl
KOffice - wsparcie dla jêzyka tad¿yckiego.

%package Thai
Summary:	KOffice suite - Thai language support
Summary(pl):	KOffice - wsparcie dla jêzyka tajlandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Thai

%description Thai
KOffice suite - Thai language support.

%description Thai -l pl
KOffice - wsparcie dla jêzyka tajlandzkiego.

%package Turkish
Summary:	KOffice suite - Turkish language support
Summary(pl):	KOffice - wsparcie dla jêzyka tureckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Turkish

%description Turkish
KOffice suite - Turkish language support.

%description Turkish -l pl
KOffice - wsparcie dla jêzyka tureckiego.

%package Ukrainian
Summary:	KOffice suite - Ukrainian language support
Summary(pl):	KOffice - wsparcie dla jêzyka ukraiñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Ukrainian

%description Ukrainian
KOffice suite - Ukrainian language support.

%description Ukrainian -l pl
KOffice - wsparcie dla jêzyka ukraiñskiego.

%package Uzbek
Summary:	KOffice suite - Uzbek language support
Summary(pl):	KOffice - wsparcie dla jêzyka uzbeckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Uzbek

%description Uzbek
KOffice suite - Uzbek language support.

%description Uzbek -l pl
KOffice - wsparcie dla jêzyka uzbeckiego.

%package Venda
Summary:	KOffice suite - Venda language support
Summary(pl):	KOffice - wsparcie dla jêzyka venda
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Venda

%description Venda
KOffice suite - Venda language support.

%description Venda -l pl
KOffice - wsparcie dla jêzyka venda.

%package Vietnamese
Summary:	KOffice suite - Vietnamese language support
Summary(pl):	KOffice - wsparcie dla jêzyka wietnamskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Vietnamese

%description Vietnamese
KOffice suite - Vietnamese language support.

%description Vietnamese -l pl
KOffice - wsparcie dla jêzyka wietnamskiego.

%package Walloon
Summary:	KOffice suite - Walloon language support
Summary(pl):	KOffice - wsparcie dla jêzyka waloñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Walloon

%description Walloon
KOffice suite - Walloon language support.

%description Walloon -l pl
KOffice - wsparcie dla jêzyka waloñskiego.

%package Xhosa
Summary:	KOffice suite - Xhosa language support
Summary(pl):	KOffice - wsparcie dla jêzyka khosa
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Xhosa

%description Xhosa
KOffice suite - Xhosa language support.

%description Xhosa -l pl
KOffice - wsparcie dla jêzyka khosa.

%package Simplified_Chinese
Summary:	KOffice suite - simplified Chinese language support
Summary(pl):	KOffice - wsparcie dla uproszczonego jêzyka chiñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Simplified_Chinese

%description Simplified_Chinese
KOffice suite - simplified Chinese language support.

%description Simplified_Chinese -l pl
KOffice - wsparcie dla uproszczonego jêzyka chiñskiego.

%package Chinese
Summary:	KOffice suite - Chinese language support
Summary(pl):	KOffice - wsparcie dla jêzyka chiñskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Chinese

%description Chinese
KOffice suite - Chinese language support.

%description Chinese -l pl
KOffice - wsparcie dla jêzyka chiñskiego.

%package Zulu
Summary:	KOffice suite - Zulu language support
Summary(pl):	KOffice - wsparcie dla jêzyka zuluskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Zulu

%description Zulu
KOffice suite - Zulu language support.

%description Zulu -l pl
KOffice - wsparcie dla jêzyka zuluskiego.

%prep
%setup -q -c -T %(seq -f '-a %g' 1 34 | egrep -v '^-a (16|25|26)$' | xargs)


%build
# broken
rm -rf koffice-l10n-es-*

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
#    $2 - long language name
	local lang="$1"
	local language="$2"

	> "$language.lang"

# share/doc/kde/HTML/(%%lang)
    if [ -d "$RPM_BUILD_ROOT%{_kdedocdir}/$lang" ]; then
		echo "%lang($lang) %{_kdedocdir}/$lang" >> "$language.lang"
    fi

# share/locale/(%%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/locale/$lang" ]; then
		echo "%lang($lang) %{_datadir}/locale/$lang/LC_MESSAGES/*.mo" >> "$language.lang"
	fi

# share/apps/koffice/autocorrect/*.xml
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/koffice/autocorrect/$lan.xml" ]; then
		echo "%lang($lang) %{_datadir}/apps/koffice/autocorrect/$lang.xml" >> "$language.lang"
	fi

	if [ ! -s $language.lang ]; then
		echo >&2 "Missing launguage: $language ($lang)"
	fi
}

ziew="\
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

for i in $ziew; do
	rm -rf `find $RPM_BUILD_ROOT -name ${i}\*\.mo`
	rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/${i}
done

FindLang af Afrikaans
#FindLang ar Arabic
#FindLang az Azerbaijani
#FindLang bg Bulgarian
FindLang br Breton
#FindLang bs Bosnian
FindLang ca Catalan
FindLang cs Czech
FindLang cy Cymraeg
FindLang da Danish
FindLang de German
FindLang el Greek
#FindLang en English
FindLang en_GB English_UK
FindLang eo Esperanto
FindLang es Spanish
FindLang et Estonian
FindLang eu Basque
FindLang fa Farsi
FindLang fi Finnish
FindLang fr French
#FindLang ga Irish
#FindLang gl Galician
FindLang he Hebrew
FindLang hsb Upper_Sorbian
#FindLang hi Hindi
#FindLang hr Croatian
FindLang hu Hungarian
#FindLang id Indonesian
#FindLang is Icelandic
FindLang it Italian
FindLang ja Japanese
#FindLang ko Korean
#FindLang lt Lithuanian
FindLang lo Lao
FindLang lv Latvian
#FindLang mi Maori
#FindLang mk Macedonian
#FindLang mn Mongolian
FindLang ms Malay
FindLang mt Maltese
FindLang nb Norwegian_Bokmaal
FindLang nl Dutch
#FindLang nn Norwegian_Nynorsk
#FindLang nso Northern_Sotho
#FindLang oc Gascon_occitan
FindLang pl Polish
FindLang pt Portuguese
FindLang pt_BR Brazil_Portuguese
#FindLang ro Romanian
FindLang ru Russian
#FindLang ss Swati
FindLang se Northern_Sami
FindLang sk Slovak
FindLang sl Slovenian
FindLang sr Serbian
FindLang sr@Latn Serbian_Latin
cat Serbian_Latin.lang >> Serbian.lang
FindLang sv Swedish
#FindLang ta Tamil
#FindLang tg Tajik
FindLang th Thai
FindLang tr Turkish
#FindLang uk Ukrainian
#FindLang uz Uzbek
FindLang ve Venda
#FindLang vi Vietnamese
#FindLang wa Walloon
FindLang xh Xhosa
FindLang zh_CN Simplified_Chinese
FindLang zh_TW Chinese
FindLang zu Zulu

%clean
rm -rf $RPM_BUILD_ROOT

%files base
%defattr(644,root,root,755)

%files -f Afrikaans.lang Afrikaans
%defattr(644,root,root,755)

#%%files -f Arabic.lang Arabic
##%files -f Azerbaijani.lang Azerbaijani

%files -f Bulgarian.lang Bulgarian
%defattr(644,root,root,755)

%files -f Breton.lang Breton
%defattr(644,root,root,755)

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

%files -f Esperanto.lang Esperanto
%defattr(644,root,root,755)

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

# %files -f Irish.lang Irish
##%files -f Galician.lang Galician
##%files -f Hindi.lang Hindi

%files -f Hebrew.lang Hebrew
%defattr(644,root,root,755)

%files -f Upper_Sorbian.lang Upper_Sorbian
%defattr(644,root,root,755)

#%%files -f Croatian.lang Croatian

%files -f Hungarian.lang Hungarian
%defattr(644,root,root,755)

##%files -f Indonesian.lang Indonesian
#%%files -f Icelandic.lang Icelandic

%files -f Italian.lang Italian
%defattr(644,root,root,755)

%files -f Japanese.lang Japanese
%defattr(644,root,root,755)

##%files -f Korean.lang Korean

%files -f Lao.lang Lao
%defattr(644,root,root,755)

#%%files -f Lithuanian.lang Lithuanian

%files -f Latvian.lang Latvian
%defattr(644,root,root,755)

%files -f Maltese.lang Maltese
%defattr(644,root,root,755)

%files -f Malay.lang Malay
%defattr(644,root,root,755)

##%files -f Mongolian.lang Mongolian
# %files -f Maori.lang Maori
#%%files -f Macedonian.lang Macedonian

%files -f Dutch.lang Dutch
%defattr(644,root,root,755)

%files -f Norwegian_Bokmaal.lang Norwegian_Bokmaal
%defattr(644,root,root,755)

%files -f Norwegian_Nynorsk.lang Norwegian_Nynorsk
%defattr(644,root,root,755)

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

%files -f Northern_Sami.lang Northern_Sami
%defattr(644,root,root,755)

#%%files -f Swati.lang Swati

%files -f Slovak.lang Slovak
%defattr(644,root,root,755)

%files -f Slovenian.lang Slovenian
%defattr(644,root,root,755)

%files -f Serbian.lang Serbian
%defattr(644,root,root,755)

%files -f Swedish.lang Swedish
%defattr(644,root,root,755)

%files -f Tamil.lang Tamil
%defattr(644,root,root,755)

%files -f Tajik.lang Tajik
%defattr(644,root,root,755)

%files -f Thai.lang Thai
%defattr(644,root,root,755)

%files -f Turkish.lang Turkish
%defattr(644,root,root,755)

##%files -f Ukrainian.lang Ukrainian
##%files -f Uzbek.lang Uzbek

%files -f Venda.lang Venda
%defattr(644,root,root,755)

#%%files -f Vietnamese.lang Vietnamese
# %files -f Walloon.lang Walloon

%files -f Xhosa.lang Xhosa
%defattr(644,root,root,755)

%files -f Simplified_Chinese.lang Simplified_Chinese
%defattr(644,root,root,755)

%files -f Chinese.lang Chinese
%defattr(644,root,root,755)

%files -f Zulu.lang Zulu
%defattr(644,root,root,755)
