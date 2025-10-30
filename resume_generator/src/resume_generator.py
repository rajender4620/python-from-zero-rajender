"""
Resume PDF Generator
Main class for generating professional resume PDFs
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
import os
from datetime import datetime

from .pdf_styles import get_resume_styles, COLORS
from .resume_data import (
    PERSONAL_INFO, SUMMARY, TECHNICAL_SKILLS, EXPERIENCE, 
    PROJECTS, EDUCATION, CERTIFICATIONS, SOFT_SKILLS
)

class ResumeGenerator:
    """
    A class to generate professional resume PDFs using ReportLab
    """
    
    def __init__(self, output_dir="output"):
        """
        Initialize the resume generator
        
        Args:
            output_dir (str): Directory to save the generated PDF
        """
        self.output_dir = output_dir
        self.styles = get_resume_styles()
        
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
    
    def _add_header(self, content):
        """Add header section with name, title, and contact info"""
        content.append(Paragraph(PERSONAL_INFO["name"], self.styles['Header']))
        content.append(Paragraph(PERSONAL_INFO["title"], self.styles['SubHeader']))
        
        contact_info = f"📞 {PERSONAL_INFO['phone']} | 📧 {PERSONAL_INFO['email']} | 🌐 {PERSONAL_INFO['linkedin']}"
        content.append(Paragraph(contact_info, self.styles['Contact']))
        
        content.append(Spacer(1, 8))
        content.append(HRFlowable(width="100%", thickness=1, color=COLORS['primary']))
        content.append(Spacer(1, 12))
    
    def _add_section_divider(self, content):
        """Add a section divider"""
        content.append(Spacer(1, 8))
        content.append(HRFlowable(width="100%", thickness=0.5, color=COLORS['divider']))
        content.append(Spacer(1, 8))
    
    def _add_summary(self, content):
        """Add professional summary section"""
        content.append(Paragraph("PROFESSIONAL SUMMARY", self.styles['SubHeader']))
        content.append(Paragraph(SUMMARY, self.styles['Body']))
        self._add_section_divider(content)
    
    def _add_technical_skills(self, content):
        """Add technical skills section"""
        content.append(Paragraph("TECHNICAL SKILLS", self.styles['SubHeader']))
        
        skills_text = ""
        for category, skills in TECHNICAL_SKILLS.items():
            skills_text += f"<b>{category}:</b> {skills}<br/>"
        
        content.append(Paragraph(skills_text, self.styles['Body']))
        self._add_section_divider(content)
    
    def _add_experience(self, content):
        """Add professional experience section"""
        content.append(Paragraph("PROFESSIONAL EXPERIENCE", self.styles['SubHeader']))
        
        for job in EXPERIENCE:
            job_header = f"<b>{job['title']} | {job['company']} | {job['location']} | {job['duration']}</b><br/>"
            responsibilities = "<br/>".join([f"• {resp}" for resp in job['responsibilities']])
            job_text = job_header + responsibilities
            
            content.append(Paragraph(job_text, self.styles['Body']))
        
        self._add_section_divider(content)
    
    def _add_projects(self, content):
        """Add projects section"""
        content.append(Paragraph("PROJECTS", self.styles['SubHeader']))
        
        projects_text = ""
        for project in PROJECTS:
            projects_text += f"• <b>{project['name']}:</b> {project['description']}<br/>"
        
        content.append(Paragraph(projects_text, self.styles['Body']))
        self._add_section_divider(content)
    
    def _add_education(self, content):
        """Add education and certifications section"""
        content.append(Paragraph("EDUCATION & CERTIFICATIONS", self.styles['SubHeader']))
        
        education_text = ""
        for edu in EDUCATION:
            education_text += f"<b>{edu['degree']}</b> – {edu['institution']} | {edu['year']}<br/>"
        
        for cert in CERTIFICATIONS:
            education_text += f"<b>Certification:</b> {cert['name']} – {cert['provider']}, {cert['year']}"
        
        content.append(Paragraph(education_text, self.styles['Body']))
        self._add_section_divider(content)
    
    def _add_soft_skills(self, content):
        """Add soft skills section"""
        content.append(Paragraph("SOFT SKILLS", self.styles['SubHeader']))
        content.append(Paragraph(SOFT_SKILLS, self.styles['Body']))
    
    def generate_resume(self, filename=None):
        """
        Generate the complete resume PDF
        
        Args:
            filename (str): Custom filename for the PDF. If None, generates timestamp-based name
            
        Returns:
            str: Path to the generated PDF file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{PERSONAL_INFO['name'].replace(' ', '_')}_Resume_{timestamp}.pdf"
        
        pdf_path = os.path.join(self.output_dir, filename)
        
        # Create document
        doc = SimpleDocTemplate(
            pdf_path,
            pagesize=A4,
            rightMargin=50,
            leftMargin=50,
            topMargin=50,
            bottomMargin=50
        )
        
        # Build content
        content = []
        
        self._add_header(content)
        self._add_summary(content)
        self._add_technical_skills(content)
        self._add_experience(content)
        self._add_projects(content)
        self._add_education(content)
        self._add_soft_skills(content)
        
        # Generate PDF
        doc.build(content)
        
        return pdf_path

if __name__ == "__main__":
    # Generate resume when run directly
    generator = ResumeGenerator()
    pdf_file = generator.generate_resume()
    print(f"Resume generated successfully: {pdf_file}")
