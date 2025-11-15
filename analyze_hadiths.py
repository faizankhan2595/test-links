#!/usr/bin/env python3
"""
Hadith Analysis Framework
Converts raw hadith data to fully analyzed format with IIS grading
"""

import json
import re
from typing import Dict, List, Any

def extract_transmission_term(text: str, pos: int) -> str:
    """Extract transmission term before a given position"""
    search_text = text[max(0, pos-50):pos]

    terms = {
        'حَدَّثَنَا': 'He narrated to us (direct hearing)',
        'ثنا': 'He narrated to us (direct hearing)',
        'نا': 'He narrated to us (direct hearing)',
        'أَخْبَرَنَا': 'He informed us (direct)',
        'أخبرنا': 'He informed us (direct)',
        'عَنْ': 'From (could be direct or indirect)',
        'عن': 'From (could be direct or indirect)',
        'قَالَ': 'He said',
        'قال': 'He said',
        'أنَّ': 'That (often indicates disconnection)',
        'بَلَغَنِي': 'Reached me (without direct chain)',
    }

    for term, meaning in terms.items():
        if term in search_text:
            return term

    return ''

def parse_chain_from_text(text_ar: str) -> List[Dict[str, Any]]:
    """Parse the complete chain from Arabic text"""
    # Extract narrators with their IDs
    pattern = r'([^/\d\n]+?)\s*L(\d+)'
    matches = re.findall(pattern, text_ar)

    chain = []
    for name, id_num in matches:
        name_clean = name.strip().replace('،', '').replace('/', '')
        idx_pos = text_ar.find('L' + id_num)
        term = extract_transmission_term(text_ar, idx_pos)

        chain.append({
            'narrator_id': int(id_num),
            'name': name_clean,
            'transmission_term': term,
            'position': len(chain)
        })

    return chain

def extract_matn_text(text_ar: str) -> str:
    """Extract the actual hadith text (matn) from the full text"""
    # Find where the actual hadith content begins
    markers = ['قَالَ :', 'قال :', 'يَقُولُ :', 'يقول:', 'سَمِعْتُ', 'سمعت']

    for marker in markers:
        pos = text_ar.find(marker)
        if pos > -1:
            # Get text after marker, excluding page references
            matn = text_ar[pos:].split('@')[0].split('*')[0]
            # Clean formatting codes
            matn = re.sub(r'L\d+|/\d+', '', matn).strip()
            return matn

    return ''

def translate_matn_to_english(matn_ar: str, hadith_id: int) -> str:
    """Translate hadith to English (literal translation)"""
    # This would be done manually for each hadith based on its content
    # For now, returning placeholder that will be filled with actual translation
    return f"[Translation for hadith ID {hadith_id} to be filled]"

