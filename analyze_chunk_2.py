import json

# Load chunk 2
with open('split_hadiths/combined_batch_1_chunk_2.json', 'r', encoding='utf-8') as f:
    chunk_data = json.load(f)

analyzed_hadiths = []

# ============= HADITH 1 (ID 6397) =============
hadith_1 = {
    "hadith_id": 6397,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1426",
    "english_translation": "Narrated by Yahya ibn Abi Kathir: I entered upon Abu Salamah ibn Abd al-Rahman while he was ill. He said: 'If you can die (now), then die. By Allah, a time will surely come upon people when death will be more beloved to one of them than red gold.'",
    "chains": [
        {
            "type": "maqta'",
            "narrators": [
                {
                    "name": "Unknown Collector",
                    "full_name": "Unknown Collector/Compiler",
                    "grade": "Majhul",
                    "generation": "Unknown",
                    "transmissionTerm": "",
                    "reliabilityIssues": ["complete_disconnection"],
                    "narrator_id": None,
                    "alternative_names": "",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "",
                    "nisba_ar": "",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Majhul",
                    "tabaqat": "Unknown",
                    "location": "",
                    "transmissionTermMeaning": ""
                },
                {
                    "name": "Yahya ibn Abi Kathir",
                    "full_name": "Yahya ibn Abi Kathir al-Yami",
                    "grade": "Thiqah",
                    "generation": "Second-Third Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["indirect_transmission"],
                    "narrator_id": None,
                    "alternative_names": "Yahya ibn Abi Kathir",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "al-Yami",
                    "nisba_ar": "اليمي",
                    "death_year": "129",
                    "birth_year": "50",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "Second-Third Generation",
                    "location": "Yaman",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Abu Salamah",
                    "full_name": "Abd al-Rahman ibn Abi Salamah ibn Abd al-Rahman ibn Awf",
                    "grade": "Thiqah",
                    "generation": "Second Generation",
                    "transmissionTerm": "قَالَ",
                    "reliabilityIssues": [],
                    "narrator_id": None,
                    "alternative_names": "Abu Salamah",
                    "original_id": None,
                    "kunya": "Abu Salamah",
                    "nisba": "",
                    "nisba_ar": "",
                    "death_year": "94",
                    "birth_year": "34",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "Second Generation",
                    "location": "Madinah",
                    "transmissionTermMeaning": "He said"
                }
            ],
            "chainIssues": ["First link missing - unknown who narrated from Yahya ibn Abi Kathir", "Yahya ibn Abi Kathir uses indirect transmission term 'عَنْ'"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain at beginning",
            "impact": "The compiler is unknown, creating a disconnection before Yahya ibn Abi Kathir."
        },
        {
            "issue": "Indirect transmission term",
            "impact": "Yahya ibn Abi Kathir uses 'عَنْ' (from) which is indirect. However, Yahya is Thiqah and a well-known reliable narrator from the second-third generation."
        },
        {
            "issue": "Maqta' hadith",
            "impact": "This appears to be a companion's statement (mawquf) or athar rather than a marfu' hadith from the Prophet ﷺ, as it is attributed to Abu Salamah's words."
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Acceptable",
    "Topics": [
        "Preparations for death",
        "Signs of the Hour - times when death becomes preferable to life",
        "Advice of Abu Salamah to seek death in righteousness"
    ]
}

analyzed_hadiths.append(hadith_1)

# ============= HADITH 2 (ID 6398) =============
hadith_2 = {
    "hadith_id": 6398,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1427",
    "english_translation": "Narrated by Ayyub through Ibn Sireen: 'When fitna (tribulation) arose, there were ten thousand companions of the Prophet ﷺ, and forty men did not diminish from them.' Ma'mar said: Others said: 'Forty joined with him, meaning Ali, two hundred and some.'",
    "chains": [
        {
            "type": "maqta'",
            "narrators": [
                {
                    "name": "Unknown Collector",
                    "full_name": "Unknown Collector/Compiler",
                    "grade": "Majhul",
                    "generation": "Unknown",
                    "transmissionTerm": "",
                    "reliabilityIssues": ["complete_disconnection"],
                    "narrator_id": None,
                    "alternative_names": "",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "",
                    "nisba_ar": "",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Majhul",
                    "tabaqat": "Unknown",
                    "location": "",
                    "transmissionTermMeaning": ""
                },
                {
                    "name": "Ayyub",
                    "full_name": "Ayyub ibn Abi Tamimah al-Sukhti",
                    "grade": "Thiqah Thabt",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": [],
                    "narrator_id": 746,
                    "alternative_names": "Ayyub al-Sukhti, Abu Muhammad",
                    "original_id": None,
                    "kunya": "Abu Muhammad",
                    "nisba": "al-Sukhti",
                    "nisba_ar": "السختي",
                    "death_year": "131",
                    "birth_year": "60",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "Second Generation",
                    "location": "Basra",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Ibn Sireen",
                    "full_name": "Muhammad ibn Sireen al-Ansari",
                    "grade": "Thiqah",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": [],
                    "narrator_id": 7016,
                    "alternative_names": "Ibn Sireen, Muhammad ibn Sireen",
                    "original_id": None,
                    "kunya": "Abu Bakr",
                    "nisba": "al-Ansari",
                    "nisba_ar": "الأنصاري",
                    "death_year": "110",
                    "birth_year": "33",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "Second Generation",
                    "location": "Basra",
                    "transmissionTermMeaning": "From (indirect transmission)"
                }
            ],
            "chainIssues": ["First link missing - unknown who narrated from Ayyub", "Two consecutive uses of 'عَنْ' (indirect transmission)"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain",
            "impact": "The compiler is unknown, and the chain starts with unknown narrator."
        },
        {
            "issue": "Multiple indirect transmission terms",
            "impact": "Both Ayyub and Ibn Sireen use 'عَنْ', but both are Thiqah narrators from the second generation."
        },
        {
            "issue": "This appears to be an athar (companion/follower statement)",
            "impact": "The text is attributed to Ibn Sireen's statement about what happened during fitna, not a hadith from the Prophet ﷺ."
        },
        {
            "issue": "Variant narrations included",
            "impact": "The text includes variant versions within the same hadith (Ma'mar and others provide different numbers), which adds complexity to the interpretation."
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Acceptable",
    "Topics": [
        "Incident during the first tribulation (fitna)",
        "Number of companions remaining steadfast",
        "Support for Ali during tribulation",
        "Historical record of companions during trial"
    ]
}

analyzed_hadiths.append(hadith_2)

# ============= HADITH 3 (ID 6399) =============
hadith_3 = {
    "hadith_id": 6399,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1428",
    "english_translation": "Narrated by Ayyub through Ibn Sireen, from Sa'd ibn Abi Waqqas: It was said to Sa'd: 'Will you not fight? Indeed you are from the people of consultation (shura), and you are more worthy of this matter than others.' He said: 'I will not fight until you bring me a sword that has two eyes, a tongue, and two lips.'",
    "chains": [
        {
            "type": "mawquf",
            "narrators": [
                {
                    "name": "Unknown Collector",
                    "full_name": "Unknown Collector/Compiler",
                    "grade": "Majhul",
                    "generation": "Unknown",
                    "transmissionTerm": "",
                    "reliabilityIssues": ["complete_disconnection"],
                    "narrator_id": None,
                    "alternative_names": "",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "",
                    "nisba_ar": "",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Majhul",
                    "tabaqat": "Unknown",
                    "location": "",
                    "transmissionTermMeaning": ""
                },
                {
                    "name": "Ayyub",
                    "full_name": "Ayyub ibn Abi Tamimah al-Sukhti",
                    "grade": "Thiqah Thabt",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": [],
                    "narrator_id": 746,
                    "alternative_names": "Ayyub al-Sukhti",
                    "original_id": None,
                    "kunya": "Abu Muhammad",
                    "nisba": "al-Sukhti",
                    "nisba_ar": "السختي",
                    "death_year": "131",
                    "birth_year": "60",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "Second Generation",
                    "location": "Basra",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Ibn Sireen",
                    "full_name": "Muhammad ibn Sireen al-Ansari",
                    "grade": "Thiqah",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": [],
                    "narrator_id": 7016,
                    "alternative_names": "Ibn Sireen",
                    "original_id": None,
                    "kunya": "Abu Bakr",
                    "nisba": "al-Ansari",
                    "nisba_ar": "الأنصاري",
                    "death_year": "110",
                    "birth_year": "33",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "Second Generation",
                    "location": "Basra",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Sa'd ibn Abi Waqqas",
                    "full_name": "Sa'd ibn Malik ibn Abi Waqqas al-Qurashi",
                    "grade": "Thiqah Thabt",
                    "generation": "Companion",
                    "transmissionTerm": "قَالَ",
                    "reliabilityIssues": [],
                    "narrator_id": 3232,
                    "alternative_names": "Sa'd ibn Abi Waqqas, Abu Ishaq",
                    "original_id": None,
                    "kunya": "Abu Ishaq",
                    "nisba": "al-Qurashi",
                    "nisba_ar": "القرشي",
                    "death_year": "54",
                    "birth_year": "",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "Companion",
                    "location": "Kufa/Madinah",
                    "transmissionTermMeaning": "He said"
                }
            ],
            "chainIssues": ["First link missing - unknown who narrated from Ayyub", "Two consecutive uses of 'عَنْ' (indirect transmission)"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain at beginning",
            "impact": "The compiler is unknown."
        },
        {
            "issue": "Multiple indirect transmission terms",
            "impact": "Both Ayyub and Ibn Sireen use 'عَنْ', but both are Thiqah narrators."
        },
        {
            "issue": "Mawquf (companion statement)",
            "impact": "This is a statement from Sa'd ibn Abi Waqqas (a companion) during tribulation, not a hadith from the Prophet ﷺ."
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Acceptable",
    "Topics": [
        "Sa'd ibn Abi Waqqas refusing to participate in fitna",
        "Wisdom and prudence in warfare",
        "Companion's stance during internal strife"
    ]
}

analyzed_hadiths.append(hadith_3)

# ============= HADITH 4 (ID 6400) =============
hadith_4 = {
    "hadith_id": 6400,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1429",
    "english_translation": "Narrated by Qatadah through al-Hasan from Abu Bakrah: The Messenger of Allah ﷺ said: 'When two Muslims meet each other with their swords (in fight) and one of them kills the other, then both the killer and the killed one are in the Fire.' The companions asked: 'O Messenger of Allah...'",
    "chains": [
        {
            "type": "marfu'",
            "narrators": [
                {
                    "name": "Unknown Collector",
                    "full_name": "Unknown Collector/Compiler",
                    "grade": "Majhul",
                    "generation": "Unknown",
                    "transmissionTerm": "",
                    "reliabilityIssues": ["complete_disconnection"],
                    "narrator_id": None,
                    "alternative_names": "",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "",
                    "nisba_ar": "",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Majhul",
                    "tabaqat": "Unknown",
                    "location": "",
                    "transmissionTermMeaning": ""
                },
                {
                    "name": "Qatadah",
                    "full_name": "Qatadah ibn Da'amah al-Sadusi",
                    "grade": "Thiqah Yukhti'",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["tadlis"],
                    "narrator_id": 6458,
                    "alternative_names": "Qatadah al-Sadusi",
                    "original_id": None,
                    "kunya": "Abu al-Khattab",
                    "nisba": "al-Sadusi",
                    "nisba_ar": "الساديسي",
                    "death_year": "117",
                    "birth_year": "61",
                    "reliability_grade": "Thiqah Yukhti'",
                    "tabaqat": "Second Generation",
                    "location": "Basra",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "al-Hasan",
                    "full_name": "al-Hasan ibn Abi al-Hasan al-Basri",
                    "grade": "Thiqah Yukhti'",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["possible_tadlis"],
                    "narrator_id": 1239,
                    "alternative_names": "al-Hasan al-Basri",
                    "original_id": None,
                    "kunya": "Abu Sa'id",
                    "nisba": "al-Basri",
                    "nisba_ar": "البصري",
                    "death_year": "110",
                    "birth_year": "21",
                    "reliability_grade": "Thiqah Yukhti'",
                    "tabaqat": "Second Generation",
                    "location": "Basra",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Abu Bakrah",
                    "full_name": "Nafi ibn al-Harith ibn Kalada",
                    "grade": "Thiqah",
                    "generation": "Companion",
                    "transmissionTerm": "قَالَ",
                    "reliabilityIssues": [],
                    "narrator_id": 7929,
                    "alternative_names": "Abu Bakrah al-Thaqafi",
                    "original_id": None,
                    "kunya": "Abu Bakrah",
                    "nisba": "al-Thaqafi",
                    "nisba_ar": "الثقفي",
                    "death_year": "51",
                    "birth_year": "",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "Companion",
                    "location": "Madinah",
                    "transmissionTermMeaning": "He said"
                },
                {
                    "name": "Prophet Muhammad ﷺ",
                    "full_name": "Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim",
                    "grade": "Awthaq al-Nas",
                    "generation": "Prophet",
                    "transmissionTerm": "",
                    "reliabilityIssues": [],
                    "narrator_id": 0,
                    "alternative_names": "Ahmad, al-Mustafa",
                    "original_id": 0,
                    "kunya": "Abu al-Qasim",
                    "nisba": "al-Hashimi al-Qurashi",
                    "nisba_ar": "الهاشمي القرشي",
                    "death_year": "11",
                    "birth_year": "53 BH",
                    "reliability_grade": "Awthaq al-Nas",
                    "tabaqat": "Prophet",
                    "location": "Makkah/Madinah",
                    "transmissionTermMeaning": ""
                }
            ],
            "chainIssues": ["First link missing - unknown who narrated from Qatadah", "Multiple uses of indirect transmission term 'عَنْ'", "Qatadah is known for tadlis (concealment of weakness in chain) - uses 'عَنْ' instead of direct transmission"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain at beginning",
            "impact": "The compiler is unknown."
        },
        {
            "issue": "Qatadah known for tadlis",
            "impact": "Qatadah ibn Da'amah is classified as a mudallis (one who hides weaknesses in transmission) and uses 'عَنْ' instead of direct transmission terms. This is problematic."
        },
        {
            "issue": "al-Hasan also uses indirect transmission",
            "impact": "al-Hasan al-Basri also uses 'عَنْ', and he too is known to have used tadlis (concealment) in some narrations."
        },
        {
            "issue": "Multiple questionable transmission links",
            "impact": "Both Qatadah and al-Hasan use indirect terms and both have issues with tadlis, which creates concern about the chain's reliability."
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Questionable But Might Be Acceptable",
    "Topics": [
        "Prohibition against fighting between Muslims",
        "Spiritual danger of killing a Muslim",
        "Both killer and killed in the Fire if the fight is unjust",
        "Guidance on internal conflicts among believers"
    ]
}

analyzed_hadiths.append(hadith_4)

# ============= HADITH 5 (ID 6401) =============
hadith_5 = {
    "hadith_id": 6401,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1430",
    "english_translation": "Narrated by Thabit through Anas: The people of Madinah were frightened one day, so the Prophet ﷺ rode a horse as though it were in readiness and drove it in their tracks. When he returned, he said: 'We found it (the source of fear) to be like an ocean.'",
    "chains": [
        {
            "type": "marfu'",
            "narrators": [
                {
                    "name": "Unknown Collector",
                    "full_name": "Unknown Collector/Compiler",
                    "grade": "Majhul",
                    "generation": "Unknown",
                    "transmissionTerm": "",
                    "reliabilityIssues": ["complete_disconnection"],
                    "narrator_id": None,
                    "alternative_names": "",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "",
                    "nisba_ar": "",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Majhul",
                    "tabaqat": "Unknown",
                    "location": "",
                    "transmissionTermMeaning": ""
                },
                {
                    "name": "Thabit",
                    "full_name": "Thabit ibn Qays ibn Shammas al-Ansari",
                    "grade": "Thiqah",
                    "generation": "Companion",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": [],
                    "narrator_id": 2009,
                    "alternative_names": "Thabit ibn Qays",
                    "original_id": None,
                    "kunya": "Abu Muhammad",
                    "nisba": "al-Ansari",
                    "nisba_ar": "الأنصاري",
                    "death_year": "34",
                    "birth_year": "",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "Companion",
                    "location": "Madinah",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Anas",
                    "full_name": "Anas ibn Malik al-Ansari",
                    "grade": "Thiqah Thabt",
                    "generation": "Companion",
                    "transmissionTerm": "قَالَ",
                    "reliabilityIssues": [],
                    "narrator_id": 720,
                    "alternative_names": "Anas ibn Malik",
                    "original_id": None,
                    "kunya": "Abu Hamzah",
                    "nisba": "al-Ansari",
                    "nisba_ar": "الأنصاري",
                    "death_year": "93",
                    "birth_year": "10 BH",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "Companion",
                    "location": "Madinah/Basra",
                    "transmissionTermMeaning": "He said"
                },
                {
                    "name": "Prophet Muhammad ﷺ",
                    "full_name": "Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim",
                    "grade": "Awthaq al-Nas",
                    "generation": "Prophet",
                    "transmissionTerm": "",
                    "reliabilityIssues": [],
                    "narrator_id": 0,
                    "alternative_names": "Ahmad, al-Mustafa",
                    "original_id": 0,
                    "kunya": "Abu al-Qasim",
                    "nisba": "al-Hashimi al-Qurashi",
                    "nisba_ar": "الهاشمي القرشي",
                    "death_year": "11",
                    "birth_year": "53 BH",
                    "reliability_grade": "Awthaq al-Nas",
                    "tabaqat": "Prophet",
                    "location": "Makkah/Madinah",
                    "transmissionTermMeaning": ""
                }
            ],
            "chainIssues": ["First link missing - unknown who narrated from Thabit", "Thabit ibn Qays uses 'عَنْ' to transmit from Anas"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain at beginning",
            "impact": "The compiler is unknown."
        },
        {
            "issue": "Unusual transmission from companion to companion",
            "impact": "Thabit is transmitting from Anas who are both companions, using 'عَنْ'. This is unusual but both are reliable companions."
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Acceptable",
    "Topics": [
        "Incident of alarm in Madinah",
        "Prophet's ﷺ quick response to frightened people",
        "Bravery and decisive action of the Prophet ﷺ",
        "Resolution of panic and fear"
    ]
}

analyzed_hadiths.append(hadith_5)

# ============= HADITH 6 (ID 6402) =============
hadith_6 = {
    "hadith_id": 6402,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1431",
    "english_translation": "Narrated by Yahya ibn Sa'id through Ibn al-Musayyab: 'The first tribulation arose and none remained from those who witnessed Badr. Then came the second tribulation and none remained from those who witnessed al-Hudaybiyyah.' He said: 'And I think if there had been a third tribulation...'",
    "chains": [
        {
            "type": "mawquf",
            "narrators": [
                {
                    "name": "Unknown Collector",
                    "full_name": "Unknown Collector/Compiler",
                    "grade": "Majhul",
                    "generation": "Unknown",
                    "transmissionTerm": "",
                    "reliabilityIssues": ["complete_disconnection"],
                    "narrator_id": None,
                    "alternative_names": "",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "",
                    "nisba_ar": "",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Majhul",
                    "tabaqat": "Unknown",
                    "location": "",
                    "transmissionTermMeaning": ""
                },
                {
                    "name": "Yahya ibn Sa'id",
                    "full_name": "Yahya ibn Sa'id al-Ansari",
                    "grade": "Thiqah",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": [],
                    "narrator_id": None,
                    "alternative_names": "Yahya ibn Sa'id al-Ansari",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "al-Ansari",
                    "nisba_ar": "الأنصاري",
                    "death_year": "143",
                    "birth_year": "74",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "Second Generation",
                    "location": "Madinah",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Ibn al-Musayyab",
                    "full_name": "Sa'id ibn al-Musayyab al-Qurashi",
                    "grade": "Thiqah",
                    "generation": "Second Generation",
                    "transmissionTerm": "قَالَ",
                    "reliabilityIssues": [],
                    "narrator_id": 3299,
                    "alternative_names": "Ibn al-Musayyab, Sa'id ibn al-Musayyab",
                    "original_id": None,
                    "kunya": "Abu Muhammad",
                    "nisba": "al-Qurashi",
                    "nisba_ar": "القرشي",
                    "death_year": "94",
                    "birth_year": "16",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "Second Generation",
                    "location": "Madinah",
                    "transmissionTermMeaning": "He said"
                }
            ],
            "chainIssues": ["First link missing - unknown who narrated from Yahya ibn Sa'id", "Yahya ibn Sa'id uses 'عَنْ' (indirect transmission)"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain at beginning",
            "impact": "The compiler is unknown."
        },
        {
            "issue": "Indirect transmission term",
            "impact": "Yahya ibn Sa'id uses 'عَنْ', though he is Thiqah."
        },
        {
            "issue": "Mawquf (follower's statement)",
            "impact": "This is Ibn al-Musayyab's historical observation about the companions, not a hadith from the Prophet ﷺ."
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Acceptable",
    "Topics": [
        "Historical record of trials and tribulations",
        "Companions who witnessed Badr and their martyrdom",
        "Companions who witnessed al-Hudaybiyyah",
        "Generations lost during periods of fitna"
    ]
}

analyzed_hadiths.append(hadith_6)

# Save to file
with open('/tmp/processed_hadiths_batch_1_chunk_2.json', 'w', encoding='utf-8') as f:
    json.dump(analyzed_hadiths, f, ensure_ascii=False, indent=2)

print("✓ Analysis complete for Chunk 2")
print(f"✓ Generated analysis for {len(analyzed_hadiths)} hadiths")
print("✓ Saved to: /tmp/processed_hadiths_batch_1_chunk_2.json")
