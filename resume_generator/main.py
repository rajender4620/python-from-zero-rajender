#!/usr/bin/env python3
"""
Main entry point for the Resume Generator
Run this script to generate a professional resume PDF
"""

import os
import sys
from src.resume_generator import ResumeGenerator

def main():
    """
    Main function to generate the resume
    """
    print("Starting Resume Generator...")
    print("=" * 50)
    
    try:
        # Create resume generator instance
        generator = ResumeGenerator(output_dir="output")
        
        # Generate the resume
        pdf_file = generator.generate_resume()
        
        # Get absolute path for display
        abs_path = os.path.abspath(pdf_file)
        
        print("Resume generated successfully!")
        print(f"File saved at: {abs_path}")
        print("=" * 50)
        
        return pdf_file
        
    except Exception as e:
        print(f"Error generating resume: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
