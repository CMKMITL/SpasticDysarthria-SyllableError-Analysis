# SpasticDysarthria-SyllableError-Analysis

Python notebooks and syllable-segmented automatic speech recognition (ASR) transcriptions for a study of Thai spastic dysarthria involving 37 patients and 37 healthy controls. The revised scoring workflow uses Apple Siri transcriptions to generate raw and syllable-normalized error scores. These are transcription-based features, not direct acoustic measurements or expert perceptual ratings of articulation.

## Current scoring notebook and dataset

- [Syllableerror_scoring.ipynb](Syllableerror_scoring.ipynb): updated from `01_Syllableerror_scoring_normalized.ipynb`; computes four raw error counts and four normalized scores.
- [syllableseparation_apple_corrected.csv](syllableseparation_apple_corrected.csv): syllable-level transcription dataset for all 74 participants.
- Output: `Syllableerror_scores_raw_and_normalized.csv`, containing participant ID, disease label, `error_1`–`error_4`, and `error_rate_1`–`error_rate_4`. Disease is coded 1 for patients and 0 for controls.

## Scoring procedure

Transcripts must already be segmented and aligned to target syllables before running the notebook. The notebook does not perform ASR, segmentation, or alignment.

For each target position, the code checks exact membership in a predefined list of accepted transcriptions. An accepted entry contributes zero errors; an unaccepted or absent target syllable contributes one error. Each additional-syllable slot contributes one error when its value is not the string `0`. A total of zero indicates no counted errors.

The accepted lists in Step 2 are the operational scoring criteria. They include selected alternative transcriptions and should not all be interpreted as strictly identical pronunciations. The code does not independently evaluate phonetic similarity, consonant accuracy, or the audio signal.

| Sentence | Feature number | Target syllables | Normalized score |
| --- | --- | --- | --- |
| LBP | 1 | 8 | raw error count / 8 |
| LAP | 2 | 8 | raw error count / 8 |
| VP | 3 | 7 | raw error count / 7 |
| MP | 4 | 11 | raw error count / 11 |

Scores express errors per target syllable. Additional-syllable errors are included, so normalized scores are not mathematically restricted to 0–1.

The pooled sentence score used in the revised downstream analysis is the sum of the four raw error counts divided by 34. This scoring notebook exports the four individual scores; it does not calculate the pooled score or ROC analyses.

## Run in Google Colab

1. Open [the scoring notebook in Colab](https://colab.research.google.com/github/CMKMITL/SpasticDysarthria-SyllableError-Analysis/blob/main/Syllableerror_scoring.ipynb).
2. Download the CSV linked above.
3. Run Step 1 and select that CSV when the upload prompt appears.
4. Run the remaining cells in order. The final scoring cell downloads `Syllableerror_scores_raw_and_normalized.csv`.

The notebook uses Python, pandas, SciPy, and Google Colab's file upload/download utilities. For local Jupyter use, replace the Colab upload with `pd.read_csv("syllableseparation_apple_corrected.csv")` and omit the Colab download call; `to_csv` already saves the output.

### Input layout

Keep the supplied CSV column order unchanged: the first two columns contain participant ID and disease label, followed by sentence blocks selected by column positions `2:11`, `11:20`, `20:29`, and `29:45`. Columns beginning with `s` contain aligned target-syllable transcriptions; those beginning with `e` contain additional-syllable slots. Preserve the supplied zero placeholders. Blank additional-syllable slots are not treated as zero by this implementation.

## Earlier analysis notebooks

The following notebooks are retained from the earlier analysis and have not been updated as part of this scoring revision:

- `LogisticRegressionModel_train-test_randomstatevariation.ipynb`
- `PermutationTest_logisticregressionmodel.ipynb`

They should not be used as the implementation of the revised individual/pooled ROC analysis or the revised 50-split combined model. Updated downstream analysis notebooks will be documented separately when uploaded.

## Data availability and citation

The complete syllable-segmented transcription CSV is available in this repository. It is a text dataset and does not contain the source audio. CSV files do not preserve the pink error highlighting shown in Supplementary Table S1.

Publication citation details will be added when available.

## License

The earlier README stated Apache 2.0 licensing, but this repository currently contains no LICENSE file. Please contact the repository maintainers for licensing clarification.
