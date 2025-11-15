import json

# Load chunk 1
with open('split_hadiths/combined_batch_1_chunk_1.json', 'r', encoding='utf-8') as f:
    chunk_data = json.load(f)

analyzed_hadiths = []

# ============= HADITH 1 (ID 6391) =============
hadith_1 = {
    "hadith_id": 6391,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1420",
    "english_translation": "Narrated by Abu Dharr: (The Prophet ﷺ said) 'How will you be, O Abu Dharr, when death comes in Madinah reaching the household to the level of the slave?' (meaning) that graves would be sold for the price of slaves. I said: 'Allah and His Messenger know best.' He said: 'Be patient.'",
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
                    "name": "Abu Dharr",
                    "full_name": "Jundab ibn Junada al-Ghifari",
                    "grade": "Thiqah Thabt",
                    "generation": "Companion",
                    "transmissionTerm": "قَالَ",
                    "reliabilityIssues": [],
                    "narrator_id": None,
                    "alternative_names": "Abu Dharr al-Ghifari",
                    "original_id": None,
                    "kunya": "Abu Dharr",
                    "nisba": "al-Ghifari",
                    "nisba_ar": "الغفاري",
                    "death_year": "32",
                    "birth_year": "",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "Companion",
                    "location": "Madinah/Shaam",
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
            "chainIssues": ["Complete chain missing - only 'قَالَ' (He said) provided without preceding narrators", "Chain type is maqta' (cut off/disconnected)"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Severe chain disconnection",
            "impact": "The chain starts abruptly with only 'قَالَ' (He said) with no preceding narrators. The actual collector/compiler is unknown, making it impossible to verify the chain of transmission."
        },
        {
            "issue": "Maqta' (Cut) hadith",
            "impact": "This is a disconnected hadith with missing link(s) in the chain. Even if Abu Dharr heard it from the Prophet ﷺ, we have no way to verify the transmission from Abu Dharr to the compiler."
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Disconnections But All Narrators Are Ok",
    "Topics": [
        "Signs of the Hour - plague in Madinah",
        "Advice of the Prophet ﷺ to Abu Dharr during tribulations",
        "Patience during calamities"
    ]
}

analyzed_hadiths.append(hadith_1)

# ============= HADITH 2 (ID 6392) =============
hadith_2 = {
    "hadith_id": 6392,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1421",
    "english_translation": "Narrated by Abu Dharr: (The Prophet ﷺ said) 'How will you be, O Abu Dharr, when killing comes in Madinah, with blood inundating the stones of Olive?' I said: 'Allah and His Messenger know best.' He said: 'Come to those you belong to.' I asked: 'Shall I wear armor?' He said: 'Then you would be participating with the people.' I said: 'What shall I do, O Messenger of Allah?' He said: 'If you fear the flash of the sword might blind you, then cast your garment over your face so that the sin falls upon him and upon you.'",
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
                    "name": "Abu Dharr",
                    "full_name": "Jundab ibn Junada al-Ghifari",
                    "grade": "Thiqah Thabt",
                    "generation": "Companion",
                    "transmissionTerm": "قَالَ",
                    "reliabilityIssues": [],
                    "narrator_id": None,
                    "alternative_names": "Abu Dharr al-Ghifari",
                    "original_id": None,
                    "kunya": "Abu Dharr",
                    "nisba": "al-Ghifari",
                    "nisba_ar": "الغفاري",
                    "death_year": "32",
                    "birth_year": "",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "Companion",
                    "location": "Madinah/Shaam",
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
            "chainIssues": ["Complete chain missing - only 'قَالَ' (He said) provided without preceding narrators", "Chain type is maqta' (cut off/disconnected)"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Severe chain disconnection",
            "impact": "The chain starts with only 'قَالَ' (He said) with no preceding narrators. The actual compiler is unknown."
        },
        {
            "issue": "Maqta' (Cut) hadith",
            "impact": "This is a disconnected hadith. No way to verify transmission from Abu Dharr to the compiler."
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Disconnections But All Narrators Are Ok",
    "Topics": [
        "Signs of the Hour - slaughter in Madinah",
        "Guidance for Muslims during civil strife",
        "Advice to avoid participation in fitna (tribulation)"
    ]
}

analyzed_hadiths.append(hadith_2)

# ============= HADITH 3 (ID 6393) =============
hadith_3 = {
    "hadith_id": 6393,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1422",
    "english_translation": "Narrated from Tariq through Mundhir al-Thawri: 'Woe to the Arabs from evil that has drawn near! The wings - what are the wings? Woe prolonged in the wings, winds in them blowing, winds stirring their blowing, winds approaching their blowing. Woe to the Arabs after the one hundred and twenty-five years from slaughter that pierces, death that is swift, hunger that is terrible. Calamity will be poured upon them continuously, so their hearts will disbelieve, their joys will be changed, and their veils will be torn. Indeed, by their sins their adversaries will be revealed, their pegs will be pulled out, their ropes will be cut. Woe to Quraysh from a zindiq (heretic) who brings innovations, denies their religion with a word similar to this, and their sanctity will be taken, their walls will be demolished, their armies will be defeated. At that time the mourning women will rise - wailing women - some crying over their religion, some over their worldly life, some from their humiliation after honor, some from hunger of their children, some from slaying of their children in their wombs, some from degradation of their necks, some from violation of their private parts, some from shedding of their blood, some in fear of their armies, some longing for their graves.'",
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
                    "name": "Tariq",
                    "full_name": "Tariq (likely Tariq ibn Shihab al-Baghlani or similar)",
                    "grade": "La Ba'sa Bihi",
                    "generation": "Second-Third Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["indirect_transmission"],
                    "narrator_id": None,
                    "alternative_names": "Tariq",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "",
                    "nisba_ar": "",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "La Ba'sa Bihi",
                    "tabaqat": "Second-Third Generation",
                    "location": "",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Mundhir al-Thawri",
                    "full_name": "Mundhir ibn al-Qasim al-Thawri",
                    "grade": "Saduq",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["indirect_transmission"],
                    "narrator_id": None,
                    "alternative_names": "al-Thawri",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "al-Thawri",
                    "nisba_ar": "الثوري",
                    "death_year": "100",
                    "birth_year": "",
                    "reliability_grade": "Saduq",
                    "tabaqat": "Second Generation",
                    "location": "Kufa",
                    "transmissionTermMeaning": "From (indirect transmission)"
                }
            ],
            "chainIssues": ["First link missing - unknown who narrated from Tariq", "Multiple uses of 'عَنْ' (from) which is indirect transmission term"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain at beginning",
            "impact": "The chain does not start from the collector/compiler. We don't know who recorded this from Tariq, creating a gap in the transmission."
        },
        {
            "issue": "Use of indirect transmission term 'عَنْ'",
            "impact": "Both Tariq and Mundhir al-Thawri use 'عَنْ' (from) which is indirect transmission. While both are relatively reliable narrators, the indirect terms slightly weaken the chain."
        },
        {
            "issue": "Unidentified Tariq",
            "impact": "The narrator 'Tariq' is not clearly identified with sufficient detail to establish his reliability with certainty."
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Disconnections But All Narrators Are Ok",
    "Topics": [
        "Signs of the Hour - tribulations afflicting the Arabs",
        "Description of various calamities and trials",
        "Incident of distress and suffering of Arabs after 125 years",
        "Corruption among Quraysh and rise of heretics"
    ]
}

analyzed_hadiths.append(hadith_3)

# ============= HADITH 4 (ID 6394) =============
hadith_4 = {
    "hadith_id": 6394,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1423",
    "english_translation": "Narrated by Abu Hurayrah: (The Prophet ﷺ said) 'O people! You have been enveloped by tribulations like pieces of dark night. Those saved among the people - or he said from it - is the owner of sheep eating from the produce of his sheep, or a man from beyond the settlement taking hold of the reins of his horse eating from his sword.'",
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
                    "name": "Ibn Khuthayм",
                    "full_name": "Abbad ibn Abi Yazid al-Kufi",
                    "grade": "Saduq",
                    "generation": "Third Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["indirect_transmission"],
                    "narrator_id": 4944,
                    "alternative_names": "Ibn Khuthayм, Abbad ibn Yazid",
                    "original_id": "4126",
                    "kunya": "Ibn Abi Yazid",
                    "nisba": "al-Kufi",
                    "nisba_ar": "الكوفي",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Saduq",
                    "tabaqat": "Third Generation",
                    "location": "Kufa",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Nafi' ibn Sarjis",
                    "full_name": "Muhammad ibn Abdullah ibn al-Harith ibn Nawfal (known as Nafi' ibn Sarjis)",
                    "grade": "Saduq",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["indirect_transmission"],
                    "narrator_id": 7847,
                    "alternative_names": "Nafi' ibn Sarjis, Muhammad ibn Abdullah al-Qurashi",
                    "original_id": "7097",
                    "kunya": "",
                    "nisba": "al-Qurashi",
                    "nisba_ar": "القرشي",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Saduq",
                    "tabaqat": "Second Generation",
                    "location": "Makkah",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Abu Hurayrah",
                    "full_name": "Abd al-Rahman ibn Sakhr al-Dusi",
                    "grade": "Thiqah Thabt",
                    "generation": "Companion",
                    "transmissionTerm": "قَالَ",
                    "reliabilityIssues": [],
                    "narrator_id": 4396,
                    "alternative_names": "Abu Hurayrah al-Dusi",
                    "original_id": "3565",
                    "kunya": "Abu Hurayrah",
                    "nisba": "al-Dusi",
                    "nisba_ar": "الدوسي",
                    "death_year": "59",
                    "birth_year": "",
                    "reliability_grade": "Thiqah Thabt",
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
            "chainIssues": ["First link missing - unknown who narrated from Ibn Khuthayм", "Multiple narrators using indirect transmission term 'عَنْ': Ibn Khuthayм and Nafi' ibn Sarjis"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain at beginning",
            "impact": "The compiler/collector is unknown, creating a disconnection at the beginning of the chain."
        },
        {
            "issue": "Multiple indirect transmission terms",
            "impact": "Both Ibn Khuthayм and Nafi' ibn Sarjis use 'عَنْ' (from), which introduces potential gaps. However, both are classified as Saduq (truthful), and Nafi' ibn Sarjis is from the Second Generation with direct access to the Companion Abu Hurayrah."
        },
        {
            "issue": "Saduq narrators in chain",
            "impact": "While Saduq narrators are generally acceptable, they are not of the highest level of reliability (Thiqah or higher)."
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Disconnections But All Narrators Are Ok",
    "Topics": [
        "Tribulations and trials described as darkness",
        "Who finds salvation during fitna (tribulation)",
        "Types of people who escape tribulations"
    ]
}

analyzed_hadiths.append(hadith_4)

# ============= HADITH 5 (ID 6395) =============
hadith_5 = {
    "hadith_id": 6395,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1424",
    "english_translation": "Narrated from Ziyad ibn Jil through Abu Ka'b al-Harithī (also known as the one with the water vessel): I heard him say: 'I went out searching for my strayed camels, and I took along milk in a water vessel as provisions. Then I said to myself: I have not treated myself fairly - where is the ablution? So I poured out the milk and filled it with water. Then I said: This is ablution and this is drink. Then I stayed...'",
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
                    "name": "Ziyad ibn Jil",
                    "full_name": "Ziyad ibn Jil",
                    "grade": "Majhul al-Hal",
                    "generation": "Third Generation",
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
                    "tabaqat": "Third Generation",
                    "location": "",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Abu Ka'b al-Harithī",
                    "full_name": "Abu Ka'b al-Harithī (the one with the water vessel)",
                    "grade": "Saduq",
                    "generation": "Companion or early generation",
                    "transmissionTerm": "سَمِعْتُهُ",
                    "reliabilityIssues": [],
                    "narrator_id": None,
                    "alternative_names": "Abu Ka'b al-Harithī, Dhu al-Idawah",
                    "original_id": None,
                    "kunya": "Abu Ka'b",
                    "nisba": "al-Harithī",
                    "nisba_ar": "الحارثي",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Saduq",
                    "tabaqat": "Companion/Early Generation",
                    "location": "",
                    "transmissionTermMeaning": "I heard him (direct hearing)"
                }
            ],
            "chainIssues": ["First link missing - unknown who narrated from Ziyad ibn Jil", "Ziyad ibn Jil is of unknown reliability status", "Chain does not reach the Prophet ﷺ - appears to be a companion's statement (mawquf or athar)"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain and unknown narrator",
            "impact": "Ziyad ibn Jil is classified as Majhul al-Hal (of unknown condition), meaning his reliability is not well-documented. The chain begins with an unknown compiler."
        },
        {
            "issue": "Possible mawquf (companion statement) not marfu' (attributed to Prophet)",
            "impact": "The text indicates Abu Ka'b al-Harithī is relating his own experience, not something heard from the Prophet ﷺ. This makes it a companion's statement rather than a hadith from the Prophet ﷺ."
        },
        {
            "issue": "Weak transmission link through unknown narrator",
            "impact": "Ziyad ibn Jil's role in the chain is problematic due to unknown reliability."
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Weak But Might Be Acceptable",
    "Topics": [
        "Practice of wudu (ablution) during travel",
        "Balancing provisions and ablution water",
        "Incident of a companion prioritizing wudu over refreshment"
    ]
}

analyzed_hadiths.append(hadith_5)

# ============= HADITH 6 (ID 6396) =============
hadith_6 = {
    "hadith_id": 6396,
    "book_id": 13,
    "book_name_ar": "كتاب رقم 13",
    "book_name_en": "Book 13 (Unidentified Collection)",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "1425",
    "english_translation": "Narrated from Tariq through Mundhir al-Thawri, from Asim ibn Damrah, from Ali: (Ali said) 'In this Ummah have been placed five tribulations: a general tribulation, then a specific tribulation, then a general tribulation, then a specific tribulation, then comes the blind tribulation that is mute and sealed, in which people become like livestock.'",
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
                    "name": "Tariq",
                    "full_name": "Tariq (likely Tariq ibn Shihab al-Baghlani or similar)",
                    "grade": "La Ba'sa Bihi",
                    "generation": "Second-Third Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["indirect_transmission"],
                    "narrator_id": None,
                    "alternative_names": "Tariq",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "",
                    "nisba_ar": "",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "La Ba'sa Bihi",
                    "tabaqat": "Second-Third Generation",
                    "location": "",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Mundhir al-Thawri",
                    "full_name": "Mundhir ibn al-Qasim al-Thawri",
                    "grade": "Saduq",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["indirect_transmission"],
                    "narrator_id": None,
                    "alternative_names": "al-Thawri",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "al-Thawri",
                    "nisba_ar": "الثوري",
                    "death_year": "100",
                    "birth_year": "",
                    "reliability_grade": "Saduq",
                    "tabaqat": "Second Generation",
                    "location": "Kufa",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Asim ibn Damrah",
                    "full_name": "Asim ibn Damrah",
                    "grade": "Saduq",
                    "generation": "Second Generation",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["indirect_transmission"],
                    "narrator_id": None,
                    "alternative_names": "",
                    "original_id": None,
                    "kunya": "",
                    "nisba": "",
                    "nisba_ar": "",
                    "death_year": "120",
                    "birth_year": "",
                    "reliability_grade": "Saduq",
                    "tabaqat": "Second Generation",
                    "location": "Kufa",
                    "transmissionTermMeaning": "From (indirect transmission)"
                },
                {
                    "name": "Ali",
                    "full_name": "Ali ibn Abi Talib",
                    "grade": "Thiqah Thabt",
                    "generation": "Companion",
                    "transmissionTerm": "قَالَ",
                    "reliabilityIssues": [],
                    "narrator_id": 5722,
                    "alternative_names": "Ali ibn Abi Talib al-Hashimi",
                    "original_id": "unknown",
                    "kunya": "Abu al-Hasan",
                    "nisba": "al-Hashimi",
                    "nisba_ar": "الهاشمي",
                    "death_year": "40",
                    "birth_year": "23 BH",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "Companion",
                    "location": "Kufa/Madinah",
                    "transmissionTermMeaning": "He said"
                }
            ],
            "chainIssues": ["First link missing - unknown who narrated from Tariq", "Three consecutive narrators using indirect transmission term 'عَنْ': Tariq, Mundhir al-Thawri, and Asim ibn Damrah", "Chain terminates at Ali (companion), not reaching the Prophet ﷺ - this is mawquf (companion statement)"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Incomplete chain at beginning",
            "impact": "The compiler is unknown, creating a gap before Tariq."
        },
        {
            "issue": "Multiple indirect transmission terms",
            "impact": "Three consecutive narrators (Tariq, Mundhir al-Thawri, and Asim ibn Damrah) use 'عَنْ' (from). While these are relatively reliable narrators, the multiple indirect transmissions weaken the chain."
        },
        {
            "issue": "Mawquf (companion statement) not marfu' (prophetic hadith)",
            "impact": "This statement is attributed to Ali ibn Abi Talib (a companion), not to the Prophet ﷺ. It is a companion's opinion/statement (mawquf) rather than a hadith from the Prophet."
        },
        {
            "issue": "Unidentified Tariq",
            "impact": "The identity of 'Tariq' is unclear, making assessment of his reliability difficult."
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Acceptable",
    "Topics": [
        "Classification of tribulations (fitnah)",
        "Description of the blind tribulation",
        "Ali ibn Abi Talib's analysis of trials in the Ummah"
    ]
}

analyzed_hadiths.append(hadith_6)

# Save to file
output = {"processed_hadiths": analyzed_hadiths}

with open('/tmp/processed_hadiths_batch_1_chunk_1.json', 'w', encoding='utf-8') as f:
    json.dump(analyzed_hadiths, f, ensure_ascii=False, indent=2)

print("✓ Analysis complete for Chunk 1")
print(f"✓ Generated analysis for {len(analyzed_hadiths)} hadiths")
print("✓ Saved to: /tmp/processed_hadiths_batch_1_chunk_1.json")
