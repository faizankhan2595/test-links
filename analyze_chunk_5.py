import json

with open('split_hadiths/combined_batch_1_chunk_5.json', 'r', encoding='utf-8') as f:
    chunk_data = json.load(f)

analyzed_hadiths = []

# ============= HADITH 1 (ID 6415) =============
hadith_1 = {
    "hadith_id": 6415,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1444",
    "english_translation": "Narrated by Qatadah and Sulayman al-Taymi (both said): Abu Najjar said that the Messenger of Allah ﷺ said: 'Whoever...'",
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
                    "name": "Sulayman al-Taymi",
                    "full_name": "Sulayman ibn Taraydah al-Taymi",
                    "grade": "Saduq",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["indirect_transmission"],
                    "narrator_id": 3601,
                    "alternative_names": "Sulayman al-Taymi",
                    "original_id": None,
                    "kunya": "Abu Muhammad",
                    "nisba": "al-Taymi",
                    "nisba_ar": "التيمي",
                    "death_year": "131",
                    "birth_year": "54",
                    "reliability_grade": "Saduq",
                    "tabaqat": "Second Generation",
                    "location": "Kufa",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Abu Najjar",
                    "full_name": "Abu Najjar (unidentified)",
                    "grade": "Majhul",
                    "generation": "Unknown",
                    "transmissionTerm": "قَالَ",
                    "reliabilityIssues": ["unknown_narrator"],
                    "narrator_id": None,
                    "alternative_names": "Abu Najjar",
                    "original_id": None,
                    "kunya": "Abu Najjar",
                    "nisba": "",
                    "nisba_ar": "",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Majhul",
                    "tabaqat": "Unknown",
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
            "chainIssues": ["First link missing", "Qatadah known for tadlis", "Abu Najjar is completely unknown", "Multiple indirect transmissions"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain at beginning",
            "impact": "The collector is unknown."
        },
        {
            "issue": "Qatadah known for tadlis",
            "impact": "Qatadah ibn Da'amah is known for concealing chain weaknesses and uses indirect transmission 'عَنْ'."
        },
        {
            "issue": "Abu Najjar is completely unknown",
            "impact": "This narrator is not identified and his reliability cannot be assessed."
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Weak But Might Be Acceptable",
    "Topics": [
        "Hadith transmitted through two chains (Qatadah and Sulayman al-Taymi)",
        "Teaching of the Prophet ﷺ"
    ]
}

analyzed_hadiths.append(hadith_1)

# ============= HADITH 2 (ID 6416) =============
hadith_2 = {
    "hadith_id": 6416,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1445",
    "english_translation": "Narrated from Ibn Tawus through his father: That the Prophet ﷺ said...",
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
                    "name": "Ibn Tawus",
                    "full_name": "Abdullah ibn Tawus al-Qurashi",
                    "grade": "Thiqah",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": [],
                    "narrator_id": 4871,
                    "alternative_names": "Ibn Tawus al-Qurashi",
                    "original_id": None,
                    "kunya": "Abu Muhammad",
                    "nisba": "al-Qurashi",
                    "nisba_ar": "القرشي",
                    "death_year": "132",
                    "birth_year": "53",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "Second Generation",
                    "location": "Makkah",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Tawus",
                    "full_name": "Tawus ibn Kaysan",
                    "grade": "Thiqah",
                    "generation": "First Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": [],
                    "narrator_id": 4002,
                    "alternative_names": "Tawus al-Yamani",
                    "original_id": None,
                    "kunya": "Abu Uthman",
                    "nisba": "al-Yamani",
                    "nisba_ar": "اليمني",
                    "death_year": "106",
                    "birth_year": "30",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "First Generation",
                    "location": "Yaman",
                    "transmissionTermMeaning": "From (indirect transmission)"
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
            "chainIssues": ["First link missing", "Two consecutive 'عَنْ' (indirect transmissions)", "Uses 'أَنَّ' (that) which is also indirect"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain at beginning",
            "impact": "The collector is unknown."
        },
        {
            "issue": "Multiple indirect transmission terms",
            "impact": "Both Ibn Tawus and his father Tawus use 'عَنْ', and 'أَنَّ' (that) is also used, indicating multiple levels of indirection."
        },
        {
            "issue": "Unclear if directly from Prophet",
            "impact": "Tawus was not a companion but from the first generation after, so the transmission from him to the Prophet ﷺ needs verification."
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Acceptable",
    "Topics": [
        "Hadith transmitted through Ibn Tawus and his father Tawus"
    ]
}

analyzed_hadiths.append(hadith_2)

# ============= HADITH 3 (ID 6417) =============
hadith_3 = {
    "hadith_id": 6417,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1446",
    "english_translation": "Narrated from Ayyub through Abu Qilabah ibn Ka'b: (The story about...)...",
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
                    "full_name": "Abdullah ibn Zaid al-Uqayli",
                    "grade": "Thiqah Yukhti'",
                    "generation": "Second Generation",
                    "transmissionTerm": "قَالَ",
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
                    "transmissionTermMeaning": "He said"
                }
            ],
            "chainIssues": ["First link missing", "Incomplete text cuts off the hadith"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain",
            "impact": "The collector is unknown, and the text itself is incomplete."
        },
        {
            "issue": "Text appears truncated",
            "impact": "The hadith text is cut off and does not provide complete meaning."
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Disconnections But All Narrators Are Ok",
    "Topics": [
        "Story or incident through Abu Qilabah (text incomplete)"
    ]
}

analyzed_hadiths.append(hadith_3)

# ============= HADITH 4 (ID 6418) =============
hadith_4 = {
    "hadith_id": 6418,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1447",
    "english_translation": "Narrated from Ayyub through Ibn Sireen: (He said) 'Ibn Abbas said...'",
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
                    "transmissionTerm": "قَالَ",
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
            "issue": "Mawquf (Ibn Abbas statement)",
            "impact": "This is Ibn Abbas' statement, not a hadith from the Prophet ﷺ."
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Acceptable",
    "Topics": [
        "Ibn Abbas' interpretation or statement"
    ]
}

analyzed_hadiths.append(hadith_4)

# ============= HADITH 5 (ID 6419) =============
hadith_5 = {
    "hadith_id": 6419,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1448",
    "english_translation": "Said by more than one from al-Hayy: Through Hind bint al-Muhallal: (She said) '...'",
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
                    "name": "Multiple narrators from al-Hayy",
                    "full_name": "Multiple unidentified narrators",
                    "grade": "Majhul",
                    "generation": "Unknown",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["unknown_narrators"],
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
                    "name": "Hind bint al-Muhallal",
                    "full_name": "Hind bint al-Muhallal",
                    "grade": "Majhul",
                    "generation": "Unknown",
                    "transmissionTerm": "قَالَتْ",
                    "reliabilityIssues": ["unknown_reliability"],
                    "narrator_id": None,
                    "alternative_names": "Hind bint al-Muhallal",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "",
                    "nisba_ar": "",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Majhul",
                    "tabaqat": "Unknown",
                    "location": "",
                    "transmissionTermMeaning": "She said"
                }
            ],
            "chainIssues": ["Multiple unknown narrators from al-Hayy", "Hind bint al-Muhallal has unknown reliability"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Multiple unknown narrators",
            "impact": "The text mentions 'more than one from al-Hayy' without identifying them, making the chain completely unreliable."
        },
        {
            "issue": "Unknown female narrator",
            "impact": "Hind bint al-Muhallal's reliability cannot be assessed."
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Weak But Might Be Acceptable",
    "Topics": [
        "Statement from Hind bint al-Muhallal (text incomplete)"
    ]
}

analyzed_hadiths.append(hadith_5)

# ============= HADITH 6 (ID 6420) =============
hadith_6 = {
    "hadith_id": 6420,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1449",
    "english_translation": "Narrated from Ayyub through Ibn Sireen: (He said) 'When the Imam becomes...'",
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
                    "transmissionTerm": "قَالَ",
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
            "issue": "Athar (follower statement)",
            "impact": "This is Ibn Sireen's statement about Imams, not a hadith from the Prophet ﷺ."
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Acceptable",
    "Topics": [
        "Ibn Sireen's teaching about Imams and leadership"
    ]
}

analyzed_hadiths.append(hadith_6)

# Save to file
with open('/tmp/processed_hadiths_batch_1_chunk_5.json', 'w', encoding='utf-8') as f:
    json.dump(analyzed_hadiths, f, ensure_ascii=False, indent=2)

print("✓ Analysis complete for Chunk 5 (FINAL)")
print(f"✓ Generated analysis for {len(analyzed_hadiths)} hadiths")
print("✓ Saved to: /tmp/processed_hadiths_batch_1_chunk_5.json")
