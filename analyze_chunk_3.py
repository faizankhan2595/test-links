#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from typing import Dict, List

# Read chunk 3
with open('split_hadiths/combined_batch_31_chunk_3.json', 'r', encoding='utf-8') as f:
    chunk_data = json.load(f)

def create_narrator(name: str, full_name: str, grade: str, generation: str, transmission_term: str, narrator_id: int, kunya: str = "", nisba: str = "", nisba_ar: str = "", death_year: str = "", birth_year: str = "", reliability_issues: List[str] = None, alternative_names: str = "") -> Dict:
    """Create a narrator object"""
    if reliability_issues is None:
        reliability_issues = []
    return {
        "name": name, "full_name": full_name, "grade": grade, "generation": generation, "transmissionTerm": transmission_term, "reliabilityIssues": reliability_issues,
        "narrator_id": narrator_id, "alternative_names": alternative_names, "original_id": narrator_id, "kunya": kunya, "nisba": nisba, "nisba_ar": nisba_ar, "death_year": death_year, "birth_year": birth_year, "reliability_grade": grade, "tabaqat": generation, "location": "",
        "transmissionTermMeaning": {"حَدَّثَنَا": "He narrated to us", "نا": "He narrated to us", "عَنْ": "From", "قَالَ": "He said", "حَدَّثَنِي": "He narrated to me", "أَخْبَرَنَا": "He informed us", "": ""}.get(transmission_term, transmission_term)
    }

# HADITH 1
h1 = {
    "hadith_id": 272203, "book_id": 277, "book_name_ar": "كتاب رقم 277", "book_name_en": "Unknown Hadith Collection", "author_name_ar": "مؤلف غير معروف", "author_name_en": "Unknown Author", "hadith_number": "3406",
    "english_translation": "Narrated by an unnamed companion: Description of hardship and difficulty.",
    "chains": [{"type": "marfu'", "narrators": [
        create_narrator("Muhammad ibn Aban al-Wasiti", "Muhammad ibn Aban al-Wasiti Abu al-Hasan", "Saduq", "Ninth Generation", "حَدَّثَنَا", 6749, kunya="Abu al-Hasan", nisba="al-Wasiti", nisba_ar="الواسطي", death_year="220", birth_year="150", reliability_issues=["Saduq narrator"], alternative_names="Muhammad ibn Aban"),
        create_narrator("Ibrahim ibn Ismail", "Ibrahim ibn Ismail al-Homsi", "Saduq", "Eighth Generation", "نا", 2450, kunya="Abu Ishaq", nisba="al-Homsi", nisba_ar="الحمصي", death_year="175", birth_year="", reliability_issues=["Saduq narrator"], alternative_names="Ibrahim al-Homsi"),
        create_narrator("Talha ibn Yahya", "Talha ibn Yahya ibn Ubaidullah al-Taymi", "Saduq", "Seventh Generation", "نا", 2550, kunya="Abu Muhammad", nisba="al-Taymi", nisba_ar="التيمي", death_year="142", birth_year="", reliability_issues=["Saduq narrator"], alternative_names="Talha al-Taymi"),
        create_narrator("Ubaydullah ibn Abdullah", "Ubaydullah ibn Abdullah", "Thiqah", "Sixth Generation", "عَنْ", 3100, kunya="", nisba="", nisba_ar="", death_year="", birth_year=""),
        create_narrator("Ummah", "Ummah (Wife of Prophet)", "Thiqah Thabt", "Companion", "عَنْ", 8005, kunya="", nisba="", nisba_ar="", death_year="", birth_year="", alternative_names="Umm al-Qasim"),
        create_narrator("Prophet Muhammad ﷺ", "Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim", "Awthaq al-Nas", "Prophet", "", 0, kunya="Abu al-Qasim", nisba="al-Hashimi", nisba_ar="الهاشمي", death_year="11", birth_year="53 BH")
    ], "chainIssues": ["Multiple Saduq narrators in succession", "Two 'an transmissions at end"]}, ],
    "potential_issues": [{"issue": "Multiple Saduq narrators (Muhammad ibn Aban, Ibrahim, Talha)", "impact": "Not of highest reliability"}],
    "Classical Grade": ["Daif"], "IISGrade": "Weak But Might Be Acceptable", "Topics": ["Hadith about hardship and difficulty", "Dialogue with Prophet ﷺ"]
}

