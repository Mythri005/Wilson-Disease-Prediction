# from fpdf import FPDF
# from PyPDF2 import PdfReader

# # Create PDF
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)

# # Data
# features = [
#     "Age", "Copper in Urine", "Copper in Blood Serum", "Ceruloplasmin Level", 
#     "ATB7B Gene Mutation", "Kayser-Fleischer Rings", "Neurological Symptoms Score", 
#     "AST", "Cognitive Function Score", "ALT"
# ]
# values = [
#     -1.551039, 0.939818, 0.955878, -1.167502, 
#     1, 1, 1.045229, 
#     1.321788, 1.858906, 1.423457
# ]

# # Add data to PDF
# pdf.set_font("Arial", style="B", size=14)
# pdf.cell(200, 10, txt="Feature Values", ln=True, align="C")
# pdf.ln(10)

# pdf.set_font("Arial", size=12)
# pdf.cell(100, 10, txt="Feature", border=1, align="C")
# pdf.cell(90, 10, txt="Value", border=1, align="C")
# pdf.ln()

# for feature, value in zip(features, values):
#     pdf.cell(100, 10, txt=feature, border=1, align="C")
#     pdf.cell(90, 10, txt=str(value), border=1, align="C")
#     pdf.ln()

# # Save PDF
# pdf_file = "feature_values.pdf"
# pdf.output(pdf_file)
# print(f"PDF created: {pdf_file}")

# # PDF Scanner
# def scan_pdf(file_path):
#     reader = PdfReader(file_path)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text()
#     return text

# # Scan and extract content from the PDF
# scanned_text = scan_pdf(pdf_file)
# print("\nScanned PDF Content:\n")
# print(scanned_text)

from fpdf import FPDF
from PyPDF2 import PdfReader

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Data
features = [
    "Age", "Copper in Urine", "Copper in Blood Serum", "Ceruloplasmin Level", 
    "ATB7B Gene Mutation", "Kayser-Fleischer Rings", "Neurological Symptoms Score", 
    "AST", "Cognitive Function Score", "ALT"
]
values = [
    -0.09725121789291359,
    -0.27862329978274275,
    0.015068075829824086,
    -0.7656000740109069,
    0.0,
    0.0,
    -0.6269858142353957,
    0.6122924563755894,
    0.27196520333948526,
    -1.9058157181163113
]

# Add data to PDF
pdf.set_font("Arial", style="B", size=14)
pdf.cell(200, 10, txt="Feature Values", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.cell(100, 10, txt="Feature", border=1, align="C")
pdf.cell(90, 10, txt="Value", border=1, align="C")
pdf.ln()

for feature, value in zip(features, values):
    pdf.cell(100, 10, txt=feature, border=1, align="C")
    pdf.cell(90, 10, txt=str(value), border=1, align="C")
    pdf.ln()

# Save PDF
pdf_file = "negative_feature_values.pdf"
pdf.output(pdf_file)
print(f"PDF created: {pdf_file}")

# PDF Scanner
def scan_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Scan and extract content from the PDF
scanned_text = scan_pdf(pdf_file)
print("\nScanned PDF Content:\n")
print(scanned_text)
