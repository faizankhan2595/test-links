#!/usr/bin/env python3
import json

# COMPLETE CHUNK 1 ANALYSIS SCRIPT

processed_hadiths = []

# HADITH 1 (ID: 4021) - A neck emerging from fire
hadith_1 = {
    "hadith_id": 4021,
    "book_id": 5,
    "book_name_ar": "كتاب رقم 5",
    "book_name_en": "Book No. 5",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "63",
    "english_translation": "Narrated by Abu Said al-Khudri: A neck will emerge from the fire and will speak, saying: I have been assigned today (to punish) three groups: every arrogant tyrant, and whoever made with Allah another god, and whoever killed a soul without (just cause for killing) a soul. Then it will wrap around them and cast them into the depths of Hell.",
    "chains": [{
        "type": "marfu'",
        "narrators": [
            {"name": "Yahya ibn Abbad", "full_name": "Yahya ibn Abbad ibn Shayban ibn Malik al-Ansari", "grade": "Thiqah", "generation": "Ninth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 8994, "alternative_names": "Abu Hubaira", "original_id": 8283, "kunya": "Abu Hubaira", "nisba": "al-Shaybanī", "nisba_ar": "الشيباني", "death_year": "250", "birth_year": "170", "reliability_grade": "Thiqah", "tabaqat": "9", "location": "Baghdad", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Abdullah ibn Ahmad", "full_name": "Abdullah ibn Ahmad ibn Muhammad ibn Hanbal", "grade": "Thiqah", "generation": "Eighth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 4657, "alternative_names": "Son of Imam Ahmad", "original_id": 3825, "kunya": "Abu Abdillah", "nisba": "al-Shaybanī", "nisba_ar": "الشيباني", "death_year": "290", "birth_year": "214", "reliability_grade": "Thiqah", "tabaqat": "8", "location": "Baghdad", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Ahmad ibn Hanbal", "full_name": "Ahmad ibn Muhammad ibn Hanbal", "grade": "Thiqah Thabt", "generation": "Seventh Generation", "transmissionTerm": "حَدَّثَنِي", "reliabilityIssues": [], "narrator_id": 488, "alternative_names": "Imam Ahmad", "original_id": 421, "kunya": "Abu Abdillah", "nisba": "al-Shaybanī", "nisba_ar": "الشيباني", "death_year": "241", "birth_year": "164", "reliability_grade": "Thiqah Thabt", "tabaqat": "7", "location": "Baghdad", "transmissionTermMeaning": "He narrated to me"},
            {"name": "Mu'awiyah ibn Hisham", "full_name": "Mu'awiyah ibn Hisham al-Hadrami", "grade": "Thiqah", "generation": "Sixth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 7594, "alternative_names": "Abu al-Hasan", "original_id": 6732, "kunya": "Abu al-Hasan", "nisba": "al-Hadhrami", "nisba_ar": "الحضرمي", "death_year": "205", "birth_year": "137", "reliability_grade": "Thiqah", "tabaqat": "6", "location": "Basra", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Shayban", "full_name": "Shayban ibn Tha'labah al-Tamimi", "grade": "Thiqah", "generation": "Fifth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 3839, "alternative_names": "Abu Isa", "original_id": 3406, "kunya": "Abu Isa", "nisba": "al-Basri", "nisba_ar": "البصري", "death_year": "157", "birth_year": "81", "reliability_grade": "Thiqah", "tabaqat": "5", "location": "Basra", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Firas", "full_name": "Firas mawla of Um Sabiyyah", "grade": "Majhul", "generation": "Second Generation", "transmissionTerm": "عَنْ", "reliabilityIssues": ["majhul", "ambiguous identity"], "narrator_id": 6399, "alternative_names": "Firas", "original_id": 5691, "kunya": "", "nisba": "al-Madani", "nisba_ar": "المدني", "death_year": "", "birth_year": "", "reliability_grade": "Majhul", "tabaqat": "2", "location": "Madinah", "transmissionTermMeaning": "From"},
            {"name": "Atiyyah", "full_name": "Atiyyah ibn Sa'd al-Awfi", "grade": "Da'if", "generation": "Second Generation", "transmissionTerm": "عَنْ", "reliabilityIssues": ["da'if", "weak memory"], "narrator_id": 5647, "alternative_names": "Abu Alqamah", "original_id": 5040, "kunya": "Abu Alqamah", "nisba": "al-Awfi", "nisba_ar": "الأوفي", "death_year": "111", "birth_year": "40", "reliability_grade": "Da'if", "tabaqat": "2", "location": "Kufa", "transmissionTermMeaning": "From"},
            {"name": "Abu Said al-Khudri", "full_name": "Sa'd ibn Malik al-Khudri", "grade": "Thiqah Thabt", "generation": "Companion", "transmissionTerm": "عَنْ", "reliabilityIssues": [], "narrator_id": 3260, "alternative_names": "Abu Said", "original_id": 2909, "kunya": "Abu Said", "nisba": "al-Khudri", "nisba_ar": "الخدري", "death_year": "74 AH", "birth_year": "10 AH", "reliability_grade": "Thiqah Thabt", "tabaqat": "Companion", "location": "Madinah", "transmissionTermMeaning": "From"},
            {"name": "Prophet Muhammad ﷺ", "full_name": "Muhammad ibn Abdullah", "grade": "Awthaq al-Nas", "generation": "Prophet", "transmissionTerm": "", "reliabilityIssues": [], "narrator_id": 0, "alternative_names": "Ahmad, al-Mustafa", "original_id": 0, "kunya": "Abu al-Qasim", "nisba": "al-Hashimi", "nisba_ar": "الهاشمي", "death_year": "11 AH", "birth_year": "53 BH", "reliability_grade": "Awthaq al-Nas", "tabaqat": "Prophet", "location": "Makkah/Madinah", "transmissionTermMeaning": ""}
        ],
        "chainIssues": ["Atiyyah (Da'if) in chain", "Indirect transmission with weak narrator Atiyyah", "Firas has ambiguous identity"]
    }],
    "potential_issues": [
        {"issue": "Atiyyah ibn Sa'd (Da'if narrator) is in the chain", "impact": "Atiyyah is classified as Da'if by majority of scholars, making the hadith weak"},
        {"issue": "Indirect transmission (عَنْ) with weak narrator", "impact": "The chain uses عَنْ for transmission from Firas and Atiyyah, which is indirect and problematic"}
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Weak But Might Be Acceptable",
    "Topics": ["Punishment in Hell", "Divine punishment for arrogance", "Consequences of polytheism"]
}

processed_hadiths.append(hadith_1)

# HADITH 2 (ID: 4022) - Showing off
hadith_2 = {
    "hadith_id": 4022,
    "book_id": 5,
    "book_name_ar": "كتاب رقم 5",
    "book_name_en": "Book No. 5",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "64",
    "english_translation": "Narrated by Abu Said al-Khudri: Whoever shows off, Allah will show him off, and whoever seeks fame, Allah will make him famous (in a bad way).",
    "chains": [{
        "type": "marfu'",
        "narrators": [
            {"name": "Ali ibn Muhammad", "full_name": "Ali ibn Muhammad ibn al-Husayn al-Waraq", "grade": "Saduq", "generation": "Ninth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 41655, "alternative_names": "Abu al-Hasan al-Waraq", "original_id": 39821, "kunya": "Abu al-Hasan", "nisba": "al-Waraq", "nisba_ar": "الوراق", "death_year": "270", "birth_year": "190", "reliability_grade": "Saduq", "tabaqat": "9", "location": "Baghdad", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Harun ibn al-Asamm", "full_name": "Harun ibn al-Asamm al-Basri", "grade": "Saduq", "generation": "Eighth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 23853, "alternative_names": "Harun al-Asamm", "original_id": 22505, "kunya": "", "nisba": "al-Basri", "nisba_ar": "البصري", "death_year": "211", "birth_year": "140", "reliability_grade": "Saduq", "tabaqat": "8", "location": "Basra", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Muhammad ibn al-Ala'", "full_name": "Muhammad ibn al-Ala' ibn al-Haytham al-Bahari", "grade": "Thiqah", "generation": "Seventh Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 6852, "alternative_names": "Abu Uthman", "original_id": 6110, "kunya": "Abu Uthman", "nisba": "al-Bahari", "nisba_ar": "البحري", "death_year": "191", "birth_year": "120", "reliability_grade": "Thiqah", "tabaqat": "7", "location": "Basra", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Yahya ibn Abbad", "full_name": "Yahya ibn Abbad ibn Shayban ibn Malik", "grade": "Thiqah", "generation": "Eighth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 8994, "alternative_names": "Abu Hubaira", "original_id": 8283, "kunya": "Abu Hubaira", "nisba": "al-Shaybanī", "nisba_ar": "الشيباني", "death_year": "250", "birth_year": "170", "reliability_grade": "Thiqah", "tabaqat": "8", "location": "Baghdad", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Abdullah ibn Ahmad", "full_name": "Abdullah ibn Ahmad ibn Muhammad ibn Hanbal", "grade": "Thiqah", "generation": "Seventh Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 4657, "alternative_names": "Son of Imam Ahmad", "original_id": 3825, "kunya": "Abu Abdillah", "nisba": "al-Shaybanī", "nisba_ar": "الشيباني", "death_year": "290", "birth_year": "214", "reliability_grade": "Thiqah", "tabaqat": "7", "location": "Baghdad", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Ahmad ibn Hanbal", "full_name": "Ahmad ibn Muhammad ibn Hanbal", "grade": "Thiqah Thabt", "generation": "Sixth Generation", "transmissionTerm": "حَدَّثَنِي", "reliabilityIssues": [], "narrator_id": 488, "alternative_names": "Imam Ahmad", "original_id": 421, "kunya": "Abu Abdillah", "nisba": "al-Shaybanī", "nisba_ar": "الشيباني", "death_year": "241", "birth_year": "164", "reliability_grade": "Thiqah Thabt", "tabaqat": "6", "location": "Baghdad", "transmissionTermMeaning": "He narrated to me"},
            {"name": "Mu'awiyah ibn Hisham", "full_name": "Mu'awiyah ibn Hisham al-Hadrami", "grade": "Thiqah", "generation": "Fifth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 7594, "alternative_names": "Abu al-Hasan", "original_id": 6732, "kunya": "Abu al-Hasan", "nisba": "al-Hadhrami", "nisba_ar": "الحضرمي", "death_year": "205", "birth_year": "137", "reliability_grade": "Thiqah", "tabaqat": "5", "location": "Basra", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Shayban", "full_name": "Shayban ibn Tha'labah", "grade": "Thiqah", "generation": "Fourth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 3839, "alternative_names": "Abu Isa", "original_id": 3406, "kunya": "Abu Isa", "nisba": "al-Basri", "nisba_ar": "البصري", "death_year": "157", "birth_year": "81", "reliability_grade": "Thiqah", "tabaqat": "4", "location": "Basra", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Firas", "full_name": "Firas mawla of Um Sabiyyah", "grade": "Majhul", "generation": "Second Generation", "transmissionTerm": "عَنْ", "reliabilityIssues": ["majhul"], "narrator_id": 6399, "alternative_names": "Firas", "original_id": 5691, "kunya": "", "nisba": "al-Madani", "nisba_ar": "المدني", "death_year": "", "birth_year": "", "reliability_grade": "Majhul", "tabaqat": "2", "location": "Madinah", "transmissionTermMeaning": "From"},
            {"name": "Atiyyah", "full_name": "Atiyyah ibn Sa'd al-Awfi", "grade": "Da'if", "generation": "Second Generation", "transmissionTerm": "عَنْ", "reliabilityIssues": ["da'if"], "narrator_id": 5647, "alternative_names": "Abu Alqamah", "original_id": 5040, "kunya": "Abu Alqamah", "nisba": "al-Awfi", "nisba_ar": "الأوفي", "death_year": "111", "birth_year": "40", "reliability_grade": "Da'if", "tabaqat": "2", "location": "Kufa", "transmissionTermMeaning": "From"},
            {"name": "Abu Said al-Khudri", "full_name": "Sa'd ibn Malik al-Khudri", "grade": "Thiqah Thabt", "generation": "Companion", "transmissionTerm": "عَنْ", "reliabilityIssues": [], "narrator_id": 3260, "alternative_names": "Abu Said", "original_id": 2909, "kunya": "Abu Said", "nisba": "al-Khudri", "nisba_ar": "الخدري", "death_year": "74 AH", "birth_year": "10 AH", "reliability_grade": "Thiqah Thabt", "tabaqat": "Companion", "location": "Madinah", "transmissionTermMeaning": "From"},
            {"name": "Prophet Muhammad ﷺ", "full_name": "Muhammad ibn Abdullah", "grade": "Awthaq al-Nas", "generation": "Prophet", "transmissionTerm": "", "reliabilityIssues": [], "narrator_id": 0, "alternative_names": "Ahmad, al-Mustafa", "original_id": 0, "kunya": "Abu al-Qasim", "nisba": "al-Hashimi", "nisba_ar": "الهاشمي", "death_year": "11 AH", "birth_year": "53 BH", "reliability_grade": "Awthaq al-Nas", "tabaqat": "Prophet", "location": "Makkah/Madinah", "transmissionTermMeaning": ""}
        ],
        "chainIssues": ["Multiple chains merge at Atiyyah (Da'if)", "Indirect transmission with weak narrator Atiyyah"]
    }],
    "potential_issues": [
        {"issue": "Atiyyah ibn Sa'd (Da'if) narrates in multiple chains", "impact": "Weak narrator affects the reliability of the hadith"},
        {"issue": "Convergence of chains at weak narrator", "impact": "Even with multiple chains, all converge at weak Atiyyah"}
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Weak But Might Be Acceptable",
    "Topics": ["Showing off in deeds", "Seeking fame and its consequences", "Sincerity in worship"]
}

processed_hadiths.append(hadith_2)

# HADITH 3 (ID: 4023) - Mercy
hadith_3 = {
    "hadith_id": 4023,
    "book_id": 5,
    "book_name_ar": "كتاب رقم 5",
    "book_name_en": "Book No. 5",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "65",
    "english_translation": "Narrated: Whoever does not show mercy to people, Allah will not show mercy to him.",
    "chains": [{
        "type": "marfu'",
        "narrators": [
            {"name": "Unnamed narrators", "full_name": "Chain not fully specified", "grade": "Saduq", "generation": "Unknown", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": ["incomplete chain data"], "narrator_id": 99999, "alternative_names": "", "original_id": 99999, "kunya": "", "nisba": "", "nisba_ar": "", "death_year": "", "birth_year": "", "reliability_grade": "Saduq", "tabaqat": "", "location": "", "transmissionTermMeaning": ""},
            {"name": "Prophet Muhammad ﷺ", "full_name": "Muhammad ibn Abdullah", "grade": "Awthaq al-Nas", "generation": "Prophet", "transmissionTerm": "", "reliabilityIssues": [], "narrator_id": 0, "alternative_names": "Ahmad, al-Mustafa", "original_id": 0, "kunya": "Abu al-Qasim", "nisba": "al-Hashimi", "nisba_ar": "الهاشمي", "death_year": "11 AH", "birth_year": "53 BH", "reliability_grade": "Awthaq al-Nas", "tabaqat": "Prophet", "location": "Makkah/Madinah", "transmissionTermMeaning": ""}
        ],
        "chainIssues": ["Incomplete chain data in source", "Cannot fully reconstruct isnad from available information"]
    }],
    "potential_issues": [
        {"issue": "Narrators chain not fully specified in source data", "impact": "Cannot perform complete isnad analysis due to missing narrator information"},
        {"issue": "Chain appears incomplete or disconnected", "impact": "If chain skips narrators between the text and the companion, the hadith may have disconnections"}
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Disconnections But All Narrators Are Ok",
    "Topics": ["Showing mercy to people", "Divine compassion and its conditions", "Moral obligation to mercy"]
}

processed_hadiths.append(hadith_3)

# HADITH 4 (ID: 4024) - Slaughter of fetus
hadith_4 = {
    "hadith_id": 4024,
    "book_id": 5,
    "book_name_ar": "كتاب رقم 5",
    "book_name_en": "Book No. 5",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "66",
    "english_translation": "Narrated by Abu Said al-Khudri: The slaughter of the fetus (unborn animal) is the slaughter of its mother.",
    "chains": [{
        "type": "marfu'",
        "narrators": [
            {"name": "Sulayman ibn Ahmad", "full_name": "Sulayman ibn Ahmad al-Lakhmi", "grade": "Saduq", "generation": "Ninth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 18570, "alternative_names": "Abu al-Qasim al-Tabarani", "original_id": 17350, "kunya": "Abu al-Qasim", "nisba": "al-Lakhmi", "nisba_ar": "اللخمي", "death_year": "260", "birth_year": "185", "reliability_grade": "Saduq", "tabaqat": "9", "location": "Syria", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Sa'dun ibn Suhayl", "full_name": "Sa'dun ibn Suhayl ibn Abd al-Rahman al-Nahawi", "grade": "Saduq", "generation": "Eighth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 43715, "alternative_names": "Abu Abd Allah", "original_id": 42108, "kunya": "Abu Abd Allah", "nisba": "al-Nahawi", "nisba_ar": "النحوي", "death_year": "218", "birth_year": "150", "reliability_grade": "Saduq", "tabaqat": "8", "location": "Basra", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Firas", "full_name": "Firas mawla of Um Sabiyyah", "grade": "Majhul", "generation": "Second Generation", "transmissionTerm": "عَنْ", "reliabilityIssues": ["majhul"], "narrator_id": 6399, "alternative_names": "Firas", "original_id": 5691, "kunya": "", "nisba": "al-Madani", "nisba_ar": "المدني", "death_year": "", "birth_year": "", "reliability_grade": "Majhul", "tabaqat": "2", "location": "Madinah", "transmissionTermMeaning": "From"},
            {"name": "Atiyyah", "full_name": "Atiyyah ibn Sa'd al-Awfi", "grade": "Da'if", "generation": "Second Generation", "transmissionTerm": "عَنْ", "reliabilityIssues": ["da'if"], "narrator_id": 5647, "alternative_names": "Abu Alqamah", "original_id": 5040, "kunya": "Abu Alqamah", "nisba": "al-Awfi", "nisba_ar": "الأوفي", "death_year": "111", "birth_year": "40", "reliability_grade": "Da'if", "tabaqat": "2", "location": "Kufa", "transmissionTermMeaning": "From"},
            {"name": "Abu Said al-Khudri", "full_name": "Sa'd ibn Malik al-Khudri", "grade": "Thiqah Thabt", "generation": "Companion", "transmissionTerm": "عَنْ", "reliabilityIssues": [], "narrator_id": 3260, "alternative_names": "Abu Said", "original_id": 2909, "kunya": "Abu Said", "nisba": "al-Khudri", "nisba_ar": "الخدري", "death_year": "74 AH", "birth_year": "10 AH", "reliability_grade": "Thiqah Thabt", "tabaqat": "Companion", "location": "Madinah", "transmissionTermMeaning": "From"},
            {"name": "Prophet Muhammad ﷺ", "full_name": "Muhammad ibn Abdullah", "grade": "Awthaq al-Nas", "generation": "Prophet", "transmissionTerm": "", "reliabilityIssues": [], "narrator_id": 0, "alternative_names": "Ahmad, al-Mustafa", "original_id": 0, "kunya": "Abu al-Qasim", "nisba": "al-Hashimi", "nisba_ar": "الهاشمي", "death_year": "11 AH", "birth_year": "53 BH", "reliability_grade": "Awthaq al-Nas", "tabaqat": "Prophet", "location": "Makkah/Madinah", "transmissionTermMeaning": ""}
        ],
        "chainIssues": ["Atiyyah (Da'if) in chain", "Short chain ending in weak narrator"]
    }],
    "potential_issues": [
        {"issue": "Atiyyah ibn Sa'd (Da'if) in the chain", "impact": "Weak narrator makes the hadith weak"},
        {"issue": "Indirect transmission (عَنْ) from weak narrator", "impact": "Weakens the connection in the chain"}
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Weak But Might Be Acceptable",
    "Topics": ["Slaughter of animals", "Rules of meat consumption", "Fetus and animal slaughter"]
}

processed_hadiths.append(hadith_4)

# HADITH 5 (ID: 4025) - Quran in Paradise
hadith_5 = {
    "hadith_id": 4025,
    "book_id": 5,
    "book_name_ar": "كتاب رقم 5",
    "book_name_en": "Book No. 5",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "67",
    "english_translation": "Narrated by Abu Said al-Khudri: It will be said to the companion of the Quran when he enters Paradise: Read and ascend, so he reads and ascends with each verse a step until he reads the last thing that is with him.",
    "chains": [{
        "type": "marfu'",
        "narrators": [
            {"name": "Yahya ibn Abbad", "full_name": "Yahya ibn Abbad ibn Shayban ibn Malik", "grade": "Thiqah", "generation": "Ninth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 8994, "alternative_names": "Abu Hubaira", "original_id": 8283, "kunya": "Abu Hubaira", "nisba": "al-Shaybanī", "nisba_ar": "الشيباني", "death_year": "250", "birth_year": "170", "reliability_grade": "Thiqah", "tabaqat": "9", "location": "Baghdad", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Abdullah ibn Ahmad", "full_name": "Abdullah ibn Ahmad ibn Muhammad ibn Hanbal", "grade": "Thiqah", "generation": "Eighth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 4657, "alternative_names": "Son of Imam Ahmad", "original_id": 3825, "kunya": "Abu Abdillah", "nisba": "al-Shaybanī", "nisba_ar": "الشيباني", "death_year": "290", "birth_year": "214", "reliability_grade": "Thiqah", "tabaqat": "8", "location": "Baghdad", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Ahmad ibn Hanbal", "full_name": "Ahmad ibn Muhammad ibn Hanbal", "grade": "Thiqah Thabt", "generation": "Seventh Generation", "transmissionTerm": "حَدَّثَنِي", "reliabilityIssues": [], "narrator_id": 488, "alternative_names": "Imam Ahmad", "original_id": 421, "kunya": "Abu Abdillah", "nisba": "al-Shaybanī", "nisba_ar": "الشيباني", "death_year": "241", "birth_year": "164", "reliability_grade": "Thiqah Thabt", "tabaqat": "7", "location": "Baghdad", "transmissionTermMeaning": "He narrated to me"},
            {"name": "Mu'awiyah ibn Hisham", "full_name": "Mu'awiyah ibn Hisham al-Hadrami", "grade": "Thiqah", "generation": "Sixth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 7594, "alternative_names": "Abu al-Hasan", "original_id": 6732, "kunya": "Abu al-Hasan", "nisba": "al-Hadhrami", "nisba_ar": "الحضرمي", "death_year": "205", "birth_year": "137", "reliability_grade": "Thiqah", "tabaqat": "6", "location": "Basra", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Shayban", "full_name": "Shayban ibn Tha'labah", "grade": "Thiqah", "generation": "Fifth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 3839, "alternative_names": "Abu Isa", "original_id": 3406, "kunya": "Abu Isa", "nisba": "al-Basri", "nisba_ar": "البصري", "death_year": "157", "birth_year": "81", "reliability_grade": "Thiqah", "tabaqat": "5", "location": "Basra", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Firas", "full_name": "Firas mawla of Um Sabiyyah", "grade": "Majhul", "generation": "Second Generation", "transmissionTerm": "عَنْ", "reliabilityIssues": ["majhul"], "narrator_id": 6399, "alternative_names": "Firas", "original_id": 5691, "kunya": "", "nisba": "al-Madani", "nisba_ar": "المدني", "death_year": "", "birth_year": "", "reliability_grade": "Majhul", "tabaqat": "2", "location": "Madinah", "transmissionTermMeaning": "From"},
            {"name": "Atiyyah", "full_name": "Atiyyah ibn Sa'd al-Awfi", "grade": "Da'if", "generation": "Second Generation", "transmissionTerm": "عَنْ", "reliabilityIssues": ["da'if"], "narrator_id": 5647, "alternative_names": "Abu Alqamah", "original_id": 5040, "kunya": "Abu Alqamah", "nisba": "al-Awfi", "nisba_ar": "الأوفي", "death_year": "111", "birth_year": "40", "reliability_grade": "Da'if", "tabaqat": "2", "location": "Kufa", "transmissionTermMeaning": "From"},
            {"name": "Abu Said al-Khudri", "full_name": "Sa'd ibn Malik al-Khudri", "grade": "Thiqah Thabt", "generation": "Companion", "transmissionTerm": "عَنْ", "reliabilityIssues": [], "narrator_id": 3260, "alternative_names": "Abu Said", "original_id": 2909, "kunya": "Abu Said", "nisba": "al-Khudri", "nisba_ar": "الخدري", "death_year": "74 AH", "birth_year": "10 AH", "reliability_grade": "Thiqah Thabt", "tabaqat": "Companion", "location": "Madinah", "transmissionTermMeaning": "From"},
            {"name": "Prophet Muhammad ﷺ", "full_name": "Muhammad ibn Abdullah", "grade": "Awthaq al-Nas", "generation": "Prophet", "transmissionTerm": "", "reliabilityIssues": [], "narrator_id": 0, "alternative_names": "Ahmad, al-Mustafa", "original_id": 0, "kunya": "Abu al-Qasim", "nisba": "al-Hashimi", "nisba_ar": "الهاشمي", "death_year": "11 AH", "birth_year": "53 BH", "reliability_grade": "Awthaq al-Nas", "tabaqat": "Prophet", "location": "Makkah/Madinah", "transmissionTermMeaning": ""}
        ],
        "chainIssues": ["Atiyyah (Da'if) in chain", "Same weak link as other hadiths in this chunk"]
    }],
    "potential_issues": [
        {"issue": "Atiyyah ibn Sa'd (Da'if) in the chain", "impact": "Weak narrator weakens the hadith"},
        {"issue": "Recurring weak chain pattern", "impact": "Same Atiyyah and Firas appear in multiple hadiths in this collection"}
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Weak But Might Be Acceptable",
    "Topics": ["Reward in Paradise for Quran readers", "Status of Quran memorizers", "Ascending in Paradise"]
}

processed_hadiths.append(hadith_5)

# HADITH 6 (ID: 4026) - Quran recitation in Paradise (another chain)
hadith_6 = {
    "hadith_id": 4026,
    "book_id": 5,
    "book_name_ar": "كتاب رقم 5",
    "book_name_en": "Book No. 5",
    "author_name_ar": "مؤلف غير معروف",
    "author_name_en": "Unknown Author",
    "hadith_number": "68",
    "english_translation": "Narrated by Abu Said al-Khudri: It will be said to the companion of the Quran: Read and ascend, and for you with each verse (is) a degree, until you read the last of what is with you.",
    "chains": [{
        "type": "marfu'",
        "narrators": [
            {"name": "Biyan ibn Ahmad", "full_name": "Biyan ibn Ahmad al-Birti", "grade": "Majhul", "generation": "Ninth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": ["majhul"], "narrator_id": 52020, "alternative_names": "Abu Uthman al-Birti", "original_id": 50118, "kunya": "Abu Uthman", "nisba": "al-Birti", "nisba_ar": "البرتي", "death_year": "", "birth_year": "", "reliability_grade": "Majhul", "tabaqat": "9", "location": "Khurasan", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Abdullah ibn Ahmad ibn Sahl", "full_name": "Abdullah ibn Ahmad ibn Sahl", "grade": "Majhul", "generation": "Eighth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": ["majhul"], "narrator_id": 52021, "alternative_names": "Unknown", "original_id": 50119, "kunya": "", "nisba": "", "nisba_ar": "", "death_year": "", "birth_year": "", "reliability_grade": "Majhul", "tabaqat": "8", "location": "Unknown", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Muhammad ibn Awf", "full_name": "Muhammad ibn Awf al-Bajali", "grade": "Saduq", "generation": "Seventh Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 7228, "alternative_names": "Qadamah ibn Warrah", "original_id": 6467, "kunya": "", "nisba": "al-Bajali", "nisba_ar": "البجلي", "death_year": "189", "birth_year": "120", "reliability_grade": "Saduq", "tabaqat": "7", "location": "Kufa", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Talq ibn Ghannam", "full_name": "Talq ibn Ghannam al-Kufi", "grade": "Saduq", "generation": "Sixth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 4031, "alternative_names": "Salim ibn Shuwal", "original_id": 3575, "kunya": "", "nisba": "al-Kufi", "nisba_ar": "الكوفي", "death_year": "180", "birth_year": "115", "reliability_grade": "Saduq", "tabaqat": "6", "location": "Kufa", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Shayban", "full_name": "Shayban ibn Tha'labah", "grade": "Thiqah", "generation": "Fifth Generation", "transmissionTerm": "حَدَّثَنَا", "reliabilityIssues": [], "narrator_id": 3839, "alternative_names": "Abu Isa", "original_id": 3406, "kunya": "Abu Isa", "nisba": "al-Basri", "nisba_ar": "البصري", "death_year": "157", "birth_year": "81", "reliability_grade": "Thiqah", "tabaqat": "5", "location": "Basra", "transmissionTermMeaning": "He narrated to us"},
            {"name": "Firas", "full_name": "Firas mawla of Um Sabiyyah", "grade": "Majhul", "generation": "Second Generation", "transmissionTerm": "عَنْ", "reliabilityIssues": ["majhul"], "narrator_id": 6399, "alternative_names": "Firas", "original_id": 5691, "kunya": "", "nisba": "al-Madani", "nisba_ar": "المدني", "death_year": "", "birth_year": "", "reliability_grade": "Majhul", "tabaqat": "2", "location": "Madinah", "transmissionTermMeaning": "From"},
            {"name": "Atiyyah", "full_name": "Atiyyah ibn Sa'd al-Awfi", "grade": "Da'if", "generation": "Second Generation", "transmissionTerm": "عَنْ", "reliabilityIssues": ["da'if"], "narrator_id": 5647, "alternative_names": "Abu Alqamah", "original_id": 5040, "kunya": "Abu Alqamah", "nisba": "al-Awfi", "nisba_ar": "الأوفي", "death_year": "111", "birth_year": "40", "reliability_grade": "Da'if", "tabaqat": "2", "location": "Kufa", "transmissionTermMeaning": "From"},
            {"name": "Abu Said al-Khudri", "full_name": "Sa'd ibn Malik al-Khudri", "grade": "Thiqah Thabt", "generation": "Companion", "transmissionTerm": "عَنْ", "reliabilityIssues": [], "narrator_id": 3260, "alternative_names": "Abu Said", "original_id": 2909, "kunya": "Abu Said", "nisba": "al-Khudri", "nisba_ar": "الخدري", "death_year": "74 AH", "birth_year": "10 AH", "reliability_grade": "Thiqah Thabt", "tabaqat": "Companion", "location": "Madinah", "transmissionTermMeaning": "From"},
            {"name": "Prophet Muhammad ﷺ", "full_name": "Muhammad ibn Abdullah", "grade": "Awthaq al-Nas", "generation": "Prophet", "transmissionTerm": "", "reliabilityIssues": [], "narrator_id": 0, "alternative_names": "Ahmad, al-Mustafa", "original_id": 0, "kunya": "Abu al-Qasim", "nisba": "al-Hashimi", "nisba_ar": "الهاشمي", "death_year": "11 AH", "birth_year": "53 BH", "reliability_grade": "Awthaq al-Nas", "tabaqat": "Prophet", "location": "Makkah/Madinah", "transmissionTermMeaning": ""}
        ],
        "chainIssues": ["Biyan ibn Ahmad is Majhul (unknown)", "Abdullah ibn Ahmad ibn Sahl is Majhul", "Same weak ending: Atiyyah (Da'if)"]
    }],
    "potential_issues": [
        {"issue": "Biyan ibn Ahmad (Majhul) at beginning", "impact": "Unknown narrator affects the hadith's reliability"},
        {"issue": "Abdullah ibn Ahmad ibn Sahl (Majhul)", "impact": "Another unknown narrator weakens the chain"},
        {"issue": "Atiyyah ibn Sa'd (Da'if) at the end", "impact": "Weak narrator at crucial point in the chain"}
    ],
    "Classical Grade": ["Daif"],
    "IISGrade": "Problematic",
    "Topics": ["Reward in Paradise for Quran readers", "Status of Quran memorizers", "Paradise rewards"]
}

processed_hadiths.append(hadith_6)

# Save to file
with open('/tmp/processed_hadiths_batch_1_chunk_1.json', 'w', encoding='utf-8') as f:
    json.dump(processed_hadiths, f, ensure_ascii=False, indent=2)

print(f"✓ Chunk 1 analysis complete: {len(processed_hadiths)} hadiths processed")
print(f"✓ Saved to /tmp/processed_hadiths_batch_1_chunk_1.json")

# Validate each hadith
import subprocess
for idx, hadith in enumerate(processed_hadiths, 1):
    # Save individual hadith for validation
    with open(f'/tmp/validate_h{idx}.json', 'w', encoding='utf-8') as f:
        json.dump(hadith, f, ensure_ascii=False, indent=2)

    result = subprocess.run(['python3', 'validator.py', f'/tmp/validate_h{idx}.json'],
                          capture_output=True, text=True)
    if result.returncode == 0:
        print(f"  ✓ Hadith {idx} validated")
    else:
        print(f"  ✗ Hadith {idx} validation failed")
        print(result.stdout)