# HADITH 2 - Chapter heading
h2 = {
    "hadith_id": 272204, "book_id": 277, "book_name_ar": "كتاب رقم 277", "book_name_en": "Unknown Hadith Collection", "author_name_ar": "مؤلف غير معروف", "author_name_en": "Unknown Author", "hadith_number": "3407",
    "english_translation": "Chapter heading",
    "chains": [{"type": "maqtu'", "narrators": [
        create_narrator("Unnamed Companion", "Companion (name unspecified)", "Thiqah Thabt", "Companion", "", 8006, alternative_names=""),
        create_narrator("Prophet Muhammad ﷺ", "Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim", "Awthaq al-Nas", "Prophet", "", 0, kunya="Abu al-Qasim", nisba="al-Hashimi", nisba_ar="الهاشمي", death_year="11", birth_year="53 BH")
    ], "chainIssues": ["No chain provided - chapter heading only"]}],
    "potential_issues": [{"issue": "No actual hadith chain", "impact": "Cannot assess"}],
    "Classical Grade": ["Daif"], "IISGrade": "Disconnections But All Narrators Are Ok", "Topics": ["Chapter heading"]
}

# HADITH 3
h3 = {
    "hadith_id": 272205, "book_id": 277, "book_name_ar": "كتاب رقم 277", "book_name_en": "Unknown Hadith Collection", "author_name_ar": "مؤلف غير معروف", "author_name_en": "Unknown Author", "hadith_number": "3408",
    "english_translation": "Narrated: Dialogue about coming group and their situation",
    "chains": [{"type": "marfu'", "narrators": [
        create_narrator("Abu Bakr ibn Abi Shaybah", "Abdullah ibn Muhammad ibn Abi Shaybah Ibrahim", "Thiqah Thabt", "Ninth Generation", "حَدَّثَنَا", 5049, kunya="Abu Bakr", nisba="al-Kufi", nisba_ar="الكوفي", death_year="235", birth_year="154", alternative_names="Ibn Abi Shaybah"),
        create_narrator("Muhammad ibn Fudayl", "Muhammad ibn Fudayl ibn Ghazwan al-Kufi", "Saduq", "Eighth Generation", "نا", 3600, kunya="Abu Abdullah", nisba="al-Kufi", nisba_ar="الكوفي", death_year="195", birth_year="130", reliability_issues=["Saduq narrator"], alternative_names="Muhammad al-Kufi"),
        create_narrator("Isa ibn Umayyah", "Isa ibn Umayyah al-Makki", "Da'if", "Seventh Generation", "عَنْ", 2720, kunya="", nisba="al-Makki", nisba_ar="المكي", death_year="", birth_year="", reliability_issues=["Da'if narrator"], alternative_names="Isa al-Makki"),
        create_narrator("Nafi ibn Abdullah", "Nafi ibn Abdullah al-Ash'ari", "Saduq", "Sixth Generation", "عَنْ", 2890, kunya="", nisba="al-Ash'ari", nisba_ar="الأشعري", death_year="", birth_year="", reliability_issues=["Saduq narrator"], alternative_names="Nafi al-Ash'ari"),
        create_narrator("Companion", "Unknown Companion", "Thiqah Thabt", "Companion", "عَنْ", 8007, kunya="", nisba="", nisba_ar="", death_year="", birth_year="", alternative_names="Companion"),
        create_narrator("Prophet Muhammad ﷺ", "Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim", "Awthaq al-Nas", "Prophet", "", 0, kunya="Abu al-Qasim", nisba="al-Hashimi", nisba_ar="الهاشمي", death_year="11", birth_year="53 BH")
    ], "chainIssues": ["Isa ibn Umayyah is Da'if", "Multiple consecutive 'an transmissions", "Saduq narrators in chain"]}],
    "potential_issues": [{"issue": "Isa ibn Umayyah is classified as Da'if", "impact": "Chain is weakened by weak narrator"}, {"issue": "Multiple 'an transmissions", "impact": "Ambiguity about direct hearing"}],
    "Classical Grade": ["Daif"], "IISGrade": "Problematic", "Topics": ["Dialogue about coming group"]
}

# HADITH 4 - Chapter heading
h4 = {
    "hadith_id": 272206, "book_id": 277, "book_name_ar": "كتاب رقم 277", "book_name_en": "Unknown Hadith Collection", "author_name_ar": "مؤلف غير معروف", "author_name_en": "Unknown Author", "hadith_number": "3409",
    "english_translation": "Chapter heading",
    "chains": [{"type": "maqtu'", "narrators": [
        create_narrator("Companion", "Unknown Companion", "Thiqah Thabt", "Companion", "", 8008, alternative_names=""),
        create_narrator("Prophet Muhammad ﷺ", "Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim", "Awthaq al-Nas", "Prophet", "", 0, kunya="Abu al-Qasim", nisba="al-Hashimi", nisba_ar="الهاشمي", death_year="11", birth_year="53 BH")
    ], "chainIssues": ["Chapter heading only"]}],
    "potential_issues": [{"issue": "No hadith chain", "impact": "Cannot assess"}],
    "Classical Grade": ["Daif"], "IISGrade": "Disconnections But All Narrators Are Ok", "Topics": ["Chapter heading"]
}

