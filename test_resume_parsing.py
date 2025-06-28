#!/usr/bin/env python3
"""
Test script for resume parsing functionality
"""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.append(str(Path(__file__).parent / "src"))

from src.resume_crew.tools import ResumeAnalysisTools

def test_resume_parsing():
    """
    Test resume parsing with different file formats.
    """
    print("🧪 Testing Resume Parsing Functionality")
    print("=" * 50)
    
    # Test text resume
    print("\n📄 Testing Text Resume Parsing...")
    text_result = ResumeAnalysisTools.analyze_resume("knowledge/CV_Mohan.txt")
    
    if text_result["status"] == "success":
        print("✅ Text resume parsing successful")
        print(f"   Content length: {len(text_result['content'])} characters")
        print(f"   File type: {text_result['file_type']}")
    else:
        print(f"❌ Text resume parsing failed: {text_result['error']}")
    
    # Test with non-existent file
    print("\n🔍 Testing Non-existent File...")
    missing_result = ResumeAnalysisTools.analyze_resume("knowledge/nonexistent.pdf")
    
    if missing_result["status"] == "error":
        print("✅ Correctly handled missing file")
    else:
        print("❌ Should have failed for missing file")
    
    # Test with unsupported format
    print("\n📁 Testing Unsupported Format...")
    unsupported_result = ResumeAnalysisTools.analyze_resume("knowledge/test.docx")
    
    if unsupported_result["status"] == "error":
        print("✅ Correctly handled unsupported format")
    else:
        print("❌ Should have failed for unsupported format")
    
    print("\n" + "=" * 50)
    print("🎉 Resume parsing tests completed!")

if __name__ == "__main__":
    test_resume_parsing() 