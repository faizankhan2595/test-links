#!/usr/bin/env python3
"""
Enhanced Hadith Processing Script with Complete Narrator Information
Processes enriched hadiths with full narrator details from source data
"""

import json
import re
from typing import List, Dict, Any, Optional

# Hadith-specific translations for common phrases
COMMON_TRANSLATIONS = {
    'قَالَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ': 'The Messenger of Allah ﷺ said:',
    'عَنْ رَسُولِ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ': 'from the Messenger of Allah ﷺ',
    'قَالَ': 'he said',
    'قَالَتْ': 'she said',
    'رَضِيَ اللَّهُ عَنْهَا': 'may Allah be pleased with her',
    'رَضِيَ اللَّهُ عَنْهُ': 'may Allah be pleased with him',
}

# Manual translations for the specific hadiths in batch 1
HADITH_TRANSLATIONS = {
    2: {
        "text": "نِيَّةُ الْمُؤْمِنِ خَيْرٌ مِنْ عَمَلِهِ",
        "translation": "The intention of a believer is better than his deeds.",
        "narrator": "Ibn Abbas",
        "topics": ["Intention and Sincerity", "Actions and Deeds"]
    },
    3: {
        "text": "إِنَّمَا الأَعْمَالُ بِالنِّيَّاتِ وَلِكُلِّ امْرِئٍ مَا نَوَى",
        "translation": "Actions are only by intentions, and every person will have what they intended.",
        "narrator": "Ibn Abbas",
        "topics": ["Intention and Sincerity", "Actions and Deeds"]
    },
    5: {
        "text": "كَيْفَ يَأْتِيكَ الْوَحْيُ",
        "translation": "How does revelation come to you, O Messenger of Allah? He said: 'Sometimes it comes to me like the ringing of a bell, and that is the hardest on me, then it departs from me and I have retained what was said. And sometimes the angel appears to me as a man and speaks to me, and I retain what he says.' Aisha said: 'I saw revelation descending upon him on an extremely cold day, and when it departed from him, his forehead was dripping with perspiration.'",
        "narrator": "Aisha",
        "topics": ["Beginning of Revelation", "Prophetic Biography", "Description of Revelation"]
    },
    7: {
        "text": "عَلِّمُوا أَوْلادَكُمُ الْقُرْآنَ فَإِنَّهُ أَوَّلُ مَا يَنْبَغِي أَنْ يُتَعَلَّمَ مِنْ عِلْمِ اللَّهِ هُوَ",
        "translation": "Teach your children the Quran, for it is the first thing that should be learned from the knowledge of Allah.",
        "narrator": "Jabir ibn Zayd",
        "topics": ["Teaching Quran", "Education", "Raising Children"],
        "chain_issue": "Mursal (disconnected) - Jabir ibn Zayd says 'it reached me' without specifying the source"
    },
    8: {
        "text": "إِذَا قَرَأْتَ الْقُرْآنَ فَرَتِّلْهُ تَرْتِيلا ، وَتَغَنَّوْا بِهِ , فَإِنَّ اللَّهَ يُحِبُّ أَنْ تَسْمَعَ الْمَلائِكَةُ لِذِكْرِهِ",
        "translation": "When you recite the Quran, recite it with tarteel (measured recitation), and beautify it with your voices, for Allah loves that the angels hear His remembrance.",
        "narrator": "Abu Hurayrah",
        "topics": ["Quran Recitation", "Etiquette of Recitation"]
    },
    9: {
        "text": "مَثَلُ صَاحِبِ الْقُرْآنِ ، كَمَثَلِ صَاحِبِ الإِبِلِ الْمُعَقَّلَةِ ، إِنْ عَاهَدَ عَلَيْهَا أَمْسَكَهَا ، وَإِنْ أَطْلَقَهَا ذَهَبَتْ",
        "translation": "The likeness of the companion of the Quran is like the companion of hobbled camels - if he tends to them, he retains them, but if he releases them, they go away.",
        "narrator": "Abu Sa'id al-Khudri",
        "topics": ["Quran Memorization", "Maintaining Quranic Knowledge", "Parables and Similitudes"]
    },
    10: {
        "text": "مَنْ تَعَلَّمَ الْقُرْآنَ ثُمَّ نَسِيَهُ حُشِرَ يَوْمَ الْقِيَامَةِ أَجْذَمَ",
        "translation": "Whoever learns the Quran then forgets it will be resurrected on the Day of Judgment as one cut off (maimed).",
        "narrator": "Ibn Abbas",
        "topics": ["Quran Memorization", "Warning Against Neglecting Quran", "Day of Judgment"]
    },
    11: {
        "text": "مَا جَمَعَ الْقُرْآنَ عَلَى عَهْدِ رَسُولِ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ إِلا سِتَّةُ نَفَرٍ",
        "translation": "No one gathered the Quran during the time of the Messenger of Allah except six people, all of them from the Ansar: Ubayy, Mu'adh, Zayd, Abu Zayd, Abu Ayyub, and Uthman. The rest of the Companions would memorize countable surahs from the Quran, some memorizing one surah and some two surahs.",
        "narrator": "Anas ibn Malik",
        "topics": ["Quran Compilation", "Companions", "Historical Incident of Quran Preservation"]
    },
    12: {
        "text": "قُلْ هُوَ اللَّهُ أَحَدٌ",
        "translation": "A man heard another man reciting 'Say: He is Allah, the One. Allah, the Eternal Refuge. He neither begets nor is born, nor is there to Him any equivalent' and repeating it. When morning came, he went to the Messenger of Allah and mentioned that to him, as if the man was belittling it. The Messenger of Allah said: 'By the One in Whose Hand is my soul, it equals a third of the Quran.'",
        "narrator": "Abu Sa'id al-Khudri",
        "topics": ["Virtues of Surah al-Ikhlas", "Quran Recitation", "Historical Incident"]
    },
    13: {
        "text": "لا يَمَسُّ الْقُرْآنَ إِلا طَاهِرٌ",
        "translation": "None should touch the Quran except one who is pure.",
        "narrator": "Abdullah ibn Umar",
        "topics": ["Purity", "Etiquette of Handling Quran", "Ritual Purification"]
    },
    14: {
        "text": "إِنَّ اللَّهَ يَرْفَعُ بِهَذَا الْكِتَابِ أَقْوَامًا وَيَضَعُ بِهِ آخَرِينَ",
        "translation": "Allah elevates some people by means of this Book and debases others by it.",
        "narrator": "Umar ibn al-Khattab",
        "topics": ["Virtues of Quran", "Warning and Promise", "Status and Honor"]
    },
    15: {
        "text": "خَيْرُكُمْ مَنْ تَعَلَّمَ الْقُرْآنَ وَعَلَّمَهُ",
        "translation": "The best of you are those who learn the Quran and teach it.",
        "narrator": "Uthman ibn Affan",
        "topics": ["Virtues of Teaching Quran", "Excellence and Merit", "Learning and Teaching"]
    }
}

