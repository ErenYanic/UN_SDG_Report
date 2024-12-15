import re
import os
import pandas as pd
from pdfplumber import open as pdf_open

# Define patterns for SDG-related extraction
patterns = {
    "SDG Goal": r"Goal\s+\d+|Sustainable Development Goal \d+",
    "SDG Target": r"Target\s+\d+\.\d+",
    "SDG Indicator": r"Indicator\s+\d+\.\d+\.\d+",
    "Global Agreement": r"(Paris Agreement|2030 Agenda|Addis Ababa Action Agenda|Sendai Framework)",
    "Climate Metrics": r"(net-zero emissions|1\.5°C target|greenhouse gas emissions|climate-resilient)",
    "Poverty": r"(poverty line|extreme poverty|social protection coverage)",
    "Education": r"(school completion rate|minimal reading proficiency|education improvement)",
    "Gender Equality": r"(gender-responsive budgeting|gender parity|women in leadership)",
    "Progress Status": r"(on track|minimal progress|regressed below baseline|stalled progress|no data)",
    "Action and Impact": r"(urgent action|transformative change|economic loss|child mortality)",
    "Data and Monitoring": r"(disaggregated data|data gaps|national monitoring)",
    "Biodiversity and Ecosystems": r"biodiversity loss|endangered species|ecosystem degradation",
    "Marine and Water Issues": r"marine pollution|life below water|ocean acidification|water stress",
    "Energy Transition": r"renewable energy investments|clean energy targets|energy efficiency",
    "Work and Employment": r"decent work|unemployment rate|labour market",
    "Inequalities": r"income inequality|reduced inequalities|social justice",
    "Health Metrics": r"universal health coverage|mental health|disease burden",
    "Progress and Performance": r"achieved progress|severe off-track|performance indicators",
    "Data Gaps": r"insufficient data|monitoring gaps|data availability",
    "Financial Support": r"climate finance|debt relief|development aid",
    "Action and Transformation": r"transformative action|radical change|bold initiatives",
    "Crisis and Emergency": r"urgent measures|crisis response|global emergencies"
}

# Input: Folder with PDF files
pdf_folder_path = "/home/ereny/PycharmProjects/PythonProject/UN_SDG_Report/sdg_pdfs"  # Update with the correct folder path
output_csv_path = "extracted_sdg_data.csv"

# Function to extract text from PDFs
def extract_text_from_pdf(pdf_path):
    extracted_text = ""
    with pdf_open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"
    return extracted_text

# Function to search patterns in text
def search_keywords_in_text(text, patterns):
    results = []
    for category, pattern in patterns.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            results.append({"Category": category, "Match": match})
    return results

# Process all PDF files
all_results = []
pdf_files = [f for f in os.listdir(pdf_folder_path) if f.endswith(".pdf")]

for pdf_file in pdf_files:
    print(f"Processing: {pdf_file}")
    pdf_path = os.path.join(pdf_folder_path, pdf_file)
    text = extract_text_from_pdf(pdf_path)
    results = search_keywords_in_text(text, patterns)
    for result in results:
        result["File"] = pdf_file
        all_results.append(result)

# Save results to a CSV file
df = pd.DataFrame(all_results)
df.to_csv(output_csv_path, index=False, encoding="utf-8")

print(f"Extraction complete! Results saved to {output_csv_path}")
