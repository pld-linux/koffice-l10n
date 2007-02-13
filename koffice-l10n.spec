# TODO
# - missing:
# - koffice-bg-1.6.0.tar.bz2
# - koffice-nn-1.6.0.tar.bz2
# - koffice-ta-1.6.0.tar.bz2
# - koffice-tg-1.6.0.tar.bz2
# - broken: es
%define	koffice_epoch	5
Summary:	KOffice suite - international support
Summary(pl.UTF-8):	KOffice - wsparcie dla wielu języków
Name:		koffice-l10n
Version:	1.6.1
Release:	1
License:	GPL
Group:		X11/Applications
#Source0:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-bg-%{version}.tar.bz2
##Source0-md5:	8daaeb614b3439490c2dd64a5ca6a90d
Source1:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-ca-%{version}.tar.bz2
# Source1-md5:	2af9ee48900b76f13c7b205f9f44e454
Source2:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-cs-%{version}.tar.bz2
# Source2-md5:	a90d191f1d84bd5c8090ca6e004253c4
Source3:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-cy-%{version}.tar.bz2
# Source3-md5:	4f5d6aef468aeb4b80c6b079e1399110
Source4:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-da-%{version}.tar.bz2
# Source4-md5:	34ac13ce5bf8452f5f8b44686d03781a
Source5:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-de-%{version}.tar.bz2
# Source5-md5:	9ec1030ec8f55b4689a4664a3032050d
Source6:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-el-%{version}.tar.bz2
# Source6-md5:	c2028907c0675534694b5bad4c85ac0f
Source7:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-en_GB-%{version}.tar.bz2
# Source7-md5:	0c8edcc2fb6570ff7629e610580cac2f
Source8:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-es-%{version}.tar.bz2
# Source8-md5:	e3095320b087fdbaf9dea4ca7384c4e7
Source9:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-et-%{version}.tar.bz2
# Source9-md5:	d7e32d741c284880ff01530d956cd524
Source28:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-eu-%{version}.tar.bz2
# Source28-md5:	33bb005893d82eeebbc1dc62495e018a
Source10:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-fi-%{version}.tar.bz2
# Source10-md5:	dc0b99fe0b1c2f0bdc5823804cf5f7f7
Source11:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-fr-%{version}.tar.bz2
# Source11-md5:	74a658f3f323f016b202cc4e2063da19
Source12:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-hu-%{version}.tar.bz2
# Source12-md5:	406eef87386bea965c9d0ec224b0a6aa
Source13:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-it-%{version}.tar.bz2
# Source13-md5:	5fc389a6885af2acce7e5b9b48a9ce12
Source29:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-ja-%{version}.tar.bz2
# Source29-md5:	39ba5b3618221ee6fa896aa16aa9f6a9
Source30:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-lv-%{version}.tar.bz2
# Source30-md5:	512650fbc0638ac0f0bae2864f295cca
Source31:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-ms-%{version}.tar.bz2
# Source31-md5:	ff1d6abe79bf4b4239ebaccc2509c35e
Source14:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-nb-%{version}.tar.bz2
# Source14-md5:	65d3a4d15e8911faf43d1aa9c6f7b6a7
Source15:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-nl-%{version}.tar.bz2
# Source15-md5:	006bc0ff8b292fc8836c989d244a45bc
#Source16:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-nn-%{version}.tar.bz2
##Source16-md5:	12a451ca1384c776045a86aa3f0fecb5
Source17:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-pl-%{version}.tar.bz2
# Source17-md5:	ca6e0bd7de872e51f342cd153598981b
Source18:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-pt-%{version}.tar.bz2
# Source18-md5:	c4e59783b4b93a50c7e5e9b53c864caa
Source19:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-pt_BR-%{version}.tar.bz2
# Source19-md5:	71efdf80a256b20baece5e58f2d4527a
Source20:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-ru-%{version}.tar.bz2
# Source20-md5:	d72bb7ce7fe685c4c92940dca4cf4bf8
Source32:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-sk-%{version}.tar.bz2
# Source32-md5:	63b2d698040b2f5ece72e7ca67407669
Source21:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-sl-%{version}.tar.bz2
# Source21-md5:	0c40d723b64bf15fbb8c78ebce17dcb3
Source22:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-sr-%{version}.tar.bz2
# Source22-md5:	ff1137b214460cfc6c647643da08e098
Source23:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-sr@Latn-%{version}.tar.bz2
# Source23-md5:	ed4eab803a7c0443ff3c4839e32757d1
Source24:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-sv-%{version}.tar.bz2
# Source24-md5:	fd5ebf8d8480797f84121f9efcb00823
#Source25:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-ta-%{version}.tar.bz2
##Source25-md5:	536e66f3b85923771f2af964b51a465e
#Source26:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-tg-%{version}.tar.bz2
##Source26-md5:	a38ec98b0f6437ddb93196f369a09485
Source33:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-tr-%{version}.tar.bz2
# Source33-md5:	909ed845836e7219a4cf6710ee128846
Source27:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-zh_CN-%{version}.tar.bz2
# Source27-md5:	055cf1eed59bc1e491063d4ffa883d9b
Source34:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/koffice-l10n/%{name}-zh_TW-%{version}.tar.bz2
# Source34-md5:	230b02b893873f1fd55f002509549793
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
Obsoletes:	koffice-l10n-Afrikaans
Obsoletes:	koffice-l10n-Breton
Obsoletes:	koffice-l10n-Bulgarian
Obsoletes:	koffice-l10n-Esperanto
Obsoletes:	koffice-l10n-Farsi
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

