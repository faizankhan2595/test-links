import json

with open('split_hadiths/combined_batch_1_chunk_3.json', 'r', encoding='utf-8') as f:
    chunk_data = json.load(f)

analyzed_hadiths = []

# ============= HADITH 1 (ID 6403) =============
hadith_1 = {
    "hadith_id": 6403,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1432",
    "english_translation": "Narrated from Abu Ishaq through Umarah ibn Abd through Hudhayfa: (Hudhayfa said) 'Beware of the Imams who (do not act) as we act. Whoever shows dislike for them as we do has cleared himself of enmity. Whoever loves them as we do loves the truth. Indeed the hypocrite listens to the word of Allah but disobeys Him.'",
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
                    "name": "Abu Ishaq",
                    "full_name": "Abu Ishaq al-Subay'i (likely Amr ibn Abdullah)",
                    "grade": "Thiqah Yukhti'",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["indirect_transmission"],
                    "narrator_id": None,
                    "alternative_names": "Abu Ishaq al-Subay'i",
                    "original_id": None,
                    "kunya": "Abu Ishaq",
                    "nisba": "al-Subay'i",
                    "nisba_ar": "السبيعي",
                    "death_year": "127",
                    "birth_year": "35",
                    "reliability_grade": "Thiqah Yukhti'",
                    "tabaqat": "Second Generation",
                    "location": "Kufa",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Umarah ibn Abd",
                    "full_name": "Umarah ibn Abd",
                    "grade": "Majhul al-Hal",
                    "generation": "Unknown",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["indirect_transmission", "unknown_reliability"],
                    "narrator_id": None,
                    "alternative_names": "",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "",
                    "nisba_ar": "",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Majhul al-Hal",
                    "tabaqat": "Unknown",
                    "location": "",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Hudhayfa",
                    "full_name": "Hudhayfa ibn al-Yaman",
                    "grade": "Thiqah",
                    "generation": "Companion",
                    "transmissionTerm": "قَالَ",
                    "reliabilityIssues": [],
                    "narrator_id": 2324,
                    "alternative_names": "Hudhayfa ibn al-Yaman, Abu Abdullah",
                    "original_id": None,
                    "kunya": "Abu Abdullah",
                    "nisba": "",
                    "nisba_ar": "",
                    "death_year": "36",
                    "birth_year": "",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "Companion",
                    "location": "Kufa",
                    "transmissionTermMeaning": "He said"
                }
            ],
            "chainIssues": ["First link missing - unknown who narrated from Abu Ishaq", "Multiple indirect transmission terms", "Umarah ibn Abd has unknown reliability status"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain at beginning",
            "impact": "The compiler is unknown."
        },
        {
            "issue": "Umarah ibn Abd of unknown reliability",
            "impact": "This narrator's reliability is not documented (Majhul al-Hal)."
        },
        {
            "issue": "Multiple indirect transmission links",
            "impact": "Both Abu Ishaq and Umarah ibn Abd use 'عَنْ'."
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Acceptable",
    "Topics": [
        "Guidance about Imams and leaders",
        "Signs of hypocrisy among leaders",
        "Distinguishing truth from falsehood in leadership",
        "Hudhayfa's counsel on identifying disbelief"
    ]
}

analyzed_hadiths.append(hadith_1)

