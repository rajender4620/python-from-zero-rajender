r"""
PDF styling configuration for the resume
Contains all the style definitions and color schemes
"""

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def get_resume_styles():
    """
    Create and return custom styles for the resume PDF
    """
    styles = getSampleStyleSheet()
    
    # Custom styles
    styles.add(ParagraphStyle(
        name='Header',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor("#0078D4"),
        spaceAfter=6,
        fontName='Helvetica-Bold',
        alignment=1  # Center alignment
    ))
    
    styles.add(ParagraphStyle(
        name='SubHeader',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#0078D4"),
        spaceAfter=4,
        fontName='Helvetica-Bold',
        underlineWidth=0.5
    ))
    
    styles.add(ParagraphStyle(
        name='Body',
        fontSize=10.5,
        leading=14,
        textColor=colors.black,
        spaceAfter=6
    ))
    
    styles.add(ParagraphStyle(
        name='Contact',
        fontSize=9.5,
        leading=12,
        textColor=colors.HexColor("#333333"),
        alignment=1  # Center alignment
    ))
    
    return styles

# Color scheme
COLORS = {
    'primary': colors.HexColor("#0078D4"),
    'text': colors.black,
    'contact': colors.HexColor("#333333"),
    'divider': colors.lightgrey
}
