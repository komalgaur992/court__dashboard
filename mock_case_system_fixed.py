"""
Enhanced Mock Case Data System for Court Dashboard Testing
Provides structured mock data for specific test cases without real scraping
"""

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
        for test_name, test_data in TEST_CASES.items():
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
                "judges": ["Justice Rajiv Sharma", "Justice Harinder Singh Sidhu"],
                "summary": "The High Court dismissed the appeal filed by Municipal Corporation Faridabad against the order of the lower court.",
                "key_points": [
                    "Municipal Corporation failed to produce original ownership documents",
                    "Adverse possession claim by Krishan Kumar established",
                    "Compensation awarded to respondent for improvements made"
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
                    "url": "/mock/judgments/CR-1205-2016-judgment.pdf"
                }
            ],
            "citations": ["AIR 2016 P&H 45", "2016 (1) PLR 234"]
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
                "sections": ["302 IPC", "34 IPC"]
            },
            "parties": {
                "prosecution": {"name": "State of Haryana", "represented_by": "Adv. Deepak Verma"},
                "accused": [
                    {"name": "Tauseef Ahmed", "age": 25, "role": "Main accused"},
                    {"name": "Rehan", "age": 24, "role": "Co-accused"}
                ],
                "victim": {"name": "Nikita Tomar", "age": 21, "occupation": "Student"}
            },
            "judgment": {
                "date": "2021-03-24",
                "type": "Sessions Trial",
                "outcome": "Convicted",
                "verdict": {
                    "Tauseef": {"finding": "Guilty", "sentence": "Life imprisonment"},
                    "Rehan": {"finding": "Acquitted"}
                }
            },
            "case_status": "Convicted"
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
            "settlement": {
                "amount": 850000,
                "breakup": {
                    "compensation": 750000,
                    "medical_expenses": 75000,
                    "loss_of_income": 25000
                },
                "payment_terms": "50% within 30 days, 50% within 60 days"
            },
            "case_status": "Settled"
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
            # Return "Case Not Found" message
            return {
                "case_id": f"{case_type}/{case_number}/{filing_year}",
                "case_type": case_type,
                "case_number": case_number,
                "filing_year": filing_year,
                "error": "Case Not Found",
                "message": f"No case found for {case_type}/{case_number}/{filing_year}",
                "court": "District Court, Faridabad",
                "case_status": "Not Found",
                "description": f'Case {case_type}/{case_number}/{filing_year} not found in records'
            }

def enhanced_fetch_case_data(case_type: str, case_number: str, filing_year: str) -> Dict[str, Any]:
    """
    Enhanced version of fetch_case_data that provides detailed mock data
    for specific test cases without real scraping
    """
    return EnhancedMockCaseData.get_mock_data(case_type, case_number, filing_year)

# Test cases for easy reference
TEST_CASES = {
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
    
    # Test unknown case
    result = enhanced_fetch_case_data("CR", "2021", "2021")
    print(f"Unknown case: {result.get('error', 'No error')}")
