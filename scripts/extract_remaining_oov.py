import os
import re

dataset_path = "dataset"
dictionary_path = "extended_dictionary.dict"

dict_words = set()
with open(dictionary_path, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() and not line.startswith(";;;"):
            word = line.split()[0].lower()
            dict_words.add(word)

def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s']", "", text)
    text = text.replace("’", "'")
    return text

transcript_words = set()
for file in os.listdir(dataset_path):
    if file.endswith(".lab") or file.endswith(".txt"):
        with open(os.path.join(dataset_path, file), "r", encoding="utf-8") as f:
            text = normalize_text(f.read())
            words = text.split()
            transcript_words.update(words)

remaining_oov = sorted(transcript_words - dict_words)

with open("remaining_oov.txt", "w", encoding="utf-8") as f:
    for word in remaining_oov:
        f.write(word + "\n")

print(f"Remaining OOV word types: {len(remaining_oov)}")
print("Saved to remaining_oov.txt")
