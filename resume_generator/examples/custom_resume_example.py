#!/usr/bin/env python3
"""
Example: How to create a custom resume with different data
This shows how to modify the resume data and generate a custom PDF
"""

import sys
import os

# Add the parent directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.resume_generator import ResumeGenerator
from src import resume_data

def create_custom_resume():
    """
    Example of creating a custom resume by modifying the data
    """
    
    # Backup original data
    original_name = resume_data.PERSONAL_INFO["name"]
    original_title = resume_data.PERSONAL_INFO["title"]
    
    # Customize the data (this is just an example)
    resume_data.PERSONAL_INFO["name"] = "JOHN DOE"
    resume_data.PERSONAL_INFO["title"] = "Senior Software Engineer"
    resume_data.PERSONAL_INFO["phone"] = "555-0123"
    resume_data.PERSONAL_INFO["email"] = "john.doe@example.com"
    resume_data.PERSONAL_INFO["linkedin"] = "linkedin.com/in/johndoe"
    
    # You can also modify other sections like:
    # resume_data.SUMMARY = "Your custom summary here..."
    # resume_data.TECHNICAL_SKILLS["Programming Languages"] = "Python, Java, C++"
    
    try:
        # Generate the custom resume
        generator = ResumeGenerator(output_dir="../output")
        pdf_path = generator.generate_resume("John_Doe_Custom_Resume.pdf")
        
        print(f"✅ Custom resume generated: {pdf_path}")
        
    finally:
        # Restore original data
        resume_data.PERSONAL_INFO["name"] = original_name
        resume_data.PERSONAL_INFO["title"] = original_title

if __name__ == "__main__":
    create_custom_resume()
