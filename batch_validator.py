import json
import sys
from pathlib import Path

# Import the validator module
sys.path.insert(0, '/home/user/test-links')
from validator import validate_hadith, REQUIRED_NARRATOR_GRADES, IIS_GRADES, CLASSICAL_GRADES

def validate_batch_file(file_path):
    """Validate a batch file containing multiple hadiths (as an array)"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not isinstance(data, list):
            print(f"✗ Error: Root must be an array of hadith objects")
            return False
        
        print(f"\nValidating {file_path} ({len(data)} hadiths)...")
        all_valid = True
        
        for idx, hadith in enumerate(data):
            is_valid, errors = validate_hadith(hadith)
            
            hadith_id = hadith.get('hadith_id', 'UNKNOWN')
            if is_valid:
                print(f"  ✓ Hadith {hadith_id} (#{idx+1}): VALID")
            else:
                print(f"  ✗ Hadith {hadith_id} (#{idx+1}): INVALID")
                for error in errors:
                    print(f"    - {error}")
                all_valid = False
        
        return all_valid
    
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return False
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON - {e}")
        return False

def main():
    batch_dir = Path('/home/user/test-links/batch_1')
    chunk_files = sorted(batch_dir.glob('processed_hadiths_batch_1_chunk_*.json'))
    
    print("=" * 60)
    print("BATCH HADITH VALIDATION REPORT")
    print("=" * 60)
    
    all_files_valid = True
    total_hadiths = 0
    
    for chunk_file in chunk_files:
        file_valid = validate_batch_file(str(chunk_file))
        all_files_valid = all_files_valid and file_valid
        
        with open(chunk_file) as f:
            data = json.load(f)
            total_hadiths += len(data)
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total chunk files: {len(chunk_files)}")
    print(f"Total hadiths validated: {total_hadiths}")
    
    if all_files_valid:
        print("✓ ALL HADITHS PASSED VALIDATION")
        return 0
    else:
        print("✗ SOME HADITHS FAILED VALIDATION")
        return 1

if __name__ == "__main__":
    sys.exit(main())