# Hadith-specific analyses
HADITH_ANALYSES = {
    270211: {
        'english_translation': 'Narrated by Abu Sudah: I heard the Messenger of Allah ﷺ saying: "The false oath by which a man seizes the wealth of a Muslim extinguishes/prevents childbirth."',
        'chain_type': 'marfu\'',
        'classical_grade': ['Daif'],
        'iis_grade': 'Weak But Might Be Acceptable',
        'issues': [
            {
                'issue': 'Unnamed narrator in the chain (just called "sheik" from Bani Tamim)',
                'impact': 'This creates a Majhul (unknown) narrator in the chain, making the hadith weaker as the narrator cannot be properly evaluated.'
            },
            {
                'issue': 'Multiple indirect transmission terms (عَنْ) in succession',
                'impact': 'Increases ambiguity about direct contact between narrators, though Abdullah ibn al-Mubarak and Yahya ibn Adam are reliable, this still weakens the chain somewhat.'
            },
            {
                'issue': 'Mu\'ammar narrating from an unnamed sheikh',
                'impact': 'Even though Mu\'ammar is a reliable narrator, without knowing the sheikh\'s identity, we cannot assess the reliability of this link.'
            }
        ],
        'topics': [
            'Incident of the Prophet\'s statement about false oaths',
            'Consequences of false oath',
            'Effects of false oath on fertility'
        ]
    },
    270222: {
        'english_translation': 'Narrated by Usamah ibn Akhdariyy: A man said to the Messenger of Allah ﷺ: "O Messenger of Allah, I desired that you would name him and supplicate for him..."',
        'chain_type': 'marfu\'',
        'classical_grade': ['Hasan'],
        'iis_grade': 'Acceptable',
        'issues': [
            {
                'issue': 'Bashir ibn Maimun narrating with indirect terms',
                'impact': 'While the chain contains reliable narrators, the transmission terms suggest some ambiguity in direct transmission.'
            }
        ],
        'topics': [
            'Incident of a man requesting the Prophet to name his child',
            'Seeking supplication from the Prophet ﷺ',
            'Naming of children in Islam'
        ]
    },
    270224: {
        'english_translation': 'Narrated by Abdullah ibn Abd al-Rahman ibn Safwan: I migrated with my father to the Messenger of Allah ﷺ...',
        'chain_type': 'marfu\'',
        'classical_grade': ['Hasan'],
        'iis_grade': 'Acceptable',
        'issues': [],
        'topics': [
            'Incident of migration to the Prophet ﷺ',
            'Family\'s seeking guidance from the Prophet ﷺ',
            'Acceptance in the Islamic community'
        ]
    },
    270226: {
        'english_translation': 'Narrated by Ibn Abi al-Jad\'a: I sat with a group of Companions of the Prophet ﷺ...',
        'chain_type': 'marfu\'',
        'classical_grade': ['Hasan'],
        'iis_grade': 'Acceptable',
        'issues': [
            {
                'issue': 'Abdullah ibn Shaqiq narrating from multiple Companions',
                'impact': 'Abdullah ibn Shaqiq is generally reliable, making this chain acceptable despite the indirect transmission.'
            }
        ],
        'topics': [
            'Conversation among Companions about Islamic teachings',
            'Companions\' knowledge and wisdom'
        ]
    },
    270228: {
        'english_translation': 'Narrated by Sulik ibn Hudba: The Messenger of Allah ﷺ asked him: "Did you perform Ruku (bowing)?"...',
        'chain_type': 'marfu\'',
        'classical_grade': ['Hasan'],
        'iis_grade': 'Acceptable',
        'issues': [
            {
                'issue': 'Hisham narrating with عَنْ from al-Hasan',
                'impact': 'While both are reliable, the indirect transmission slightly weakens the certainty of transmission.'
            }
        ],
        'topics': [
            'Incident of someone not performing Ruku properly',
            'Prayer perfection and its significance',
            'The Prophet\'s teaching on correct prayer methodology'
        ]
    },
    270230: {
        'english_translation': 'Narrated by Amr ibn Sulayman al-Awfi: "The ancestries were presented to me and I saw the ancestry of Bani Amir as a camel..."',
        'chain_type': 'marfu\'',
        'classical_grade': ['Daif'],
        'iis_grade': 'Questionable But Might Be Acceptable',
        'issues': [
            {
                'issue': 'Ismail ibn Ayyash is known to be weak when narrating from people outside of Syria',
                'impact': 'Even though this chain includes Ismail ibn Ayyash, his general weakness affects the reliability of the hadith.'
            },
            {
                'issue': 'Bishr ibn Abdullah is not well-documented',
                'impact': 'Limited biographical information makes evaluation of this narrator difficult.'
            }
        ],
        'topics': [
            'The Prophet\'s vision of ancestries',
            'Discussion of genealogies',
            'Metaphorical descriptions in the Quran and Hadith'
        ]
    },
    270232: {
        'english_translation': 'Narrated by al-Hasan: "I was circumambulating around the House (Kaaba) during the time of Uthman (may Allah be pleased with him)..."',
        'chain_type': 'marfu\'',
        'classical_grade': ['Hasan'],
        'iis_grade': 'Acceptable',
        'issues': [
            {
                'issue': 'Ali ibn Zaid ibn Jadaan is known to be weak as a narrator',
                'impact': 'Ali ibn Zaid ibn Jadaan is criticized by some scholars, though some accept him as Saduq, making this chain questionable.'
            }
        ],
        'topics': [
            'Tawaf (circumambulation) around the Kaaba',
            'Practice of worship during different Islamic periods',
            'Uthman ibn Affan\'s era and Islamic practice'
        ]
    },
    270234: {
        'english_translation': 'Narrated by Umm Amr al-Suraymmiyyah: My uncle narrated to me that he was with the Prophet ﷺ...',
        'chain_type': 'marfu\'',
        'classical_grade': ['Hasan'],
        'iis_grade': 'Acceptable',
        'issues': [
            {
                'issue': 'Narration from a female companion through her uncle',
                'impact': 'While the chain contains reliable narrators, the transmission through family members requires careful evaluation.'
            }
        ],
        'topics': [
            'Narration from a female companion',
            'Incident involving the Prophet ﷺ',
            'Teaching transmitted through women in Islamic tradition'
        ]
    },
    270236: {
        'english_translation': 'Narrated by Sharahil: Abu Zaid al-Hawzani said that Sharahil said...',
        'chain_type': 'marfu\'',
        'classical_grade': ['Hasan'],
        'iis_grade': 'Acceptable',
        'issues': [
            {
                'issue': 'Ismail ibn Ayyash narrating from non-Syrian sources',
                'impact': 'Ismail ibn Ayyash is weak when narrating from non-Syrians, though this chain may still be acceptable depending on context.'
            }
        ],
        'topics': [
            'Teaching from Abu Zaid al-Hawzani',
            'Narration with multiple intermediaries'
        ]
    },
    270237: {
        'english_translation': 'Yes, whatever you spend on your children is charity, and perhaps it will be a reward for you...',
        'chain_type': 'mawquf',
        'classical_grade': ['Hasan'],
        'iis_grade': 'Acceptable',
        'issues': [],
        'topics': [
            'Spending on children as an act of charity',
            'Spiritual rewards for supporting family',
            'Islamic ethics regarding financial obligations'
        ]
    },
    270238: {
        'english_translation': 'The Messenger of Allah ﷺ said: "Do not be jealous of one another, do not inflate prices against one another..."',
        'chain_type': 'marfu\'',
        'classical_grade': ['Hasan'],
        'iis_grade': 'Acceptable',
        'issues': [
            {
                'issue': 'Long chain with 12 narrators',
                'impact': 'While each individual narrator may be reliable, the length of the chain increases the potential for errors in transmission.'
            },
            {
                'issue': 'Unnamed narrator (rajul) in the chain',
                'impact': 'An unnamed transmitter weakens the chain as the reliability of this particular link cannot be assessed.'
            }
        ],
        'topics': [
            'Prohibition of jealousy among Muslims',
            'Prohibition of artificial price inflation',
            'Islamic economic ethics',
            'Fair dealing in commerce'
        ]
    },
    270240: {
        'english_translation': 'Narrated by Hind ibn Abi Halah al-Tamimi (the Prophet\'s stepson): The Messenger of Allah ﷺ said to him...',
        'chain_type': 'marfu\'',
        'classical_grade': ['Daif'],
        'iis_grade': 'Weak But Might Be Acceptable',
        'issues': [
            {
                'issue': 'Very long chain with 17 narrators',
                'impact': 'The extensive length of the chain significantly increases the likelihood of transmission errors or breaks in the chain.'
            },
            {
                'issue': 'Multiple indirect transmission terms throughout the chain',
                'impact': 'The repeated use of عَنْ throughout suggests potential gaps in the chain of direct transmission.'
            }
        ],
        'topics': [
            'Narration from Hind ibn Abi Halah',
            'The Prophet\'s stepson\'s transmission of hadith',
            'Historical account from early Islamic period'
        ]
    },
    270213: {
        'english_translation': 'Narrated by Nadlah al-Hirmaazi: A man from them called al-A\'mash, whose name is Abdullah ibn al-A\'war, said: "There was a woman from them called..." [The woman\'s story regarding marriage and wig]',
        'chain_type': 'marfu\'',
        'classical_grade': ['Daif'],
        'iis_grade': 'Questionable But Might Be Acceptable',
        'issues': [
            {
                'issue': 'Chain contains biographical commentary mixed with actual transmission',
                'impact': 'The text "وَكَانَ ثِقَةً" (and he was reliable) appears to be editorial commentary, making the separation of actual chain from analysis unclear.'
            },
            {
                'issue': 'Narration appears to be mawquf (stopped at companion) rather than marfu\' (reaching Prophet)',
                'impact': 'The story appears to be about events during a companion\'s time, not directly attributed to the Prophet ﷺ.'
            }
        ],
        'topics': [
            'Incident of a woman wearing a wig',
            'Religious ruling about wearing wigs',
            'Marital relations and jealousy'
        ]
    },
    270215: {
        'english_translation': 'Narrated by Suwaid ibn Hubairah: The Messenger of Allah ﷺ said: "The best wealth of a man is a well-cultivated date palm or a well-trained horse."',
        'chain_type': 'marfu\'',
        'classical_grade': ['Hasan'],
        'iis_grade': 'Acceptable',
        'issues': [
            {
                'issue': 'Muslim ibn Budail narrating with عَنْ from Iyas ibn Zuhayr',
                'impact': 'Muslim ibn Budail is known for doing tadlis, though he is generally reliable. The عَنْ term requires caution but does not necessarily invalidate the chain.'
            },
            {
                'issue': 'Zuhayr ibn Hunaid has limited biographical documentation',
                'impact': 'While not explicitly weak, this narrator has less documentation than major figures in the chain.'
            }
        ],
        'topics': [
            'Best forms of wealth according to the Prophet ﷺ',
            'Excellence of agricultural and equestrian investments',
            'Economic wisdom in Islamic teaching'
        ]
    },
    270217: {
        'english_translation': 'Narrated by Abu Rifa\'ah: I came to the Messenger of Allah ﷺ while he was delivering the khutbah (sermon). I said: "O Messenger of Allah..."',
        'chain_type': 'marfu\'',
        'classical_grade': ['Hasan'],
        'iis_grade': 'Acceptable',
        'issues': [
            {
                'issue': 'Humaid ibn Hilal narrating with عَنْ from Abu Rifa\'ah',
                'impact': 'Humaid ibn Hilal is generally reliable (Sadooq), but the عَنْ term suggests potentially indirect transmission, though this is acceptable given his reliability.'
            }
        ],
        'topics': [
            'Incident of a man approaching the Prophet during khutbah',
            'Proper conduct during congregational sermon',
            'Direct inquiry to the Prophet ﷺ about Islamic matters'
        ]
    },
    270218: {
        'english_translation': 'Narrated by [unnamed man] from Humaid ibn Hilal: The Messenger of Allah ﷺ said: "Hide from me what Allah has hidden from you..."',
        'chain_type': 'marfu\'',
        'classical_grade': ['Daif'],
        'iis_grade': 'Weak But Might Be Acceptable',
        'issues': [
            {
                'issue': 'Unnamed narrator (just called "rajul" - a man) in the chain',
                'impact': 'This creates a Majhul (unknown) narrator, significantly weakening the chain as there is no way to evaluate his reliability.'
            },
            {
                'issue': 'Ayub narrating with direct term but narrating from Humaid ibn Hilal who uses عَنْ',
                'impact': 'Inconsistency in transmission terminology suggests potential issues with the chain preservation.'
            }
        ],
        'topics': [
            'Divine concealment and mercy',
            'Concept of things hidden by Allah',
            'Modesty and privacy in Islamic teaching'
        ]
    },
    270220: {
        'english_translation': 'Narrated from Umm al-Dardah (may Allah be pleased with her): I was sitting with Umm al-Dardah when...',
        'chain_type': 'mawquf',
        'classical_grade': ['Hasan'],
        'iis_grade': 'Acceptable',
        'issues': [
            {
                'issue': 'Short chain with only two narrators before female companion',
                'impact': 'While short chains can be reliable if narrators are trustworthy, this one lacks intermediate documentation which could affect certainty.'
            },
            {
                'issue': 'Mudrik ibn Sa\'d narrating with عَنْ from Umm al-Dardah',
                'impact': 'The عَنْ term is acceptable here as both narrators are generally reliable, and direct hearing is possible given their contemporaneity.'
            }
        ],
        'topics': [
            'Narration from Umm al-Dardah (female companion)',
            'Women\'s contributions to hadith transmission',
            'Teachings related to household matters or Islamic practice'
        ]
    }
}

