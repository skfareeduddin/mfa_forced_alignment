# Forced Alignment using Montreal Forced Aligner (MFA)

**Applicant:** Syed Khaja Fareeduddin  
**Project:** Speech-to-Speech Machine Translation Internship – Assignment 1  

---

## Objective
The goal of this assignment is to perform **forced alignment** of speech audio with its corresponding text transcript using **Montreal Forced Aligner (MFA)**.  
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
├─ report/
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

## Run Forced Alignment

```bash
mfa align --clean --overwrite "dataset" "path_to_dictionary/english_us_arpa.dict" "path_to_acoustic_model/english_us_arpa.zip" "outputs"
```

- **dataset**: Path to the folder containing audio and transcript files.  
- **outputs**: Folder where TextGrid alignment files will be saved.

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
- Minor warnings due to single speaker processing, but they did not affect alignment quality.  
- Viewing results in **Praat** allowed clear visualization of word and phoneme boundaries.  

---

## References
- Montreal Forced Aligner Documentation: [https://montreal-forced-aligner.readthedocs.io](https://montreal-forced-aligner.readthedocs.io)  
- Praat Software: [http://www.fon.hum.uva.nl/praat/](http://www.fon.hum.uva.nl/praat/)
