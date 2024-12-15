import pdfplumber
import os

# PDF dosyalarının bulunduğu klasörün yolu
pdf_folder_path = "/home/ereny/PycharmProjects/PythonProject/UN_SDG_Report/sdg_pdfs"  # BURAYI GÜNCELLE

# Metin dosyalarını kaydedeceğimiz ana klasör
output_folder_path = "extracted_sdg_texts"
os.makedirs(output_folder_path, exist_ok=True)


# Metin çıkarma fonksiyonu
def extract_text_from_pdf(pdf_path):
    extracted_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:  # Eğer sayfa metin içeriyorsa ekle
                extracted_text += text + "\n"
    return extracted_text


# PDF dosyalarının isimlerini al ve döngü ile işle
pdf_files = [f for f in os.listdir(pdf_folder_path) if f.endswith(".pdf")]

for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_folder_path, pdf_file)
    print(f"Processing: {pdf_file}")

    # Metni PDF'den çıkar
    extracted_text = extract_text_from_pdf(pdf_path)

    # Çıktıyı PDF adına göre kaydet (örneğin: SDG2020.txt, SDG2021.txt)
    output_file_name = f"{os.path.splitext(pdf_file)[0]}.txt"  # PDF ismi .txt olarak ayarlanır
    output_file_path = os.path.join(output_folder_path, output_file_name)

    with open(output_file_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(extracted_text)

print("All PDFs processed and saved successfully!")
