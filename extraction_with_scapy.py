import spacy
import os
import pandas as pd

# SpaCy modelini yükle
nlp = spacy.load("en_core_web_trf")  # Gerekirse model kur: python -m spacy download en_core_web_sm

# Metin dosyalarının olduğu klasör
text_folder_path = "/home/ereny/PycharmProjects/PythonProject/UN_SDG_Report/extracted_sdg_texts"
output_csv_path = "trf_spacy_extracted_sdg_data.csv"

# Tüm metin dosyalarını işleyip sonuçları toplama
all_results = []

# Metin dosyalarını işleme
txt_files = [f for f in os.listdir(text_folder_path) if f.endswith(".txt")]

for txt_file in txt_files:
    print(f"Processing: {txt_file}")
    file_path = os.path.join(text_folder_path, txt_file)
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # SpaCy modeli ile işlem yap
    doc = nlp(text)
    for ent in doc.ents:
        all_results.append({
            "File": txt_file,
            "Entity": ent.text,
            "Label": ent.label_  # Örneğin: PERSON, ORG, DATE
        })

# Sonuçları CSV olarak kaydet
df = pd.DataFrame(all_results)
df.to_csv(output_csv_path, index=False, encoding="utf-8")

print(f"Extraction complete! Results saved to {output_csv_path}")