def build_narrator_object(narrator_id: int, name: str, transmission_term: str, generation: str = '') -> Dict[str, Any]:
    """Build a complete narrator object with grading and biography"""
    # Narrator database with their reliability assessments
    narrator_db = {
        1284: {
            'full_name': 'al-Hasan ibn Ali',
            'grade': 'Thiqah',
            'generation': 'Third Generation',
            'kunya': '',
            'nisba': 'al-Akki',
            'nisba_ar': 'العكي',
            'death_year': '',
            'birth_year': '',
            'reliability_grade': 'Thiqah',
            'tabaqat': '3',
            'location': 'Kufa'
        },
        8192: {
            'full_name': 'Yahya ibn Adam al-Qurashi',
            'grade': 'Thiqah',
            'generation': 'Second Generation',
            'kunya': 'Abu Zakariyyah',
            'nisba': 'al-Qurashi',
            'nisba_ar': 'القرشي',
            'death_year': '203',
            'birth_year': '120',
            'reliability_grade': 'Thiqah',
            'tabaqat': '2',
            'location': 'Kufa'
        },
        4716: {
            'full_name': 'Abdullah ibn al-Mubarak ibn Wadih al-Hanzi',
            'grade': 'Thiqah Thabt',
            'generation': 'Second Generation',
            'kunya': 'Abu Abd al-Rahman',
            'nisba': 'al-Hanzi',
            'nisba_ar': 'الحنزي',
            'death_year': '181',
            'birth_year': '118',
            'reliability_grade': 'Thiqah Thabt',
            'tabaqat': '2',
            'location': 'Merv'
        },
        7633: {
            'full_name': 'Mu\'ammar ibn Rashid al-Azdi al-Basri',
            'grade': 'Thiqah',
            'generation': 'Second Generation',
            'kunya': 'Abu Ubaydah',
            'nisba': 'al-Azdi',
            'nisba_ar': 'الأزدي',
            'death_year': '153',
            'birth_year': '71',
            'reliability_grade': 'Thiqah',
            'tabaqat': '2',
            'location': 'Basra'
        },
        1131: {
            'full_name': 'Unknown sheikh from Bani Tamim',
            'grade': 'Majhul',
            'generation': 'Second Generation',
            'kunya': '',
            'nisba': 'al-Tamimi',
            'nisba_ar': 'التميمي',
            'death_year': '',
            'birth_year': '',
            'reliability_grade': 'Majhul',
            'tabaqat': '2',
            'location': 'Bani Tamim territory'
        },
        221: {
            'full_name': 'Abu Sudah (also known as Abu Wakin)',
            'grade': 'Saduq',
            'generation': 'Companion',
            'kunya': 'Abu Sudah',
            'nisba': '',
            'nisba_ar': '',
            'death_year': '',
            'birth_year': '',
            'reliability_grade': 'Saduq',
            'tabaqat': 'Companion',
            'location': ''
        },
        6171: {
            'full_name': 'Amr ibn Ali ibn al-Furat al-Faqih',
            'grade': 'Thiqah Thabt',
            'generation': 'Second Generation',
            'kunya': 'Abu Hafs al-Bashshi',
            'nisba': 'al-Bashshi',
            'nisba_ar': 'الباشي',
            'death_year': '249',
            'birth_year': '170',
            'reliability_grade': 'Thiqah Thabt',
            'tabaqat': '2',
            'location': 'Baghdad'
        },
        5336: {
            'full_name': 'Ubaidullah ibn Abd al-Rahman Abu Salamah al-Hanafi',
            'grade': 'Saduq',
            'generation': 'Second Generation',
            'kunya': 'Abu Salamah',
            'nisba': 'al-Hanafi',
            'nisba_ar': 'الحنفي',
            'death_year': '174',
            'birth_year': '',
            'reliability_grade': 'Saduq',
            'tabaqat': '2',
            'location': 'Madinah'
        },
        1174: {
            'full_name': 'al-Junaid ibn Amin ibn Dhirwah al-Hirmaazi',
            'grade': 'La Ba\'sa Bihi',
            'generation': 'Second Generation',
            'kunya': '',
            'nisba': 'al-Hirmaazi',
            'nisba_ar': 'الحرمازي',
            'death_year': '',
            'birth_year': '',
            'reliability_grade': 'La Ba\'sa Bihi',
            'tabaqat': '2',
            'location': ''
        },
        711: {
            'full_name': 'Amin ibn Dhirwah al-Hirmaazi',
            'grade': 'Saduq',
            'generation': 'First Generation',
            'kunya': '',
            'nisba': 'al-Hirmaazi',
            'nisba_ar': 'الحرمازي',
            'death_year': '',
            'birth_year': '',
            'reliability_grade': 'Saduq',
            'tabaqat': '1',
            'location': ''
        },
        40812: {
            'full_name': 'Nadlah ibn Nahd al-Hirmaazi',
            'grade': 'Saduq',
            'generation': 'Companion',
            'kunya': '',
            'nisba': 'al-Hirmaazi',
            'nisba_ar': 'الحرمازي',
            'death_year': '',
            'birth_year': '',
            'reliability_grade': 'Saduq',
            'tabaqat': 'Companion',
            'location': ''
        },
        469: {
            'full_name': 'Ahmad ibn Abdah ibn Quriah al-Marwazi',
            'grade': 'Thiqah',
            'generation': 'Second Generation',
            'kunya': 'Abu Jafar',
            'nisba': 'al-Marwazi',
            'nisba_ar': 'المروزي',
            'death_year': '227',
            'birth_year': '',
            'reliability_grade': 'Thiqah',
            'tabaqat': '2',
            'location': 'Merv'
        },
        17302: {
            'full_name': 'Zuhayr ibn Hunaid al-Khurasani',
            'grade': 'Saduq',
            'generation': 'Second Generation',
            'kunya': 'Abu Khaled',
            'nisba': 'al-Khurasani',
            'nisba_ar': 'الخراساني',
            'death_year': '219',
            'birth_year': '',
            'reliability_grade': 'Saduq',
            'tabaqat': '2',
            'location': 'Khorasan'
        },
        6179: {
            'full_name': 'Abu Na\'amah al-Fadl ibn Dubai al-Aslami',
            'grade': 'Saduq',
            'generation': 'Second Generation',
            'kunya': 'Abu Na\'amah',
            'nisba': 'al-Aslami',
            'nisba_ar': 'الأسلمي',
            'death_year': '201',
            'birth_year': '',
            'reliability_grade': 'Saduq',
            'tabaqat': '2',
            'location': 'Madinah'
        },
        7459: {
            'full_name': 'Muslim ibn Budail ibn Urah al-Jahani',
            'grade': 'La Ba\'sa Bihi',
            'generation': 'Second Generation',
            'kunya': 'Abu Bishr',
            'nisba': 'al-Jahani',
            'nisba_ar': 'الجهني',
            'death_year': '172',
            'birth_year': '',
            'reliability_grade': 'La Ba\'sa Bihi',
            'tabaqat': '2',
            'location': 'Khurassan',
            'reliabilityIssues': ['mudallis']
        },
        1074: {
            'full_name': 'Iyas ibn Zuhayr al-Tamimi',
            'grade': 'Saduq',
            'generation': 'First Generation',
            'kunya': '',
            'nisba': 'al-Tamimi',
            'nisba_ar': 'التميمي',
            'death_year': '',
            'birth_year': '',
            'reliability_grade': 'Saduq',
            'tabaqat': '1',
            'location': 'Taif'
        },
        3720: {
            'full_name': 'Suwaid ibn Hubairah al-Tamimi al-Qurashi',
            'grade': 'Saduq',
            'generation': 'Companion',
            'kunya': 'Abu Talib',
            'nisba': 'al-Tamimi',
            'nisba_ar': 'التميمي',
            'death_year': '',
            'birth_year': '',
            'reliability_grade': 'Saduq',
            'tabaqat': 'Companion',
            'location': 'Taif'
        },
        3840: {
            'full_name': 'Shaybah ibn Farrukh al-Azdi',
            'grade': 'Thiqah',
            'generation': 'Second Generation',
            'kunya': 'Abu Ishaq',
            'nisba': 'al-Azdi',
            'nisba_ar': 'الأزدي',
            'death_year': '197',
            'birth_year': '120',
            'reliability_grade': 'Thiqah',
            'tabaqat': '2',
            'location': 'Basra'
        },
        3570: {
            'full_name': 'Sulayman ibn al-Mughirah al-Makhzumi al-Makki',
            'grade': 'Thiqah',
            'generation': 'Second Generation',
            'kunya': 'Abu Muhammad',
            'nisba': 'al-Makhzumi',
            'nisba_ar': 'المخزومي',
            'death_year': '193',
            'birth_year': '',
            'reliability_grade': 'Thiqah',
            'tabaqat': '2',
            'location': 'Makkah'
        },
        2553: {
            'full_name': 'Humaid ibn Hilal al-Azdi al-Yamami',
            'grade': 'Saduq/Sadooq',
            'generation': 'Second Generation',
            'kunya': 'Abu Hilal',
            'nisba': 'al-Azdi',
            'nisba_ar': 'الأزدي',
            'death_year': '154',
            'birth_year': '70',
            'reliability_grade': 'Saduq',
            'tabaqat': '2',
            'location': 'Yamama'
        },
        21465: {
            'full_name': 'Abu Rifa\'ah al-Adawi Adi ibn Tamim',
            'grade': 'Saduq',
            'generation': 'Companion',
            'kunya': 'Abu Rifa\'ah',
            'nisba': 'al-Adawi',
            'nisba_ar': 'العدوي',
            'death_year': '',
            'birth_year': '',
            'reliability_grade': 'Saduq',
            'tabaqat': 'Companion',
            'location': ''
        },
        6861: {
            'full_name': 'Abu Musa Muhammad ibn Utham',
            'grade': 'Thiqah',
            'generation': 'Second Generation',
            'kunya': 'Abu Musa',
            'nisba': 'al-Basri',
            'nisba_ar': 'البصري',
            'death_year': '213',
            'birth_year': '130',
            'reliability_grade': 'Thiqah',
            'tabaqat': '2',
            'location': 'Basra'
        },
        5280: {
            'full_name': 'Abd al-Wahhab ibn Abd al-Majid al-Thaqafi',
            'grade': 'Thiqah Thabt',
            'generation': 'Second Generation',
            'kunya': 'Abu Muhammad',
            'nisba': 'al-Thaqafi',
            'nisba_ar': 'الثقفي',
            'death_year': '194',
            'birth_year': '119',
            'reliability_grade': 'Thiqah Thabt',
            'tabaqat': '2',
            'location': 'Basra'
        },
        746: {
            'full_name': 'Ayub ibn Abi Tamimah al-Sakhtiyani',
            'grade': 'Thiqah Thabt',
            'generation': 'Second Generation',
            'kunya': 'Abu Muhammad',
            'nisba': 'al-Sakhtiyani',
            'nisba_ar': 'السختياني',
            'death_year': '131',
            'birth_year': '61',
            'reliability_grade': 'Thiqah Thabt',
            'tabaqat': '2',
            'location': 'Basra'
        },
        468: {
            'full_name': 'Ahmad ibn Abdah al-Marwazi',
            'grade': 'Thiqah',
            'generation': 'Second Generation',
            'kunya': 'Abu Jafar',
            'nisba': 'al-Marwazi',
            'nisba_ar': 'المروزي',
            'death_year': '225',
            'birth_year': '',
            'reliability_grade': 'Thiqah',
            'tabaqat': '2',
            'location': 'Merv'
        },
        7376: {
            'full_name': 'Mudrik ibn Sa\'d ibn Ibrahim',
            'grade': 'Saduq',
            'generation': 'Second Generation',
            'kunya': '',
            'nisba': 'al-Qurashi',
            'nisba_ar': 'القرشي',
            'death_year': '',
            'birth_year': '',
            'reliability_grade': 'Saduq',
            'tabaqat': '2',
            'location': 'Madinah'
        },
        2761: {
            'full_name': 'Umm al-Dardah al-Sughra (Umm al-Dardah Junior)',
            'grade': 'Thiqah',
            'generation': 'Companion',
            'kunya': 'Umm al-Dardah',
            'nisba': 'al-Himyari',
            'nisba_ar': 'الحميري',
            'death_year': '81',
            'birth_year': '',
            'reliability_grade': 'Thiqah',
            'tabaqat': 'Companion',
            'location': 'Madinah/Damascus'
        }
    }

    if narrator_id in narrator_db:
        info = narrator_db[narrator_id].copy()
        info['name'] = name
        info['narrator_id'] = narrator_id
        info['transmissionTerm'] = transmission_term
        info['reliabilityIssues'] = info.get('reliabilityIssues', [])
        info['original_id'] = narrator_id
        info['alternative_names'] = ''
        info['transmissionTermMeaning'] = {
            'حَدَّثَنَا': 'He narrated to us (direct hearing)',
            'ثنا': 'He narrated to us (direct hearing)',
            'نا': 'He narrated to us (direct hearing)',
            'أَخْبَرَنَا': 'He informed us (direct)',
            'عَنْ': 'From (could be direct or indirect)',
            'قَالَ': 'He said'
        }.get(transmission_term, '')
        return info

    # Default for unknown narrators
    return {
        'name': name,
        'full_name': name,
        'grade': 'Majhul',
        'generation': generation,
        'transmissionTerm': transmission_term,
        'reliabilityIssues': ['unknown'],
        'narrator_id': narrator_id,
        'alternative_names': '',
        'original_id': narrator_id,
        'kunya': '',
        'nisba': '',
        'nisba_ar': '',
        'death_year': '',
        'birth_year': '',
        'reliability_grade': 'Majhul',
        'tabaqat': '',
        'location': '',
        'transmissionTermMeaning': ''
    }

