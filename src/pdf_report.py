from fpdf import FPDF

def generate_pdf_report(df, image_path, output_path="visualizations/elearning_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.cell(200, 10, txt="E-Learning Platform Analysis Report", ln=True, align="C")
    pdf.ln(10)

    # Section Heading
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Course Enrollment Summary:", ln=True, align="L")

    pdf.set_font("Arial", size=12)
    pdf.ln(5)

    # Add course data
    for index, row in df.iterrows():
        pdf.cell(200, 10, txt=f"{row['Course_Title']}: {row['Enrollments']} enrollments", ln=True, align="L")

    pdf.ln(10)

    # Add bar chart image
    try:
        pdf.image(image_path, x=10, w=180)
    except RuntimeError:
        print("⚠️ Could not load image:", image_path)

    # Save PDF
    pdf.output(output_path)
    print("📄 PDF Report generated at:", output_path)
