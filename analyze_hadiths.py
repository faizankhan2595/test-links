#!/usr/bin/env python3
"""
Helper script to validate individual hadith analyses against the JSON schema
"""
import json
import sys

REQUIRED_NARRATOR_GRADES = [
    "Awthaq al-Nas", "Thabt Hujjah", "Thabt Hafiz", "Thiqah Thabt", "Thiqah",
    "Thiqah Yukhti'", "La Ba'sa Bihi", "Saduq", "Sadooq", "Saduq/Sadooq", "Saduq Yahim",
    "Saduq Lahu Awham", "Saduq Sayyi' al-Hifz", "Saduq Yugrib", "Saduq Yukhtī",
    "Maqbul", "Layyin al-Hadith", "Majhul", "Majhul al-Hal", "Da'if",
    "Da'if Jiddan", "Munkar al-Hadith", "Matruk", "Matruk al-Hadith",
    "Kadhdhab", "Wadda'"
]

IIS_GRADES = ["Perfect", "Sound", "Acceptable", "Questionable But Might Be Acceptable",
              "Weak But Might Be Acceptable", "Disconnections But All Narrators Are Ok", "Problematic"]

CLASSICAL_GRADES = ["Sahih", "Hasan", "Daif", "Mursal", "Maqtu'", "Mawquf"]

def validate_hadith(hadith_dict):
    """Validate single hadith JSON structure"""
    errors = []

    # Check required top-level fields
    required_fields = [
        "hadith_id", "book_id", "book_name_ar", "book_name_en",
        "author_name_ar", "author_name_en", "hadith_number",
        "english_translation", "chains", "potential_issues",
        "Classical Grade", "IISGrade", "Topics"
    ]

    for field in required_fields:
        if field not in hadith_dict:
            errors.append(f"Missing: {field}")
        elif field in ["english_translation"] and not hadith_dict[field]:
            errors.append(f"Empty: {field}")

    # Check IISGrade
    if "IISGrade" in hadith_dict and hadith_dict["IISGrade"] not in IIS_GRADES:
        errors.append(f"Invalid IISGrade: {hadith_dict['IISGrade']}")

    # Check Classical Grade
    if "Classical Grade" in hadith_dict:
        for grade in hadith_dict["Classical Grade"]:
            if grade not in CLASSICAL_GRADES:
                errors.append(f"Invalid Classical Grade: {grade}")

    # Check chains
    if "chains" in hadith_dict:
        for chain_idx, chain in enumerate(hadith_dict["chains"]):
            if "type" not in chain:
                errors.append(f"Chain {chain_idx}: missing 'type'")
            if "narrators" not in chain or not isinstance(chain["narrators"], list):
                errors.append(f"Chain {chain_idx}: invalid 'narrators'")
            if "chainIssues" not in chain:
                errors.append(f"Chain {chain_idx}: missing 'chainIssues'")

            # Check narrators
            required_narrator_fields = [
                "name", "full_name", "grade", "generation", "transmissionTerm",
                "reliabilityIssues", "narrator_id", "alternative_names",
                "original_id", "kunya", "nisba", "nisba_ar", "death_year",
                "birth_year", "reliability_grade", "tabaqat", "location",
                "transmissionTermMeaning"
            ]

            for narrator_idx, narrator in enumerate(chain.get("narrators", [])):
                for field in required_narrator_fields:
                    if field not in narrator:
                        errors.append(f"Chain {chain_idx}, Narrator {narrator_idx}: missing '{field}'")

                if "grade" in narrator and narrator["grade"] not in REQUIRED_NARRATOR_GRADES:
                    errors.append(f"Chain {chain_idx}, Narrator {narrator_idx}: invalid grade '{narrator['grade']}'")

    return len(errors) == 0, errors

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_hadiths.py <hadith.json>")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            data = json.load(f)

        is_valid, errors = validate_hadith(data)

        if is_valid:
            print(f"✓ Hadith {data.get('hadith_id', 'unknown')} is valid!")
            sys.exit(0)
        else:
            print(f"✗ Hadith {data.get('hadith_id', 'unknown')} validation failed:")
            for error in errors:
                print(f"  - {error}")
            sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON - {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File not found - {sys.argv[1]}")
        sys.exit(1)
