import pdfplumber
import os
import pandas as pd

# PDF klasör yolu
pdf_folder_path = "/home/ereny/PycharmProjects/PythonProject/UN_SDG_Report/sdg_pdfs"
output_folder_path = "extracted_tables"
os.makedirs(output_folder_path, exist_ok=True)


# PDF'den tablo ayırma ve kaydetme fonksiyonu
def extract_tables_from_pdf(pdf_path, output_file):
    with pdfplumber.open(pdf_path) as pdf:
        all_tables = []
        for page_num, page in enumerate(pdf.pages):
            tables = page.extract_tables()  # Sayfadaki tabloları al
            for table in tables:
                # Tabloyu DataFrame'e dönüştür
                df = pd.DataFrame(table)
                all_tables.append(df)

        # Tabloları tek bir Excel dosyasında kaydet
        if all_tables:
            with pd.ExcelWriter(output_file) as writer:
                for idx, table in enumerate(all_tables):
                    table.to_excel(writer, sheet_name=f"Table_{idx + 1}", index=False)


# Tüm PDF'leri işle
pdf_files = [f for f in os.listdir(pdf_folder_path) if f.endswith(".pdf")]

for pdf_file in pdf_files:
    print(f"Processing tables in: {pdf_file}")
    pdf_path = os.path.join(pdf_folder_path, pdf_file)
    output_file = os.path.join(output_folder_path, f"{os.path.splitext(pdf_file)[0]}_tables.xlsx")
    extract_tables_from_pdf(pdf_path, output_file)

print("All tables extracted and saved successfully!")
