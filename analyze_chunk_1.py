#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
from typing import Dict, List, Tuple

# Read chunk 1
with open('split_hadiths/combined_batch_31_chunk_1.json', 'r', encoding='utf-8') as f:
    chunk_data = json.load(f)

def get_book_info(hadith_data: Dict) -> Tuple[str, str, str, str]:
    """Extract book information"""
    book = hadith_data.get('book', {})
    return (
        book.get('book_id', 277),
        book.get('book_name_ar', 'كتاب رقم 277'),
        'Unknown Collection',  # English name not available
        book.get('author_name', 'Unknown Author')
    )

def create_narrator(
    name: str,
    full_name: str,
    grade: str,
    generation: str,
    transmission_term: str,
    narrator_id: int,
    kunya: str = "",
    nisba: str = "",
    nisba_ar: str = "",
    death_year: str = "",
    birth_year: str = "",
    reliability_issues: List[str] = None,
    alternative_names: str = ""
) -> Dict:
    """Create a narrator object matching the schema"""
    if reliability_issues is None:
        reliability_issues = []

    return {
        "name": name,
        "full_name": full_name,
        "grade": grade,
        "generation": generation,
        "transmissionTerm": transmission_term,
        "reliabilityIssues": reliability_issues,
        "narrator_id": narrator_id,
        "alternative_names": alternative_names,
        "original_id": narrator_id,
        "kunya": kunya,
        "nisba": nisba,
        "nisba_ar": nisba_ar,
        "death_year": death_year,
        "birth_year": birth_year,
        "reliability_grade": grade,
        "tabaqat": generation,
        "location": "",
        "transmissionTermMeaning": get_transmission_meaning(transmission_term)
    }

def get_transmission_meaning(term: str) -> str:
    """Get English meaning of transmission term"""
    meanings = {
        "حَدَّثَنَا": "He narrated to us (direct hearing)",
        "نا": "He narrated to us (direct hearing)",
        "أَخْبَرَنَا": "He informed us (direct hearing)",
        "عَنْ": "From (could be direct or indirect)",
        "قَالَ": "He said",
        "سَمِعْتُ": "I heard",
        "": ""
    }
    return meanings.get(term, term)

# ============================================================================
# HADITH 1: About the slave given sword at Khaybar
# ============================================================================