# ============= HADITH 2 (ID 6404) =============
hadith_2 = {
    "hadith_id": 6404,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1433",
    "english_translation": "Narrated by more than one person, including al-Hasan: (That the Prophet ﷺ said) 'Verily this knowledge will migrate and will not remain in its place for three (days/times)...' or he said: 'For three (periods)...'",
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
                    "name": "Multiple Narrators including al-Hasan",
                    "full_name": "Multiple narrators (details incomplete)",
                    "grade": "Thiqah Yukhti'",
                    "generation": "Second Generation",
                    "transmissionTerm": "أَنَّ",
                    "reliabilityIssues": ["indirect_transmission", "multiple_chains_not_detailed"],
                    "narrator_id": 1131,
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
                    "transmissionTermMeaning": "That (indirect transmission)"
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
            "chainIssues": ["First link missing - unknown who collected this", "Multiple narrators mentioned but details incomplete", "Uses 'أَنَّ' which is an indirect transmission term"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain information",
            "impact": "Multiple narrators are mentioned but their details are not fully provided in the source. The text says 'غير واحد' (more than one) without specifying all of them."
        },
        {
            "issue": "Use of indirect transmission 'أَنَّ'",
            "impact": "The use of 'أَنَّ' (that) is an indirect transmission term which creates ambiguity."
        },
        {
            "issue": "Variant in text interpretation",
            "impact": "The text mentions uncertainty about whether it is 'three (days)' or 'three (periods)' showing potential variations in narration."
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Acceptable",
    "Topics": [
        "Migration of Islamic knowledge",
        "Spread of hadith and Islamic sciences",
        "Preservation and transmission of Prophet's ﷺ teachings"
    ]
}

analyzed_hadiths.append(hadith_2)

# ============= HADITH 3 (ID 6405) =============
hadith_3 = {
    "hadith_id": 6405,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1434",
    "english_translation": "Narrated by Qatadah through Ibn Mas'ud: 'How would you be if you were clothed (covered) in hypocrisy like the dye of a garment? People would not recognize anything except hypocrisy.'",
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
                    "name": "Ibn Mas'ud",
                    "full_name": "Abdullah ibn Mas'ud ibn Ghafil al-Qurashi",
                    "grade": "Thiqah Thabt",
                    "generation": "Companion",
                    "transmissionTerm": "أَنَّ",
                    "reliabilityIssues": [],
                    "narrator_id": 5079,
                    "alternative_names": "Abdullah ibn Mas'ud, Abu Abd al-Rahman",
                    "original_id": None,
                    "kunya": "Abu Abd al-Rahman",
                    "nisba": "al-Qurashi",
                    "nisba_ar": "القرشي",
                    "death_year": "32",
                    "birth_year": "",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "Companion",
                    "location": "Kufa/Madinah",
                    "transmissionTermMeaning": "That (could indicate indirect)"
                }
            ],
            "chainIssues": ["First link missing", "Qatadah known for tadlis uses 'عَنْ'", "Ibn Mas'ud's statement uses 'أَنَّ' (that)"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Qatadah known for tadlis",
            "impact": "Qatadah ibn Da'amah is known for concealing weaknesses in transmission (tadlis) and uses indirect term 'عَنْ'."
        },
        {
            "issue": "Use of indirect transmission 'أَنَّ'",
            "impact": "The 'أَنَّ' transmission term from Ibn Mas'ud suggests potential indirectness."
        },
        {
            "issue": "Mawquf statement",
            "impact": "This is Ibn Mas'ud's statement, not from the Prophet ﷺ."
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Acceptable",
    "Topics": [
        "Warning against hypocrisy",
        "Prevalence of hypocrisy in people",
        "Ibn Mas'ud's concern about widespread hypocrisy"
    ]
}

analyzed_hadiths.append(hadith_3)

# ============= HADITH 4 (ID 6406) =============
hadith_4 = {
    "hadith_id": 6406,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1435",
    "english_translation": "Narrated from Aban through Sulaym ibn Qays al-Handhali: Umar gave a sermon saying: 'Indeed...'",
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
                    "name": "Aban",
                    "full_name": "Aban ibn Uthman ibn Affan (or Aban ibn Taghlib)",
                    "grade": "Saduq",
                    "generation": "Third Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["indirect_transmission"],
                    "narrator_id": None,
                    "alternative_names": "Aban",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "",
                    "nisba_ar": "",
                    "death_year": "105",
                    "birth_year": "",
                    "reliability_grade": "Saduq",
                    "tabaqat": "Third Generation",
                    "location": "",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Sulaym ibn Qays al-Handhali",
                    "full_name": "Sulaym ibn Qays al-Handhali",
                    "grade": "Matruk",
                    "generation": "Companion or early follower",
                    "transmissionTerm": "قَالَ",
                    "reliabilityIssues": ["rejected_narrator"],
                    "narrator_id": None,
                    "alternative_names": "Sulaym ibn Qays",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "al-Handhali",
                    "nisba_ar": "الهندلي",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Matruk",
                    "tabaqat": "Companion/Follower",
                    "location": "Kufa",
                    "transmissionTermMeaning": "He said"
                }
            ],
            "chainIssues": ["First link missing", "Sulaym ibn Qays al-Handhali is classified as Matruk (abandoned) - a weak narrator"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Matruk narrator in chain",
            "impact": "Sulaym ibn Qays al-Handhali is classified as Matruk (abandoned/rejected), which is a serious weakness in the chain. Hadiths through him are generally considered problematic."
        },
        {
            "issue": "Incomplete chain",
            "impact": "The beginning of the chain is missing."
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Problematic",
    "Topics": [
        "Umar's sermon and governance",
        "Historical record of Umar ibn al-Khattab's teachings"
    ]
}

analyzed_hadiths.append(hadith_4)

