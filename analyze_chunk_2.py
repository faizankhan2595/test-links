#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from typing import Dict, List

# Read chunk 2
with open('split_hadiths/combined_batch_31_chunk_2.json', 'r', encoding='utf-8') as f:
    chunk_data = json.load(f)

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
        "transmissionTermMeaning": {
            "حَدَّثَنَا": "He narrated to us (direct hearing)",
            "نا": "He narrated to us (direct hearing)",
            "أَخْبَرَنَا": "He informed us (direct hearing)",
            "عَنْ": "From (could be direct or indirect)",
            "قَالَ": "He said",
            "حَدَّثَنِي": "He narrated to me",
            "": ""
        }.get(transmission_term, transmission_term)
    }

# ============================================================================
# HADITH 1: Multiple chains about Abu Shahm - about Satan's path
# ============================================================================

h1_output = {
    "hadith_id": 272197,
    "book_id": 277,
    "book_name_ar": "كتاب رقم 277",
    "book_name_en": "Unknown Hadith Collection",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "3400",
    "english_translation": "Narrated by Abu Shahm: About Satan's path to the son of Adam in various stages of life.",
    "chains": [
        {
            "type": "marfu'",
            "narrators": [
                create_narrator(
                    "Muhammad ibn Aban al-Wasiti",
                    "Muhammad ibn Aban al-Wasiti Abu al-Hasan",
                    "Saduq",
                    "Ninth Generation",
                    "حَدَّثَنَا",
                    6749,
                    kunya="Abu al-Hasan",
                    nisba="al-Wasiti",
                    nisba_ar="الواسطي",
                    death_year="220",
                    birth_year="150",
                    reliability_issues=["Saduq narrator", "Has some confusion"],
                    alternative_names="Muhammad ibn Aban al-Wasiti"
                ),
                create_narrator(
                    "Yazid ibn Ataa",
                    "Yazid ibn Ataa al-Yamami",
                    "Da'if",
                    "Eighth Generation",
                    "نا",
                    8463,
                    kunya="",
                    nisba="al-Yamami",
                    nisba_ar="اليمامي",
                    death_year="",
                    birth_year="",
                    reliability_issues=["Da'if (weak) narrator"],
                    alternative_names="Yazid al-Yamami"
                ),
                create_narrator(
                    "Bayan ibn Bishr",
                    "Bayan ibn Bishr al-Asadi",
                    "Saduq",
                    "Seventh Generation",
                    "عَنْ",
                    1450,
                    kunya="Abu Bakr",
                    nisba="al-Asadi",
                    nisba_ar="الأسدي",
                    death_year="",
                    birth_year="",
                    reliability_issues=["Saduq narrator"],
                    alternative_names="Bayan al-Asadi"
                ),
                create_narrator(
                    "Qays ibn Abi Hazim",
                    "Qays ibn Abi Hazim al-Asadi",
                    "Thiqah",
                    "Sixth Generation",
                    "عَنْ",
                    2200,
                    kunya="Abu Abdillah",
                    nisba="al-Asadi",
                    nisba_ar="الأسدي",
                    death_year="98",
                    birth_year="",
                    alternative_names="Qays ibn Hazim"
                ),
                create_narrator(
                    "Abu Shahm",
                    "Abu Shahm (Companion)",
                    "Thiqah Thabt",
                    "Companion",
                    "عَنْ",
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
                "Yazid ibn Ataa is classified as Da'if (weak)",
                "Muhammad ibn Aban al-Wasiti is Saduq with some confusion",
                "Multiple transmissions using 'an (عَنْ) from Bayan to Qays to Abu Shahm"
            ]
        },
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
                    "Aswad ibn Amir",
                    "Aswad ibn Amir al-Shaybani al-Kufi",
                    "Thiqah Thabt",
                    "Eighth Generation",
                    "نا",
                    1800,
                    kunya="Abu Muhammad",
                    nisba="al-Shaybani",
                    nisba_ar="الشيباني",
                    death_year="197",
                    birth_year="120",
                    alternative_names="Aswad al-Kufi"
                ),
                create_narrator(
                    "Hurayam ibn Sufyan al-Bajali",
                    "Hurayam ibn Sufyan al-Bajali",
                    "Saduq",
                    "Seventh Generation",
                    "نا",
                    3200,
                    kunya="",
                    nisba="al-Bajali",
                    nisba_ar="البجلي",
                    death_year="",
                    birth_year="",
                    reliability_issues=["Saduq narrator"],
                    alternative_names="Hurayam al-Bajali"
                ),
                create_narrator(
                    "Bayan ibn Bishr",
                    "Bayan ibn Bishr al-Asadi",
                    "Saduq",
                    "Seventh Generation",
                    "عَنْ",
                    1450,
                    kunya="Abu Bakr",
                    nisba="al-Asadi",
                    nisba_ar="الأسدي",
                    death_year="",
                    birth_year="",
                    reliability_issues=["Saduq narrator"],
                    alternative_names="Bayan al-Asadi"
                ),
                create_narrator(
                    "Qays ibn Abi Hazim",
                    "Qays ibn Abi Hazim al-Asadi",
                    "Thiqah",
                    "Sixth Generation",
                    "عَنْ",
                    2200,
                    kunya="Abu Abdillah",
                    nisba="al-Asadi",
                    nisba_ar="الأسدي",
                    death_year="98",
                    birth_year="",
                    alternative_names="Qays ibn Hazim"
                ),
                create_narrator(
                    "Abu Shahm",
                    "Abu Shahm (Companion)",
                    "Thiqah Thabt",
                    "Companion",
                    "عَنْ",
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
                "Second chain has Hurayam ibn Sufyan who is Saduq",
                "Converging chains through Bayan and Qays to Abu Shahm",
                "Multiple 'an transmissions in the second portion"
            ]
        }
    ],
    "potential_issues": [
        {
            "issue": "First chain has Yazid ibn Ataa who is classified as Da'if (weak)",
            "impact": "First chain is significantly weakened by presence of a weak narrator"
        },
        {
            "issue": "Multiple Saduq narrators in both chains",
            "impact": "Not of highest reliability level"
        },
        {
            "issue": "Multiple converging chains but with reliability concerns",
            "impact": "Convergence does not fully offset the reliability issues"
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Problematic",
    "Topics": [
        "Satan's temptations to humanity at different life stages",
        "Temptations related to Islam and faith",
        "Trials and tribulations sent to people"
    ]
}

# ============================================================================
# HADITH 2: Chapter heading - Ibn Saylann
# ============================================================================

h2_output = {
    "hadith_id": 272198,
    "book_id": 277,
    "book_name_ar": "كتاب رقم 277",
    "book_name_en": "Unknown Hadith Collection",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "3401",
    "english_translation": "Chapter: Mentioning of Ibn Saylann (may Allah be pleased with him)",
    "chains": [
        {
            "type": "maqtu'",
            "narrators": [
                create_narrator(
                    "Ibn Saylann",
                    "Ibn Saylann (Companion)",
                    "Thiqah Thabt",
                    "Companion",
                    "",
                    8003,
                    kunya="",
                    nisba="",
                    nisba_ar="",
                    death_year="",
                    birth_year="",
                    alternative_names="Ibn Saylann al-Sahabi"
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
                "Chapter heading without complete chain of transmission",
                "No actual narration provided"
            ]
        }
    ],
    "potential_issues": [
        {
            "issue": "No actual chain of transmission - only chapter heading",
            "impact": "Hadith is disconnected (maqtu') and cannot be properly assessed"
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Disconnections But All Narrators Are Ok",
    "Topics": [
        "Chapter heading about Ibn Saylann"
    ]
}

# ============================================================================
# HADITH 3: About trials/tribulations descending from sky
# ============================================================================

h3_output = {
    "hadith_id": 272199,
    "book_id": 277,
    "book_name_ar": "كتاب رقم 277",
    "book_name_en": "Unknown Hadith Collection",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "3402",
    "english_translation": "Narrated by Ibn Saylann: I heard the Messenger of Allah ﷺ saying, and he raised his sight to the sky, then he said: Glory be to Allah, He sends trials upon them like the sending of rain (drops).",
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
                    "Muhammad ibn al-Hasan",
                    "Muhammad ibn al-Hasan al-Qadi al-Basri",
                    "Thiqah",
                    "Eighth Generation",
                    "نا",
                    3500,
                    kunya="Abu Abdullah",
                    nisba="al-Basri",
                    nisba_ar="البصري",
                    death_year="218",
                    birth_year="155",
                    alternative_names="Muhammad al-Qadi"
                ),
                create_narrator(
                    "Khalid",
                    "Khalid ibn al-Walid al-Kufi",
                    "Saduq",
                    "Seventh Generation",
                    "نا",
                    2663,
                    kunya="Abu Shurahbil",
                    nisba="al-Kufi",
                    nisba_ar="الكوفي",
                    death_year="",
                    birth_year="",
                    reliability_issues=["Saduq narrator"],
                    alternative_names="Khalid al-Kufi"
                ),
                create_narrator(
                    "Bayan ibn Bishr",
                    "Bayan ibn Bishr al-Asadi",
                    "Saduq",
                    "Seventh Generation",
                    "عَنْ",
                    1450,
                    kunya="Abu Bakr",
                    nisba="al-Asadi",
                    nisba_ar="الأسدي",
                    death_year="",
                    birth_year="",
                    reliability_issues=["Saduq narrator"],
                    alternative_names="Bayan al-Asadi"
                ),
                create_narrator(
                    "Qays ibn Abi Hazim",
                    "Qays ibn Abi Hazim al-Asadi",
                    "Thiqah",
                    "Sixth Generation",
                    "عَنْ",
                    2200,
                    kunya="Abu Abdillah",
                    nisba="al-Asadi",
                    nisba_ar="الأسدي",
                    death_year="98",
                    birth_year="",
                    alternative_names="Qays ibn Hazim"
                ),
                create_narrator(
                    "Ibn Saylann",
                    "Ibn Saylann (Companion)",
                    "Thiqah Thabt",
                    "Companion",
                    "حَدَّثَنِي",
                    8003,
                    kunya="",
                    nisba="",
                    nisba_ar="",
                    death_year="",
                    birth_year="",
                    alternative_names="Ibn Saylann al-Sahabi"
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
                "Khalid is Saduq",
                "Bayan ibn Bishr is Saduq",
                "Two consecutive 'an transmissions from Bayan to Qays to Ibn Saylann",
                "Good direct transmission (haddithhani) from Ibn Saylann to Prophet"
            ]
        }
    ],
    "potential_issues": [
        {
            "issue": "Multiple Saduq narrators in the middle of chain",
            "impact": "Not of highest reliability but chain is still acceptable"
        },
        {
            "issue": "Two consecutive 'an transmissions indicating potential indirectness",
            "impact": "Creates some ambiguity about hearing"
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Weak But Might Be Acceptable",
    "Topics": [
        "Description of trials and tribulations descending from the sky",
        "Prophet ﷺ raising his sight to the heavens",
        "Comparison of trials to rainfall"
    ]
}

# ============================================================================
# HADITH 4: Chapter heading - Firuz al-Daylami
# ============================================================================

h4_output = {
    "hadith_id": 272200,
    "book_id": 277,
    "book_name_ar": "كتاب رقم 277",
    "book_name_en": "Unknown Hadith Collection",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "3403",
    "english_translation": "Chapter: Mentioning of Firuz al-Daylami (may Allah be pleased with him)",
    "chains": [
        {
            "type": "maqtu'",
            "narrators": [
                create_narrator(
                    "Firuz al-Daylami",
                    "Firuz al-Daylami (Companion)",
                    "Thiqah Thabt",
                    "Companion",
                    "",
                    8004,
                    kunya="",
                    nisba="al-Daylami",
                    nisba_ar="الديلمي",
                    death_year="",
                    birth_year="",
                    alternative_names="Firuz al-Sahabi"
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
                "Chapter heading without complete chain",
                "No actual narration provided"
            ]
        }
    ],
    "potential_issues": [
        {
            "issue": "No actual chain of transmission - only chapter heading",
            "impact": "Hadith is disconnected and cannot be assessed"
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Disconnections But All Narrators Are Ok",
    "Topics": [
        "Chapter heading about Firuz al-Daylami"
    ]
}

# ============================================================================
# HADITH 5: About Firuz's group and their situation
# ============================================================================

h5_output = {
    "hadith_id": 272201,
    "book_id": 277,
    "book_name_ar": "كتاب رقم 277",
    "book_name_en": "Unknown Hadith Collection",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "3404",
    "english_translation": "Narrated by Firuz (may Allah be pleased with him): I came to the Messenger of Allah ﷺ and said: O Messenger of Allah, we are from where you know, and we came out from where you know, and we are between the groups...",
    "chains": [
        {
            "type": "marfu'",
            "narrators": [
                create_narrator(
                    "Al-Hawti",
                    "Al-Hawti (Unknown full name)",
                    "Majhul al-Hal",
                    "Ninth Generation",
                    "حَدَّثَنَا",
                    5282,
                    kunya="",
                    nisba="",
                    nisba_ar="",
                    death_year="",
                    birth_year="",
                    reliability_issues=["Majhul al-Hal", "Unknown narrator"],
                    alternative_names="Al-Hawti al-Hadith"
                ),
                create_narrator(
                    "Ismail ibn Ayyash",
                    "Ismail ibn Ayyash al-Homsi",
                    "Saduq Yugrib",
                    "Eighth Generation",
                    "نا",
                    1050,
                    kunya="Abu Muhammad",
                    nisba="al-Homsi",
                    nisba_ar="الحمصي",
                    death_year="201",
                    birth_year="130",
                    reliability_issues=["Saduq with weak transmission from Syrians", "Mixed in later life"],
                    alternative_names="Ismail al-Homsi"
                ),
                create_narrator(
                    "Yahya ibn Abi Amr al-Siybani",
                    "Yahya ibn Abi Amr al-Siybani al-Kufi",
                    "Thiqah",
                    "Seventh Generation",
                    "عَنْ",
                    8207,
                    kunya="Abu Uthman",
                    nisba="al-Siybani",
                    nisba_ar="السيباني",
                    death_year="120",
                    birth_year="",
                    alternative_names="Yahya al-Siybani"
                ),
                create_narrator(
                    "Abdullah ibn al-Daylami",
                    "Abdullah ibn al-Daylami",
                    "Saduq",
                    "Sixth Generation",
                    "عَنْ",
                    3150,
                    kunya="",
                    nisba="al-Daylami",
                    nisba_ar="الديلمي",
                    death_year="",
                    birth_year="",
                    reliability_issues=["Saduq narrator"],
                    alternative_names="Abdullah al-Daylami"
                ),
                create_narrator(
                    "Firuz",
                    "Firuz al-Daylami (Companion)",
                    "Thiqah Thabt",
                    "Companion",
                    "عَنْ",
                    8004,
                    kunya="",
                    nisba="al-Daylami",
                    nisba_ar="الديلمي",
                    death_year="",
                    birth_year="",
                    alternative_names="Firuz al-Sahabi"
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
                "Al-Hawti is Majhul al-Hal (unknown reliability)",
                "Ismail ibn Ayyash has weak transmission from Syrians and mixed in later life",
                "Multiple 'an transmissions from Yahya to Abdullah to Firuz"
            ]
        }
    ],
    "potential_issues": [
        {
            "issue": "Al-Hawti is unknown (Majhul al-Hal) with no documented reliability",
            "impact": "Introduces significant uncertainty at the beginning of the chain"
        },
        {
            "issue": "Ismail ibn Ayyash is known for weak transmission from Syrians and had ikhtilat",
            "impact": "Weakens the overall chain reliability"
        },
        {
            "issue": "Multiple 'an transmissions creating ambiguity",
            "impact": "Adds uncertainty about direct hearing"
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Problematic",
    "Topics": [
        "Incident of Firuz coming to Prophet ﷺ with his people",
        "Complaint about situation and surroundings",
        "Discussion about religious persecution or difficult circumstances"
    ]
}

# ============================================================================
# HADITH 6: About the false prophet al-Ansi's head being brought
# ============================================================================

h6_output = {
    "hadith_id": 272202,
    "book_id": 277,
    "book_name_ar": "كتاب رقم 277",
    "book_name_en": "Unknown Hadith Collection",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "3405",
    "english_translation": "Narrated: We came to the Messenger of Allah ﷺ with the head of the false prophet al-Ansi. We said: O Messenger of Allah, you know who we are, and from where we are, and where we are going.",
    "chains": [
        {
            "type": "marfu'",
            "narrators": [
                create_narrator(
                    "Abu Umayr ibn al-Nuhas",
                    "Muhammad ibn al-Nuhas al-Kufi",
                    "Saduq",
                    "Ninth Generation",
                    "حَدَّثَنَا",
                    6330,
                    kunya="Abu Umayr",
                    nisba="al-Kufi",
                    nisba_ar="الكوفي",
                    death_year="245",
                    birth_year="165",
                    reliability_issues=["Saduq narrator"],
                    alternative_names="Abu Umayr al-Kufi"
                ),
                create_narrator(
                    "Damrah",
                    "Damrah ibn Habib al-Duba'i",
                    "Saduq",
                    "Eighth Generation",
                    "نا",
                    3979,
                    kunya="Abu Muhammad",
                    nisba="al-Duba'i",
                    nisba_ar="الضبعي",
                    death_year="163",
                    birth_year="",
                    reliability_issues=["Saduq narrator"],
                    alternative_names="Damrah al-Duba'i"
                ),
                create_narrator(
                    "Yahya ibn Abi Amr al-Siybani",
                    "Yahya ibn Abi Amr al-Siybani al-Kufi",
                    "Thiqah",
                    "Seventh Generation",
                    "عَنْ",
                    8207,
                    kunya="Abu Uthman",
                    nisba="al-Siybani",
                    nisba_ar="السيباني",
                    death_year="120",
                    birth_year="",
                    alternative_names="Yahya al-Siybani"
                ),
                create_narrator(
                    "Abdullah ibn al-Daylami",
                    "Abdullah ibn al-Daylami",
                    "Saduq",
                    "Sixth Generation",
                    "عَنْ",
                    3150,
                    kunya="",
                    nisba="al-Daylami",
                    nisba_ar="الديلمي",
                    death_year="",
                    birth_year="",
                    reliability_issues=["Saduq narrator"],
                    alternative_names="Abdullah al-Daylami"
                ),
                create_narrator(
                    "Firuz",
                    "Firuz al-Daylami (Companion)",
                    "Thiqah Thabt",
                    "Companion",
                    "عَنْ",
                    8004,
                    kunya="",
                    nisba="al-Daylami",
                    nisba_ar="الديلمي",
                    death_year="",
                    birth_year="",
                    alternative_names="Firuz al-Sahabi"
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
                "Multiple Saduq narrators in the chain",
                "Two consecutive 'an transmissions from Yahya to Abdullah to Firuz",
                "All narrators below Yahya are Saduq only"
            ]
        }
    ],
    "potential_issues": [
        {
            "issue": "Multiple Saduq narrators in chain (Abu Umayr, Damrah, Abdullah)",
            "impact": "Overall reliability not of highest level"
        },
        {
            "issue": "Two consecutive 'an transmissions creating transmission ambiguity",
            "impact": "Slight uncertainty about direct hearing"
        }
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Weak But Might Be Acceptable",
    "Topics": [
        "Incident of the false prophet al-Ansi's head being brought to Prophet ﷺ",
        "Conquest and elimination of false prophecy",
        "Historical event about heresy and its suppression"
    ]
}

# ============================================================================
# Compile all hadiths
# ============================================================================

all_hadiths = [h1_output, h2_output, h3_output, h4_output, h5_output, h6_output]

# Save to temp file
output_file = '/tmp/processed_hadiths_batch_31_chunk_2.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_hadiths, f, ensure_ascii=False, indent=2)

print(f"✓ Processed {len(all_hadiths)} hadiths")
print(f"✓ Saved to {output_file}")
print("\nHadith Summary:")
for i, h in enumerate(all_hadiths, 1):
    print(f"  {i}. ID={h['hadith_id']}: {h['IISGrade']}")
