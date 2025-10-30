from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# File path
pdf_path = "/mnt/data/S_Rajender_Reddy_Flutter_Developer_Resume_Colored.pdf"

# Create doc
doc = SimpleDocTemplate(pdf_path, pagesize=A4, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)

# Styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Header', fontSize=18, leading=22, textColor=colors.HexColor("#0078D4"), spaceAfter=6, fontName='Helvetica-Bold', alignment=1))
styles.add(ParagraphStyle(name='SubHeader', fontSize=12, leading=16, textColor=colors.HexColor("#0078D4"), spaceAfter=4, fontName='Helvetica-Bold', underlineWidth=0.5))
styles.add(ParagraphStyle(name='Body', fontSize=10.5, leading=14, textColor=colors.black, spaceAfter=6))
styles.add(ParagraphStyle(name='Contact', fontSize=9.5, leading=12, textColor=colors.HexColor("#333333"), alignment=1))

content = []

# Header
content.append(Paragraph("S RAJENDER REDDY", styles['Header']))
content.append(Paragraph("Flutter Developer", styles['SubHeader']))
content.append(Paragraph("📞 8886781737 | 📧 rajender.4620@gmail.com | 🌐 linkedin.com/in/s-rajender-reddy-8a425522a/", styles['Contact']))
content.append(Spacer(1, 8))
content.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#0078D4")))
content.append(Spacer(1, 12))

# Summary
content.append(Paragraph("PROFESSIONAL SUMMARY", styles['SubHeader']))
summary_text = """
Dynamic Flutter developer with over 3.5 years of experience building high-performance, cross-platform mobile applications for 
enterprise collaboration and e-learning domains. Proficient in BLoC, HydratedBloc, and F-DDD architecture for scalable, 
offline-capable solutions. Skilled in Firebase, Node.js, and REST API integration, delivering real-time and interactive app experiences.
"""
content.append(Paragraph(summary_text, styles['Body']))
content.append(Spacer(1, 8))
content.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey))
content.append(Spacer(1, 8))

# Technical Skills
content.append(Paragraph("TECHNICAL SKILLS", styles['SubHeader']))
skills = """
<b>Programming Languages:</b> Dart, TypeScript, JavaScript, Python<br/>
<b>Frontend:</b> Flutter, Angular <br/>
<b>State Management:</b> BLoC, HydratedBloc, Provider<br/>
<b>Backend & APIs:</b> Firebase, SQLite, REST APIs, GraphQL, Dio, Chopper<br/>
<b>Tools:</b> Git, VS Code, Android Studio, Cursor AI, CI/CD Pipelines<br/>
<b>Architecture:</b> F-DDD, SOLID Principles<br/>
<b>Other:</b> Performance Optimization, Animations, Unit & Widget Testing, Agile Development
"""
content.append(Paragraph(skills, styles['Body']))
content.append(Spacer(1, 8))
content.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey))
content.append(Spacer(1, 8))

# Experience
content.append(Paragraph("PROFESSIONAL EXPERIENCE", styles['SubHeader']))

# inLynk
inlynk = """
<b>Flutter Developer | inLynk | Hyderabad | Feb 2025 – Present</b><br/>
• Developed the mobile version of inLynk, an Enterprise Collaboration & B2B SaaS platform connecting employees, partners, and clients.<br/>
• Implemented real-time messaging, feed posting, task/resource tracking, and push notifications using Firebase Firestore and BLoC.<br/>
• Applied F-DDD architecture for scalable, offline-capable architecture.<br/>
• Leveraged Cursor AI for rapid prototyping and improved animations and UI transitions.<br/>
"""
content.append(Paragraph(inlynk, styles['Body']))

# WeXL Edu
wexl = """
<b>Flutter Developer | WeXL Edu Pvt Ltd | Hyderabad | May 2022 – Jan 2024</b><br/>
• Built the mobile version of WeXL Schools, an e-learning platform integrated with Zoom and Google Meet.<br/>
• Developed modules for course content, live classes, and quizzes with efficient state management using BLoC.<br/>
• Led the development of a grocery e-commerce app with location-based store discovery and Razorpay integration.<br/>
• Published apps to Play Store and App Store ensuring optimized performance and clean architecture.<br/>
"""
content.append(Paragraph(wexl, styles['Body']))
content.append(Spacer(1, 8))
content.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey))
content.append(Spacer(1, 8))

# Projects
content.append(Paragraph("PROJECTS", styles['SubHeader']))
projects = """
• <b>AI-Powered Expense Tracker:</b> Smart financial tracker leveraging Firebase backend for authentication and data management.<br/>
• <b>Social Media App:</b> Real-time posting and chat features powered by Firebase Firestore with modern Flutter UI.<br/>
"""
content.append(Paragraph(projects, styles['Body']))
content.append(Spacer(1, 8))
content.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey))
content.append(Spacer(1, 8))

# Education & Certifications
content.append(Paragraph("EDUCATION & CERTIFICATIONS", styles['SubHeader']))
education = """
<b>B.Sc in Mathematics, Physics, and Computer Science</b> – Gowthami Degree College, Mahabubnagar | 2021<br/>
<b>Certification:</b> Flutter Development – Udemy, 2024
"""
content.append(Paragraph(education, styles['Body']))
content.append(Spacer(1, 8))
content.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey))
content.append(Spacer(1, 8))

# Soft Skills
content.append(Paragraph("SOFT SKILLS", styles['SubHeader']))
soft_skills = "Problem-Solving, Collaboration, Communication, Adaptability, Attention to Detail"
content.append(Paragraph(soft_skills, styles['Body']))

# Build PDF
doc.build(content)
pdf_path
