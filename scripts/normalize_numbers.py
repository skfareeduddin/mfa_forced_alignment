import os
from num2words import num2words

dataset_path = "dataset"

def normalize_text(text):
    words = text.split()
    normalized_words = []
    
    for word in words:
        if word.isdigit():
            try:
                normalized_words.append(num2words(int(word)))
            except:
                normalized_words.append(word)
        else:
            normalized_words.append(word)
    
    return " ".join(normalized_words)

for file in os.listdir(dataset_path):
    if file.endswith(".lab") or file.endswith(".txt"):
        file_path = os.path.join(dataset_path, file)
        
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read().lower()
        
        normalized = normalize_text(text)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(normalized)

print("Number normalization complete.")
