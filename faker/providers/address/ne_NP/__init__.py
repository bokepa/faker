from .. import Provider as AddressProvider


class Provider(AddressProvider):
    building_number_formats = ('#', '##', '###')
    street_name_formats = ('{{last_name}} {{street_suffix}}',)
    street_address_formats = ('{{street_name}}',)
    city_formats = ('{{city}}',)
    # http://www.nepalpost.gov.np/index.php/postal-codes-of-nepal
    postcode_formats = ('#####',)

    address_formats = (
        "{{street_name}} {{building_prefix}} {{building_number}} \n{{city}}\n{{district}} {{postcode}}",
    )

    street_suffixes = (
        'मार्ग',
        'आश्रम',
        'बाटो',
        'पथ',
        'गल्ली',
        'गेट',
        'हाईट',
        'टार',
        'रोड',
        'कुना',
        'चौर',
        'निवास',
    )

    building_prefixes = ('वडा', 'घर')
    # https://en.wikipedia.org/wiki/List_of_sovereign_states
    countries = (
        'अंगोला',
        'अक्रोटिरी र धेकेलिया',
        'अजरबैजान',
        'अफगानिस्तान',
        'अमेरिकी सामोआ',
        'अरुबा',
        'अर्जेन्टिना',
        'अर्मेनिया',
        'अलडेर्नी',
        'अल्जेरिया',
        'अल्बानिया',
        'अस्ट्रिया',
        'अस्ट्रेलिया',
        'आइजल अफ म्यान',
        'आइभोरी कोस्ट',
        'आइसल्याण्ड',
        'आजाद कश्मीर',
        'आयरल्याण्ड',
        'इक्वेटोरियल गिनी',
        'इक्वेडर',
        'इजरायल',
        'इटाली',
        'इण्डोनेशिया',
        'इथियोपिया',
        'इराक',
        'इरान',
        'इस्टोनिया',
        'उज्बेकिस्तान',
        'उत्तर कोरिया',
        'उत्तरी मारिआना टापु',
        'उत्तरी साइप्रस',
        'उरुग्वे',
        'एङगुइला',
        'एण्डोरा',
        'एन्टिगुआ र बर्बुडा',
        'एरिट्रिया',
        'एल साल्भादोर',
        'एशमोर र कर्टियर टापु',
        'ओमान',
        'कजाख्स्तान',
        'कतार',
        'कम्बोडिया',
        'किरिबाटी',
        'किर्गिजस्तान',
        'कुक द्वीप',
        'कुराकाओ',
        'कुवैत',
        'केन्या',
        'केप भर्ड',
        'केम्यान टापु',
        'कोकोस टापु',
        'कोटे डी आइभोरी',
        'कोमोरोस',
        'कोरल सी टापु क्षेत्र',
        'कोलम्बिया',
        'कोसोभो',
        'कोस्टारिका',
        'क्यानडा',
        'क्यामेरून',
        'क्युबा',
        'क्रिसमस टापु',
        'क्रोएसिया',
        'क्लिप्परटन द्वीप',
        'क्वीन माउड ल्याण्ड',
        'गणतन्त्र कङ्गो',
        'गणतन्त्र कोरिया',
        'गणतन्त्र स्पर्स्का',
        'गाबोन',
        'गिनी',
        'गिब्राल्टार',
        'गिलगीत',
        'गुयना',
        'गुर्न्जी',
        'ग्रिनाडा',
        'ग्रीनल्याण्ड',
        'ग्रीस',
        'ग्वाटेमाला',
        'ग्वाम',
        'घाना',
        'चाड',
        'चिली',
        'चीन',
        'चेक गणतन्त्र',
        'जमैका',
        'जर्मनी',
        'जर्सी',
        'जापान',
        'जाम्बिया',
        'जिबुटी',
        'जोर्डन',
        'टर्की',
        'टिमोर',
        'टुभालु',
        'टुर्क्स तथा काइकोस टापु',
        'टोंगा',
        'टोकेलाउ',
        'टोगो',
        'ट्युनिसिया',
        'ट्रान्सनिसट्रिया',
        'ट्रिनिडाड र टोबागो',
        'डेनमार्क',
        'डोमिनिकन गणतन्त्र',
        'डोमिनिका',
        'तन्जानिया',
        'ताइवान',
        'ताजिकिस्तान',
        'तुर्कमेनिस्तान',
        'थाइल्याण्ड',
        'दक्षिण अफ्रिका',
        'दक्षिण ओसेटिया',
        'दक्षिण कोरिया',
        'दक्षिण जर्जिया तथा दक्षिण स्याण्डवीच टापु',
        'दक्षिणी सुडान',
        'नर्वे',
        'नर्वेको',
        'नाइजर',
        'नाइजेरिया',
        'नाउरु',
        'नागोर्नो',
        'नामिबिया',
        'निकाराग्वा',
        'नियु',
        'नेदरल्याण्ड',
        'नेपाल',
        'नोर्फोक टापु',
        'न्यु क्यालोडेनिया',
        'न्युजिल्यान्ड',
        'पपुवा न्युगिनी',
        'पलाउ',
        'पाकिस्तान',
        'पानामा',
        'पाराग्वे',
        'पिटकेर्न टापु',
        'पिटर द्वीप',
        'पूर्वी टिमोर',
        'पेरु',
        'पोर्चुगल',
        'पोल्याण्ड',
        'प्यालेस्टाइन',
        'प्युर्तो रिको',
        'प्रजातान्त्रिक गणतन्त्र कंगो',
        'प्रजातान्त्रिक गणतन्त्र कोरिया',
        'प्रिडेनेस्ट्रोभी',
        'फकल्याण्ड टापु',
        'फरोइ टापु',
        'फिजी',
        'फिनल्याण्ड',
        'फिलिपिन्स',
        'फ्रान्स',
        'फ्रेन्च दक्षिणी र अन्टार्कटिक द्वीप',
        'फ्रेन्च पोलिनेसिया',
        'बंगलादेश',
        'बर्मा',
        'बर्मुडा',
        'बहराइन',
        'बहामस',
        'बार्बाडोस',
        'बुरुन्डी',
        'बुर्किना फासो',
        'बुल्गेरिया',
        'बेनिन',
        'बेलारूस',
        'बेलिज',
        'बेल्जियम',
        'बोत्स्वाना',
        'बोलिभिया',
        'बोस्निया र हर्जगोभिना',
        'बोस्निया र हर्जगोभिना संघ',
        'बौभेट द्वीप',
        'ब्राजिल',
        'ब्रिटिस भर्जिन टापु',
        'ब्रुनेई',
        'भानुअटु',
        'भारत',
        'भियतनाम',
        'भुटान',
        'भेनेजुएला',
        'भ्याटिकन',
        'भ्याटिकन सिटी',
        'मकाउ',
        'मङ्गोलिया',
        'मध्य अफ्रिकी गणतन्त्र',
        'मलावी',
        'मलेशिया',
        'माइक्रोनेसियाको संघीय राज्य',
        'माडागास्कर',
        'मार्शल द्वीप',
        'माली',
        'माल्टा',
        'माल्दिभ्स',
        'मिश्र',
        'मेक्सिको',
        'मोजाम्बिक',
        'मोनाको',
        'मोन्टसेराट',
        'मोन्टेनेग्रो',
        'मोरक्को',
        'मोल्डोभा',
        'मौरिसनिया',
        'मौरिसस',
        'म्यानमार',
        'म्यासेडोनिया',
        'यमन',
        'युक्रेन',
        'युगान्डा',
        'रसिया',
        'रुवाण्डा',
        'रोमानिया',
        'रोस डिपेन्डेन्सी',
        'लक्जेम्बर्ग',
        'लाईबेरिया',
        'लाओस',
        'लात्भिया',
        'लिचटेन्स्टाइन',
        'लिथुआनिया',
        'लिबिया',
        'लेबनान',
        'लेसोथो',
        'वाल्लिस र फुटुना',
        'श्रीलंका',
        'संघीय राज्य माइक्रोनेसिया',
        'संयुक्त अधिराज्य',
        'संयुक्त अरब इमिरेट्स',
        'संयुक्त राज्य अमेरिका',
        'संयुक्त राज्य भर्जिन टापु',
        'सर्बिया',
        'साइप्रस',
        'साउदी अरब',
        'साओ टोमे र प्रिन्सिपे',
        'सान मारिनो',
        'साबा',
        'सामोआ',
        'साहरवी अरब लोकतान्त्रिक गणतन्त्र',
        'सिंगापुर',
        'सिन्ट मार्टिन',
        'सीरियन कुर्दिस्तान',
        'सीरिया',
        'सुडान',
        'सुरिनेम',
        'सेनेगल',
        'सेन्ट किट्स र नेभिस',
        'सेन्ट पियेर्रे र मिकुएलन',
        'सेन्ट बार्थेलेमी',
        'सेन्ट भिन्सेन्ट र ग्रेनाडाइन्स',
        'सेन्ट मार्टिन',
        'सेन्ट लुसिया',
        'सेन्ट हेलेना',
        'सेरा लियोन',
        'सेसेल्स',
        'सोमालिया',
        'सोमालील्याण्ड',
        'सोलोमन द्वीप',
        'स्पेन',
        'स्लोभाकिया',
        'स्लोभेनिया',
        'स्वाजिल्याण्ड',
        'स्विजरल्याण्ड',
        'स्वीडेन',
        'हंगेरी',
        'हङकङ',
        'हर्म',
        'हाइटी',
        'हेयर्ड द्वीप र म्याकडोनाल्ड टापु',
        'होन्डुरस',
        'अबखाजिया',
        'जर्जिया',
    )

    # cities are taken from
    # https://en.wikipedia.org/wiki/List_of_cities_in_Nepal
    cities = (
        'मिर्चैया',
        'प्युठान',
        'कञ्चनपुर',
        'लुम्बिनी सांस्कृतिक',
        'बागलुङ',
        'इलाम',
        'भक्तपुर',
        'भद्रपुर',
        'घोराही',
        'स्याङ्जा',
        'खैरहानी नगरपालिका',
        'म्याग्दी',
        'रंगेली',
        'काठमाडौं',
        'शनि-अर्जुन',
        'पर्वत',
        'सप्तरी',
        'पनौती',
        'जयपृथ्वी',
        'लहान',
        'वालिङ',
        'बर्दघाट',
        'डोटी',
        'धरान',
        'पथरी शनिश्चरे',
        'चन्दननाथ',
        'नवलपरासी',
        'किर्तिपुर',
        'दैलेख',
        'सुनसरी',
        'बेलौरी',
        'कुस्मा',
        'मकवानपुर',
        'कञ्चनरूप',
        'गुलरिया',
        'टीकापुर',
        'राजापुर',
        'फिदिम',
        'खोटाङ',
        'धनुषाधाम',
        'झापा',
        'पुनर्वास',
        'भक्तपुर',
        'बर्दिया',
        'बागलुङ',
        'दमक',
        'तेह्रथुम',
        'नारायण',
        'ताप्लेजुङ',
        'तानसेन',
        'पाँचखाल',
        'बनेपा',
        'म्याङ्लुङ',
        'ललितपुर',
        'दिपायल',
        'अपी',
        'दाङ',
        'सन्धिखर्क',
        'धनकुटा',
        'बिरेन्द्रनगर',
        'गौर',
        'मोरङ',
        'सङ्खुवासभा',
        'लम्की-चुहा',
        'बारा',
        'हरिवन नगरपालिका',
        'मलङ्वा',
        'सिराहा',
        'जनकपुर',
        'सल्यान',
        'सिन्धुपाल्चोक',
        'दुल्लु',
        'ओखलढुङ्गा',
        'पाल्पा',
        'इटहरी',
        'रेसुङगा',
        'कृष्णनगर',
        'शुक्लगण्डकी',
        'नुवाकोट',
        'साँफेबगर',
        'राजविराज',
        'नेपालगंज',
        'भिमेश्वर',
        'ताप्लेजुङ',
        'धुलिखेल',
        'व्यास',
        'भोजपुर',
        'धादिङ',
        'बेनी',
        'अर्घाखाँची',
        'भीमदत्त',
        'रौतहट',
        'जलेश्वर',
        'देवदह',
        'बेलवारी',
        'बुटवल',
        'सुर्खेत',
        'मङ्गलसेन',
        'कैलाली',
        'धनकुटा',
        'रुपन्देही',
        'सल्यान',
        'रामपुर',
        'बिराटनगर',
        'चौतारा',
        'देवचुली',
        'कपिलवस्तु',
        'सुनवल',
        'शिवराज',
        'चम्पापुर (चापागाउँ)',
        'भरतपुर',
        'गढिमाई',
        'उर्लावारी',
        'लेखनाथ',
        'सिद्धिचरण',
        'मेचीनगर',
        'चित्रवन',
        'कास्की',
        'गौशाला',
        'पुतलीबजार',
        'बिदुर',
        'शम्भुनाथ',
        'पर्सा',
        'प्युठान',
        'निजगढ',
        'डडेलधुरा',
        'कन्काई',
        'गैंडाकोट',
        'पाल्पा',
        'कार्यविनायक*',
        'तिलोत्तमा',
        'तुलसीपुर',
        'वीरगञ्ज',
        'शंखरपुर*',
        'अत्तरिया',
        'बझाङ',
        'मन्थली*',
        'कपिलवस्तु',
        'कटारी',
        'हेटौडा',
        'कलैया',
        'सुन्दर दुलारी',
        'सिन्धुली',
        'थाहा',
        'बाँके',
        'ललितपुर',
        'दार्चुला',
        'पोखरा',
        'बन्दीपुर',
        'सर्लाही',
        'कोहलपुर',
        'सैनामैना',
        'अमरागढी',
        'उदयपुर',
        'काठमाडौं',
        'सुर्योदय',
        'सिराहा',
        'महोत्तरी',
        'धनगढी',
        'शारदा',
        'काभ्रेपलाञ्चोक',
        'त्रियुगा',
        'रामेछाप',
        'पाँचथर',
        'इलाम',
        'भोजपुर',
        'मध्यपुर ठिमी',
        'दुहवी-भलुवा',
        'दशरथचन्द',
        'बैतडी',
        'कोशी हरैंचा',
        'चापाकोट',
        'दिक्तेल',
        'चन्द्रपुर',
        'लालबन्दी',
        'चितवन',
        'रत्ननगर',
        'पृथ्वीनारायण',
        'धनुषा',
        'गुल्मी',
        'बेंसीशहर',
        'लमजुङ',
        'अछाम',
        'तनहुँ',
        'खाँदबारी',
        'बिर्तामोड',
        'कमलामाई',
        'छिरेश्वरनाथ',
        'सिद्धार्थनगर',
        'निलकण्ठ',
        'गोर्खा',
        'दोलखा',
        'रामग्राम',
        'इनरूवा',
        'कावासोती',
        'बेल्टार बसाहा',
        'जुम्ला',
        'ईश्वरपुर',
    )

    # district taken from
    # https://www.election.gov.np/election/np/district-wise-constituency-map.html
    districts = (
        'अछाम',
        'अर्घाखाँची',
        'इलाम',
        'उदयपुर',
        'ओखलढुङ्गा',
        'कञ्चनपुर',
        'कपिलवस्तु',
        'काठमाडौं',
        'काभ्रेपलाञ्चोक',
        'कालीकोट',
        'कास्की',
        'कैलाली',
        'खोटाङ',
        'गुल्मी',
        'गोर्खा',
        'चितवन',
        'जाजरकोट',
        'जुम्ला',
        'झापा',
        'डडेल्धुरा',
        'डोटी',
        'डोल्पा',
        'तनहुँ',
        'ताप्लेजुङ',
        'तेह्रथुम',
        'दाङ',
        'दार्चुला',
        'दैलेख',
        'दोलखा',
        'धनकुटा',
        'धनुषा',
        'धादिङ',
        'नवलपरासी (बर्दघाट सुस्ता पूर्व)',
        'नवलपरासी (बर्दघाट सुस्ता पश्चिम)',
        'नुवाकोट',
        'पर्वत',
        'पर्सा',
        'पाँचथर',
        'पाल्पा',
        'प्युठान',
        'बझाङ',
        'बर्दिया',
        'बाँके',
        'बाग्लुङ',
        'बाजुरा',
        'बारा',
        'भक्तपुर',
        'भोजपुर',
        'मकवानपुर',
        'मनाङ',
        'महोत्तरी',
        'मुगु',
        'मुस्ताङ',
        'मोरङ',
        'म्याग्दी',
        'रसुवा',
        'रामेछाप',
        '‍रुकुम पूर्व',
        'रुकुम पश्चिम',
        'रूपन्देही',
        'रोल्पा',
        'रौतहट',
        'लमजुङ्',
        'ललितपुर',
        'वैतडी',
        'संखुवासभा',
        'सप्तरी',
        'सर्लाही',
        'सल्यान',
        'सिन्धुपलाञ्चोक',
        'सिन्धुली',
        'सिराहा',
        'सुनसरी',
        'सुर्खेत',
        'सोलुखुम्बु',
        'स्याङ्जा',
        'हुम्ला',
    )

    # province taken from
    # https://ne.wikipedia.org/wiki/%E0%A4%A8%E0%A5%87%E0%A4%AA%E0%A4%BE%E0%A4%B2%E0%A4%95%E0%A4%BE_%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%A6%E0%A5%87%E0%A4%B6%E0%A4%B9%E0%A4%B0%E0%A5%82  # noqa: E501
    provinces = (
        'प्रदेश नं १',
        'प्रदेश नं २',
        'बाग्मती प्रदेश',
        'गण्डकी प्रदेश',
        'प्रदेश नं ५',
        'कर्णाली प्रदेश',
        'सुदूरपश्चिम प्रदेश',
    )

    def province(self):
        """
        :example सुदूरपश्चिम प्रदेश
        """
        return self.random_element(self.provinces)

    def district(self):
        """
        :example अछाम
        """
        return self.random_element(self.districts)

    def city(self):
        """
        :example कावासोती
        """
        return self.random_element(self.cities)

    def building_prefix(self):
        """
        :example वडा
        """
        return self.random_element(self.building_prefixes)
