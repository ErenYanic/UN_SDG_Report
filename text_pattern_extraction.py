import re
import os
import pandas as pd

# Metin dosyalarının olduğu klasör
text_folder_path = "/home/ereny/PycharmProjects/PythonProject/UN_SDG_Report/extracted_sdg_texts"  # Metin dosyalarının bulunduğu klasörü buraya girin
output_csv_path = "text_extracted_sdg_data.csv"  # Çıktı dosyası için isim

# Aranacak Regex kalıpları
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

# Fonksiyon: Belirli bir dosyadaki anahtar kelimeleri bul
def search_keywords_in_text(text, patterns):
    results = []
    for category, pattern in patterns.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            results.append({"Category": category, "Match": match})
    return results

# Tüm metin dosyalarını işleyip sonuçları toplama
all_results = []

txt_files = [f for f in os.listdir(text_folder_path) if f.endswith(".txt")]

for txt_file in txt_files:
    print(f"Processing: {txt_file}")
    file_path = os.path.join(text_folder_path, txt_file)
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    results = search_keywords_in_text(text, patterns)
    for result in results:
        result["File"] = txt_file  # Hangi dosyadan geldiğini ekle
        all_results.append(result)

# Sonuçları CSV olarak kaydet
df = pd.DataFrame(all_results)
df.to_csv(output_csv_path, index=False, encoding="utf-8")

print(f"Extraction complete! Results saved to {output_csv_path}")
