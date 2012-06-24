Summary:	KOffice suite - international support
Summary(pl):	KOffice - wsparcie dla wielu j�zyk�w
Name:		koffice-i18n
Version:	1.3.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/koffice-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	6455f496f6031e810398ad6b065eb929
# Source0-size:	27798685
BuildRequires:	gettext-devel
# It creates symlinks to some not-translated files.
BuildRequires:	kdelibs-devel >= 9:3.2
BuildRequires:	libxml2-progs >= 2.4.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KOffice suite - international support.

%description -l pl
KOffice - wsparcie dla wielu j�zyk�w.

%package base
Summary:	Empty metapackage to handle obsoletes
Summary(pl):	Pusty metapakiet z obsoletes
Group:		X11/Applications
Requires:	kde-i18n-base
Obsoletes:	koffice-common-i18n
Obsoletes:	koffice-karbon-i18n
Obsoletes:	koffice-kchart-i18n
Obsoletes:	koffice-kformula-i18n
Obsoletes:	koffice-kivio-i18n
Obsoletes:	koffice-kpresenter-i18n
Obsoletes:	koffice-kspread-i18n
Obsoletes:	koffice-kugar-i18n
Obsoletes:	koffice-kword-i18n

%description base
Empty metapackage to handle obsoletes for individual i18n subpackages.

%description base -l pl
Pusty metapakiet z Obsoletes dla oddzielnych podpakiet�w i18n.

%package Afrikaans
Summary:	KOffice suite - Afrikaans language support
Summary(pl):	KOffice - wsparcie dla j�zyka afrykanerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Afrikaans
KOffice suite - Afrikaans language support.

%description Afrikaans -l pl
KOffice - wsparcie dla j�zyka afrykanerskiego.

%package Arabic
Summary:	KOffice suite - Arabic language support
Summary(pl):	KOffice - wsparcie dla j�zyka arabskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Arabic
KOffice suite - Arabic language support.

%description Arabic -l pl
KOffice - wsparcie dla j�zyka arabskiego.

%package Azerbaijani
Summary:	KOffice suite - Azerbaijani language support
Summary(pl):	KOffice - wsparcie dla j�zyka azerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Azerbaijani
KOffice suite - Azerbaijani language support.

%description Azerbaijani -l pl
KOffice - wsparcie dla j�zyka azerskiego.

%package Bulgarian
Summary:	KOffice suite - Bulgarian language support
Summary(pl):	KOffice - wsparcie dla j�zyka bu�garskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Bulgarian
KOffice suite - Bulgarian language support.

%description Bulgarian -l pl
KOffice - wsparcie dla j�zyka bu�garskiego.

%package Breton
Summary:	KOffice suite - Breton language support
Summary(pl):	KOffice - wsparcie dla j�zyka breto�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Breton
KOffice suite - Breton language support.

%description Breton -l pl
KOffice - wsparcie dla j�zyka breto�skiego.

%package Bosnian
Summary:	KOffice suite - Bosnian language support
Summary(pl):	KOffice - wsparcie dla j�zyka bo�niackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Bosnian
KOffice suite - Bosnian language support.

%description Bosnian -l pl
KOffice - wsparcie dla j�zyka bo�niackiego.

%package Catalan
Summary:	KOffice suite - Catalan language support
Summary(pl):	KOffice - wsparcie dla j�zyka katalo�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Catalan
KOffice suite - Catalan language support.

%description Catalan -l pl
KOffice - wsparcie dla j�zyka katalo�skiego.

%package Czech
Summary:	KOffice suite - Czech language support
Summary(pl):	KOffice - wsparcie dla j�zyka czeskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Czech
KOffice suite - Czech language support.

%description Czech -l pl
KOffice - wsparcie dla j�zyka czeskiego.

%package Cymraeg
Summary:	KOffice suite - Cymraeg language support
Summary(pl):	KOffice - wsparcie dla j�zyka walijskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Cymraeg
KOffice suite - Cymraeg language support.

%description Cymraeg -l pl
KOffice - wsparcie dla j�zyka walijskiego.

%package Danish
Summary:	KOffice suite - Danish language support
Summary(pl):	KOffice - wsparcie dla j�zyka du�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Danish
KOffice suite - Danish language support.

%description Danish -l pl
KOffice - wsparcie dla j�zyka du�skiego.

