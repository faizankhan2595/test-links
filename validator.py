import json
from typing import Dict, List, Any
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

CLASSICAL_GRADES = ["Sahih", "Hasan", "Daif", "Mursal", "Mawquf", "Maqtu'"]

def validate_hadith(data: Dict[str, Any]) -> tuple[bool, List[str]]:
    errors = []
    
    # Required top-level fields
    required_fields = [
        ("hadith_id", int), ("book_id", int), ("book_name_ar", str),
        ("book_name_en", str), ("author_name_ar", str), ("author_name_en", str),
        ("hadith_number", str), ("english_translation", str), ("chains", list),
        ("potential_issues", list), ("Classical Grade", list), ("IISGrade", str),
        ("Topics", list)
    ]
    
    for field, field_type in required_fields:
        if field not in data:
            errors.append(f"Missing required field: {field}")
        elif not isinstance(data[field], field_type):
            errors.append(f"Field '{field}' must be {field_type.__name__}, got {type(data[field]).__name__}")
    
    # Validate IISGrade
    if "IISGrade" in data and data["IISGrade"] not in IIS_GRADES:
        errors.append(f"Invalid IISGrade: {data['IISGrade']}. Must be one of {IIS_GRADES}")
    
    # Validate Classical Grade
    if "Classical Grade" in data:
        for grade in data["Classical Grade"]:
            if grade not in CLASSICAL_GRADES:
                errors.append(f"Invalid Classical Grade: {grade}. Must be one of {CLASSICAL_GRADES}")
    
    # Validate chains
    if "chains" in data and isinstance(data["chains"], list):
        for idx, chain in enumerate(data["chains"]):
            if not isinstance(chain, dict):
                errors.append(f"Chain {idx} must be a dict")
                continue
            
            if "type" not in chain:
                errors.append(f"Chain {idx} missing 'type'")
            if "narrators" not in chain or not isinstance(chain["narrators"], list):
                errors.append(f"Chain {idx} missing or invalid 'narrators'")
                continue
            
            if "chainIssues" not in chain:
                errors.append(f"Chain {idx} missing 'chainIssues'")
            
            # Validate narrators
            for n_idx, narrator in enumerate(chain["narrators"]):
                narrator_required = [
                    "name", "full_name", "grade", "generation", "transmissionTerm",
                    "reliabilityIssues", "narrator_id", "alternative_names",
                    "original_id", "kunya", "nisba", "nisba_ar", "death_year",
                    "birth_year", "reliability_grade", "tabaqat", "location",
                    "transmissionTermMeaning"
                ]
                
                for field in narrator_required:
                    if field not in narrator:
                        errors.append(f"Chain {idx}, Narrator {n_idx} missing '{field}'")
                
                if "grade" in narrator and narrator["grade"] not in REQUIRED_NARRATOR_GRADES:
                    errors.append(f"Chain {idx}, Narrator {n_idx} has invalid grade: {narrator['grade']}")
    
    # Validate potential_issues
    if "potential_issues" in data and isinstance(data["potential_issues"], list):
        for idx, issue in enumerate(data["potential_issues"]):
            if not isinstance(issue, dict):
                errors.append(f"potential_issues {idx} must be a dict")
                continue
            if "issue" not in issue or "impact" not in issue:
                errors.append(f"potential_issues {idx} must have 'issue' and 'impact'")
    
    return len(errors) == 0, errors

def main():
    if len(sys.argv) < 2:
        print("Usage: python validator.py <json_file>")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        is_valid, errors = validate_hadith(data)
        
        if is_valid:
            print("✓ JSON is valid!")
        else:
            print("✗ Validation failed:")
            for error in errors:
                print(f"  - {error}")
            sys.exit(1)
    
    except FileNotFoundError:
        print(f"Error: File not found: {sys.argv[1]}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON - {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