%description base
Empty metapackage to handle obsoletes for individual i18n subpackages.

%description base -l pl.UTF-8
Pusty metapakiet z Obsoletes dla oddzielnych podpakietów i18n.

%package Afrikaans
Summary:	KOffice suite - Afrikaans language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka afrykanerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Afrikaans

%description Afrikaans
KOffice suite - Afrikaans language support.

%description Afrikaans -l pl.UTF-8
KOffice - wsparcie dla języka afrykanerskiego.

%package Arabic
Summary:	KOffice suite - Arabic language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka arabskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Arabic

%description Arabic
KOffice suite - Arabic language support.

%description Arabic -l pl.UTF-8
KOffice - wsparcie dla języka arabskiego.

%package Azerbaijani
Summary:	KOffice suite - Azerbaijani language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka azerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Azerbaijani

%description Azerbaijani
KOffice suite - Azerbaijani language support.

%description Azerbaijani -l pl.UTF-8
KOffice - wsparcie dla języka azerskiego.

%package Bulgarian
Summary:	KOffice suite - Bulgarian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka bułgarskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Bulgarian

%description Bulgarian
KOffice suite - Bulgarian language support.

%description Bulgarian -l pl.UTF-8
KOffice - wsparcie dla języka bułgarskiego.

%package Breton
Summary:	KOffice suite - Breton language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka bretońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Breton

%description Breton
KOffice suite - Breton language support.

%description Breton -l pl.UTF-8
KOffice - wsparcie dla języka bretońskiego.

%package Bosnian
Summary:	KOffice suite - Bosnian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka bośniackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Bosnian

%description Bosnian
KOffice suite - Bosnian language support.

%description Bosnian -l pl.UTF-8
KOffice - wsparcie dla języka bośniackiego.

%package Catalan
Summary:	KOffice suite - Catalan language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka katalońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Catalan

%description Catalan
KOffice suite - Catalan language support.

%description Catalan -l pl.UTF-8
KOffice - wsparcie dla języka katalońskiego.

%package Czech
Summary:	KOffice suite - Czech language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka czeskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Czech

%description Czech
KOffice suite - Czech language support.

%description Czech -l pl.UTF-8
KOffice - wsparcie dla języka czeskiego.

%package Cymraeg
Summary:	KOffice suite - Cymraeg language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka walijskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Cymraeg

%description Cymraeg
KOffice suite - Cymraeg language support.

