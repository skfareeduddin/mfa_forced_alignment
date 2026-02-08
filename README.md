# Forced Alignment using Montreal Forced Aligner (MFA)

## Objective
The goal of this project is to perform forced alignment of speech audio with its corresponding transcripts using Montreal Forced Aligner (MFA).

Forced alignment determines the start and end times of words and phonemes in an audio recording given the transcript.

This project also implements systematic handling of Out Of Vocabulary (OOV) words and compares alignment results before and after OOV correction.

---

## Dataset

- 6 audio files (`.wav`)
- 6 transcript files (`.lab`)

The dataset was provided as part of the assignment and used without modification to audio content.

---

## Final Repository Structure

```
forced_alignment_mfa/
├── dataset/
│ ├── *.wav
│ ├── *.lab
│
├── aligned_baseline/
│ ├── *.TextGrid
│
├── aligned_oov_fixed/
│ ├── *.TextGrid
│
├── scripts/
│ ├── extract_oov.py
│ ├── extract_remaining_oov.py
│ ├── normalize_numbers.py
│
├── base_dictionary.dict
├── extended_dictionary.dict
├── README.md
└── Report - Assignment 1.pdf
```
---

## Environment Setup

### 1. Install Conda

Download and install Miniconda if not already installed.

### 2. Create MFA Environment

```bash
conda config --add channels conda-forge
conda create -n aligner montreal-forced-aligner
conda activate aligner
```

### 3. Download Pretrained Models

```bash
mfa model download acoustic english_us_arpa
mfa model download dictionary english_us_arpa
mfa model download g2p english_us_arpa
```
---
### Step 1: Baseline Alignment

Run forced alignment using the pretrained dictionary:
```
mfa align dataset english_us_arpa english_us_arpa aligned_baseline --clean --overwrite
```

Validate alignment and check OOV count:
```
mfa validate dataset english_us_arpa english_us_arpa
```

Initial baseline showed multiple OOV words.

### Step 2: Extract OOV Words

Extract words not present in dictionary:
```
python scripts/extract_oov.py
```

This generates:
```
oov_words.txt
```

### Step 3: Generate Pronunciations using G2P

Generate phoneme sequences for OOV words:
```
mfa g2p oov_words.txt english_us_arpa generated_oov.dict
```

### Step 4: Extend Dictionary

Append generated pronunciations to the base dictionary:
```
base_dictionary.dict + generated_oov.dict → extended_dictionary.dict
```

This creates a dictionary containing both original and generated pronunciations.

### Step 5: Numeric Normalization

Some OOV words were numeric tokens such as:
```
1971
300
35
800
```

These were converted into spoken forms using:
```
python scripts/normalize_numbers.py
```

Example conversions:
```
1971 → nineteen seventy one
300 → three hundred
35 → thirty five
800 → eight hundred
```

### Step 6: Re-run Alignment with Extended Dictionary
```
mfa align dataset extended_dictionary.dict english_us_arpa aligned_oov_fixed --clean --overwrite
```

Validate again:
```
mfa validate dataset extended_dictionary.dict english_us_arpa
```
OOV count reduced significantly after correction.
---

### Alignment Inspection

TextGrid files were inspected using Praat software.

Two versions were compared:

- `aligned_baseline/`
- `aligned_oov_fixed/`

---

### Observations

Baseline alignment:

- Skipped or poorly segmented words in OOV regions
- Minor boundary inaccuracies
- Silence segments in place of missing pronunciations

After OOV handling:
-Previously skipped words correctly aligned
- Improved word boundary placement
- More stable phoneme segmentation
- Reduced silence artifacts
---