# Narrator information for English names and scholarly evaluation
NARRATOR_ENGLISH_INFO = {
    31544: {
        "english_name": "Abu Ubayda Muslim ibn Abi Karima",
        "full_name_english": "Abu Ubayda Muslim ibn Abi Karima al-Tamimi",
        "grade": "Saduq",
        "generation": "Fourth Generation",
        "notes": "Student of Jabir ibn Zayd, known narrator from Ibadi tradition"
    },
    2063: {
        "english_name": "Jabir ibn Zayd",
        "full_name_english": "Jabir ibn Zayd al-Azdi al-Basri",
        "grade": "Thiqah",
        "generation": "Second Generation (Tabi'in)",
        "notes": "Major Tabi'i scholar, student of Ibn Abbas and Aisha"
    },
    4883: {
        "english_name": "Abdullah ibn Abbas",
        "full_name_english": "Abdullah ibn Abbas ibn Abd al-Muttalib",
        "grade": "Companion",
        "generation": "Companion",
        "notes": "Cousin of the Prophet, 'Hibr al-Umma' (Scholar of the Nation)"
    },
    4049: {
        "english_name": "Aisha",
        "full_name_english": "Aisha bint Abi Bakr al-Siddiq",
        "grade": "Companion",
        "generation": "Companion",
        "notes": "Wife of the Prophet, Mother of the Believers"
    },
    4396: {
        "english_name": "Abu Hurayrah",
        "full_name_english": "Abd al-Rahman ibn Sakhr al-Dawsi",
        "grade": "Companion",
        "generation": "Companion",
        "notes": "Most prolific narrator of hadith among Companions"
    },
    3260: {
        "english_name": "Abu Sa'id al-Khudri",
        "full_name_english": "Sa'd ibn Malik al-Khudri",
        "grade": "Companion",
        "generation": "Companion",
        "notes": "Major Companion narrator"
    },
    720: {
        "english_name": "Anas ibn Malik",
        "full_name_english": "Anas ibn Malik al-Ansari",
        "grade": "Companion",
        "generation": "Companion",
        "notes": "Servant of the Prophet"
    },
    5299: {
        "english_name": "Abdullah ibn Umar",
        "full_name_english": "Abdullah ibn Umar ibn al-Khattab",
        "grade": "Companion",
        "generation": "Companion",
        "notes": "Son of Umar ibn al-Khattab"
    },
    5740: {
        "english_name": "Umar ibn al-Khattab",
        "full_name_english": "Umar ibn al-Khattab al-Adawi",
        "grade": "Companion",
        "generation": "Companion",
        "notes": "Second Caliph of Islam"
    },
    4590: {
        "english_name": "Uthman ibn Affan",
        "full_name_english": "Uthman ibn Affan al-Umawi",
        "grade": "Companion",
        "generation": "Companion",
        "notes": "Third Caliph of Islam, compiler of the Quran"
    }
}