# ============= HADITH 5 (ID 6407) =============
hadith_5 = {
    "hadith_id": 6407,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1436",
    "english_translation": "Narrated from Aban through al-Hasan from Abu Musa al-Ash'ari: (He said) 'Indeed the Messenger of Allah ﷺ said to me...'",
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
                    "name": "Aban",
                    "full_name": "Aban ibn Uthman ibn Affan",
                    "grade": "Saduq",
                    "generation": "Third Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["indirect_transmission"],
                    "narrator_id": 9,
                    "alternative_names": "Aban ibn Uthman",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "",
                    "nisba_ar": "",
                    "death_year": "105",
                    "birth_year": "30",
                    "reliability_grade": "Saduq",
                    "tabaqat": "Third Generation",
                    "location": "Madinah",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "al-Hasan",
                    "full_name": "al-Hasan ibn Abi al-Hasan al-Basri",
                    "grade": "Thiqah Yukhti'",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["indirect_transmission"],
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
                    "name": "Abu Musa al-Ash'ari",
                    "full_name": "Abdullah ibn Qays al-Ash'ari",
                    "grade": "Thiqah",
                    "generation": "Companion",
                    "transmissionTerm": "قَالَ",
                    "reliabilityIssues": [],
                    "narrator_id": 5021,
                    "alternative_names": "Abu Musa al-Ash'ari",
                    "original_id": None,
                    "kunya": "Abu Musa",
                    "nisba": "al-Ash'ari",
                    "nisba_ar": "الأشعري",
                    "death_year": "42",
                    "birth_year": "",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "Companion",
                    "location": "Basra",
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
            "chainIssues": ["First link missing", "Multiple narrators using indirect transmission term 'عَنْ'", "al-Hasan al-Basri known to have used tadlis in some narrations"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain",
            "impact": "The compiler is unknown."
        },
        {
            "issue": "Multiple indirect transmission terms",
            "impact": "Both Aban and al-Hasan use 'عَنْ'."
        },
        {
            "issue": "al-Hasan known for possible tadlis",
            "impact": "al-Hasan al-Basri is known in some narrations to have concealed chain weaknesses."
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Acceptable",
    "Topics": [
        "Prophet's ﷺ message to Abu Musa al-Ash'ari",
        "Duties and responsibilities of Islamic officials"
    ]
}

analyzed_hadiths.append(hadith_5)

# ============= HADITH 6 (ID 6408) =============
hadith_6 = {
    "hadith_id": 6408,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1437",
    "english_translation": "Narrated from Ayyub through Abu Qilabah: He (Abu Qilabah) and Muslim ibn Yasar and Kulayb (gathered together), and they discussed the tribulation (fitna). When the fitna arose...",
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
                    "name": "Abu Qilabah",
                    "full_name": "Abdullahibn Zaid al-Uqayli",
                    "grade": "Thiqah Yukhti'",
                    "generation": "Second Generation",
                    "transmissionTerm": "أَنَّ",
                    "reliabilityIssues": [],
                    "narrator_id": None,
                    "alternative_names": "Abu Qilabah al-Uqayli",
                    "original_id": None,
                    "kunya": "Abu Qilabah",
                    "nisba": "al-Uqayli",
                    "nisba_ar": "العقيلي",
                    "death_year": "104",
                    "birth_year": "22",
                    "reliability_grade": "Thiqah Yukhti'",
                    "tabaqat": "Second Generation",
                    "location": "Basra",
                    "transmissionTermMeaning": "That (indirect transmission)"
                }
            ],
            "chainIssues": ["First link missing", "Multiple indirect transmission terms", "Chain is incomplete - appears to be a fragment"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain",
            "impact": "The compiler is unknown and the chain appears fragmented."
        },
        {
            "issue": "Use of indirect terms",
            "impact": "Both Ayyub and Abu Qilabah use indirect transmission terms."
        },
        {
            "issue": "Athar (follower's statement)",
            "impact": "This appears to be a discussion among followers about tribulation, not a hadith from the Prophet ﷺ."
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Acceptable",
    "Topics": [
        "Discussion among followers about tribulations",
        "Incident of Followers preparing for fitna",
        "Historical record of early Islamic scholars discussing trials"
    ]
}

analyzed_hadiths.append(hadith_6)

# Save to file
with open('/tmp/processed_hadiths_batch_1_chunk_3.json', 'w', encoding='utf-8') as f:
    json.dump(analyzed_hadiths, f, ensure_ascii=False, indent=2)

print("✓ Analysis complete for Chunk 3")
print(f"✓ Generated analysis for {len(analyzed_hadiths)} hadiths")
print("✓ Saved to: /tmp/processed_hadiths_batch_1_chunk_3.json")