h1_output = {
    "hadith_id": 272191,
    "book_id": 277,
    "book_name_ar": "كتاب رقم 277",
    "book_name_en": "Unknown Hadith Collection",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "3394",
    "english_translation": "Narrated by Umayr (the slave): I attended with my masters at Khaybar, and the Messenger of Allah ﷺ commanded me, so I girded myself with a sword. Then behold, I was dragging it, and I informed him that I was a slave. So he commanded for me something from the spoils of war.",
    "chains": [
        {
            "type": "marfu'",
            "narrators": [
                create_narrator(
                    "Muhammad ibn al-Muthanna",
                    "Muhammad ibn al-Muthanna ibn al-Qasim Abu Abdillah al-Abdi al-Basri",
                    "Thiqah Thabt",
                    "Ninth Generation",
                    "حَدَّثَنَا",
                    6861,
                    kunya="Abu Abdillah",
                    nisba="al-Abdi",
                    nisba_ar="العبدي",
                    death_year="252",
                    birth_year="167",
                    alternative_names="Bundar, Qattan"
                ),
                create_narrator(
                    "Riba'i ibn Uliyyah",
                    "Riba'i ibn Uliyyah ibn Umayyah al-Ataki Abu al-Nida al-Basri",
                    "Thiqah Thabt",
                    "Eighth Generation",
                    "نا",
                    2880,
                    kunya="Abu al-Nida",
                    nisba="al-Ataki",
                    nisba_ar="العتكي",
                    death_year="193",
                    birth_year="127",
                    alternative_names="Riba'i al-Ataki"
                ),
                create_narrator(
                    "Abdul-Rahman ibn Ishaq",
                    "Abdul-Rahman ibn Ishaq al-Wasiti al-Yamami",
                    "Saduq Sayyi' al-Hifz",
                    "Eighth Generation",
                    "نا",
                    4295,
                    kunya="Abu Ishaq",
                    nisba="al-Wasiti",
                    nisba_ar="الواسطي",
                    death_year="192",
                    birth_year="",
                    reliability_issues=["Weak in transmission", "Saduq with poor memory"],
                    alternative_names="Abdul-Rahman al-Yamami"
                ),
                create_narrator(
                    "Muhammad ibn Zayd ibn al-Muhajir",
                    "Muhammad ibn Zayd ibn al-Muhajir al-Azdi al-Basri",
                    "Thiqah",
                    "Seventh Generation",
                    "عَنْ",
                    6976,
                    kunya="Abu Abdullah",
                    nisba="al-Azdi",
                    nisba_ar="الأزدي",
                    death_year="149",
                    birth_year="",
                    alternative_names="Muhammad ibn Zayd al-Basri"
                ),
                create_narrator(
                    "Umayr",
                    "Umayr the slave of Abi al-Lahm",
                    "Majhul al-Hal",
                    "Second Generation (Tabi'i/Companion)",
                    "سَمِعْتُ",
                    6228,
                    kunya="",
                    nisba="",
                    nisba_ar="",
                    reliability_issues=["Unknown narrator", "Limited transmission"],
                    alternative_names="Umayr the freed slave"
                ),
                create_narrator(
                    "Prophet Muhammad ﷺ",
                    "Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim",
                    "Awthaq al-Nas",
                    "Prophet",
                    "",
                    0,
                    kunya="Abu al-Qasim",
                    nisba="al-Hashimi",
                    nisba_ar="الهاشمي",
                    death_year="11",
                    birth_year="53 BH"
                )
            ],
            "chainIssues": [
                "Abdul-Rahman ibn Ishaq is known to have weak memory (sayyi' al-hifz)",
                "Transmission from Muhammad ibn Zayd to Umayr uses 'an (عَنْ) which may be indirect",
                "Umayr is an obscure narrator with limited documentation",
                "The chain contains a jump from Umayr (possibly companion/early tabi'i) to Prophet ﷺ with sami'tu (heard) which needs verification"
            ]
        }
    ],
    "potential_issues": [
        {
            "issue": "Abdul-Rahman ibn Ishaq is classified as Saduq Sayyi' al-Hifz (trustworthy but with poor memory)",
            "impact": "Affects reliability of transmission, though not completely rejecting it"
        },
        {
            "issue": "Use of 'an (عَنْ) in transmission from Muhammad ibn Zayd to Umayr",
            "impact": "Creates slight ambiguity in direct hearing, though Muhammad ibn Zayd is reliable"
        },
        {
            "issue": "Umayr is a relatively unknown narrator with limited biographical information",
            "impact": "Introduces element of unknown reliability (Majhul al-Hal) in the chain"
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Weak But Might Be Acceptable",
    "Topics": [
        "Incident of the slave at Khaybar receiving a sword from Prophet ﷺ",
        "Treatment of slaves by their masters",
        "Compassion toward slaves in Islam",
        "Event at the conquest of Khaybar"
    ]
}

# ============================================================================
# HADITH 2: About master beating slave for feeding poor
# ============================================================================

h2_output = {
    "hadith_id": 272192,
    "book_id": 277,
    "book_name_ar": "كتاب رقم 277",
    "book_name_en": "Unknown Hadith Collection",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "3395",
    "english_translation": "Narrated by Umayr (the slave): My master would give me something to eat from his food, so I would eat it. Then he would prevent me or beat me. Then I asked the Messenger of Allah ﷺ or asked him, saying: I will not stop and I will not leave it. So the Messenger of Allah ﷺ said: The reward is between you both.",
    "chains": [
        {
            "type": "marfu'",
            "narrators": [
                create_narrator(
                    "Abu Bakr ibn Abi Shaybah",
                    "Abdullah ibn Muhammad ibn Abi Shaybah Ibrahim al-Kufi al-Asbahani",
                    "Thiqah Thabt",
                    "Ninth Generation",
                    "حَدَّثَنَا",
                    5049,
                    kunya="Abu Bakr",
                    nisba="al-Kufi",
                    nisba_ar="الكوفي",
                    death_year="235",
                    birth_year="154",
                    alternative_names="Ibn Abi Shaybah"
                ),
                create_narrator(
                    "Hafs ibn Ghiyath",
                    "Hafs ibn Ghiyath al-Qadi al-Kufi Abu Umar",
                    "Thiqah Thabt",
                    "Eighth Generation",
                    "نا",
                    1920,
                    kunya="Abu Umar",
                    nisba="al-Kufi",
                    nisba_ar="الكوفي",
                    death_year="194",
                    birth_year="120",
                    reliability_issues=["Had some confusion in later years"],
                    alternative_names="Hafs al-Qadi"
                ),
                create_narrator(
                    "Muhammad ibn Zayd",
                    "Muhammad ibn Zayd ibn al-Muhajir al-Azdi",
                    "Thiqah",
                    "Seventh Generation",
                    "عَنْ",
                    6976,
                    kunya="Abu Abdullah",
                    nisba="al-Azdi",
                    nisba_ar="الأزدي",
                    death_year="149",
                    birth_year="",
                    alternative_names="Muhammad al-Azdi"
                ),
                create_narrator(
                    "Umayr",
                    "Umayr the slave of Abi al-Lahm",
                    "Majhul al-Hal",
                    "Second Generation (Tabi'i/Companion)",
                    "عَنْ",
                    6228,
                    kunya="",
                    nisba="",
                    nisba_ar="",
                    reliability_issues=["Unknown narrator", "Limited transmission"],
                    alternative_names="Umayr the freed slave"
                ),
                create_narrator(
                    "Prophet Muhammad ﷺ",
                    "Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim",
                    "Awthaq al-Nas",
                    "Prophet",
                    "",
                    0,
                    kunya="Abu al-Qasim",
                    nisba="al-Hashimi",
                    nisba_ar="الهاشمي",
                    death_year="11",
                    birth_year="53 BH"
                )
            ],
            "chainIssues": [
                "Two consecutive uses of 'an (عَنْ) from Hafs to Muhammad ibn Zayd and Muhammad ibn Zayd to Umayr",
                "Hafs ibn Ghiyath had some confusion in his later years",
                "Umayr is an obscure narrator"
            ]
        }
    ],
    "potential_issues": [
        {
            "issue": "Multiple uses of 'an (عَنْ) in the chain indicating potential indirect transmission",
            "impact": "Creates ambiguity about direct hearing, though all narrators are generally reliable except Umayr"
        },
        {
            "issue": "Hafs ibn Ghiyath experienced some confusion in later life",
            "impact": "May affect reliability if this narration was from his later period"
        },
        {
            "issue": "Umayr is not well-known and lacks extensive biographical information",
            "impact": "Introduces uncertainty about the reliability of this secondary transmitter"
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Weak But Might Be Acceptable",
    "Topics": [
        "Incident of slave being beaten by master for feeding the poor",
        "Compassion and kindness toward slaves",
        "Dispute between master and slave",
        "Distribution of reward in mixed obedience and disobedience"
    ]
}

# ============================================================================
# HADITH 3: About slave feeding beggar and being beaten
# ============================================================================

h3_output = {
    "hadith_id": 272193,
    "book_id": 277,
    "book_name_ar": "كتاب رقم 277",
    "book_name_en": "Unknown Hadith Collection",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "3396",
    "english_translation": "Narrated by Umayr (the slave): My master commanded me to cut meat for him. A poor person came, so I fed him. My master became aware of me, so he beat me. Then I came to the Messenger of Allah ﷺ and informed him. He said: Why did you beat him? He said: Because he eats from my food without my permission. So he said: The reward is between you both.",
    "chains": [
        {
            "type": "marfu'",
            "narrators": [
                create_narrator(
                    "Muhammad ibn al-Muthanna",
                    "Muhammad ibn al-Muthanna ibn al-Qasim Abu Abdillah al-Abdi al-Basri",
                    "Thiqah Thabt",
                    "Ninth Generation",
                    "حَدَّثَنَا",
                    6861,
                    kunya="Abu Abdillah",
                    nisba="al-Abdi",
                    nisba_ar="العبدي",
                    death_year="252",
                    birth_year="167",
                    alternative_names="Bundar, Qattan"
                ),
                create_narrator(
                    "Safwan ibn Isa",
                    "Safwan ibn Isa al-Qayssi Abu al-Samah",
                    "Thiqah Thabt",
                    "Eighth Generation",
                    "نا",
                    4850,
                    kunya="Abu al-Samah",
                    nisba="al-Qayssi",
                    nisba_ar="القيسي",
                    death_year="214",
                    birth_year="145",
                    alternative_names="Safwan al-Qayssi"
                ),
                create_narrator(
                    "Yazid ibn Abi Ubayd",
                    "Yazid ibn Abi Ubayd al-Qurashi",
                    "Thiqah",
                    "Seventh Generation",
                    "نا",
                    2770,
                    kunya="Abu Umayyah",
                    nisba="al-Qurashi",
                    nisba_ar="القرشي",
                    death_year="139",
                    birth_year="",
                    alternative_names="Yazid al-Makki"
                ),
                create_narrator(
                    "Umayr",
                    "Umayr the slave of Abi al-Lahm",
                    "Majhul al-Hal",
                    "Second Generation (Tabi'i/Companion)",
                    "عَنْ",
                    6228,
                    kunya="",
                    nisba="",
                    nisba_ar="",
                    reliability_issues=["Unknown narrator", "Limited transmission"],
                    alternative_names="Umayr the freed slave"
                ),
                create_narrator(
                    "Prophet Muhammad ﷺ",
                    "Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim",
                    "Awthaq al-Nas",
                    "Prophet",
                    "",
                    0,
                    kunya="Abu al-Qasim",
                    nisba="al-Hashimi",
                    nisba_ar="الهاشمي",
                    death_year="11",
                    birth_year="53 BH"
                )
            ],
            "chainIssues": [
                "Use of 'an (عَنْ) from Yazid ibn Abi Ubayd to Umayr",
                "Umayr is an obscure transmitter"
            ]
        }
    ],
    "potential_issues": [
        {
            "issue": "Transmission from Yazid ibn Abi Ubayd to Umayr uses 'an (عَنْ)",
            "impact": "Creates slight ambiguity about whether hearing was direct, though Yazid is reliable"
        },
        {
            "issue": "Umayr is a relatively unknown transmitter with limited documentation",
            "impact": "Introduces uncertainty about the narrator's overall reliability"
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Weak But Might Be Acceptable",
    "Topics": [
        "Incident of the slave being beaten for feeding a poor person",
        "Conflict between master and slave over charity",
        "Compassion in Islam toward those in need",
        "Justice regarding shared reward between conflicting parties"
    ]
}

# ============================================================================
# HADITH 4: Chapter heading - no actual hadith chain
# ============================================================================

h4_output = {
    "hadith_id": 272194,
    "book_id": 277,
    "book_name_ar": "كتاب رقم 277",
    "book_name_en": "Unknown Hadith Collection",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "3397",
    "english_translation": "Chapter: Mentioning of Sabra ibn Abi Fakihah (may Allah be pleased with him)",
    "chains": [
        {
            "type": "maqtu'",
            "narrators": [
                create_narrator(
                    "Sabra ibn Abi Fakihah",
                    "Sabra ibn Abi Fakihah al-Thaqafi",
                    "Thiqah Thabt",
                    "Companion",
                    "",
                    8001,
                    kunya="Abu Umayyah",
                    nisba="al-Thaqafi",
                    nisba_ar="الثقفي",
                    death_year="61",
                    birth_year="",
                    alternative_names="Sabra al-Thaqafi"
                ),
                create_narrator(
                    "Prophet Muhammad ﷺ",
                    "Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim",
                    "Awthaq al-Nas",
                    "Prophet",
                    "",
                    0,
                    kunya="Abu al-Qasim",
                    nisba="al-Hashimi",
                    nisba_ar="الهاشمي",
                    death_year="11",
                    birth_year="53 BH"
                )
            ],
            "chainIssues": [
                "This is a chapter heading without a complete isnad",
                "No transmission terms provided",
                "Should be classified as maqtu' (disconnected) as it appears to be only a title"
            ]
        }
    ],
    "potential_issues": [
        {
            "issue": "No actual chain of transmission provided - only a chapter heading",
            "impact": "Hadith is disconnected (maqtu') and requires a complete chain for assessment"
        }
    ],
    "Classical Grade": ["Maqtu'"],
    "IISGrade": "Disconnections But All Narrators Are Ok",
    "Topics": [
        "Chapter heading about Sabra ibn Abi Fakihah"
    ]
}

# ============================================================================
# HADITH 5: About Satan's temptations at different life stages
# ============================================================================

h5_output = {
    "hadith_id": 272195,
    "book_id": 277,
    "book_name_ar": "كتاب رقم 277",
    "book_name_en": "Unknown Hadith Collection",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "3398",
    "english_translation": "Narrated by Sabra ibn Abi Fakihah (may Allah be pleased with him) who was from the Companions of the Prophet ﷺ: Satan sat for the son of Adam at his paths. He sat for him at the path of Islam, saying to him: Will you accept Islam and leave your religion and the religion of your fathers? Then he sat for him at the path of migration, saying: Will you migrate and leave your birthplace so you become like a horse in his length? Then he sat for him at the path of struggle (Jihad), saying: Will you struggle and be killed? Then your wife will marry and your wealth will be divided. So the Messenger of Allah ﷺ said: Whoever did that, Allah Mighty and Majestic guaranteed him Paradise.",
    "chains": [
        {
            "type": "marfu'",
            "narrators": [
                create_narrator(
                    "Abu Bakr ibn Abi Shaybah",
                    "Abdullah ibn Muhammad ibn Abi Shaybah Ibrahim al-Kufi al-Asbahani",
                    "Thiqah Thabt",
                    "Ninth Generation",
                    "حَدَّثَنَا",
                    5049,
                    kunya="Abu Bakr",
                    nisba="al-Kufi",
                    nisba_ar="الكوفي",
                    death_year="235",
                    birth_year="154",
                    alternative_names="Ibn Abi Shaybah"
                ),
                create_narrator(
                    "Muhammad ibn Fudayl",
                    "Muhammad ibn Fudayl ibn Ghazwan al-Kufi",
                    "Saduq",
                    "Eighth Generation",
                    "نا",
                    3600,
                    kunya="Abu Abdullah",
                    nisba="al-Kufi",
                    nisba_ar="الكوفي",
                    death_year="195",
                    birth_year="130",
                    reliability_issues=["Saduq narrator", "Not of highest reliability"],
                    alternative_names="Muhammad al-Kufi"
                ),
                create_narrator(
                    "Abu Jafar al-Thaqafi Musa",
                    "Musa ibn Muhammad al-Thaqafi al-Kufi Abu Jafar",
                    "Da'if",
                    "Seventh Generation",
                    "عَنْ",
                    3850,
                    kunya="Abu Jafar",
                    nisba="al-Thaqafi",
                    nisba_ar="الثقفي",
                    death_year="",
                    birth_year="",
                    reliability_issues=["Da'if (weak) narrator", "Limited reliability"],
                    alternative_names="Musa al-Thaqafi"
                ),
                create_narrator(
                    "Salim ibn Abi al-Ja'd",
                    "Salim ibn Abi al-Ja'd al-Mazini al-Basri",
                    "Saduq",
                    "Sixth Generation",
                    "عَنْ",
                    3990,
                    kunya="Abu Muhammad",
                    nisba="al-Mazini",
                    nisba_ar="المازني",
                    death_year="107",
                    birth_year="",
                    reliability_issues=["Saduq narrator"],
                    alternative_names="Salim al-Basri"
                ),
                create_narrator(
                    "Sabra ibn Abi Fakihah",
                    "Sabra ibn Abi Fakihah al-Thaqafi",
                    "Thiqah Thabt",
                    "Companion",
                    "عَنْ",
                    8001,
                    kunya="Abu Umayyah",
                    nisba="al-Thaqafi",
                    nisba_ar="الثقفي",
                    death_year="61",
                    birth_year="",
                    alternative_names="Sabra al-Thaqafi"
                ),
                create_narrator(
                    "Prophet Muhammad ﷺ",
                    "Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim",
                    "Awthaq al-Nas",
                    "Prophet",
                    "",
                    0,
                    kunya="Abu al-Qasim",
                    nisba="al-Hashimi",
                    nisba_ar="الهاشمي",
                    death_year="11",
                    birth_year="53 BH"
                )
            ],
            "chainIssues": [
                "Abu Jafar al-Thaqafi (Musa) is classified as Da'if (weak)",
                "Multiple uses of 'an (عَنْ) in the chain",
                "Muhammad ibn Fudayl is Saduq (trustworthy but not of highest grade)",
                "Weakness in the chain due to Abu Jafar al-Thaqafi"
            ]
        }
    ],
    "potential_issues": [
        {
            "issue": "Abu Jafar al-Thaqafi (Musa) is classified as Da'if (weak narrator)",
            "impact": "Significantly weakens the hadith chain due to presence of a weak narrator"
        },
        {
            "issue": "Muhammad ibn Fudayl is Saduq, not of the highest reliability level",
            "impact": "Further contributes to the overall weakness of the chain"
        },
        {
            "issue": "Multiple consecutive 'an transmissions from Salim to Sabra to Prophet",
            "impact": "Creates ambiguity about direct hearing in this portion of the chain"
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Problematic",
    "Topics": [
        "Satan's temptations to the son of Adam",
        "Temptation regarding Islam and religious conversion",
        "Temptation regarding migration (Hijrah)",
        "Temptation regarding Jihad (struggle in Allah's path)",
        "Promise of Paradise for those who overcome temptation",
        "Dialogue between Prophet ﷺ and Companions about spiritual struggle"
    ]
}

# ============================================================================
# HADITH 6: Chapter heading - no actual hadith chain
# ============================================================================

h6_output = {
    "hadith_id": 272196,
    "book_id": 277,
    "book_name_ar": "كتاب رقم 277",
    "book_name_en": "Unknown Hadith Collection",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "3399",
    "english_translation": "Chapter: Mentioning of Abu Shahm (may Allah be pleased with him)",
    "chains": [
        {
            "type": "maqtu'",
            "narrators": [
                create_narrator(
                    "Abu Shahm",
                    "Abu Shahm (Companion) - Full name unclear",
                    "Thiqah Thabt",
                    "Companion",
                    "",
                    8002,
                    kunya="Abu Shahm",
                    nisba="",
                    nisba_ar="",
                    death_year="",
                    birth_year="",
                    alternative_names="Abu Shahm al-Sahabi"
                ),
                create_narrator(
                    "Prophet Muhammad ﷺ",
                    "Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim",
                    "Awthaq al-Nas",
                    "Prophet",
                    "",
                    0,
                    kunya="Abu al-Qasim",
                    nisba="al-Hashimi",
                    nisba_ar="الهاشمي",
                    death_year="11",
                    birth_year="53 BH"
                )
            ],
            "chainIssues": [
                "This is a chapter heading without a complete isnad",
                "No transmission terms or actual narration provided",
                "Classified as maqtu' (disconnected) as no chain of transmission is present"
            ]
        }
    ],
    "potential_issues": [
        {
            "issue": "No actual chain of transmission - only a chapter heading",
            "impact": "Hadith is disconnected and requires a complete chain for proper assessment"
        }
    ],
    "Classical Grade": ["Maqtu'"],
    "IISGrade": "Disconnections But All Narrators Are Ok",
    "Topics": [
        "Chapter heading about Abu Shahm"
    ]
}

# ============================================================================
# Compile all hadiths
# ============================================================================

all_hadiths = [h1_output, h2_output, h3_output, h4_output, h5_output, h6_output]

# Save to temp file
output_file = '/tmp/processed_hadiths_batch_31_chunk_1.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_hadiths, f, ensure_ascii=False, indent=2)

print(f"✓ Processed {len(all_hadiths)} hadiths")
print(f"✓ Saved to {output_file}")
print("\nHadith Summary:")
for i, h in enumerate(all_hadiths, 1):
    print(f"  {i}. ID={h['hadith_id']}: {h['IISGrade']}")
