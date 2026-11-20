# Spastic dysarthria: ASR syllable-error analysis

Reproducible analysis for **Automatic Speech Recognition and Phonetics-Informed Sentence Design for Spastic Dysarthria and Corticobulbar Lesion Detection**.

The study includes 37 patients and 37 controls. Four Thai sentences target labial (LBP), lingual-alveolar/palatal (LAP), velopharyngeal (VP), and mixed (MP) consonant groups. Apple Siri transcriptions are converted to syllable-error scores, then evaluated directly by ROC analysis. A combined logistic regression model is a secondary analysis.

## Notebooks

Run the notebooks in numerical order from this repository folder. Each has numbered step headings; generated tables and figures are saved in `results/`.

| Notebook | Manuscript outputs |
| --- | --- |
| [01 — Syllable-error scoring](01_Syllable_error_scoring.ipynb) | Raw and normalized scores for all 74 participants |
| [02 — Score comparisons](02_Score_comparisons.ipynb) | Figure 2; Supplementary Table S3 |
| [03 — Individual and pooled ROC analysis](03_Individual_and_pooled_ROC.ipynb) | Figure 3; Table 2; paired AUC comparisons |
| [04 — Combined logistic regression](04_Combined_logistic_model.ipynb) | Figure 4; Supplementary Figure S2; Supplementary Tables S4–S5 |

Earlier individual-sentence logistic regression and permutation-test notebooks have been removed from the current version. They remain available in Git history.

## Run the analysis

Use Python 3.12 or 3.13. Install the pinned analysis packages in a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python run_analysis.py
```

On Windows, activate the environment with `.venv\Scripts\activate` instead. The runner executes the notebook code without requiring Jupyter. For interactive use, install JupyterLab in the same environment (`python -m pip install jupyterlab`) and open the notebooks there.

The complete run includes **100 repetitions of nested five-fold validation within each of 50 training subsets** and can take substantial time. To regenerate the final fitted models and all supported manuscript figures/tables without repeating that separate validation calculation:

```bash
python run_analysis.py --skip-nested
```

This option still refits all 50 final models. It does not substitute stored predictions or reduce the number of train–test splits. In notebook 04, `RUN_NESTED_CV` controls the same optional omission and defaults to `True`.

## Data and scoring

- [Aligned ASR transcriptions](syllableseparation_apple_corrected.csv): the existing public syllable-level CSV for all 74 participants.
- `Syllableerror_scores_raw_and_normalized.csv`: generated locally by notebook 01; run that notebook before the downstream analyses.
- `sub_id` identifies participants; `disease` is 1 for patients and 0 for controls.
- `s1_1`, `s1_2`, etc. contain aligned target syllables; `e1_1`, etc. are additional-syllable slots. Preserve the supplied zero placeholders.

| Sentence | Raw score | Normalized score | Target syllables |
| --- | --- | --- | --- |
| LBP | `error_1` | `error_rate_1` | 8 |
| LAP | `error_2` | `error_rate_2` | 8 |
| VP | `error_3` | `error_rate_3` | 7 |
| MP | `error_4` | `error_rate_4` | 11 |

The predefined accepted-transcription lists are shown in notebook 01. Each unaccepted or absent target syllable counts as one error. Each additional-syllable slot counts as one error unless its value is `0`. These are transcription-based scoring rules, not direct acoustic judgments. The code starts from already segmented and aligned transcriptions; it does not perform ASR or alignment.

Normalized scores equal raw errors divided by target syllable count. Additional errors are included, so the formula is not mathematically restricted to 0–1. The pooled score is **the sum of the four raw error counts divided by 34**, not the unweighted mean of the four normalized scores.

## Analysis details

- Individual and pooled ROC analyses use all 74 participants. DeLong intervals account for ties, and paired DeLong comparisons use Holm correction across all 10 pairs.
- Youden thresholds classify scores at or above the threshold as positive. Ties select the highest finite threshold. Full-cohort threshold metrics are apparent performance estimates.
- The combined model uses L2 logistic regression, training-only standardization, 50 stratified 70:30 splits (seeds 42–91), and the original 17-value C grid. Final five-fold grid search is separate from repeated nested validation.
- The representative split is the earliest split with test AUC closest to the median. Its comparisons use the same 23 test participants and Holm correction across five model-versus-score tests. These results and intervals are conditional on the selected split.
- Supplementary Table S4 uses independent Jeffreys Beta(0.5, 0.5) priors and 200,000 posterior draws (seed 42). Table S5 describes coefficient variation across overlapping partitions; no significance tests across split rows are performed.
- The reported combined-AUC numerical summary retains the original empirical quartiles. The violin plot retains the original linearly interpolated quartiles.

**Figure 2 reporting note:** the uploaded code and reported p-values use **two-sided Mann–Whitney tests with Holm correction across four sentences** (VP: 0.002; MP: 0.004 after rounding). Notebook 02 preserves this implementation. The submitted Methods wording “one-sided” is inconsistent with those results and should be clarified; the repository does not silently change the analysis to match that wording.

## Reproducibility scope

Figures are exported as PNG and PDF; tables and underlying numerical results are exported as CSV. Plot layout and fonts may differ from the final assembled publication figures.

The public transcription data support the four notebooks above. **Table 1 requires restricted demographic/clinical data. Supplementary Table S1 requires the separate repeated-transcription input files, which are not included here.** Figure 1 is a recruitment diagram, Supplementary Figure S1 is an assessment instrument, and Supplementary Table S2 is a formatted transcription excerpt; these are not generated by the four analysis notebooks. The public CSV supplies the underlying transcriptions for Table S2, without its cell highlighting.

Original speech recordings and clinical information are not distributed in this repository. Access requests should be directed to the corresponding author or the Chulalongkorn Cognitive Clinical & Computational Neuroscience Center, subject to the study's privacy and institutional requirements.

## Verification

The cleaned scoring was checked against the original scoring code for every participant and sentence. All four notebooks were executed, including all 50 final model fits, using Python 3.12.14 and the pinned numerical packages. The checks reproduced the primary AUCs, combined AUC median/IQR, representative split 29 (seed 70), its threshold and counts, Bayesian summaries, and reported coefficient medians/IQRs.

Two split-level tuning selections (33 and 50) differed from the stored outputs of the original Python 3.13.2 notebook in this execution environment. Running the original fitting code here produced the same selections as the cleaned code. All 50 combined test AUCs and the manuscript-reported coefficient medians/IQRs were preserved, but exact coefficient means and individual fitted probabilities are not identical. No C values or predictions are hard-coded to conceal this difference.

The nested-validation code was also executed for all 100 repetitions of the first training subset. The full 50 × 100 procedure remains the default, but all 5,000 repetitions were not rerun during this cleanup. A `--skip-nested` run is not a complete rerun of that procedure.
