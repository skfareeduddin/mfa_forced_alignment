import os
import subprocess

base_dir = os.path.dirname(os.path.abspath(__file__))

project_root = os.path.dirname(base_dir)

dataset_path = os.path.join(project_root, "dataset")
output_path = os.path.join(project_root, "outputs")

dict_path = os.path.expanduser(r"~/Documents/MFA/pretrained_models/dictionary/english_us_arpa.dict")
acoustic_path = os.path.expanduser(r"~/Documents/MFA/pretrained_models/acoustic/english_us_arpa.zip")

command = [
    "mfa", "align", "--clean", "--overwrite",
    dataset_path, dict_path, acoustic_path, output_path
]

print("Running MFA forced alignment...")
print("Dataset:", dataset_path)
print("Dictionary:", dict_path)
print("Acoustic Model:", acoustic_path)
print("Output:", output_path)

subprocess.run(command, check=True)
print("\n✅ Alignment completed successfully!")
