"""
Enhanced Mock Case Data System for Court Dashboard Testing
Provides structured mock data for specific test cases without real scraping
"""

import json
from datetime import datetime
from typing import Dict, Any, Optional

class EnhancedMockCaseData:
    """Enhanced mock data provider for specific test cases"""
    
    # Test case identifiers
    TEST_CASES = {
        "second_appeal_1205_2016": {
            "case_type": "CR",
            "case_number": "1205",
            "filing_year": "2016",
            "description": "Second Appeal No. 1205 of 2016 – Municipal Corporation Faridabad vs Krishan Kumar"
        },
        "nikita_tomar": {
            "case_type": "CRM",
            "case_number": "1234",
            "filing_year": "2020",
            "description": "Nikita Tomar murder case"
        },
        "mact_lok_adalat": {
            "case_type": "MACP",
            "case_number": "5678",
            "filing_year": "2025",
            "description": "MACT case resolved by Lok Adalat in Faridabad"
        }
    }
    
    @staticmethod
    def detect_test_case(case_type: str, case_number: str, filing_year: str) -> Optional[str]:
        """Detect which test case this input matches"""
        for test_name, test_data in EnhancedMockCaseData.TEST_CASES.items():
            if (test_data["case_type"] == case_type and 
                test_data["case_number"] == case_number and 
                test_data["filing_year"] == filing_year):
                return test_name
        return None
    
    @staticmethod
    def get_second_appeal_1205_2016() -> Dict[str, Any]:
        """Detailed mock data for Second Appeal No. 1205 of 2016"""
        return {
            "case_id": "CR/1205/2016",
            "case_type": "CR",
            "case_number": "1205",
            "filing_year": "2016",
            "court": "Punjab and Haryana High Court",
            "court_code": "PHHC",
            "parties": {
                "appellant": {
                    "name": "Municipal Corporation Faridabad",
                    "type": "Government Body",
                    "represented_by": "Adv. Ramesh Sharma"
                },
                "respondent": {
                    "name": "Krishan Kumar",
                    "type": "Individual",
                    "represented_by": "Adv. Deepak Verma"
                }
            },
            "judgment": {
                "date": "2015-12-24",
                "type": "Second Appeal",
                "outcome": "Appeal dismissed",
                "judges": [
                    "Justice Rajiv Sharma",
                    "Justice Harinder Singh Sidhu"
                ],
                "summary": "The High Court dismissed the appeal filed by Municipal Corporation Faridabad against the order of the lower court. The court held that the corporation failed to establish its ownership rights over the disputed property.",
                "key_points": [
                    "Municipal Corporation failed to produce original ownership documents",
                    "Adverse possession claim by Krishan Kumar established",
                    "Compensation awarded to respondent for improvements made",
                    "Court costs imposed on appellant"
                ]
            },
            "case_status": "Disposed",
            "disposal_date": "2015-12-24",
            "court_fees": 5000,
            "documents": [
                {
                    "type": "Judgment",
                    "title": "Second Appeal Judgment",
                    "date": "2015-12-24",
                    "url": "/mock/judgments/CR-1205-2016-judgment.pdf",
                    "size": "2.3 MB"
                },
                {
                    "type": "Order",
                    "title": "Final Order",
                    "date": "2015-12-24",
                    "url": "/mock/orders/CR-1205-2016-order.pdf",
                    "size": "1.1 MB"
                }
            ],
            "citations": [
                "AIR 2016 P&H 45",
                "2016 (1) PLR 234",
                "2016 (2) RCR (Civil) 123"
            ]
        }
    
    @staticmethod
    def get_nikita_tomar_case() -> Dict[str, Any]:
        """Detailed mock data for Nikita Tomar murder case"""
        return {
            "case_id": "CRM/1234/2020",
            "case_type": "CRM",
            "case_number": "1234",
            "filing_year": "2020",
            "court": "Fast Track Court, Faridabad",
            "court_code": "FTCF",
            "crime": {
                "date": "2020-10-26",
                "location": "Ballabhgarh, Faridabad",
                "type": "Murder",
                "sections": ["302 IPC", "34 IPC", "120B IPC"]
            },
            "parties": {
                "prosecution": {
                    "name": "State of Haryana",
                    "represented_by": "Adv. Deepak Verma"
                },
                "accused": [
                    {
                        "name": "Tauseef Ahmed",
                        "age": 25,
                        "role": "Main accused",
                        "represented_by": "Adv. Ramesh Sharma"
                    },
                    {
                        "name": "Rehan",
                        "age": 24,
                        "role": "Co-accused",
                        "represented_by": "Adv. Priya Singh"
                    }
                ],
                "victim": {
                    "name": "Nikita Tomar",
                    "age": 21,
                    "occupation": "Student"
                }
            },
            "judgment": {
                "date": "2021-03-24",
                "type": "Sessions Trial",
                "outcome": "Convicted",
                "verdict": {
                    "Tauseef": {
                        "finding": "Guilty",
                        "sections": ["302 IPC"],
                        "sentence": "Life imprisonment + ₹50,000 fine",
                        "appeal": "Filed in High Court"
                    },
                    "Rehan": {
                        "finding": "Acquitted",
                        "reason": "Benefit of doubt",
                        "appeal": "None"
                    }
                },
                "judge": "Shri Justice Rajesh Singh"
            },
            "evidence": {
                "witnesses": 15,
                "key_evidence": [
                    "CCTV footage showing the shooting",
                    "Forensic ballistic report matching the weapon",
                    "Eyewitness testimony from 3 witnesses",
                    "Mobile phone location data",
                    "Call detail records",
                    "Recovery of weapon used in crime"
                ],
                "forensic": {
                    "weapon": "Country-made pistol recovered",
                    "ballistics": "Bullets matched with recovered weapon",
                    "dna": "DNA evidence collected from crime scene"
                }
            },
            "case_status": "Convicted",
            "documents": [
                {
                    "type": "Charge Sheet",
                    "title": "Final Report",
                    "date": "2020-12-15",
                    "url": "/mock/chargesheets/nikita-tomar-charge-sheet.pdf",
                    "size": "3.2 MB"
                },
                {
                    "type": "Judgment",
                    "title": "Sessions Court Judgment",
                    "date": "2021-03-24",
                    "url": "/mock/judgments/nikita-tomar-judgment.pdf",
                    "size": "4.5 MB"
                }
            ]
        }
    
    @staticmethod
    def get_second_appeal_1205_2016() -> Dict[str, Any]:
        """Detailed mock data for Second Appeal No. 1205 of 2016"""
        return {
            "case_id": "CR/1205/2016",
            "case_type": "CR",
            "case_number": "1205",
            "filing_year": "2016",
            "court": "Punjab and Haryana High Court",
            "court_code": "PHHC",
            "parties": {
                "appellant": {
                    "name": "Municipal Corporation Faridabad",
                    "type": "Government Body",
                    "represented_by": "Adv. Ramesh Sharma"
                },
                "respondent": {
                    "name": "Krishan Kumar",
                    "type": "Individual",
                    "represented_by": "Adv. Deepak Verma"
                }
            },
            "judgment": {
                "date": "2015-12-24",
                "type": "Second Appeal",
                "outcome": "Appeal dismissed",
                "judges": [
                    "Justice Rajiv Sharma",
                    "Justice Harinder Singh Sidhu"
                ],
                "summary": "The High Court dismissed the appeal filed by Municipal Corporation Faridabad against the order of the lower court. The court held that the corporation failed to establish its ownership rights over the disputed property.",
                "key_points": [
                    "Municipal Corporation failed to produce original ownership documents",
                    "Adverse possession claim by Krishan Kumar established",
                    "Compensation awarded to respondent for improvements made",
                    "Court costs imposed on appellant"
                ]
            },
            "case_status": "Disposed",
            "disposal_date": "2015-12-24",
            "court_fees": 5000,
            "documents": [
                {
                    "type": "Judgment",
                    "title": "Second Appeal Judgment",
                    "date": "2015-12-24",
                    "url": "/mock/judgments/CR-1205-2016-judgment.pdf",
                    "size": "2.3 MB"
                },
                {
                    "type": "Order",
                    "title": "Final Order",
                    "date": "2015-12-24",
                    "url": "/mock/orders/CR-1205-2016-order.pdf",
                    "size": "1.1 MB"
                }
            ],
            "citations": [
                "AIR 2016 P&H 45",
                "2016 (1) PLR 234",
                "2016 (2) RCR (Civil) 123"
            ],
            "proceedings": [
                {
                    "date": "2016-01-15",
                    "event": "Appeal filed",
                    "description": "Second appeal filed by Municipal Corporation Faridabad"
                },
                {
                    "date": "2016-03-20",
                    "event": "Notice issued",
                    "description": "Notice issued to respondent Krishan Kumar"
                },
                {
                    "date": "2016-06-10",
                    "event": "Written statement filed",
                    "description": "Respondent filed written statement"
                },
                {
                    "date": "2016-09-05",
                    "event": "Arguments heard",
                    "description": "Final arguments heard by court"
                },
                {
                    "date": "2015-12-24",
                    "event": "Judgment delivered",
                    "description": "Appeal dismissed with costs"
                }
            ]
        }
    
    @staticmethod
    def get_nikita_tomar_case() -> Dict[str, Any]:
        """Detailed mock data for Nikita Tomar murder case"""
        return {
            "case_id": "CRM/1234/2020",
            "case_type": "CRM",
            "case_number": "1234",
            "filing_year": "2020",
            "court": "Fast Track Court, Faridabad",
            "court_code": "FTCF",
            "crime": {
                "date": "2020-10-26",
                "location": "Ballabhgarh, Faridabad",
                "type": "Murder",
                "sections": ["302 IPC", "34 IPC", "120B IPC"]
            },
            "parties": {
                "prosecution": {
                    "name": "State of Haryana",
                    "represented_by": "Adv. Deepak Verma"
                },
                "accused": [
                    {
                        "name": "Tauseef Ahmed",
                        "age": 25,
                        "role": "Main accused",
                        "represented_by": "Adv. Ramesh Sharma"
                    },
                    {
                        "name": "Rehan",
                        "age": 24,
                        "role": "Co-accused",
                        "represented_by": "Adv. Priya Singh"
                    }
                ],
                "victim": {
                    "name": "Nikita Tomar",
                    "age": 21,
                    "occupation": "Student"
                }
            },
            "judgment": {
                "date": "2021-03-24",
                "type": "Sessions Trial",
                "outcome": "Convicted",
                "verdict": {
                    "Tauseef": {
                        "finding": "Guilty",
                        "sections": ["302 IPC"],
                        "sentence": "Life imprisonment + ₹50,000 fine",
                        "appeal": "Filed in High Court"
                    },
                    "Rehan": {
                        "finding": "Acquitted",
                        "reason": "Benefit of doubt",
                        "appeal": "None"
                    }
                },
                "judge": "Shri Justice Rajesh Singh"
            },
            "evidence": {
                "witnesses": 15,
                "key_evidence": [
                    "CCTV footage showing the shooting",
                    "Forensic ballistic report matching the weapon",
                    "Eyewitness testimony from 3 witnesses",
                    "Mobile phone location data",
                    "Call detail records",
                    "Recovery of weapon used in crime"
                ],
                "forensic": {
                    "weapon": "Country-made pistol recovered",
                    "ballistics": "Bullets matched with recovered weapon",
                    "dna": "DNA evidence collected from crime scene"
                }
            },
            "case_status": "Convicted",
            "documents": [
                {
                    "type": "Charge Sheet",
                    "title": "Final Report",
                    "date": "2020-12-15",
                    "url": "/mock/chargesheets/nikita-tomar-charge-sheet.pdf",
                    "size": "3.2 MB"
                },
                {
                    "type": "Judgment",
                    "title": "Sessions Court Judgment",
                    "date": "2021-03-24",
                    "url": "/mock/judgments/nikita-tomar-judgment.pdf",
                    "size": "4.5 MB"
                }
            ]
        }
    
    @staticmethod
    def get_mact_lok_adalat_case() -> Dict[str, Any]:
        """Detailed mock data for MACT case resolved by Lok Adalat"""
        return {
            "case_id": "MACP/5678/2025",
            "case_type": "MACP",
            "case_number": "5678",
            "filing_year": "2025",
            "court": "Motor Accident Claims Tribunal, Faridabad",
            "court_code": "MACT",
            "lok_adalat": {
                "date": "2025-01-18",
                "venue": "District Court Complex, Faridabad",
                "mediators": [
                    "Sh. R.K. Sharma (Retd. Judge)",
                    "Ms. Priya Singh (Advocate)"
                ]
            },
            "accident": {
                "date": "2023-05-15",
                "time": "14:30",
                "location": "Sector 15, Faridabad",
                "vehicle": {
                    "registration": "HR-38-A-1234",
                    "type": "Car",
                    "owner": "Rajesh Kumar"
                },
                "injury": {
                    "type": "Permanent disability",
                    "percentage": 40,
                    "description": "Loss of earning capacity due to injuries"
                }
            },
            "parties": {
                "claimant": {
                    "name": "Smt. Sunita Devi",
                    "age": 35,
                    "occupation": "Housewife",
                    "represented_by": "Adv. Deepak Verma"
                },
                "respondent": {
                    "name": "Oriental Insurance Co. Ltd.",
                    "represented_by": "Adv. Ramesh Sharma"
                },
                "vehicle_owner": {
                    "name": "Rajesh Kumar",
                    "relationship": "Vehicle owner"
                }
            },
            "settlement": {
                "amount": 850000,
                "currency": "INR",
                "breakup": {
                    "compensation": 750000,
                    "medical_expenses": 75000,
                    "loss_of_income": 25000
                },
                "payment_terms": "50% within 30 days, 50% within 60 days",
                "payment_status": "First installment paid"
            },
            "case_status": "Settled",
            "settlement_type": "Lok Adalat",
            "documents": [
                {
                    "type": "Settlement Agreement",
                    "title": "Lok Adalat Settlement",
                    "date": "2025-01-18",
                    "url": "/mock/settlements/mact-5678-2025-settlement.pdf",
                    "size": "1.8 MB"
                },
                {
                    "type": "Disability Certificate",
                    "title": "Medical Disability Certificate",
                    "date": "2024-12-15",
                    "url": "/mock/medical/disability-certificate-5678.pdf",
                    "size": "0.5 MB"
                }
            ]
        }  
    @staticmethod
    def get_mock_data(case_type: str, case_number: str, filing_year: str) -> Dict[str, Any]:
        """Main function to get mock data based on input parameters"""
        test_case = EnhancedMockCaseData.detect_test_case(case_type, case_number, filing_year)
        
        if test_case == "second_appeal_1205_2016":
            return EnhancedMockCaseData.get_second_appeal_1205_2016()
        elif test_case == "nikita_tomar":
            return EnhancedMockCaseData.get_nikita_tomar_case()
        elif test_case == "mact_lok_adalat":
            return EnhancedMockCaseData.get_mact_lok_adalat_case()
        else:
            # Return enhanced default mock data
            return {
                "case_id": f"{case_type}/{case_number}/{filing_year}",
                "case_type": case_type,
                "case_number": case_number,
                "filing_year": filing_year,
                "court": "District Court, Faridabad",
                "parties": {
                    "petitioner": f"Petitioner for Case {case_number}",
                    "respondent": f"Respondent for Case {case_number}"
                },
                "case_status": "Pending",
                "next_hearing_date": "To be scheduled",
                "description": f"Case {case_type}/{case_number}/{filing_year} details",
                "mock_note": "This is a generic mock case for testing purposes"
            }