%description Cymraeg -l pl.UTF-8
KOffice - wsparcie dla języka walijskiego.

%package Danish
Summary:	KOffice suite - Danish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka duńskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Danish

%description Danish
KOffice suite - Danish language support.

%description Danish -l pl.UTF-8
KOffice - wsparcie dla języka duńskiego.

%package German
Summary:	KOffice suite - German language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka niemieckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-German

%description German
KOffice suite - German language support.

%description German -l pl.UTF-8
KOffice - wsparcie dla języka niemieckiego.

%package Greek
Summary:	KOffice suite - Greek language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka greckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Greek

%description Greek
KOffice suite - Greek language support.

%description Greek -l pl.UTF-8
KOffice - wsparcie dla języka greckiego.

%package English
Summary:	KOffice suite - English language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka angielskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-English

%description English
KOffice suite - English language support.

%description English -l pl.UTF-8
KOffice - wsparcie dla języka angielskiego.

%package English_UK
Summary:	KOffice suite - KOffice suite - English (UK) language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka angielskiego (odmiany brytyjskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-English_UK

%description English_UK
KOffice suite - English (UK) language support.

%description English_UK -l pl.UTF-8
KOffice - wsparcie dla języka angielskiego (odmiany brytyjskiej).

%package Esperanto
Summary:	KOffice suite - Esperanto language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka esperanto
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Esperanto

%description Esperanto
KOffice suite - Esperanto language support.

%description Esperanto -l pl.UTF-8
KOffice - wsparcie dla języka esperanto.

%package Spanish
Summary:	KOffice suite - Spanish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka hiszpańskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Spanish

%description Spanish
KOffice suite - Spanish language support.

%description Spanish -l pl.UTF-8
KOffice - wsparcie dla języka hiszpańskiego.

%package Estonian
Summary:	KOffice suite - Estonian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka estońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Estonian

%description Estonian
KOffice suite - Estonian language support.

%description Estonian -l pl.UTF-8
KOffice - wsparcie dla języka estońskiego.

%package Basque
Summary:	KOffice suite - Basque language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka baskijskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Basque

%description Basque
KOffice suite - Basque language support.

%description Basque -l pl.UTF-8
KOffice - wsparcie dla języka baskijskiego.

%package Farsi
Summary:	KOffice suite - Farsi language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka perskiego (farsi)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Farsi

%description Farsi
KOffice suite - Farsi language support.

%description Farsi -l pl.UTF-8
KOffice - wsparcie dla języka perskiego (farsi).

%package Finnish
Summary:	KOffice suite - Finnish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka fińskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Finnish

%description Finnish
KOffice suite - Finnish language support.

%description Finnish -l pl.UTF-8
KOffice - wsparcie dla języka fińskiego.

%package French
Summary:	KOffice suite - French language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka francuskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-French

%description French
KOffice suite - French language support.

%description French -l pl.UTF-8
KOffice - wsparcie dla języka francuskiego.

%package Irish
Summary:	KOffice suite - Irish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka irlandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Irish

%description Irish
KOffice suite - Irish language support.

%description Irish -l pl.UTF-8
KOffice - wsparcie dla języka irlandzkiego.

%package Galician
Summary:	KOffice suite - Galician language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka galicyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Galician

%description Galician
KOffice suite - Galician language support.

%description Galician -l pl.UTF-8
KOffice - wsparcie dla języka galicyjskiego.

%package Hindi
Summary:	KOffice suite - Hindi language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka hindi
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Hindi

%description Hindi
KOffice suite - Hindi language support.

%description Hindi -l pl.UTF-8
KOffice - wsparcie dla języka hindi.

%package Hebrew
Summary:	KOffice suite - Hebrew language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka hebrajskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Hebrew

%description Hebrew
KOffice suite - Hebrew language support.

%description Hebrew -l pl.UTF-8
KOffice - wsparcie dla języka hebrajskiego.

%package Croatian
Summary:	KOffice suite - Croatian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka chorwackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Croatian

%description Croatian
KOffice suite - Croatian language support.

%description Croatian -l pl.UTF-8
KOffice - wsparcie dla języka chorwackiego.

%package Hungarian
Summary:	KOffice suite - Hungarian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka węgierskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Hungarian

%description Hungarian
KOffice suite - Hungarian language support.

%description Hungarian -l pl.UTF-8
KOffice - wsparcie dla języka węgierskiego.

%package Upper_Sorbian
Summary:	KOffice suite - Upper Sorbian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka górnołużyckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Upper_Sorbian

%description Upper_Sorbian
KOffice suite - Upper Sorbian language support.

%description Upper_Sorbian  -l pl.UTF-8
KOffice - wsparcie dla języka górnołużyckiego.

%package Indonesian
Summary:	KOffice suite - Indonesian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka indonezyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Indonesian

%description Indonesian
KOffice suite - Indonesian language support.

%description Indonesian -l pl.UTF-8
KOffice - wsparcie dla języka indonezyjskiego.

%package Icelandic
Summary:	KOffice suite - Icelandic language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka islandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Icelandic

%description Icelandic
KOffice suite - Icelandic language support.

%description Icelandic -l pl.UTF-8
KOffice - wsparcie dla języka islandzkiego.

%package Italian
Summary:	KOffice suite - Italian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka włoskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Italian

%description Italian
KOffice suite - Italian language support.

%description Italian -l pl.UTF-8
KOffice - wsparcie dla języka włoskiego.

%package Japanese
Summary:	KOffice suite - Japanese language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka japońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Japanese

%description Japanese
KOffice suite - Japanese language support.

%description Japanese -l pl.UTF-8
KOffice - wsparcie dla języka japońskiego.

%package Korean
Summary:	KOffice suite - Korean language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka koreańskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Korean

%description Korean
KOffice suite - Korean language support.

%description Korean -l pl.UTF-8
KOffice - wsparcie dla języka koreańskiego.

%package Lithuanian
Summary:	KOffice suite - Lithuanian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka litewskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Lithuanian

%description Lithuanian
KOffice suite - Lithuanian language support.

%description Lithuanian -l pl.UTF-8
KOffice - Wsparcie dla języka litewskiego.

%package Lao
Summary:	KOffice suite - Lao language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka laotańskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Lao

%description Lao
KOffice suite - lao language support.

%description Lao -l pl.UTF-8
KOffice - wsparcie dla języka laotańskiego.

%package Latvian
Summary:	KOffice suite - Latvian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka łotewskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Latvian

%description Latvian
KOffice suite - Latvian language support.

%description Latvian -l pl.UTF-8
KOffice - wsparcie dla języka łotewskiego.

%package Maori
Summary:	KOffice suite - Maori language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka maoryjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Maori

%description Maori
KOffice suite - Maori language support.

%description Maori -l pl.UTF-8
KOffice - wsparcie dla języka maoryjskiego.

%package Macedonian
Summary:	KOffice suite - Macedonian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka macedońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Macedonian

%description Macedonian
KOffice suite - Macedonian language support.

%description Macedonian -l pl.UTF-8
KOffice - wsparcie dla języka macedońskiego.

%package Malay
Summary:	KOffice suite - Malay language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka malajskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Malay

%description Malay
KOffice suite - Malay language support.

%description Malay -l pl.UTF-8
KOffice - wsparcie dla języka malajskiego.

%package Maltese
Summary:	KOffice suite - Maltese language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka maltańskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Maltese

%description Maltese
KOffice suite - Maltese language support.

%description Maltese -l pl.UTF-8
KOffice - wsparcie dla języka maltańskiego.

%package Mongolian
Summary:	KOffice suite - Mongolian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka mongolskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Mongolian

%description Mongolian
KOffice suite - Mongolian language support.

%description Mongolian -l pl.UTF-8
KOffice - wsparcie dla języka mongolskiego.

%package Dutch
Summary:	KOffice suite - Dutch language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka holenderskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Dutch

%description Dutch
KOffice suite - Dutch language support.

%description Dutch -l pl.UTF-8
KOffice - wsparcie dla języka holenderskiego.

%package Norwegian_Bokmaal
Summary:	KOffice suite - Norwegian (Bokmaal) language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka norweskiego (odmiany bokmaal)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Norwegian_Bokmaal

%description Norwegian_Bokmaal
KOffice suite - Norwegian (Bokmaal) language support.

%description Norwegian_Bokmaal -l pl.UTF-8
KOffice - wsparcie dla języka norweskiego (odmiany bokmaal).

%package Norwegian_Nynorsk
Summary:	KOffice suite - Norwegian (Nynorsk) language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka norweskiego (odmiany nynorsk)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Norwegian_Nynorsk

%description Norwegian_Nynorsk
KOffice suite - Norwegian (Nynorsk) language support.

%description Norwegian_Nynorsk -l pl.UTF-8
KOffice - wsparcie dla języka norweskiego (odmiany nynorsk).

%package Northern_Sotho
Summary:	KOffice suite - Northern Sotho language support
Summary(pl.UTF-8):	KOffice - wsparcie dla północnej odmiany języka ludu Soto
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Northern_Sotho

%description Northern_Sotho
KOffice suite - Northern Sotho language support.

%description Northern_Sotho -l pl.UTF-8
KOffice - wsparcie dla północnej odmiany języka ludu Soto.

%package Gascon_occitan
Summary:	KOffice suite - Occitan (Gascon) language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka oksytańskiego (dialektu gaskońskiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Gascon_occitan

%description Gascon_occitan
KOffice suite - Occitan (Gascon) language support.

%description Gascon_occitan -l pl.UTF-8
KOffice - wsparcie dla języka oksytańskiego (dialektu gaskońskiego).

%package Polish
Summary:	KOffice suite - Polish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka polskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Polish

%description Polish
KOffice suite - Polish language support.

%description Polish -l pl.UTF-8
KOffice - wsparcie dla języka polskiego.

%package Portuguese
Summary:	KOffice suite - Portuguese language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka portugalskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Portuguese

%description Portuguese
KOffice suite - Portuguese language support.

%description Portuguese -l pl.UTF-8
KOffice - wsparcie dla języka portugalskiego.

%package Brazil_Portuguese
Summary:	KOffice suite - Portuguese (Brazil) language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka portugalskiego (odmiany brazylijskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Brazil_Portuguese

%description Brazil_Portuguese
KOffice suite - Portuguese (Brazil) language support.

%description Brazil_Portuguese -l pl.UTF-8
KOffice - wsparcie dla języka portugalskiego (odmiany brazylijskiej).

%package Romanian
Summary:	KOffice suite - Romanian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka rumuńskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Romanian

%description Romanian
KOffice suite - Romanian language support.

%description Romanian -l pl.UTF-8
KOffice - wsparcie dla języka rumuńskiego.

%package Russian
Summary:	KOffice suite - Russian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka rosyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Russian

%description Russian
KOffice suite - Russian language support.

%description Russian -l pl.UTF-8
KOffice - wsparcie dla języka rosyjskiego.

%package Swati
Summary:	KOffice suite - Swati language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka swati
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Swati

%description Swati
KOffice suite - Swati language support.

%description Swati -l pl.UTF-8
KOffice - wsparcie dla języka swati.

%package Northern_Sami
Summary:	KOffice suite - Northern Sami language support
Summary(pl.UTF-8):	KOffice - wsparcie dla północnego języka saami (lapońskiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Northern_Sami

%description Northern_Sami
KOffice suite - Northern Sami language support.

%description Northern_Sami -l pl.UTF-8
KOffice - wsparcie dla północnego języka saami (lapońskiego).

%package Slovak
Summary:	KOffice suite - Slovak language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka słowackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Slovak

%description Slovak
KOffice suite - Slovak language support.

%description Slovak -l pl.UTF-8
KOffice - wsparcie dla języka słowackiego.

%package Slovenian
Summary:	KOffice suite - Slovenian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka słoweńskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Slovenian

%description Slovenian
KOffice suite - Slovenian language support.

%description Slovenian -l pl.UTF-8
KOffice - wsparcie dla języka słoweńskiego.

%package Serbian
Summary:	KOffice suite - Serbian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka serbskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Serbian

%description Serbian
KOffice suite - Serbian language support.

%description Serbian -l pl.UTF-8
KOffice - wsparcie dla języka serbskiego.

%package Swedish
Summary:	KOffice suite - Swedish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka szwedzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Swedish

%description Swedish
KOffice suite - Swedish language support.

%description Swedish -l pl.UTF-8
KOffice - wsparcie dla języka szwedzkiego.

%package Tamil
Summary:	KOffice suite - Tamil language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka tamilskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Tamil

%description Tamil
KOffice suite - Tamil language support.

%description Tamil -l pl.UTF-8
KOffice - wsparcie dla języka tamilskiego.

%package Tajik
Summary:	KOffice - Tajik language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka tadżyckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Tajik

%description Tajik
KOffice - Tajik language support.

%description Tajik -l pl.UTF-8
KOffice - wsparcie dla języka tadżyckiego.

%package Thai
Summary:	KOffice suite - Thai language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka tajlandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Thai

%description Thai
KOffice suite - Thai language support.

%description Thai -l pl.UTF-8
KOffice - wsparcie dla języka tajlandzkiego.

%package Turkish
Summary:	KOffice suite - Turkish language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka tureckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Turkish

%description Turkish
KOffice suite - Turkish language support.

%description Turkish -l pl.UTF-8
KOffice - wsparcie dla języka tureckiego.

%package Ukrainian
Summary:	KOffice suite - Ukrainian language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka ukraińskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Ukrainian

%description Ukrainian
KOffice suite - Ukrainian language support.

%description Ukrainian -l pl.UTF-8
KOffice - wsparcie dla języka ukraińskiego.

%package Uzbek
Summary:	KOffice suite - Uzbek language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka uzbeckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Uzbek

%description Uzbek
KOffice suite - Uzbek language support.

%description Uzbek -l pl.UTF-8
KOffice - wsparcie dla języka uzbeckiego.

%package Venda
Summary:	KOffice suite - Venda language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka venda
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Venda

%description Venda
KOffice suite - Venda language support.

%description Venda -l pl.UTF-8
KOffice - wsparcie dla języka venda.

%package Vietnamese
Summary:	KOffice suite - Vietnamese language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka wietnamskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Vietnamese

%description Vietnamese
KOffice suite - Vietnamese language support.

%description Vietnamese -l pl.UTF-8
KOffice - wsparcie dla języka wietnamskiego.

%package Walloon
Summary:	KOffice suite - Walloon language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka walońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Walloon

%description Walloon
KOffice suite - Walloon language support.

%description Walloon -l pl.UTF-8
KOffice - wsparcie dla języka walońskiego.

%package Xhosa
Summary:	KOffice suite - Xhosa language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka khosa
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Xhosa

%description Xhosa
KOffice suite - Xhosa language support.

%description Xhosa -l pl.UTF-8
KOffice - wsparcie dla języka khosa.

%package Simplified_Chinese
Summary:	KOffice suite - simplified Chinese language support
Summary(pl.UTF-8):	KOffice - wsparcie dla uproszczonego języka chińskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Simplified_Chinese

%description Simplified_Chinese
KOffice suite - simplified Chinese language support.

%description Simplified_Chinese -l pl.UTF-8
KOffice - wsparcie dla uproszczonego języka chińskiego.

%package Chinese
Summary:	KOffice suite - Chinese language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka chińskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Chinese

%description Chinese
KOffice suite - Chinese language support.

%description Chinese -l pl.UTF-8
KOffice - wsparcie dla języka chińskiego.

%package Zulu
Summary:	KOffice suite - Zulu language support
Summary(pl.UTF-8):	KOffice - wsparcie dla języka zuluskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	koffice-i18n-Zulu

%description Zulu
KOffice suite - Zulu language support.

%description Zulu -l pl.UTF-8
KOffice - wsparcie dla języka zuluskiego.

%prep
%setup -q -c -T %(seq -f '-a %g' 0 34 | egrep -v '^-a (0|16|25|26)$' | xargs)

# broken
rm -rf koffice-l10n-es-*

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
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/koffice/autocorrect/$lang.xml" ]; then
		echo "%lang($lang) %{_datadir}/apps/koffice/autocorrect/$lang.xml" >> "$language.lang"
	fi

	if [ ! -s $language.lang ]; then
		echo >&2 "Missing launguage: $language ($lang)"
		exit 1
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
	rm -rf $(find $RPM_BUILD_ROOT -name "$i*.mo")
	rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/$i
done

#FindLang af Afrikaans
#FindLang ar Arabic
#FindLang az Azerbaijani
#FindLang bg Bulgarian
#FindLang br Breton
#FindLang bs Bosnian
FindLang ca Catalan
FindLang cs Czech
FindLang cy Cymraeg
FindLang da Danish
FindLang de German
FindLang el Greek
#FindLang en English
FindLang en_GB English_UK
#FindLang eo Esperanto
#FindLang es Spanish
FindLang et Estonian
FindLang eu Basque
#FindLang fa Farsi
FindLang fi Finnish
FindLang fr French
#FindLang ga Irish
#FindLang gl Galician
#FindLang he Hebrew
#FindLang hsb Upper_Sorbian
#FindLang hi Hindi
#FindLang hr Croatian
FindLang hu Hungarian
#FindLang id Indonesian
#FindLang is Icelandic
FindLang it Italian
FindLang ja Japanese
#FindLang ko Korean
#FindLang lt Lithuanian
#FindLang lo Lao
FindLang lv Latvian
#FindLang mi Maori
#FindLang mk Macedonian
#FindLang mn Mongolian
FindLang ms Malay
#FindLang mt Maltese
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
#FindLang se Northern_Sami
FindLang sk Slovak
FindLang sl Slovenian
FindLang sr Serbian
FindLang sr@Latn Serbian_Latin
cat Serbian_Latin.lang >> Serbian.lang
rm -f Serbian_Latin.lang
FindLang sv Swedish
#FindLang ta Tamil
#FindLang tg Tajik
#FindLang th Thai
FindLang tr Turkish
#FindLang uk Ukrainian
#FindLang uz Uzbek
#FindLang ve Venda
#FindLang vi Vietnamese
#FindLang wa Walloon
#FindLang xh Xhosa
FindLang zh_CN Simplified_Chinese
FindLang zh_TW Chinese
#FindLang zu Zulu

# we ignore dialects (currently sr@Latn is the only case)
dirs=$(ls -1d %{name}-*-%{version} | %{__sed} '/@/d' | wc -l)
langs=$(echo *.lang | wc -w)
if [ $dirs != $langs ]; then
	echo >&2 "Not all languages processed! Dirs: $dirs, Langs: $langs"
	exit 1
fi

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

rm -rf $RPM_BUILD_ROOT

%files base
%defattr(644,root,root,755)

#%files -f Afrikaans.lang Afrikaans
#%defattr(644,root,root,755)

#%%files -f Arabic.lang Arabic
##%files -f Azerbaijani.lang Azerbaijani

#%files -f Bulgarian.lang Bulgarian
#%defattr(644,root,root,755)

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

#%files -f Spanish.lang Spanish
#%defattr(644,root,root,755)

%files -f Estonian.lang Estonian
%defattr(644,root,root,755)

%files -f Basque.lang Basque
%defattr(644,root,root,755)

#%files -f Farsi.lang Farsi
#%defattr(644,root,root,755)

%files -f Finnish.lang Finnish
%defattr(644,root,root,755)

%files -f French.lang French
%defattr(644,root,root,755)

# %files -f Irish.lang Irish
##%files -f Galician.lang Galician
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

##%files -f Ukrainian.lang Ukrainian
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
