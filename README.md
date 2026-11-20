# Spastic dysarthria: ASR syllable-error analysis

Analysis code for **Automatic Speech Recognition and Phonetics-Informed Sentence Design for Spastic Dysarthria and Corticobulbar Lesion Detection**.

The study includes 37 patients and 37 controls. Four Thai sentences target labial (LBP), lingual-alveolar/palatal (LAP), velopharyngeal (VP), and mixed (MP) consonant groups. Apple Siri transcriptions are converted to syllable-error scores and evaluated by ROC analysis. Combined logistic regression is a secondary analysis.

## Notebooks

Run the notebooks in numerical order from the repository folder. Tables and figures are saved in `results/` as CSV, PNG, and PDF files.

| Notebook | Outputs |
| --- | --- |
| [01 — Syllable-error scoring](01_Syllable_error_scoring.ipynb) | Raw and normalized scores |
| [02 — Score comparisons](02_Score_comparisons.ipynb) | Figure 2; Supplementary Table S3 |
| [03 — Individual and pooled ROC analysis](03_Individual_and_pooled_ROC.ipynb) | Figure 3; Table 2 |
| [04 — Combined logistic regression](04_Combined_logistic_model.ipynb) | Figure 4; Supplementary Figure S2; Supplementary Tables S4–S5 |

## Run

Use Python 3.12 or 3.13:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python run_analysis.py
```

On Windows, activate with `.venv\Scripts\activate`. For interactive use, install JupyterLab in the same environment with `python -m pip install jupyterlab`.

The complete run includes 100 repetitions of nested five-fold validation within each of 50 training subsets. To generate the figures and tables, including all 50 final model fits, without repeating this separate validation calculation:

```bash
python run_analysis.py --skip-nested
```

In notebook 04, `RUN_NESTED_CV` controls the same option and defaults to `True`.

## Data and scoring

[syllableseparation_apple_corrected.csv](syllableseparation_apple_corrected.csv) contains aligned ASR transcriptions for all 74 participants. Notebook 01 generates `Syllableerror_scores_raw_and_normalized.csv` locally.

`sub_id` identifies participants; `disease` is 1 for patients and 0 for controls. Columns beginning with `s` contain aligned target syllables; columns beginning with `e` contain additional-syllable slots. Preserve the supplied zero placeholders.

| Sentence | Raw score | Normalized score | Target syllables |
| --- | --- | --- | --- |
| LBP | `error_1` | `error_rate_1` | 8 |
| LAP | `error_2` | `error_rate_2` | 8 |
| VP | `error_3` | `error_rate_3` | 7 |
| MP | `error_4` | `error_rate_4` | 11 |

Each unaccepted or absent target syllable counts as one error. Each additional-syllable slot counts as one error unless its value is `0`. Accepted transcriptions are defined in notebook 01. The code begins with segmented, aligned transcriptions and does not perform ASR or alignment.

Normalized scores equal raw errors divided by target syllable count. Additional errors are included, so scores are not clipped at 1. The pooled score is the sum of raw errors across all four sentences divided by 34.

## Statistical methods

- Score comparisons: two-sided Mann–Whitney tests with Holm correction across four sentences; Shapiro–Wilk normality tests within each group.
- ROC analysis: DeLong confidence intervals and paired AUC comparisons, with Holm correction across 10 pairs. Youden ties select the highest finite threshold. Full-cohort threshold metrics describe apparent performance.
- Combined model: training-only standardization, L2 logistic regression, 50 stratified 70:30 splits (seeds 42–91), and 17 C values from 10⁻⁴ to 10⁴. Final five-fold tuning is separate from repeated nested validation. Thresholds are derived from the full training subset.
- Representative model: test AUC closest to the median, selecting the earliest split in a tie. Five model-versus-score comparisons use Holm correction. Estimates and intervals are conditional on the selected split.
- Bayesian intervals: independent Jeffreys Beta(0.5, 0.5) priors and 200,000 draws (seed 42).
- Coefficients: descriptive summaries across overlapping splits, on standardized and per-0.10 error-rate scales. These summaries do not test coefficient differences.
- AUC quartiles: empirical quartiles for the numerical combined-model summary and linear interpolation for the violin plot.

## Scope and reproducibility

The notebooks generate the outputs listed above. Table 1 requires restricted clinical data, and Supplementary Table S1 requires separate repeat-transcription inputs. Figure 1, Supplementary Figure S1, and the formatted transcription excerpt in Supplementary Table S2 are not generated here. The public CSV provides the transcriptions underlying Table S2.

Speech recordings and clinical information are not included. Access requests should be directed to the corresponding author or the Chulalongkorn Cognitive Clinical & Computational Neuroscience Center, subject to institutional privacy requirements.

Execution checks covered all 50 final models and 100 nested-validation repetitions for the first training subset. The complete 5,000-repetition validation is available but was not included in that check.

All 50 test AUCs and reported coefficient medians and quartiles were reproduced. In Python 3.12.14, selected C values for splits 33 and 50 differed from saved Python 3.13.2 results; individual coefficients, their means, and fitted probabilities can therefore vary across environments. Use the pinned package versions for reproducibility.
