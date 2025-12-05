# Forced Alignment using Montreal Forced Aligner (MFA)

## Objective
The goal is to perform **forced alignment** of speech audio with its corresponding text transcript using **Montreal Forced Aligner (MFA)**.  
Forced alignment automatically determines the start and end times of words and phonemes in an audio recording, given the transcript.

---

## Dataset
- Audio files (`.wav`) and corresponding transcripts (`.txt`) are provided.  
- Number of audio files: 6  
- Number of speakers: 1  
- Each transcript corresponds to a single utterance.  

---

## Folder Structure
```
forced_alignment_mfa/
├─ dataset/
├─ outputs/                
├─ praat_screenshots/
├─ scripts/
|  ├─ automate_alignment.py
|  └─ run_alignment.bat
└─ README.md
```

---

## Setup Instructions

### 1. Install Conda (if not already installed)
[Miniconda installation guide](https://docs.conda.io/en/latest/miniconda.html)

### 2. Create Conda Environment and Install MFA
```bash
conda config --add channels conda-forge
conda create -n aligner montreal-forced-aligner
conda activate aligner
```

### 3. Download Pretrained Models
```bash
mfa model download acoustic english_us_arpa
mfa model download dictionary english_us_arpa
```

---

## Running Forced Alignment
You have two options to run the alignment: manually using the MFA CLI command or automatically using the provided Python and batch scripts.

---

## Option 1: Run Forced Alignment (Manual)

```bash
mfa align --clean --overwrite "dataset" "path_to_dictionary/english_us_arpa.dict" "path_to_acoustic_model/english_us_arpa.zip" "outputs"
```

- **dataset**: Path to the folder containing audio and transcript files.  
- **outputs**: Folder where TextGrid alignment files will be saved.

---

## Option 2: Automation (Extra Credit Work)
To improve efficiency and reproducibility, the entire alignment process was automated using a Python script and a Windows batch file.

## Python Script - `automate_alignment.py`
This script dynamically detects the dataset and output paths relative to its location, making it fully portable across systems.

This script runs the complete MFA pipeline with the `--clean` and `--overwrite` flags for all `.wav` and `.txt` pairs in the dataset folder.

<details>
<summary> Click here to view the python script </summary>

```python
import os
import subprocess

# Get the directory where this script is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Move one level up (to the project root)
project_root = os.path.dirname(base_dir)

# Build dynamic paths
dataset_path = os.path.join(project_root, "dataset")
output_path = os.path.join(project_root, "outputs")

# Expand user path for pretrained models (cross-platform)
dict_path = os.path.expanduser(r"~/Documents/MFA/pretrained_models/dictionary/english_us_arpa.dict")
acoustic_path = os.path.expanduser(r"~/Documents/MFA/pretrained_models/acoustic/english_us_arpa.zip")

# Build the MFA command
command = [
    "mfa", "align", "--clean", "--overwrite",
    dataset_path, dict_path, acoustic_path, output_path
]

print("Running MFA forced alignment...")
print("Dataset:", dataset_path)
print("Dictionary:", dict_path)
print("Acoustic Model:", acoustic_path)
print("Output:", output_path)

# Run the command
subprocess.run(command, check=True)
print("\n✅ Alignment completed successfully!")
```

</details>

## Batch File - `run_alignment.bat`
This batch file activates the Conda environment and runs the Python automation script automatically.

<details>
<summary> Click here to view the batch file </summary>

```bat
@echo off
call conda activate aligner
python automate_alignment.py
```

</details>

## How To Use

Simply double-click the `run_alignment.bat` file to automatically:
- Activate the Conda environment
- Run the alignment script
- Generate aligned `.TextGrid` files inside the `outputs/` folder

---

## Inspecting Results
- Generated TextGrid files can be viewed using **[Praat](http://www.fon.hum.uva.nl/praat/)** software.  
- Screenshots of alignments in Praat are included in the `praat_screenshots/` folder.

**Sample Alignment (`ISLE_SESS0131_BLOCKD02_01_sprt1.TextGrid`):**

**Words:**
```
0.0 – 0.44     (silence)
0.44 – 0.53    i
0.53 – 0.92    said
0.92 – 1.33    white
1.33 – 1.48    (silence)
1.48 – 1.8     not
1.8 – 2.25     bait
2.25 – 4.125   (silence)
```

**Phonemes:**
```
0.0 – 0.44     (silence)
0.44 – 0.53    AY1
0.53 – 0.71    S
0.71 – 0.79    EH1
0.79 – 0.92    D
0.92 – 1.03    W
1.03 – 1.17    AY1
1.17 – 1.33    T
1.33 – 1.48    (silence)
1.48 – 1.55    N
1.55 – 1.62    AA1
1.62 – 1.8     T
1.8 – 1.84     B
1.84 – 2.05    EY1
2.05 – 2.25    T
2.25 – 4.125   (silence)
```

---

## Observations
- MFA successfully aligned all audio files.
- The automation script ensures consistent, repeatable results and reduces manual effort.
- Dynamic path detection allows this script to run seamlessly on any system.
- Viewing results in Praat provided a clear visual representation of word and phoneme boundaries.
- Minor warnings (due to single-speaker data) did not impact alignment quality. 

---

## References
- Montreal Forced Aligner Documentation: [https://montreal-forced-aligner.readthedocs.io](https://montreal-forced-aligner.readthedocs.io)  
- Praat Software: [http://www.fon.hum.uva.nl/praat/](http://www.fon.hum.uva.nl/praat/)