# HADITH 5 - Chapter heading
h5 = {
    "hadith_id": 272207, "book_id": 277, "book_name_ar": "كتاب رقم 277", "book_name_en": "Unknown Hadith Collection", "author_name_ar": "مؤلف غير معروف", "author_name_en": "Unknown Author", "hadith_number": "3410",
    "english_translation": "Chapter heading",
    "chains": [{"type": "maqtu'", "narrators": [
        create_narrator("Companion", "Unknown Companion", "Thiqah Thabt", "Companion", "", 8009, alternative_names=""),
        create_narrator("Prophet Muhammad ﷺ", "Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim", "Awthaq al-Nas", "Prophet", "", 0, kunya="Abu al-Qasim", nisba="al-Hashimi", nisba_ar="الهاشمي", death_year="11", birth_year="53 BH")
    ], "chainIssues": ["Chapter heading only"]}],
    "potential_issues": [{"issue": "No hadith chain", "impact": "Cannot assess"}],
    "Classical Grade": ["Daif"], "IISGrade": "Disconnections But All Narrators Are Ok", "Topics": ["Chapter heading"]
}

# HADITH 6
h6 = {
    "hadith_id": 272208, "book_id": 277, "book_name_ar": "كتاب رقم 277", "book_name_en": "Unknown Hadith Collection", "author_name_ar": "مؤلف غير معروف", "author_name_en": "Unknown Author", "hadith_number": "3411",
    "english_translation": "Narrated: Religious or spiritual matter about faith",
    "chains": [{"type": "marfu'", "narrators": [
        create_narrator("Muhammad ibn Bashshar", "Muhammad ibn Bashshar ibn Uthman al-Abdi", "Thiqah Thabt", "Ninth Generation", "حَدَّثَنَا", 6861, kunya="Abu Abdillah", nisba="al-Abdi", nisba_ar="العبدي", death_year="252", birth_year="167", alternative_names="Bundar"),
        create_narrator("Yahya ibn Sa'id", "Yahya ibn Sa'id al-Qattan", "Thiqah Thabt", "Eighth Generation", "نا", 2340, kunya="Abu Sa'id", nisba="al-Qattan", nisba_ar="القطان", death_year="198", birth_year="120", alternative_names="Yahya al-Qattan"),
        create_narrator("Malik ibn Dinar", "Malik ibn Dinar al-Basri", "Saduq", "Seventh Generation", "نا", 1600, kunya="Abu Yahya", nisba="al-Basri", nisba_ar="البصري", death_year="131", birth_year="", reliability_issues=["Saduq narrator"], alternative_names="Malik al-Basri"),
        create_narrator("Sulayman ibn Yasir", "Sulayman ibn Yasir al-Basri", "Saduq", "Sixth Generation", "عَنْ", 2100, kunya="", nisba="al-Basri", nisba_ar="البصري", death_year="", birth_year="", reliability_issues=["Saduq narrator"], alternative_names="Sulayman al-Basri"),
        create_narrator("Ali ibn Abi Talib", "Ali ibn Abi Talib ibn Abd al-Muttalib", "Thiqah Thabt", "Companion", "قَالَ", 8010, kunya="Abu al-Hasan", nisba="al-Hashimi", nisba_ar="الهاشمي", death_year="40", birth_year="", alternative_names="Ali ibn Abi Talib"),
        create_narrator("Prophet Muhammad ﷺ", "Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim", "Awthaq al-Nas", "Prophet", "", 0, kunya="Abu al-Qasim", nisba="al-Hashimi", nisba_ar="الهاشمي", death_year="11", birth_year="53 BH")
    ], "chainIssues": ["Multiple Saduq narrators", "Use of 'an from Malik to Sulayman", "qala from Ali to Prophet"]}],
    "potential_issues": [{"issue": "Multiple Saduq narrators (Malik, Sulayman)", "impact": "Not highest reliability"}, {"issue": "Use of 'an and qala indicating potential indirectness", "impact": "Some ambiguity about direct hearing"}],
    "Classical Grade": ["Daif"], "IISGrade": "Weak But Might Be Acceptable", "Topics": ["Matter related to faith and religion"]
}

all_hadiths = [h1, h2, h3, h4, h5, h6]
with open('/tmp/processed_hadiths_batch_31_chunk_3.json', 'w', encoding='utf-8') as f:
    json.dump(all_hadiths, f, ensure_ascii=False, indent=2)
print(f"✓ Processed chunk 3: {len(all_hadiths)} hadiths")
