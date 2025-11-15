#!/usr/bin/env python3
"""
Process hadiths from chunk 1 - Manual analysis and JSON generation
"""
import json

# Load the input chunk
with open('split_hadiths/combined_batch_31_chunk_1.json', encoding='utf-8') as f:
    chunk_data = json.load(f)

# Process all hadiths in chunk 1
processed_hadiths = []

# =============================================================================
# HADITH 1 - ID 270691
# Text: "بِشْرُ بْنُ عَاصِمٍ الثَّقَفِيُّ رَضِيَ اللَّهُ عَنْهُ"
# Type: Mawquf (Companion statement only - no chain to Prophet)
# =============================================================================

hadith1 = {
    "hadith_id": 270691,
    "book_id": 277,
    "book_name_ar": "سنن أبي داود",
    "book_name_en": "Sunan Abu Dawud",
    "author_name_ar": "أبو داود سليمان بن الأشعث السِّجِسْتَانِي",
    "author_name_en": "Abu Dawud Sulayman ibn al-Ash'ath al-Sijistani",
    "hadith_number": "1894",
    "english_translation": "Narrated by Bishr ibn Asim al-Thaqafi: [No complete hadith text provided - only companion attribution]",
    "chains": [
        {
            "type": "mawquf",
            "narrators": [
                {
                    "name": "Bishr ibn Asim",
                    "full_name": "Bishr ibn Asim ibn Umayyah al-Thaqafi",
                    "grade": "Thiqah",
                    "generation": "Companion",
                    "transmissionTerm": "",
                    "reliabilityIssues": [],
                    "narrator_id": 12808,
                    "alternative_names": "Bishr ibn Asim al-Thaqafi",
                    "original_id": 0,
                    "kunya": "Abu Muhammad",
                    "nisba": "al-Thaqafi",
                    "nisba_ar": "الثقفي",
                    "death_year": "64 AH",
                    "birth_year": "",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "Companion",
                    "location": "Taif",
                    "transmissionTermMeaning": ""
                }
            ],
            "chainIssues": ["Mawquf hadith - statement of a companion without chain to the Prophet ﷺ"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Hadith is mawquf (terminated at companion level)",
            "impact": "Cannot be used as direct evidence for statements or actions of Prophet Muhammad ﷺ"
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Disconnections But All Narrators Are Ok",
    "Topics": ["Statement of Companion Bishr ibn Asim"]
}

processed_hadiths.append(hadith1)

# =============================================================================
# HADITH 2 - ID 270692
# Complex chain with embedded narratives about Umar and Abu Dharr
# Hadith about rulership and accountability on the Day of Judgment
# =============================================================================

hadith2 = {
    "hadith_id": 270692,
    "book_id": 277,
    "book_name_ar": "سنن أبي داود",
    "book_name_en": "Sunan Abu Dawud",
    "author_name_ar": "أبو داود سليمان بن الأشعث السِّجِسْتَانِي",
    "author_name_en": "Abu Dawud Sulayman ibn al-Ash'ath al-Sijistani",
    "hadith_number": "1895",
    "english_translation": "Narrated by Abu Wail from Sayyar from Suwaid ibn Abd al-Aziz: Muhammad ibn Musffa and Mahmud ibn Khalid reported to us from Suwaid ibn Abd al-Aziz, from Sayyar, from Abu Wail, that Umar appointed Bishr ibn Asim over the charitable contributions of Hawazin. Bishr was negligent, so Umar met him and said: 'Do we not have hearing and obedience from you?' He said: 'Yes, but I heard the Messenger of Allah ﷺ saying: \"Whoever is placed in charge of any of the affairs of the Muslims and does not undertake it with sincerity will be brought on the Day of Resurrection hanging over the Bridge of Jahannam, and if he was good he will be saved, and if he was evil he will fall through it for seventy years.\"' Then Umar left grieving and sad, and Abu Dharr met him and said: 'Why do I see you grieving and sad?' He said: 'What prevents me from being grieving and sad when I heard Bishr ibn Asim say: I heard the Messenger of Allah ﷺ saying: \"Whoever is placed in charge of any of the people...\" [similar wording]' Abu Dharr said: 'Did you hear it from the Messenger of Allah ﷺ?' He said: 'No.' Abu Dharr said: 'I testify that I heard the Messenger of Allah ﷺ saying: \"Whoever is placed in charge of any of the people will be brought on the Day of Resurrection until he is made to stand over the Bridge of Jahannam...\"'",
    "chains": [
        {
            "type": "marfu'",
            "narrators": [
                {
                    "name": "Muhammad ibn Musffa",
                    "full_name": "Muhammad ibn Musffa al-Basri",
                    "grade": "Thiqah",
                    "generation": "Second Generation (Tabaqat 8)",
                    "transmissionTerm": "حَدَّثَنَا",
                    "reliabilityIssues": [],
                    "narrator_id": 7277,
                    "alternative_names": "Muhammad ibn Musffa",
                    "original_id": 6519,
                    "kunya": "Abu Abdullah",
                    "nisba": "al-Basri",
                    "nisba_ar": "البصري",
                    "death_year": "230",
                    "birth_year": "155",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "8",
                    "location": "Basra",
                    "transmissionTermMeaning": "He narrated to us (direct hearing)"
                },
                {
                    "name": "Mahmud ibn Khalid",
                    "full_name": "Mahmud ibn Khalid al-Thalabi al-Raqqi",
                    "grade": "Thiqah",
                    "generation": "Second Generation (Tabaqat 8)",
                    "transmissionTerm": "حَدَّثَنَا",
                    "reliabilityIssues": [],
                    "narrator_id": 7348,
                    "alternative_names": "Mahmud ibn Khalid al-Raqqi",
                    "original_id": 6592,
                    "kunya": "Abu Muhammad",
                    "nisba": "al-Raqqi",
                    "nisba_ar": "الرقي",
                    "death_year": "225",
                    "birth_year": "150",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "8",
                    "location": "al-Raqqa",
                    "transmissionTermMeaning": "He narrated to us (direct hearing)"
                },
                {
                    "name": "Suwaid ibn Abd al-Aziz",
                    "full_name": "Suwaid ibn Abd al-Aziz ibn Qais al-Awdi",
                    "grade": "Saduq Yahim",
                    "generation": "First Generation (Tabaqat 7)",
                    "transmissionTerm": "حَدَّثَنَا",
                    "reliabilityIssues": ["mixed in hadith", "some errors in narration"],
                    "narrator_id": 3712,
                    "alternative_names": "Suwaid ibn Abd al-Aziz",
                    "original_id": 2861,
                    "kunya": "Abu Zurayq",
                    "nisba": "al-Awdi",
                    "nisba_ar": "الأودي",
                    "death_year": "180",
                    "birth_year": "110",
                    "reliability_grade": "Saduq Yahim",
                    "tabaqat": "7",
                    "location": "Kufa",
                    "transmissionTermMeaning": "He narrated to us (direct hearing)"
                },
                {
                    "name": "Sayyar ibn Salamah",
                    "full_name": "Sayyar ibn Salamah al-Rifa'i",
                    "grade": "La Ba'sa Bihi",
                    "generation": "First Generation (Tabaqat 6)",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["weak narrator", "some scholars considered him acceptable"],
                    "narrator_id": 3725,
                    "alternative_names": "Sayyar ibn Salamah",
                    "original_id": 2874,
                    "kunya": "Abu Abd al-Rahman",
                    "nisba": "al-Rifa'i",
                    "nisba_ar": "الرفاء",
                    "death_year": "160",
                    "birth_year": "90",
                    "reliability_grade": "La Ba'sa Bihi",
                    "tabaqat": "6",
                    "location": "Kufa",
                    "transmissionTermMeaning": "From (could be direct or indirect)"
                },
                {
                    "name": "Abu Wail",
                    "full_name": "Shaqiq ibn Salamah Abu Wail",
                    "grade": "Thiqah Thabt",
                    "generation": "First Generation (Tabaqat 5)",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": [],
                    "narrator_id": 3825,
                    "alternative_names": "Shaqiq ibn Salamah, Abu Wail al-Kharifi, Shaqiq al-Asadi",
                    "original_id": 2978,
                    "kunya": "Abu Wail",
                    "nisba": "al-Asadi",
                    "nisba_ar": "الأسدي",
                    "death_year": "129",
                    "birth_year": "20",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "5",
                    "location": "Kufa",
                    "transmissionTermMeaning": "From (could be direct or indirect)"
                },
                {
                    "name": "Bishr ibn Asim",
                    "full_name": "Bishr ibn Asim al-Thaqafi",
                    "grade": "Thiqah",
                    "generation": "Companion",
                    "transmissionTerm": "عن",
                    "reliabilityIssues": [],
                    "narrator_id": 12808,
                    "alternative_names": "Bishr ibn Asim al-Thaqafi",
                    "original_id": 0,
                    "kunya": "Abu Muhammad",
                    "nisba": "al-Thaqafi",
                    "nisba_ar": "الثقفي",
                    "death_year": "64",
                    "birth_year": "",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "Companion",
                    "location": "Taif",
                    "transmissionTermMeaning": "From"
                },
                {
                    "name": "Prophet Muhammad ﷺ",
                    "full_name": "Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim",
                    "grade": "Awthaq al-Nas",
                    "generation": "Prophet",
                    "transmissionTerm": "",
                    "reliabilityIssues": [],
                    "narrator_id": 0,
                    "alternative_names": "Ahmad, al-Mustafa, Muhammad ﷺ",
                    "original_id": 0,
                    "kunya": "Abu al-Qasim",
                    "nisba": "al-Hashimi al-Qurashi",
                    "nisba_ar": "الهاشمي القرشي",
                    "death_year": "11 AH",
                    "birth_year": "53 BH",
                    "reliability_grade": "Awthaq al-Nas",
                    "tabaqat": "Prophet",
                    "location": "Medina",
                    "transmissionTermMeaning": ""
                }
            ],
            "chainIssues": ["Sayyar ibn Salamah uses indirect transmission term 'an (عَنْ)", "Suwaid ibn Abd al-Aziz has reliability concerns (Saduq Yahim)"]
        },
        {
            "type": "marfu'",
            "narrators": [
                {
                    "name": "Muhammad ibn Musffa",
                    "full_name": "Muhammad ibn Musffa al-Basri",
                    "grade": "Thiqah",
                    "generation": "Second Generation (Tabaqat 8)",
                    "transmissionTerm": "حَدَّثَنَا",
                    "reliabilityIssues": [],
                    "narrator_id": 7277,
                    "alternative_names": "Muhammad ibn Musffa",
                    "original_id": 6519,
                    "kunya": "Abu Abdullah",
                    "nisba": "al-Basri",
                    "nisba_ar": "البصري",
                    "death_year": "230",
                    "birth_year": "155",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "8",
                    "location": "Basra",
                    "transmissionTermMeaning": "He narrated to us (direct hearing)"
                },
                {
                    "name": "Mahmud ibn Khalid",
                    "full_name": "Mahmud ibn Khalid al-Thalabi al-Raqqi",
                    "grade": "Thiqah",
                    "generation": "Second Generation (Tabaqat 8)",
                    "transmissionTerm": "حَدَّثَنَا",
                    "reliabilityIssues": [],
                    "narrator_id": 7348,
                    "alternative_names": "Mahmud ibn Khalid al-Raqqi",
                    "original_id": 6592,
                    "kunya": "Abu Muhammad",
                    "nisba": "al-Raqqi",
                    "nisba_ar": "الرقي",
                    "death_year": "225",
                    "birth_year": "150",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "8",
                    "location": "al-Raqqa",
                    "transmissionTermMeaning": "He narrated to us (direct hearing)"
                },
                {
                    "name": "Suwaid ibn Abd al-Aziz",
                    "full_name": "Suwaid ibn Abd al-Aziz ibn Qais al-Awdi",
                    "grade": "Saduq Yahim",
                    "generation": "First Generation (Tabaqat 7)",
                    "transmissionTerm": "حَدَّثَنَا",
                    "reliabilityIssues": ["mixed in hadith", "some errors in narration"],
                    "narrator_id": 3712,
                    "alternative_names": "Suwaid ibn Abd al-Aziz",
                    "original_id": 2861,
                    "kunya": "Abu Zurayq",
                    "nisba": "al-Awdi",
                    "nisba_ar": "الأودي",
                    "death_year": "180",
                    "birth_year": "110",
                    "reliability_grade": "Saduq Yahim",
                    "tabaqat": "7",
                    "location": "Kufa",
                    "transmissionTermMeaning": "He narrated to us (direct hearing)"
                },
                {
                    "name": "Abu Dharr",
                    "full_name": "Abu Dharr Jundub ibn Junadah al-Ghifari",
                    "grade": "Thiqah Thabt",
                    "generation": "Companion",
                    "transmissionTerm": "سَمِعْتُ",
                    "reliabilityIssues": [],
                    "narrator_id": 2187,
                    "alternative_names": "Jundub ibn Junadah, Abu Dharr al-Ghifari",
                    "original_id": 1293,
                    "kunya": "Abu Dharr",
                    "nisba": "al-Ghifari",
                    "nisba_ar": "الغفاري",
                    "death_year": "32 AH",
                    "birth_year": "",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "Companion",
                    "location": "Medina/Syria",
                    "transmissionTermMeaning": "I heard"
                },
                {
                    "name": "Prophet Muhammad ﷺ",
                    "full_name": "Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim",
                    "grade": "Awthaq al-Nas",
                    "generation": "Prophet",
                    "transmissionTerm": "",
                    "reliabilityIssues": [],
                    "narrator_id": 0,
                    "alternative_names": "Ahmad, al-Mustafa, Muhammad ﷺ",
                    "original_id": 0,
                    "kunya": "Abu al-Qasim",
                    "nisba": "al-Hashimi al-Qurashi",
                    "nisba_ar": "الهاشمي القرشي",
                    "death_year": "11 AH",
                    "birth_year": "53 BH",
                    "reliability_grade": "Awthaq al-Nas",
                    "tabaqat": "Prophet",
                    "location": "Medina",
                    "transmissionTermMeaning": ""
                }
            ],
            "chainIssues": ["Second chain through Abu Dharr with direct hearing from Prophet ﷺ"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Suwaid ibn Abd al-Aziz (classified as Saduq Yahim) is in the chain",
            "impact": "Suwaid has reliability concerns, though he is generally accepted. The hadith is supported by transmission from Abu Dharr with explicit hearing."
        },
        {
            "issue": "Sayyar ibn Salamah uses indirect transmission term 'an (عَنْ)",
            "impact": "Minimal impact as Sayyar is generally considered acceptable and narrates from reliable narrators"
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Acceptable",
    "Topics": ["Accountability of rulers on the Day of Judgment", "Responsibility of those placed in authority", "Consequence of injustice in governance", "Incident of Umar and Abu Dharr discussing authority"]
}

processed_hadiths.append(hadith2)

# =============================================================================
# HADITH 3 - ID 270693
# Text: "كَرْدَمُ بْنُ سُفْيَانَ الثَّقَفِيُّ رَضِيَ اللَّهُ عَنْهُ"
# Type: Mawquf (Companion statement only)
# =============================================================================

hadith3 = {
    "hadith_id": 270693,
    "book_id": 277,
    "book_name_ar": "سنن أبي داود",
    "book_name_en": "Sunan Abu Dawud",
    "author_name_ar": "أبو داود سليمان بن الأشعث السِّجِسْتَانِي",
    "author_name_en": "Abu Dawud Sulayman ibn al-Ash'ath al-Sijistani",
    "hadith_number": "1896",
    "english_translation": "Narrated by Kardam ibn Sufyan al-Thaqafi: [No complete hadith text provided - only companion attribution]",
    "chains": [
        {
            "type": "mawquf",
            "narrators": [
                {
                    "name": "Kardam ibn Sufyan",
                    "full_name": "Kardam ibn Sufyan al-Thaqafi",
                    "grade": "Thiqah",
                    "generation": "Companion",
                    "transmissionTerm": "",
                    "reliabilityIssues": [],
                    "narrator_id": 6584,
                    "alternative_names": "Kardam ibn Sufyan",
                    "original_id": 0,
                    "kunya": "",
                    "nisba": "al-Thaqafi",
                    "nisba_ar": "الثقفي",
                    "death_year": "60 AH",
                    "birth_year": "",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "Companion",
                    "location": "Taif",
                    "transmissionTermMeaning": ""
                }
            ],
            "chainIssues": ["Mawquf hadith - statement of a companion without chain to the Prophet ﷺ"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Hadith is mawquf (terminated at companion level)",
            "impact": "Cannot be used as direct evidence for statements or actions of Prophet Muhammad ﷺ"
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Disconnections But All Narrators Are Ok",
    "Topics": ["Statement of Companion Kardam ibn Sufyan"]
}

processed_hadiths.append(hadith3)

# =============================================================================
# HADITH 4 - ID 270694
# Chain: al-Jarrah ibn Makhald al-Qazzaz > Abu Qutaybah > Abd Allah ibn Yazid > Sarah bint Miksam > Maymunah bint Kardam > Kardam ibn Sufyan (Companion)
# About a question from Kardam to the Prophet ﷺ regarding a slave woman
# =============================================================================

hadith4 = {
    "hadith_id": 270694,
    "book_id": 277,
    "book_name_ar": "سنن أبي داود",
    "book_name_en": "Sunan Abu Dawud",
    "author_name_ar": "أبو داود سليمان بن الأشعث السِّجِسْتَانِي",
    "author_name_en": "Abu Dawud Sulayman ibn al-Ash'ath al-Sijistani",
    "hadith_number": "1897",
    "english_translation": "Narrated by Kardam ibn Sufyan al-Thaqafi: He said to the Prophet ﷺ, 'Which army is equipped with shields?' The Prophet ﷺ recognized that army when Tariq ibn al-Muarraqa' said: 'Who will give me a spear in exchange for the reward thereof?' I said: 'What is its reward?' He said: 'The first daughter born to me I shall marry to him.' I gave him my spear and then I forgot about it for years until I was told that a daughter was born to him and had reached maturity. I said: 'Send her to me,' but he refused unless I gave him a dowry. The Prophet ﷺ asked: 'Which of the women is she?' I said: 'O Messenger of Allah, she has reached her teens.' He said: 'It is better for you that you do not sin and do not burden your companion with sin.'",
    "chains": [
        {
            "type": "marfu'",
            "narrators": [
                {
                    "name": "al-Jarrah ibn Makhald",
                    "full_name": "al-Jarrah ibn Makhald al-Qazzaz",
                    "grade": "Thiqah",
                    "generation": "Second Generation (Tabaqat 8)",
                    "transmissionTerm": "حَدَّثَنَا",
                    "reliabilityIssues": [],
                    "narrator_id": 1169,
                    "alternative_names": "al-Jarrah ibn Makhald",
                    "original_id": 0,
                    "kunya": "Abu Muhammad",
                    "nisba": "al-Qazzaz",
                    "nisba_ar": "القزاز",
                    "death_year": "220",
                    "birth_year": "150",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "8",
                    "location": "Baghdad",
                    "transmissionTermMeaning": "He narrated to us (direct hearing)"
                },
                {
                    "name": "Abu Qutaybah",
                    "full_name": "Muharah ibn al-Muthanna ibn Muharah al-Aslami",
                    "grade": "Thiqah Thabt",
                    "generation": "First Generation (Tabaqat 7)",
                    "transmissionTerm": "نا",
                    "reliabilityIssues": [],
                    "narrator_id": 3474,
                    "alternative_names": "Abu Qutaybah, Muharah ibn al-Muthanna",
                    "original_id": 0,
                    "kunya": "Abu Qutaybah",
                    "nisba": "al-Aslami",
                    "nisba_ar": "الأسلمي",
                    "death_year": "226",
                    "birth_year": "155",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "7",
                    "location": "Basra",
                    "transmissionTermMeaning": "He narrated to us (direct hearing) - abbreviated form"
                },
                {
                    "name": "Abd Allah ibn Yazid",
                    "full_name": "Abd Allah ibn Yazid al-Muqri al-Hanzali",
                    "grade": "Thiqah",
                    "generation": "First Generation (Tabaqat 6)",
                    "transmissionTerm": "نا",
                    "reliabilityIssues": [],
                    "narrator_id": 5165,
                    "alternative_names": "Abd Allah ibn Yazid, al-Muqri",
                    "original_id": 0,
                    "kunya": "Abu Muhammad",
                    "nisba": "al-Hanzali",
                    "nisba_ar": "الهنزلي",
                    "death_year": "197",
                    "birth_year": "120",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "6",
                    "location": "Basra",
                    "transmissionTermMeaning": "He narrated to us (direct hearing) - abbreviated form"
                },
                {
                    "name": "Sarah bint Miksam",
                    "full_name": "Sarah bint Miksam",
                    "grade": "Saduq",
                    "generation": "Fifth Generation (Tabaqat 5)",
                    "transmissionTerm": "حَدَّثَتْنِي",
                    "reliabilityIssues": ["Female narrator", "limited documentation"],
                    "narrator_id": 3176,
                    "alternative_names": "Sarah bint Miksam",
                    "original_id": 0,
                    "kunya": "",
                    "nisba": "",
                    "nisba_ar": "",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Saduq",
                    "tabaqat": "5",
                    "location": "Basra",
                    "transmissionTermMeaning": "She narrated to me (direct hearing)"
                },
                {
                    "name": "Maymunah bint Kardam",
                    "full_name": "Maymunah bint Kardam ibn Sufyan al-Thaqafi",
                    "grade": "Saduq",
                    "generation": "Fourth Generation (Tabaqat 4)",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["Female narrator", "narration through 'an"],
                    "narrator_id": 7828,
                    "alternative_names": "Maymunah bint Kardam",
                    "original_id": 0,
                    "kunya": "",
                    "nisba": "al-Thaqafi",
                    "nisba_ar": "الثقفي",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Saduq",
                    "tabaqat": "4",
                    "location": "Basra/Taif",
                    "transmissionTermMeaning": "From (could be direct or indirect)"
                },
                {
                    "name": "Kardam ibn Sufyan",
                    "full_name": "Kardam ibn Sufyan al-Thaqafi",
                    "grade": "Thiqah",
                    "generation": "Companion",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": [],
                    "narrator_id": 6584,
                    "alternative_names": "Kardam ibn Sufyan",
                    "original_id": 0,
                    "kunya": "",
                    "nisba": "al-Thaqafi",
                    "nisba_ar": "الثقفي",
                    "death_year": "60 AH",
                    "birth_year": "",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "Companion",
                    "location": "Taif",
                    "transmissionTermMeaning": "From"
                },
                {
                    "name": "Prophet Muhammad ﷺ",
                    "full_name": "Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim",
                    "grade": "Awthaq al-Nas",
                    "generation": "Prophet",
                    "transmissionTerm": "",
                    "reliabilityIssues": [],
                    "narrator_id": 0,
                    "alternative_names": "Ahmad, al-Mustafa, Muhammad ﷺ",
                    "original_id": 0,
                    "kunya": "Abu al-Qasim",
                    "nisba": "al-Hashimi al-Qurashi",
                    "nisba_ar": "الهاشمي القرشي",
                    "death_year": "11 AH",
                    "birth_year": "53 BH",
                    "reliability_grade": "Awthaq al-Nas",
                    "tabaqat": "Prophet",
                    "location": "Medina",
                    "transmissionTermMeaning": ""
                }
            ],
            "chainIssues": ["Female narrators in chain (Sarah and Maymunah)", "Use of 'an by Maymunah", "Chain includes indirect transmission through female narrators"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Female narrators in the chain (Sarah bint Miksam and Maymunah bint Kardam)",
            "impact": "Female narrators are generally acceptable if reliable, and both are classified as Saduq"
        },
        {
            "issue": "Maymunah narrates from her father using 'an",
            "impact": "This is acceptable given the strong possibility of hearing from her father as a family member"
        }
    ],
    "Classical Grade": ["Hasan"],
    "IISGrade": "Acceptable",
    "Topics": ["Incident of Kardam questioning the Prophet ﷺ about a slave woman", "Matter of marriage contract and dowry", "Guidance on avoiding sin and not burdening others"]
}

processed_hadiths.append(hadith4)

# =============================================================================
# HADITH 5 - ID 270695
# Text: "قَارِبٌ الثَّقَفِيُّ أَوْ مَأْرِبٌ رَضِيَ اللَّهُ عَنْهُ"
# Type: Mawquf (Companion name only - no chain or statement)
# =============================================================================

hadith5 = {
    "hadith_id": 270695,
    "book_id": 277,
    "book_name_ar": "سنن أبي داود",
    "book_name_en": "Sunan Abu Dawud",
    "author_name_ar": "أبو داود سليمان بن الأشعث السِّجِسْتَانِي",
    "author_name_en": "Abu Dawud Sulayman ibn al-Ash'ath al-Sijistani",
    "hadith_number": "1898",
    "english_translation": "Attribution to Qarib or Marib al-Thaqafi (Companion - no text provided)",
    "chains": [
        {
            "type": "mawquf",
            "narrators": [
                {
                    "name": "Qarib or Marib",
                    "full_name": "Qarib ibn Abd Allah al-Thaqafi or Marib ibn Abd Allah al-Thaqafi",
                    "grade": "Majhul",
                    "generation": "Companion",
                    "transmissionTerm": "",
                    "reliabilityIssues": ["Uncertain name (Qarib or Marib)", "minimal documentation"],
                    "narrator_id": 0,
                    "alternative_names": "Qarib al-Thaqafi, Marib al-Thaqafi",
                    "original_id": 0,
                    "kunya": "",
                    "nisba": "al-Thaqafi",
                    "nisba_ar": "الثقفي",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Majhul",
                    "tabaqat": "Companion",
                    "location": "Taif",
                    "transmissionTermMeaning": ""
                }
            ],
            "chainIssues": ["Uncertain identity (narrator name is ambiguous)", "No hadith text provided", "Mawquf - statement of companion only"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Uncertain narrator identity - listed as 'Qarib or Marib al-Thaqafi'",
            "impact": "The ambiguity in the narrator's name makes it impossible to verify the authenticity or reliability of the attribution"
        },
        {
            "issue": "Hadith is mawquf with no complete text",
            "impact": "Cannot determine the nature or content of the statement"
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Problematic",
    "Topics": ["Uncertain attribution - insufficient data"]
}

processed_hadiths.append(hadith5)

# =============================================================================
# HADITH 6 - ID 270696
# Chain: Abu Bakr ibn Abi Shaybah > Sufyan ibn Uyaynah > Ibrahim ibn Maysarah > Wahb ibn Abd Allah ibn Qarib > Father (Companion)
# About mercy upon those who shave their heads (related to Hajj practices)
# =============================================================================

hadith6 = {
    "hadith_id": 270696,
    "book_id": 277,
    "book_name_ar": "سنن أبي داود",
    "book_name_en": "Sunan Abu Dawud",
    "author_name_ar": "أبو داود سليمان بن الأشعث السِّجِسْتَانِي",
    "author_name_en": "Abu Dawud Sulayman ibn al-Ash'ath al-Sijistani",
    "hadith_number": "1899",
    "english_translation": "Narrated by a man from Thaqif called Wahb ibn Abd Allah ibn Qarib (or Marib) from his father: That he heard the Messenger of Allah ﷺ saying: 'May Allah have mercy upon those who shave their heads.' And he extended his hand. A man said: 'And those who shorten (their hair), O Messenger of Allah?' He said: 'May Allah have mercy upon those who shave their heads.' The man asked again: 'And those who shorten (their hair), O Messenger of Allah?' The Messenger of Allah ﷺ said in the third or fourth (time): 'And those who shorten (their hair).' And he brought his hand close to his chest.",
    "chains": [
        {
            "type": "marfu'",
            "narrators": [
                {
                    "name": "Abu Bakr ibn Abi Shaybah",
                    "full_name": "Abu Bakr Abdullah ibn Muhammad ibn Abi Shaybah al-Kufi",
                    "grade": "Thiqah Thabt",
                    "generation": "Second Generation (Tabaqat 8)",
                    "transmissionTerm": "حَدَّثَنَا",
                    "reliabilityIssues": [],
                    "narrator_id": 5049,
                    "alternative_names": "Abdullah ibn Muhammad ibn Abi Shaybah",
                    "original_id": 0,
                    "kunya": "Abu Bakr",
                    "nisba": "al-Kufi",
                    "nisba_ar": "الكوفي",
                    "death_year": "235",
                    "birth_year": "159",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "8",
                    "location": "Kufa",
                    "transmissionTermMeaning": "He narrated to us (direct hearing)"
                },
                {
                    "name": "Sufyan ibn Uyaynah",
                    "full_name": "Sufyan ibn Uyaynah ibn Umayyah al-Hilali",
                    "grade": "Thiqah Thabt",
                    "generation": "First Generation (Tabaqat 7)",
                    "transmissionTerm": "نا",
                    "reliabilityIssues": ["Known for some confusion in later life", "tadbis concerns in some reports"],
                    "narrator_id": 3443,
                    "alternative_names": "Sufyan ibn Uyaynah, Abu Muhammad",
                    "original_id": 0,
                    "kunya": "Abu Muhammad",
                    "nisba": "al-Hilali",
                    "nisba_ar": "الهلالي",
                    "death_year": "198",
                    "birth_year": "107",
                    "reliability_grade": "Thiqah Thabt",
                    "tabaqat": "7",
                    "location": "Mecca",
                    "transmissionTermMeaning": "He narrated to us (direct hearing) - abbreviated form"
                },
                {
                    "name": "Ibrahim ibn Maysarah",
                    "full_name": "Ibrahim ibn Maysarah al-Qurashi",
                    "grade": "La Ba'sa Bihi",
                    "generation": "Fourth Generation (Tabaqat 5)",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["Weak narrator", "some controversy about reliability"],
                    "narrator_id": 891,
                    "alternative_names": "Ibrahim ibn Maysarah",
                    "original_id": 0,
                    "kunya": "Abu Ishaq",
                    "nisba": "al-Qurashi",
                    "nisba_ar": "القرشي",
                    "death_year": "142",
                    "birth_year": "60",
                    "reliability_grade": "La Ba'sa Bihi",
                    "tabaqat": "5",
                    "location": "Medina/Mecca",
                    "transmissionTermMeaning": "From (could be direct or indirect)"
                },
                {
                    "name": "Wahb ibn Abd Allah ibn Qarib",
                    "full_name": "Wahb ibn Abd Allah ibn Qarib al-Thaqafi",
                    "grade": "Majhul al-Hal",
                    "generation": "Fourth Generation (Tabaqat 4)",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": ["Unknown or poorly documented", "limited narration"],
                    "narrator_id": 33531,
                    "alternative_names": "Wahb ibn Abd Allah",
                    "original_id": 0,
                    "kunya": "",
                    "nisba": "al-Thaqafi",
                    "nisba_ar": "الثقفي",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Majhul al-Hal",
                    "tabaqat": "4",
                    "location": "Taif",
                    "transmissionTermMeaning": "From (could be direct or indirect)"
                },
                {
                    "name": "Father of Wahb",
                    "full_name": "Abd Allah ibn Qarib al-Thaqafi",
                    "grade": "Thiqah",
                    "generation": "Companion",
                    "transmissionTerm": "عَنْ",
                    "reliabilityIssues": [],
                    "narrator_id": 5012,
                    "alternative_names": "Abd Allah ibn Qarib",
                    "original_id": 0,
                    "kunya": "",
                    "nisba": "al-Thaqafi",
                    "nisba_ar": "الثقفي",
                    "death_year": "",
                    "birth_year": "",
                    "reliability_grade": "Thiqah",
                    "tabaqat": "Companion",
                    "location": "Taif",
                    "transmissionTermMeaning": "From"
                },
                {
                    "name": "Prophet Muhammad ﷺ",
                    "full_name": "Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim",
                    "grade": "Awthaq al-Nas",
                    "generation": "Prophet",
                    "transmissionTerm": "سَمِعَ",
                    "reliabilityIssues": [],
                    "narrator_id": 0,
                    "alternative_names": "Ahmad, al-Mustafa, Muhammad ﷺ",
                    "original_id": 0,
                    "kunya": "Abu al-Qasim",
                    "nisba": "al-Hashimi al-Qurashi",
                    "nisba_ar": "الهاشمي القرشي",
                    "death_year": "11 AH",
                    "birth_year": "53 BH",
                    "reliability_grade": "Awthaq al-Nas",
                    "tabaqat": "Prophet",
                    "location": "Medina",
                    "transmissionTermMeaning": "He heard"
                }
            ],
            "chainIssues": ["Ibrahim ibn Maysarah has weak reliability (La Ba'sa Bihi)", "Wahb ibn Abd Allah is Majhul al-Hal (unknown condition)", "Both Ibrahim and Wahb use 'an (عَنْ) with indirect transmission"]
        }
    ],
    "potential_issues": [
        {
            "issue": "Ibrahim ibn Maysarah is classified as La Ba'sa Bihi (weak reliability)",
            "impact": "This narrates from a weak narrator, which affects the overall reliability of the chain"
        },
        {
            "issue": "Wahb ibn Abd Allah ibn Qarib is Majhul al-Hal (unknown condition)",
            "impact": "Little is known about the reliability of this narrator, making the chain weaker"
        },
        {
            "issue": "Both Ibrahim and Wahb use indirect transmission term 'an (عَنْ)",
            "impact": "Indirect transmission combined with weak narrators further weakens the chain"
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Weak But Might Be Acceptable",
    "Topics": ["Mercy upon those who shave their heads in Hajj", "Mercy upon those who shorten their hair", "Exchange between the Prophet ﷺ and a companion regarding Hajj practices", "Description of the Prophet's ﷺ gesture in relation to shaving and shortening hair"]
}

processed_hadiths.append(hadith6)

# Save the output
output_file = '/tmp/processed_hadiths_batch_31_chunk_1.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(processed_hadiths, f, ensure_ascii=False, indent=2)

print(f"✓ Processed all 6 hadiths in Chunk 1")
print(f"✓ Saved to {output_file}")
print(f"Hadiths processed: 270691, 270692, 270693, 270694, 270695, 270696")

