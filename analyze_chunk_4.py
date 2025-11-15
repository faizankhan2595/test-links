import json

with open('split_hadiths/combined_batch_1_chunk_4.json', 'r', encoding='utf-8') as f:
    chunk_data = json.load(f)

analyzed_hadiths = []

# ============= HADITH 1 (ID 6409) =============
hadith_1 = {
    "hadith_id": 6409,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1438",
    "english_translation": "Narrated from a man through Ibn al-Musayyab: 'There will be a tribulation that separates the close ones and brings together the distant ones.'",
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
                    "name": "Unknown Man",
                    "full_name": "Unknown narrator",
                    "grade": "Majhul",
                    "generation": "Unknown",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["unknown_narrator"],
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
                    "transmissionTermMeaning": "From"
                },
                {
                    "name": "Ibn al-Musayyab",
                    "full_name": "Sa'id ibn al-Musayyab al-Qurashi",
                    "grade": "Thiqah",
                    "generation": "Second Generation",
                    "transmissionTerm": "قَالَ",
                    "reliabilityIssues": [],
                    "narrator_id": 3299,
                    "alternative_names": "Ibn al-Musayyab",
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
            "chainIssues": ["First narrator is completely unknown (identified only as 'a man')", "Complete missing beginning of chain"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Unknown narrator in chain",
            "impact": "The text identifies the narrator only as 'a man' (رجل) without providing any identification or details."
        },
        {
            "issue": "Incomplete chain at multiple points",
            "impact": "Both the collector and the initial narrator are unknown."
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Weak But Might Be Acceptable",
    "Topics": [
        "Effects of tribulation on relationships",
        "How fitna separates and divides people",
        "Ibn al-Musayyab's observations on social division"
    ]
}

analyzed_hadiths.append(hadith_1)

# ============= HADITH 2 (ID 6410) =============
hadith_2 = {
    "hadith_id": 6410,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1439",
    "english_translation": "Narrated by al-Zuhari through Urwah ibn al-Zubayr from Kurz ibn Jabir al-Fihri: (He said) 'I was with the Prophet ﷺ...'",
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
                    "name": "al-Zuhari",
                    "full_name": "Muhammad ibn Shihab al-Zuhari",
                    "grade": "Thiqah Thabt",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["mild_tadlis"],
                    "narrator_id": 7272,
                    "alternative_names": "Ibn Shihab al-Zuhari",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "al-Zuhari",
                    "nisba_ar": "الزهري",
                    "death_year": "124",
                    "birth_year": "50",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "Second Generation",
                    "location": "Madinah/Egypt",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Urwah ibn al-Zubayr",
                    "full_name": "Urwah ibn al-Zubayr ibn al-Awwam",
                    "grade": "Thiqah Thabt",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": [],
                    "narrator_id": 5594,
                    "alternative_names": "Urwah al-Qurashi",
                    "original_id": None,
                    "kunya": "Abu Abdullâh",
                    "nisba": "al-Qurashi",
                    "nisba_ar": "القرشي",
                    "death_year": "94",
                    "birth_year": "20",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "Second Generation",
                    "location": "Madinah",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Kurz ibn Jabir",
                    "full_name": "Kurz ibn Jabir al-Fihri",
                    "grade": "Saduq",
                    "generation": "Companion",
                    "transmissionTerm": "قَالَ",
                    "reliabilityIssues": [],
                    "narrator_id": None,
                    "alternative_names": "Kurz al-Fihri",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "al-Fihri",
                    "nisba_ar": "الفهري",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Saduq",
                    "tabaqat": "Companion",
                    "location": "",
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
            "chainIssues": ["First link missing - unknown who narrated from al-Zuhari", "Multiple narrators using indirect transmission term 'عَنْ'"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain at beginning",
            "impact": "The collector is unknown."
        },
        {
            "issue": "al-Zuhari uses indirect transmission",
            "impact": "While al-Zuhari (Ibn Shihab) is Thiqah Thabt and highly reliable, he is known by some scholars to occasionally have used tadlis (concealment). However, he is generally trusted even with 'عَنْ' terms."
        },
        {
            "issue": "Multiple indirect transmissions",
            "impact": "Both al-Zuhari and Urwah use 'عَنْ', but both are highly reliable narrators."
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Sound",
    "Topics": [
        "Incident with Kurz ibn Jabir and the Prophet ﷺ",
        "Teaching and guidance of the Prophet ﷺ"
    ]
}

analyzed_hadiths.append(hadith_2)

# ============= HADITH 3 (ID 6411) =============
hadith_3 = {
    "hadith_id": 6411,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1440",
    "english_translation": "Narrated by al-Zuhari from Hind bint al-Harith: (al-Zuhari said) 'This was mentioned in the hadith about the Dajjal (Antichrist)...'",
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
                    "name": "al-Zuhari",
                    "full_name": "Muhammad ibn Shihab al-Zuhari",
                    "grade": "Thiqah Thabt",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["mild_tadlis"],
                    "narrator_id": 7272,
                    "alternative_names": "Ibn Shihab al-Zuhari",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "al-Zuhari",
                    "nisba_ar": "الزهري",
                    "death_year": "124",
                    "birth_year": "50",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "Second Generation",
                    "location": "Madinah/Egypt",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Hind bint al-Harith",
                    "full_name": "Hind bint al-Harith",
                    "grade": "Majhul al-Hal",
                    "generation": "Companion or follower",
                    "transmissionTerm": "قَالَ",
                    "reliabilityIssues": ["unknown_reliability"],
                    "narrator_id": 8102,
                    "alternative_names": "Hind bint al-Harith",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "",
                    "nisba_ar": "",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Majhul al-Hal",
                    "tabaqat": "Companion/Follower",
                    "location": "",
                    "transmissionTermMeaning": "She said"
                }
            ],
            "chainIssues": ["First link missing", "Hind bint al-Harith has unknown reliability status"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain",
            "impact": "The collector is unknown."
        },
        {
            "issue": "Hind bint al-Harith of unknown reliability",
            "impact": "This narrator is classified as Majhul al-Hal (of unknown condition)."
        },
        {
            "issue": "This is not clearly a hadith from the Prophet",
            "impact": "The text suggests this is al-Zuhari's commentary about the Dajjal hadith, making it a scholarly statement rather than a direct hadith transmission."
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Weak But Might Be Acceptable",
    "Topics": [
        "The Dajjal (Antichrist)",
        "al-Zuhari's scholarly commentary on Dajjal hadith"
    ]
}

analyzed_hadiths.append(hadith_3)

# ============= HADITH 4 (ID 6412) =============
hadith_4 = {
    "hadith_id": 6412,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1441",
    "english_translation": "Narrated by al-Zuhari through Urwah from Zaynab bint Abi Salamah from Umm Salamah: (She said) 'O Messenger of Allah, will you make dua for me?'",
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
                    "name": "al-Zuhari",
                    "full_name": "Muhammad ibn Shihab al-Zuhari",
                    "grade": "Thiqah Thabt",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["mild_tadlis"],
                    "narrator_id": 7272,
                    "alternative_names": "Ibn Shihab al-Zuhari",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "al-Zuhari",
                    "nisba_ar": "الزهري",
                    "death_year": "124",
                    "birth_year": "50",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "Second Generation",
                    "location": "Madinah/Egypt",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Urwah ibn al-Zubayr",
                    "full_name": "Urwah ibn al-Zubayr ibn al-Awwam",
                    "grade": "Thiqah Thabt",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": [],
                    "narrator_id": 5594,
                    "alternative_names": "Urwah al-Qurashi",
                    "original_id": None,
                    "kunya": "Abu Abdullah",
                    "nisba": "al-Qurashi",
                    "nisba_ar": "القرشي",
                    "death_year": "94",
                    "birth_year": "20",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "Second Generation",
                    "location": "Madinah",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Zaynab bint Abi Salamah",
                    "full_name": "Zaynab bint Abi Salamah al-Qurashi",
                    "grade": "Thiqah",
                    "generation": "First Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": [],
                    "narrator_id": None,
                    "alternative_names": "Zaynab al-Qurashi",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "al-Qurashi",
                    "nisba_ar": "القرشي",
                    "death_year": "73",
                    "birth_year": "4 BH",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "First Generation",
                    "location": "Madinah",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Umm Salamah",
                    "full_name": "Hind bint Abi Umayyah al-Makhzumiyyah",
                    "grade": "Thiqah Thabt",
                    "generation": "Companion",
                    "transmissionTerm": "قَالَتْ",
                    "reliabilityIssues": [],
                    "narrator_id": None,
                    "alternative_names": "Umm Salamah, Hind al-Makhzumiyyah",
                    "original_id": None,
                    "kunya": "Umm Salamah",
                    "nisba": "al-Makhzumiyyah",
                    "nisba_ar": "المخزومية",
                    "death_year": "62",
                    "birth_year": "",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "Companion",
                    "location": "Madinah",
                    "transmissionTermMeaning": "She said"
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
            "chainIssues": ["First link missing - unknown collector", "Multiple narrators using 'عَنْ' (indirect transmission)"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain",
            "impact": "The collector is unknown."
        },
        {
            "issue": "Multiple indirect transmission terms",
            "impact": "al-Zuhari, Urwah, and Zaynab all use 'عَنْ', but all are highly reliable narrators."
        },
        {
            "issue": "Multiple female narrators in chain",
            "impact": "While female narrators are acceptable and these are reliable, the chain length and multiple indirect terms slightly reduce reliability."
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Sound",
    "Topics": [
        "Supplication (dua) for healing",
        "Umm Salamah's request for the Prophet's ﷺ dua",
        "Prophet's ﷺ mercy and compassion"
    ]
}

analyzed_hadiths.append(hadith_4)

# ============= HADITH 5 (ID 6413) =============
hadith_5 = {
    "hadith_id": 6413,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1442",
    "english_translation": "Narrated by al-Zuhari from Abu Idris al-Khawlani: (He said) 'I went to Muawiyah asking for provision, and he gave me...'",
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
                    "name": "al-Zuhari",
                    "full_name": "Muhammad ibn Shihab al-Zuhari",
                    "grade": "Thiqah Thabt",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["mild_tadlis"],
                    "narrator_id": 7272,
                    "alternative_names": "Ibn Shihab al-Zuhari",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "al-Zuhari",
                    "nisba_ar": "الزهري",
                    "death_year": "124",
                    "birth_year": "50",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "Second Generation",
                    "location": "Madinah/Egypt",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Abu Idris al-Khawlani",
                    "full_name": "Auwf ibn Malik al-Khawlani",
                    "grade": "Thiqah",
                    "generation": "Second Generation",
                    "transmissionTerm": "قَالَ",
                    "reliabilityIssues": [],
                    "narrator_id": None,
                    "alternative_names": "Abu Idris al-Khawlani",
                    "original_id": None,
                    "kunya": "Abu Idris",
                    "nisba": "al-Khawlani",
                    "nisba_ar": "الخولاني",
                    "death_year": "103",
                    "birth_year": "20",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "Second Generation",
                    "location": "Syria",
                    "transmissionTermMeaning": "He said"
                }
            ],
            "chainIssues": ["First link missing"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain",
            "impact": "The collector is unknown."
        },
        {
            "issue": "Mawquf (follower's statement)",
            "impact": "This is Abu Idris al-Khawlani's personal experience with Muawiyah, not a hadith from the Prophet ﷺ."
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Acceptable",
    "Topics": [
        "Incident of Abu Idris seeking provision from Muawiyah",
        "Generosity of leaders and governors"
    ]
}

analyzed_hadiths.append(hadith_5)

# ============= HADITH 6 (ID 6414) =============
hadith_6 = {
    "hadith_id": 6414,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1443",
    "english_translation": "Narrated by al-Zuhari through Ibn al-Musayyab: (He said) 'When tribulation arose...'",
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
                    "name": "al-Zuhari",
                    "full_name": "Muhammad ibn Shihab al-Zuhari",
                    "grade": "Thiqah Thabt",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["mild_tadlis"],
                    "narrator_id": 7272,
                    "alternative_names": "Ibn Shihab al-Zuhari",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "al-Zuhari",
                    "nisba_ar": "الزهري",
                    "death_year": "124",
                    "birth_year": "50",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "Second Generation",
                    "location": "Madinah/Egypt",
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
                    "alternative_names": "Ibn al-Musayyab",
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
            "chainIssues": ["First link missing"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain",
            "impact": "The collector is unknown."
        },
        {
            "issue": "Mawquf (follower's statement)",
            "impact": "This is Ibn al-Musayyab's observation about historical events, not a hadith from the Prophet ﷺ."
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Acceptable",
    "Topics": [
        "Historical events during early Islamic tribulations",
        "Ibn al-Musayyab's observations on fitna"
    ]
}

analyzed_hadiths.append(hadith_6)

# Save to file
with open('/tmp/processed_hadiths_batch_1_chunk_4.json', 'w', encoding='utf-8') as f:
    json.dump(analyzed_hadiths, f, ensure_ascii=False, indent=2)

print("✓ Analysis complete for Chunk 4")
print(f"✓ Generated analysis for {len(analyzed_hadiths)} hadiths")
print("✓ Saved to: /tmp/processed_hadiths_batch_1_chunk_4.json")