%package German
Summary:	KOffice suite - German language support
Summary(pl):	KOffice - wsparcie dla j�zyka niemieckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description German
KOffice suite - German language support.

%description German -l pl
KOffice - wsparcie dla j�zyka niemieckiego.

%package Greek
Summary:	KOffice suite - Greek language support
Summary(pl):	KOffice - wsparcie dla j�zyka greckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Greek
KOffice suite - Greek language support.

%description Greek -l pl
KOffice - wsparcie dla j�zyka greckiego.

%package English
Summary:	KOffice suite - English language support
Summary(pl):	KOffice - wsparcie dla j�zyka angielskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description English
KOffice suite - English language support.

%description English -l pl
KOffice - wsparcie dla j�zyka angielskiego.

%package English_UK
Summary:	KOffice suite - KOffice suite - English (UK) language support
Summary(pl):	KOffice - wsparcie dla j�zyka angielskiego (odmiany brytyjskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description English_UK
KOffice suite - English (UK) language support.

%description English_UK -l pl
KOffice - wsparcie dla j�zyka angielskiego (odmiany brytyjskiej).

%package Esperanto
Summary:	KOffice suite - Esperanto language support
Summary(pl):	KOffice - wsparcie dla j�zyka esperanto
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Esperanto
KOffice suite - Esperanto language support.

%description Esperanto -l pl
KOffice - wsparcie dla j�zyka esperanto.

%package Spanish
Summary:	KOffice suite - Spanish language support
Summary(pl):	KOffice - wsparcie dla j�zyka hiszpa�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Spanish
KOffice suite - Spanish language support.

%description Spanish -l pl
KOffice - wsparcie dla j�zyka hiszpa�skiego.

%package Estonian
Summary:	KOffice suite - Estonian language support
Summary(pl):	KOffice - wsparcie dla j�zyka esto�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Estonian
KOffice suite - Estonian language support.

%description Estonian -l pl
KOffice - wsparcie dla j�zyka esto�skiego.

%package Basque
Summary:	KOffice suite - Basque language support
Summary(pl):	KOffice - wsparcie dla j�zyka baskijskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Basque
KOffice suite - Basque language support.

%description Basque -l pl
KOffice - wsparcie dla j�zyka baskijskiego.

%package Farsi
Summary:	KOffice suite - Farsi language support
Summary(pl):	KOffice - wsparcie dla j�zyka perskiego (farsi)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Farsi
KOffice suite - Farsi language support.

%description Farsi -l pl
KOffice - wsparcie dla j�zyka perskiego (farsi).


%package Finnish
Summary:	KOffice suite - Finnish language support
Summary(pl):	KOffice - wsparcie dla j�zyka fi�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Finnish
KOffice suite - Finnish language support.

%description Finnish -l pl
KOffice - wsparcie dla j�zyka fi�skiego.

%package French
Summary:	KOffice suite - French language support
Summary(pl):	KOffice - wsparcie dla j�zyka francuskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description French
KOffice suite - French language support.

%description French -l pl
KOffice - wsparcie dla j�zyka francuskiego.

%package Irish
Summary:	KOffice suite - Irish language support
Summary(pl):	KOffice - wsparcie dla j�zyka irlandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Irish
KOffice suite - Irish language support.

%description Irish -l pl
KOffice - wsparcie dla j�zyka irlandzkiego.

%package Galician
Summary:	KOffice suite - Galician language support
Summary(pl):	KOffice - wsparcie dla j�zyka galicyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Galician
KOffice suite - Galician language support.

%description Galician -l pl
KOffice - wsparcie dla j�zyka galicyjskiego.

%package Hindi
Summary:	KOffice suite - Hindi language support
Summary(pl):	KOffice - wsparcie dla j�zyka hindi
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hindi
KOffice suite - Hindi language support.

%description Hindi -l pl
KOffice - wsparcie dla j�zyka hindi.

%package Hebrew
Summary:	KOffice suite - Hebrew language support
Summary(pl):	KOffice - wsparcie dla j�zyka hebrajskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hebrew
KOffice suite - Hebrew language support.

%description Hebrew -l pl
KOffice - wsparcie dla j�zyka hebrajskiego.

%package Croatian
Summary:	KOffice suite - Croatian language support
Summary(pl):	KOffice - wsparcie dla j�zyka chorwackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Croatian
KOffice suite - Croatian language support.

%description Croatian -l pl
KOffice - wsparcie dla j�zyka chorwackiego.

%package Hungarian
Summary:	KOffice suite - Hungarian language support
Summary(pl):	KOffice - wsparcie dla j�zyka w�gierskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hungarian
KOffice suite - Hungarian language support.

%description Hungarian -l pl
KOffice - wsparcie dla j�zyka w�gierskiego.

%package Upper_Sorbian
Summary:	KOffice suite - Upper Sorbian language support
Summary(pl):	KOffice - wsparcie dla j�zyka g�rno�u�yckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Upper_Sorbian
KOffice suite - Upper Sorbian language support.

%description Upper_Sorbian  -l pl
KOffice - wsparcie dla j�zyka g�rno�u�yckiego.

%package Indonesian
Summary:	KOffice suite - Indonesian language support
Summary(pl):	KOffice - wsparcie dla j�zyka indonezyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Indonesian
KOffice suite - Indonesian language support.

%description Indonesian -l pl
KOffice - wsparcie dla j�zyka indonezyjskiego.

%package Icelandic
Summary:	KOffice suite - Icelandic language support
Summary(pl):	KOffice - wsparcie dla j�zyka islandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Icelandic
KOffice suite - Icelandic language support.

%description Icelandic -l pl
KOffice - wsparcie dla j�zyka islandzkiego.

%package Italian
Summary:	KOffice suite - Italian language support
Summary(pl):	KOffice - wsparcie dla j�zyka w�oskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Italian
KOffice suite - Italian language support.

%description Italian -l pl
KOffice - wsparcie dla j�zyka w�oskiego.

%package Japanese
Summary:	KOffice suite - Japanese language support
Summary(pl):	KOffice - wsparcie dla j�zyka japo�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Japanese
KOffice suite - Japanese language support.

%description Japanese -l pl
KOffice - wsparcie dla j�zyka japo�skiego.

%package Korean
Summary:	KOffice suite - Korean language support
Summary(pl):	KOffice - wsparcie dla j�zyka korea�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Korean
KOffice suite - Korean language support.

%description Korean -l pl
KOffice - wsparcie dla j�zyka korea�skiego.

%package Lithuanian
Summary:	KOffice suite - Lithuanian language support
Summary(pl):	KOffice - wsparcie dla j�zyka litewskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Lithuanian
KOffice suite - Lithuanian language support.

%description Lithuanian -l pl
KOffice - Wsparcie dla j�zyka litewskiego.

%package Lao
Summary:	KOffice suite - Lao language support
Summary(pl):	KOffice - wsparcie dla j�zyka laota�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Lao
KOffice suite - lao language support.

%description Lao -l pl
KOffice - wsparcie dla j�zyka laota�skiego.

%package Latvian
Summary:	KOffice suite - Latvian language support
Summary(pl):	KOffice - wsparcie dla j�zyka �otewskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Latvian
KOffice suite - Latvian language support.

%description Latvian -l pl
KOffice - wsparcie dla j�zyka �otewskiego.

%package Maori
Summary:	KOffice suite - Maori language support
Summary(pl):	KOffice - wsparcie dla j�zyka maoryjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Maori
KOffice suite - Maori language support.

%description Maori -l pl
KOffice - wsparcie dla j�zyka maoryjskiego.

%package Macedonian
Summary:	KOffice suite - Macedonian language support
Summary(pl):	KOffice - wsparcie dla j�zyka macedo�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Macedonian
KOffice suite - Macedonian language support.

%description Macedonian -l pl
KOffice - wsparcie dla j�zyka macedo�skiego.

%package Malay
Summary:	KOffice suite - Malay language support
Summary(pl):	KOffice - wsparcie dla j�zyka malajskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Malay
KOffice suite - Malay language support.

%description Malay -l pl
KOffice - wsparcie dla j�zyka malajskiego.

%package Maltese
Summary:	KOffice suite - Maltese language support
Summary(pl):	KOffice - wsparcie dla j�zyka malta�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Maltese
KOffice suite - Maltese language support.

%description Maltese -l pl
KOffice - wsparcie dla j�zyka malta�skiego.

%package Mongolian
Summary:	KOffice suite - Mongolian language support
Summary(pl):	KOffice - wsparcie dla j�zyka mongolskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Mongolian
KOffice suite - Mongolian language support.

%description Mongolian -l pl
KOffice - wsparcie dla j�zyka mongolskiego.

%package Dutch
Summary:	KOffice suite - Dutch language support
Summary(pl):	KOffice - wsparcie dla j�zyka holenderskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Dutch
KOffice suite - Dutch language support.

%description Dutch -l pl
KOffice - wsparcie dla j�zyka holenderskiego.

%package Norwegian_Bokmaal
Summary:	KOffice suite - Norwegian (Bokmaal) language support
Summary(pl):	KOffice - wsparcie dla j�zyka norweskiego (odmiany bokmaal)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Norwegian_Bokmaal
KOffice suite - Norwegian (Bokmaal) language support.

%description Norwegian_Bokmaal -l pl
KOffice - wsparcie dla j�zyka norweskiego (odmiany bokmaal).

%package Norwegian_Nynorsk
Summary:	KOffice suite - Norwegian (Nynorsk) language support
Summary(pl):	KOffice - wsparcie dla j�zyka norweskiego (odmiany nynorsk)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Norwegian_Nynorsk
KOffice suite - Norwegian (Nynorsk) language support.

%description Norwegian_Nynorsk -l pl
KOffice - wsparcie dla j�zyka norweskiego (odmiany nynorsk).

%package Northern_Sotho
Summary:	KOffice suite - Northern Sotho language support
Summary(pl):	KOffice - wsparcie dla p�nocnej odmiany j�zyka ludu Soto
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Northern_Sotho
KOffice suite - Northern Sotho language support.

%description Northern_Sotho -l pl
KOffice - wsparcie dla p�nocnej odmiany j�zyka ludu Soto.

%package Gascon_occitan
Summary:	KOffice suite - Occitan (Gascon) language support
Summary(pl):	KOffice - wsparcie dla j�zyka oksyta�skiego (dialektu gasko�skiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Gascon_occitan
KOffice suite - Occitan (Gascon) language support.

%description Gascon_occitan -l pl
KOffice - wsparcie dla j�zyka oksyta�skiego (dialektu gasko�skiego).

%package Polish
Summary:	KOffice suite - Polish language support
Summary(pl):	KOffice - wsparcie dla j�zyka polskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Polish
KOffice suite - Polish language support.

%description Polish -l pl
KOffice - wsparcie dla j�zyka polskiego.

%package Portuguese
Summary:	KOffice suite - Portuguese language support
Summary(pl):	KOffice - wsparcie dla j�zyka portugalskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Portuguese
KOffice suite - Portuguese language support.

%description Portuguese -l pl
KOffice - wsparcie dla j�zyka portugalskiego.

%package Brazil_Portuguese
Summary:	KOffice suite - Portuguese (Brazil) language support
Summary(pl):	KOffice - wsparcie dla j�zyka portugalskiego (odmiany brazylijskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Brazil_Portuguese
KOffice suite - Portuguese (Brazil) language support.

%description Brazil_Portuguese -l pl
KOffice - wsparcie dla j�zyka portugalskiego (odmiany brazylijskiej).

%package Romanian
Summary:	KOffice suite - Romanian language support
Summary(pl):	KOffice - wsparcie dla j�zyka rumu�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Romanian
KOffice suite - Romanian language support.

%description Romanian -l pl
KOffice - wsparcie dla j�zyka rumu�skiego.

%package Russian
Summary:	KOffice suite - Russian language support
Summary(pl):	KOffice - wsparcie dla j�zyka rosyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Russian
KOffice suite - Russian language support.

%description Russian -l pl
KOffice - wsparcie dla j�zyka rosyjskiego.

%package Swati
Summary:	KOffice suite - Swati language support
Summary(pl):	KOffice - wsparcie dla j�zyka swati
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Swati
KOffice suite - Swati language support.

%description Swati -l pl
KOffice - wsparcie dla j�zyka swati.

%package Northern_Sami
Summary:	KOffice suite - Northern Sami language support
Summary(pl):	KOffice - wsparcie dla p�nocnego j�zyka saami (lapo�skiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Northern_Sami
KOffice suite - Northern Sami language support.

%description Northern_Sami -l pl
KOffice - wsparcie dla p�nocnego j�zyka saami (lapo�skiego).

%package Slovak
Summary:	KOffice suite - Slovak language support
Summary(pl):	KOffice - wsparcie dla j�zyka s�owackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Slovak
KOffice suite - Slovak language support.

%description Slovak -l pl
KOffice - wsparcie dla j�zyka s�owackiego.

%package Slovenian
Summary:	KOffice suite - Slovenian language support
Summary(pl):	KOffice - wsparcie dla j�zyka s�owe�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Slovenian
KOffice suite - Slovenian language support.

%description Slovenian -l pl
KOffice - wsparcie dla j�zyka s�owe�skiego.

%package Serbian
Summary:	KOffice suite - Serbian language support
Summary(pl):	KOffice - wsparcie dla j�zyka serbskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Serbian
KOffice suite - Serbian language support.

%description Serbian -l pl
KOffice - wsparcie dla j�zyka serbskiego.

%package Swedish
Summary:	KOffice suite - Swedish language support
Summary(pl):	KOffice - wsparcie dla j�zyka szwedzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Swedish
KOffice suite - Swedish language support.

%description Swedish -l pl
KOffice - wsparcie dla j�zyka szwedzkiego.

%package Tamil
Summary:	KOffice suite - Tamil language support
Summary(pl):	KOffice - wsparcie dla j�zyka tamilskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Tamil
KOffice suite - Tamil language support.

%description Tamil -l pl
KOffice - wsparcie dla j�zyka tamilskiego.

%package Tajik
Summary:	KOffice - Tajik language support
Summary(pl):	KOffice - wsparcie dla j�zyka tad�yckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Tajik
KOffice - Tajik language support.

%description Tajik -l pl
KOffice - wsparcie dla j�zyka tad�yckiego.

%package Thai
Summary:	KOffice suite - Thai language support
Summary(pl):	KOffice - wsparcie dla j�zyka tajlandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Thai
KOffice suite - Thai language support.

%description Thai -l pl
KOffice - wsparcie dla j�zyka tajlandzkiego.

%package Turkish
Summary:	KOffice suite - Turkish language support
Summary(pl):	KOffice - wsparcie dla j�zyka tureckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Turkish
KOffice suite - Turkish language support.

%description Turkish -l pl
KOffice - wsparcie dla j�zyka tureckiego.

%package Ukrainian
Summary:	KOffice suite - Ukrainian language support
Summary(pl):	KOffice - wsparcie dla j�zyka ukrai�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Ukrainian
KOffice suite - Ukrainian language support.

%description Ukrainian -l pl
KOffice - wsparcie dla j�zyka ukrai�skiego.

%package Uzbek
Summary:	KOffice suite - Uzbek language support
Summary(pl):	KOffice - wsparcie dla j�zyka uzbeckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Uzbek
KOffice suite - Uzbek language support.

%description Uzbek -l pl
KOffice - wsparcie dla j�zyka uzbeckiego.

%package Venda
Summary:	KOffice suite - Venda language support
Summary(pl):	KOffice - wsparcie dla j�zyka venda
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Venda
KOffice suite - Venda language support.

%description Venda -l pl
KOffice - wsparcie dla j�zyka venda.

%package Vietnamese
Summary:	KOffice suite - Vietnamese language support
Summary(pl):	KOffice - wsparcie dla j�zyka wietnamskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Vietnamese
KOffice suite - Vietnamese language support.

%description Vietnamese -l pl
KOffice - wsparcie dla j�zyka wietnamskiego.

%package Walloon
Summary:	KOffice suite - Walloon language support
Summary(pl):	KOffice - wsparcie dla j�zyka walo�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Walloon
KOffice suite - Walloon language support.

%description Walloon -l pl
KOffice - wsparcie dla j�zyka walo�skiego.

%package Xhosa
Summary:	KOffice suite - Xhosa language support
Summary(pl):	KOffice - wsparcie dla j�zyka khosa
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Xhosa
KOffice suite - Xhosa language support.

%description Xhosa -l pl
KOffice - wsparcie dla j�zyka khosa.

%package Simplified_Chinese
Summary:	KOffice suite - simplified Chinese language support
Summary(pl):	KOffice - wsparcie dla uproszczonego j�zyka chi�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Simplified_Chinese
KOffice suite - simplified Chinese language support.

%description Simplified_Chinese -l pl
KOffice - wsparcie dla uproszczonego j�zyka chi�skiego.

%package Chinese
Summary:	KOffice suite - Chinese language support
Summary(pl):	KOffice - wsparcie dla j�zyka chi�skiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Chinese
KOffice suite - Chinese language support.

%description Chinese -l pl
KOffice - wsparcie dla j�zyka chi�skiego.

%package Zulu
Summary:	KOffice suite - Zulu language support
Summary(pl):	KOffice - wsparcie dla j�zyka zuluskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Zulu
KOffice suite - Zulu language support.

%description Zulu -l pl
KOffice - wsparcie dla j�zyka zuluskiego.

%prep
%setup -q

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
kde_libs_htmldir="%{_kdedocdir}"; export kde_libs_htmldir

LDFLAGS="%{rpmldflags}"
#export UNSERMAKE=%{_datadir}/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure
%{__make} \
	RPM_OPT_FLAGS="%{rpmcflags}" \
	kde_htmldir="%{_kdedocdir}" \
	kde_libs_htmldir="%{_kdedocdir}"

%install
rm -rf $RPM_BUILD_ROOT
rm -rf *.lang

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}" \
	kde_libs_htmldir="%{_kdedocdir}"

FindLang() {
#    $1 - short language name
#    $2 - long language name

    echo "%defattr(644,root,root,755)" > "$2.lang"

# share/doc/kde/HTML/(%%lang)
    if [ -d "$RPM_BUILD_ROOT%{_kdedocdir}/$1" ]; then
	echo "%lang($1) %{_kdedocdir}/$1" >> "$2.lang"
    fi

# share/locale/(%%lang)
    if [ -d "$RPM_BUILD_ROOT%{_datadir}/locale/$1" ]; then
#       echo "%lang($1) %{_datadir}/locale/$1/[cef]*" >> "$2.lang"
       echo "%lang($1) %{_datadir}/locale/$1/LC_MESSAGES/*.mo" >> "$2.lang"
    fi

# share/apps/koffice/autocorrect/*.xml
    if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/koffice/autocorrect/${1}.xml" ]; then
        echo "%lang($1) %{_datadir}/apps/koffice/autocorrect/${1}.xml" >> "$2.lang"
    fi
}

FindLang af Afrikaans
##FindLang ar Arabic
##FindLang az Azerbaijani
FindLang bg Bulgarian
FindLang br Breton
##FindLang bs Bosnian
FindLang ca Catalan
FindLang cs Czech
FindLang cy Cymraeg
FindLang da Danish
FindLang de German
FindLang el Greek
# FindLang en English
FindLang en_GB English_UK
FindLang eo Esperanto
FindLang es Spanish
FindLang et Estonian
##FindLang eu Basque
FindLang fa Farsi
FindLang fi Finnish
FindLang fr French
# FindLang ga Irish
##FindLang gl Galician
FindLang he Hebrew
FindLang hsb Upper_Sorbian
##FindLang hi Hindi
##FindLang hr Croatian
FindLang hu Hungarian
# FindLang id Indonesian
##FindLang is Icelandic
FindLang it Italian
FindLang ja Japanese
## FindLang ko Korean
##FindLang lt Lithuanian
FindLang lo Lao
## FindLang lv Latvian
# FindLang mi Maori
##FindLang mk Macedonian
##FindLang mn Mongolian
##FindLang ms Malay
FindLang mt Maltese
FindLang nb Norwegian_Bokmaal
FindLang nl Dutch
FindLang nn Norwegian_Nynorsk
#indLang nso Northern_Sotho
# FindLang oc Gascon_occitan
FindLang pl Polish
FindLang pt Portuguese
FindLang pt_BR Brazil_Portuguese
##FindLang ro Romanian
FindLang ru Russian
##FindLang ss Swati
FindLang se Northern_Sami
FindLang sk Slovak
FindLang sl Slovenian
FindLang sr Serbian
FindLang sv Swedish
##FindLang ta Tamil
FindLang tg Tajik
FindLang th Thai
FindLang tr Turkish
##FindLang uk Ukrainian
##FindLang uz Uzbek
FindLang ven Venda
##FindLang vi Vietnamese
# FindLang wa Walloon
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
##%files -f Basque.lang Basque
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
##%files -f Latvian.lang Latvian
%files -f Maltese.lang Maltese
%defattr(644,root,root,755)
##%files -f Malay.lang Malay
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
#%%{_datadir}/services/searchproviders/*.desktop
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
##%files -f Tamil.lang Tamil
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
