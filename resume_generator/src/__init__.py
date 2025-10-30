"""
Resume Generator Package
A Python package for generating professional resume PDFs
"""

from .resume_generator import ResumeGenerator
from .resume_data import PERSONAL_INFO
from .pdf_styles import get_resume_styles

__version__ = "1.0.0"
__author__ = "S Rajender Reddy"

__all__ = ["ResumeGenerator", "PERSONAL_INFO", "get_resume_styles"]