def process_hadith(hadith_data: Dict[str, Any]) -> Dict[str, Any]:
    """Process a single hadith into the output format"""
    hadith_id = hadith_data['hadith_id']

    # Get analysis from database
    if hadith_id not in HADITH_ANALYSES:
        return None

    analysis = HADITH_ANALYSES[hadith_id]

    # Parse the chain
    chain_data = parse_chain_from_text(hadith_data['text_ar'])

    # Build narrators array
    narrators = []
    for narrator in chain_data:
        narr_obj = build_narrator_object(
            narrator['narrator_id'],
            narrator['name'],
            narrator['transmission_term'],
            'Second Generation'
        )
        narrators.append(narr_obj)

    # Add Prophet ﷺ as final point in chain
    narrators.append({
        'name': 'Prophet Muhammad ﷺ',
        'full_name': 'Muhammad ibn Abdullah ibn Abd al-Muttalib ibn Hashim',
        'grade': 'Awthaq al-Nas',
        'generation': 'Prophet',
        'transmissionTerm': '',
        'reliabilityIssues': [],
        'narrator_id': 0,
        'alternative_names': 'Ahmad, al-Mustafa',
        'original_id': 0,
        'kunya': 'Abu al-Qasim',
        'nisba': 'al-Hashimi al-Qurashi',
        'nisba_ar': 'الهاشمي القرشي',
        'death_year': '11',
        'birth_year': '53 BH',
        'reliability_grade': 'Awthaq al-Nas',
        'tabaqat': 'Prophet',
        'location': 'Makkah/Madinah',
        'transmissionTermMeaning': ''
    })

    # Build output object
    output = {
        'hadith_id': hadith_id,
        'book_id': hadith_data['book_id'],
        'book_name_ar': hadith_data['book'].get('book_name_ar', 'Unknown'),
        'book_name_en': 'Unknown Collection',  # Extracting from book data if available
        'author_name_ar': hadith_data['book'].get('author_name', 'Unknown'),
        'author_name_en': 'Unknown Author',
        'hadith_number': str(hadith_data['hadith_number']),
        'english_translation': analysis['english_translation'],
        'chains': [
            {
                'type': analysis['chain_type'],
                'narrators': narrators,
                'chainIssues': []
            }
        ],
        'potential_issues': analysis['issues'],
        'Classical Grade': analysis['classical_grade'],
        'IISGrade': analysis['iis_grade'],
        'Topics': analysis['topics']
    }

    return output


# Main processing
if __name__ == '__main__':
    import sys

    input_file = sys.argv[1] if len(sys.argv) > 1 else '/tmp/chunk1_for_analysis.json'
    output_file = sys.argv[2] if len(sys.argv) > 2 else '/tmp/processed_chunk1.json'

    with open(input_file, 'r', encoding='utf-8') as f:
        chunk = json.load(f)

    processed = []
    for hadith in chunk['hadiths']:
        result = process_hadith(hadith)
        if result:
            processed.append(result)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(processed, f, ensure_ascii=False, indent=2)

    print(f"Processed {len(processed)} hadiths to {output_file}")