def extract_transmission_term(text_ar: str, position: int) -> str:
    """Extract the transmission term from Arabic text based on narrator position."""
    # Common transmission terms in order of strength
    if 'سَمِعْتُ' in text_ar:
        return 'سَمِعْتُ'
    elif 'حَدَّثَنِي' in text_ar and position == 1:
        return 'حَدَّثَنِي'
    elif 'حَدَّثَنَا' in text_ar and position == 1:
        return 'حَدَّثَنَا'
    elif 'أَخْبَرَنَا' in text_ar:
        return 'أَخْبَرَنَا'
    elif 'أَنْبَأَنَا' in text_ar:
        return 'أَنْبَأَنَا'
    elif 'قَالَ' in text_ar:
        return 'قَالَ'
    else:
        return 'عَنْ'


def create_narrator_object(narrator_data: Dict, text_ar: str) -> Dict:
    """Create a complete narrator object with all information."""
    narrator_id = narrator_data['narrator_id']
    position = narrator_data.get('position_in_isnad', 1)

    # Get English information
    eng_info = NARRATOR_ENGLISH_INFO.get(narrator_id, {
        "english_name": narrator_data.get('primary_name', ''),
        "full_name_english": narrator_data.get('primary_name', ''),
        "grade": narrator_data.get('reliability_grade', 'Unknown') or 'Unknown',
        "generation": "Later Narrator",
        "notes": ""
    })

    # Extract transmission term
    transmission_term = extract_transmission_term(text_ar, position)

    # Build narrator object with all fields
    narrator_obj = {
        # English fields (evaluated)
        "name": eng_info['english_name'],
        "full_name": eng_info['full_name_english'],
        "grade": eng_info['grade'],
        "generation": eng_info['generation'],
        "transmissionTerm": transmission_term,
        "reliabilityIssues": [],
        "notes": eng_info.get('notes', ''),

        # Original data fields from enriched file (in Arabic)
        "narrator_id": narrator_id,
        "original_id": narrator_data.get('original_id'),
        "primary_name": narrator_data.get('primary_name'),
        "alternative_names": narrator_data.get('alternative_names'),
        "kunya": narrator_data.get('kunya'),
        "nisba": narrator_data.get('nisba'),
        "death_year": narrator_data.get('death_year'),
        "birth_year": narrator_data.get('birth_year'),
        "reliability_grade": narrator_data.get('reliability_grade'),
        "tabaqat": narrator_data.get('tabaqat'),
        "location": narrator_data.get('location'),
        "position_in_isnad": position
    }

    return narrator_obj


