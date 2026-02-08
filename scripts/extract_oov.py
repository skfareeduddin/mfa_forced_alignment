import os

dataset_path = "dataset"

dictionary_path = r"C:\Users\skfar\Documents\MFA\pretrained_models\dictionary\english_us_arpa.dict"

dict_words = set()
with open(dictionary_path, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() and not line.startswith(";;;"):
            word = line.split()[0]
            dict_words.add(word.lower())

transcript_words = set()
for file in os.listdir(dataset_path):
    if file.endswith(".lab") or file.endswith(".txt"):
        with open(os.path.join(dataset_path, file), "r", encoding="utf-8") as f:
            text = f.read().lower()
            words = text.split()
            transcript_words.update(words)

oov_words = sorted(transcript_words - dict_words)

with open("oov_words.txt", "w", encoding="utf-8") as f:
    for word in oov_words:
        f.write(word + "\n")

print(f"Found {len(oov_words)} OOV words.")
print("Saved to oov_words.txt")