def enhanced_fetch_case_data(case_type: str, case_number: str, filing_year: str, **kwargs) -> Dict[str, Any]:
    """
    Enhanced version of fetch_case_data that provides detailed mock data
    for specific test cases without real scraping
    """
    return EnhancedMockCaseData.get_mock_data(case_type, case_number, filing_year)

# Test cases for easy reference
# These test cases are for reference only and not used in the class implementation
TEST_CASES_REFERENCE = {
    "Second Appeal 1205/2016": {
        "case_type": "CR",
        "case_number": "1205",
        "filing_year": "2016"
    },
    "Nikita Tomar Case": {
        "case_type": "CRM",
        "case_number": "1234",
        "filing_year": "2020"
    },
    "MACT Lok Adalat": {
        "case_type": "MACP",
        "case_number": "5678",
        "filing_year": "2025"
    }
}

if __name__ == "__main__":
    # Test the mock system
    print("Testing mock case system...")
    
    # Test Second Appeal 1205/2016
    result = enhanced_fetch_case_data("CR", "1205", "2016")
    print(f"\nSecond Appeal 1205/2016: {result['case_id']}")
    
    # Test Nikita Tomar case
    result = enhanced_fetch_case_data("CRM", "1234", "2020")
    print(f"Nikita Tomar case: {result['case_id']}")
    
    # Test MACT Lok Adalat
    result = enhanced_fetch_case_data("MACP", "5678", "2025")
    print(f"MACT Lok Adalat: {result['case_id']}")