def evaluate_chain_integrity(narrators: List[Dict]) -> tuple:
    """Evaluate the chain integrity and return grade and issues."""
    issues = []

    if not narrators:
        return "Problematic", ["No narrators in chain"]

    # Check for weak narrators
    weak_grades = ['Da\'if', 'Matruk', 'Munkar al-Hadith', 'Kadhab', 'Layyin al-Hadith', 'Mutaham']
    weak_narrators = [n for n in narrators if n['grade'] in weak_grades]
    if weak_narrators:
        issues.append(f"Contains weak narrator(s): {', '.join([n['name'] for n in weak_narrators])}")

    # Check for unknown narrators
    unknown_narrators = [n for n in narrators if n['grade'] == 'Unknown']
    if unknown_narrators:
        issues.append(f"Contains narrator(s) with unknown status")

    # Check transmission terms
    ambiguous_terms = [n for n in narrators if n['transmissionTerm'] in ['عَنْ', 'قَالَ', 'أَنَّ']]
    if len(ambiguous_terms) > len(narrators) / 2:
        issues.append("Majority of transmission terms are ambiguous")

    # Determine grade based on issues
    if not issues:
        # Check if all narrators are strong
        strong_grades = ['Companion', 'Awthaq al-Nas', 'Thiqah Thabt', 'Thiqah Hafiz', 'Thiqah']
        strong_narrators = [n for n in narrators if n['grade'] in strong_grades]
        if len(strong_narrators) == len(narrators):
            return "Perfect", []
        elif len(strong_narrators) >= len(narrators) * 0.8:
            return "Sound", []
        else:
            return "Acceptable", []
    elif len(issues) == 1 and "unknown status" in issues[0]:
        return "Questionable But Might Be Acceptable", issues
    elif weak_narrators:
        return "Problematic", issues
    else:
        return "Weak But Might Be Acceptable", issues


def determine_hadith_grade(chain_grade: str, issues: List[str]) -> str:
    """Determine overall hadith grade based on chain integrity."""
    if chain_grade == "Perfect":
        return "Sahih"
    elif chain_grade in ["Sound", "Acceptable"]:
        return "Hasan"
    elif "Questionable" in chain_grade or "Weak" in chain_grade:
        return "Da'if"
    else:
        return "Very Weak"


def clean_arabic_text(text: str) -> str:
    """Remove formatting codes from Arabic text."""
    if not text:
        return ""

    # Remove formatting codes like /94, /26, etc.
    cleaned = re.sub(r'/\d+', '', text)
    # Remove L-codes like L31544
    cleaned = re.sub(r'L\d+', '', cleaned)
    # Remove special markers
    cleaned = re.sub(r'[#$]\w+', '', cleaned)
    # Clean up extra whitespace
    cleaned = re.sub(r'\s+', ' ', cleaned)
    cleaned = cleaned.strip()

    return cleaned


