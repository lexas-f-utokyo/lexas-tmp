# LEXAS: Lifescience EXperiment seArch and Suggestion

## Introduction

This repository contains the source code used to develop the LEXAS system (https://lexas.f.u-tokyo.ac.jp).

LEXAS curates the description of biomedical experiments and suggests genes
to be analyzed and a specific experimental method for the next experiment.



## Installation

1. Clone the source code.

```
git clone https://github.com/lexas-f-utokyo/lexas-tmp.git
```

2. Download required data from [google drive repository]() and unzip the tar.gz files.

```
wget 
tar -zxvf 
```

3. Before running scripts, prepair directories as follows.



## Dependencies
- ahocorapy>=1.6.1
- en_core_sci_sm>=0.4.0
- numpy>=1.19.5
- pandas>=1.1.5
- scipy>=1.5.4
- scispacy>=0.4.0
- shap>=0.39.0
- torch>=1.9.1
- tqdm>=4.61.1
- transformers>=4.3.3
- xgboost>=1.4.2

## Search

This section describes how you can obtain information about gene-relaed biological experiments from PMC articles

### 0. Downloading PMC articles

We have already prepare seven sample articles. If you want to run on your interest article, please follow the below step.

1. Download PMC articles of interest from PMC FTP service and put it in the articles directory.
2. Generate a list of the PMCID in PMCID_list.txt, one ID per one line.

### 1. Extracting the result sections

1. Run "1.result-extract.py" to extract only the result section except figure legends.
2. The output file is preserved in data/

### 2. Sentence segmentation

1. Run "2.sentence_segmentation.py" to perform sentence segmentation with sci-spacy.
2. The output file is preserved in data/

### 3. Extracting the sentences descibing gene-related experiments

With manually compiled experimental list and human gene term list provided by HGNC, you can retrieve
 sentences that include at least one gene and one method.

1. Run "3.Sentence-extraction.py"
2. The output file is preserved in data/

### 4. Relation extraction between gene names and experimental methods

Using pre-trained model based on bio-BERT, do relation extraction.

1. Edit the "4.Relation-extraction.ipynb" to select if you use "cpu" or "cuda".
2. Run "4.Relation-extraction.ipynb" to extract target-manipulation relations between gene names and experimental methods in one sentence.


## Suggestion

We have already prepared two pre-trained models, one use all features and the other use only databases.
You can start from step 8.


### 5. Change the style for training a model

1. Run "5.py" to number the experiment for training.

### 6. Collect gene feature

To generate feature vectors, you have to prepair two dictionary.
One is the key, another is the number.

We prepare two sets of feature dictionary and number dictionary.
Alldic, allnum is for all features, and datdic, datnum are for or only databases.

If you want to use your own feature, run the following step.

1. Run "6.feature.py" to generate feature dictionary.

### 7. Training a suggestion model

1. Run "7. XGBoost_train.ipynb"

### 8. Suggesting the gene in the next experiment

1. Run "7. XGBoost_suggestion.ipynb"


## License

This source code may be used for non-commercial purpose including. 

- Research by academic institutions

- Non-commercial research, including research conducted within commercial organizations

- Personal use, including blog posts.

If you want to use the source code for a commercial purpose, please contact the following email addresses.

Miho Sakao : sakao [at_mark] todaitlo.jp



## Acknowledgement

LEXAS relies on many information sources:

[PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/)
[HGNC](https://www.genenames.org/)
[GO](http://geneontology.org/)
[MGI](http://www.informatics.jax.org/)
[HPO](https://hpo.jax.org/app/)
[OMIM](https://www.omim.org/)
[Orphanet](https://www.orpha.net/)
[HPA](https://www.proteinatlas.org/)
[BioGRID](https://thebiogrid.org/)
[DepMap](https://depmap.org/)
[ENCODE](https://www.encodeproject.org/)

We gratefully acknowledge these resources.
