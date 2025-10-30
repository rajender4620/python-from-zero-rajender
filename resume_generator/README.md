# Resume Generator 📄

A professional Python-based resume generator that creates beautifully formatted PDF resumes using ReportLab.

## Features ✨

- **Professional Layout**: Clean, modern design with proper typography
- **Customizable Colors**: Professional blue color scheme with customizable options
- **Modular Structure**: Well-organized code with separate modules for data, styling, and generation
- **Easy to Modify**: Simple data structure for updating personal information
- **High Quality Output**: PDF generation with proper formatting and styling

## Project Structure 📁

```
resume_generator/
├── src/
│   ├── __init__.py           # Package initialization
│   ├── resume_data.py        # Personal and professional data
│   ├── pdf_styles.py         # PDF styling and color configuration
│   └── resume_generator.py   # Main resume generation logic
├── output/                   # Generated PDF files
├── templates/                # Future template storage
├── main.py                   # Main entry point
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## Installation 🚀

1. **Clone or download the project**
   ```bash
   cd resume_generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage 💻

### Quick Start

Run the main script to generate a resume:

```bash
python main.py
```

This will create a PDF file in the `output/` directory.

### Customizing Your Resume

1. **Update Personal Information**: Edit `src/resume_data.py`
   - Modify `PERSONAL_INFO` with your details
   - Update `SUMMARY` with your professional summary
   - Add/modify entries in `EXPERIENCE`, `PROJECTS`, etc.

2. **Customize Styling**: Edit `src/pdf_styles.py`
   - Change colors, fonts, and spacing
   - Modify the color scheme in the `COLORS` dictionary

3. **Advanced Usage**: Use the ResumeGenerator class directly
   ```python
   from src.resume_generator import ResumeGenerator
   
   generator = ResumeGenerator(output_dir="custom_output")
   pdf_path = generator.generate_resume("my_custom_resume.pdf")
   print(f"Resume saved to: {pdf_path}")
   ```

## Customization Guide 🎨

### Updating Your Information

Edit the following sections in `src/resume_data.py`:

- **PERSONAL_INFO**: Name, title, contact information
- **SUMMARY**: Professional summary/objective
- **TECHNICAL_SKILLS**: Technical skills by category
- **EXPERIENCE**: Work experience with responsibilities
- **PROJECTS**: Personal/professional projects
- **EDUCATION**: Educational background
- **CERTIFICATIONS**: Professional certifications
- **SOFT_SKILLS**: Soft skills and competencies

### Styling Options

In `src/pdf_styles.py`, you can customize:

- **Colors**: Primary color, text colors, divider colors
- **Fonts**: Font families and sizes
- **Spacing**: Line spacing and margins
- **Alignment**: Text alignment options

## Dependencies 📦

- **reportlab**: PDF generation library
- **Python 3.7+**: Required Python version

## Output 📋

The generated resume includes:

- Professional header with contact information
- Professional summary
- Technical skills organized by category
- Work experience with detailed responsibilities
- Projects showcase
- Education and certifications
- Soft skills

## Contributing 🤝

Feel free to fork this project and customize it for your needs. Some ideas for enhancement:

- Multiple resume templates
- Web interface for easy editing
- Export to different formats
- Integration with LinkedIn API
- Dynamic skill visualization

## License 📄

This project is open source and available under the MIT License.

## Author 👨‍💻

**S Rajender Reddy**
- Flutter Developer
- Email: rajender.4620@gmail.com
- LinkedIn: [s-rajender-reddy](https://linkedin.com/in/s-rajender-reddy-8a425522a/)

---

*Generated with ❤️ using Python and ReportLab*
