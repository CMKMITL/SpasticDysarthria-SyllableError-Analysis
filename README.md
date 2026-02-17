# SpasticDysarthria‑SyllableError‑Analysis

This repository contains Python code for analyzing acoustic features of syllables produced by people with spastic dysarthria and healthy controls. It supports a research study that evaluates syllable‑level pronunciation errors and builds classification models to distinguish between the two groups.

## Contents

- **`Syllableerror_scoring.ipynb`** — Computes syllable‑level error scores by counting misspellings in automatic speech‑recognition (ASR) transcripts for each sentence.
- **`LogisticRegressionModel_train-test_randomstatevariation.ipynb`** — Builds logistic‑regression classifiers with **random state shuffling**. We train 10 000 models using different random seeds for train/test splits, then compute the median area under the ROC curve (AUC) and illustrate the distribution in violin plots.
- **`PermutationTest_logisticregressionmodel.ipynb`** — Performs permutation tests to assess the statistical significance of the observed median AUC values. It compares the empirical AUC distribution against distributions derived from label‑shuffled data and computes p‑values. 

## Usage

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/CMKMITL/SpasticDysarthria-SyllableError-Analysis.git

## License and Citation

No open‑source license is provided at this time, as the code is intended for academic use only. If you use this code for academic purposes, please cite our forthcoming article (**“[To be announced]”**). Feel free to contact us for citation details.

## Data Availability

The original data file containing ASR-transcribed syllables for all subjects is not publicly shared due to privacy and data protection regulations in accordance with the ethical review board. Access may be granted upon reasonable request to the primary or the corresponding author.