def process_hadith(hadith: Dict, trans_info: Dict) -> Optional[Dict]:
    """Process a single hadith with complete narrator information."""
    # Skip if no translation info
    if not trans_info:
        return None

    hadith_id = hadith['hadith_id']
    text_ar = hadith.get('text_ar', '')
    narrators_in_isnad = hadith.get('narrators_in_isnad', [])

    # Build narrator chain with complete information
    narrators_list = []
    for narrator_data in narrators_in_isnad:
        narrator_obj = create_narrator_object(narrator_data, text_ar)
        narrators_list.append(narrator_obj)

    # Reverse to go from original narrator to compiler
    narrators_list.reverse()

    # Create plain chain
    plain_chain = " → ".join([n['name'] for n in narrators_list])
    if narrators_list:
        plain_chain += " → Prophet Muhammad ﷺ"

    # Determine chain issues
    chain_issues = []
    if 'chain_issue' in trans_info:
        chain_issues.append(trans_info['chain_issue'])

    # Evaluate chain integrity
    chain_grade, eval_issues = evaluate_chain_integrity(narrators_list)
    chain_issues.extend(eval_issues)

    # Determine overall grade
    hadith_grade = determine_hadith_grade(chain_grade, chain_issues)

    # Build full translation
    full_translation = f"Narrated by {trans_info['narrator']}: The Prophet ﷺ said: \"{trans_info['translation']}\""

    # Handle special cases
    if hadith_id == 5:  # Aisha's narration about revelation
        full_translation = f"Narrated by {trans_info['narrator']}: Al-Harith ibn Hisham asked the Messenger of Allah ﷺ: \"{trans_info['translation']}\""
    elif hadith_id == 7:  # Mursal from Jabir ibn Zayd
        full_translation = f"It reached {trans_info['narrator']} that the Prophet ﷺ said: \"{trans_info['translation']}\""
    elif hadith_id == 11:  # Statement of Anas
        full_translation = f"Narrated by {trans_info['narrator']}: \"{trans_info['translation']}\""
    elif hadith_id == 12:  # Incident narration
        full_translation = f"Narrated by {trans_info['narrator']}: {trans_info['translation']}"

    # Clean Arabic text
    clean_arabic = clean_arabic_text(text_ar)

    # Get book information
    book_info = hadith.get('book', {})

    # Create processed hadith
    processed = {
        "english_translation": full_translation,
        "chains": [
            {
                "type": "marfu'",
                "narrators": narrators_list,
                "chainIssues": chain_issues
            }
        ],
        "plainChains": [plain_chain] if plain_chain else [],
        "potential_issues": chain_issues,
        "IISGrade": chain_grade,
        "Topics": trans_info['topics'],
        "arabicText": clean_arabic,
        "collection": book_info.get('book_name_ar', 'Unknown'),
        "collection_english": "Book Number 1",  # Translate as needed
        "author_arabic": book_info.get('author_name', 'Unknown Author'),
        "author_english": "Unknown Author",  # Translate as needed
        "reference_number": hadith_id,
        "grade": hadith_grade
    }

    return processed


def main():
    """Main processing function."""
    print("Loading enriched hadiths...")

    # Load input file
    with open('batch_1/enriched_hadiths_1.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    hadiths = data.get('hadiths', [])
    print(f"Found {len(hadiths)} hadiths to process")

    # Process each hadith
    processed_hadiths = []
    skipped = 0

    for hadith in hadiths:
        hadith_id = hadith['hadith_id']

        # Skip chapter headers
        if hadith_id in [1, 4, 6]:
            skipped += 1
            continue

        # Get translation info
        trans_info = HADITH_TRANSLATIONS.get(hadith_id)
        if not trans_info:
            skipped += 1
            continue

        processed = process_hadith(hadith, trans_info)
        if processed:
            processed_hadiths.append(processed)
        else:
            skipped += 1

    print(f"Processed {len(processed_hadiths)} hadiths")
    print(f"Skipped {skipped} entries (chapter headers or incomplete data)")

    # Create output structure
    output = {
        "batch_number": data.get('batch_number'),
        "file_number": data.get('file_number'),
        "record_count": len(processed_hadiths),
        "processing_info": {
            "total_hadiths_in_source": data.get('record_count'),
            "processed_hadiths": len(processed_hadiths),
            "skipped_entries": skipped,
            "processing_notes": [
                "Narrators include complete information from source data",
                "Narrator IDs are preserved from enriched file",
                "Chain integrity assessed using rigorous criteria",
                "Topics classified based on content analysis",
                "All narrator biographical data included in both Arabic and English"
            ]
        },
        "hadiths": processed_hadiths
    }

    # Save output
    output_file = 'batch_1/processed_hadiths_1.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nProcessed data saved to: {output_file}")
    print("\nProcessing Summary:")
    print(f"  - Total hadiths processed: {len(processed_hadiths)}")
    print(f"  - Skipped entries: {skipped}")

    # Print grade distribution
    grade_dist = {}
    for h in processed_hadiths:
        grade = h.get('IISGrade', 'Unknown')
        grade_dist[grade] = grade_dist.get(grade, 0) + 1

    print("\nChain Integrity Grade Distribution:")
    for grade, count in sorted(grade_dist.items()):
        print(f"  - {grade}: {count}")


if __name__ == '__main__':
    main()
