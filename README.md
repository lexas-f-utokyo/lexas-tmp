# lexas
LEXAS: Lifescience EXperiment seArch and Suggestion

## Introduction

LEXAS helps researchers to efficiently design biological experiments.

LEXAS curates the description of biomedical experiments (Search) and suggests genes
to be analyzed and a specific experimental method for the next experiment (Suggestion). 

## Google drive data repository

## Installation

1. Clone.

$ git clone ????

2. Download pretrained model from google ////

Folder like this.

3. Acquire required module

sci-spacy, pandas, numpy, ??, ??
pip install ?


## Search

This section describes how you can obtain information about gene-relaed biological experiments from PMC articles

### 0. Downloading PMC articles

We prepare seven articles as sample. If you want to run on your interest article, please do the below.

1. Download PMC articles of interest from PMC FTP service and put it in the articles directory.
2. Generate a list of the PMCID in PMCID_list.txt, one ID per one line.


### 1. Extracting the result sections

1. Run "1.result-extract.py" to extract only the result section except figure legends.
2. The output file is preserved in data/

### 2. Sentence segmentation

1. Run "2.sentence_segmentation.py" to perform sentence segmentation with sci-spacy
2. The output file is preserved in data/

### 3. Extracting the sentences descibing gene-related experiments

With experimental list and genelist from HGNC, you can retrieve sentences that include at least one gene and one method.

1. Run "3.Sentence-extraction.py"
2. The output file

### 4. Relation extraction between gene names and experimental methods

Using pre-trained model based on bio-BERT, do relation extraction.

1. Edit the "4.Relation-extraction.ipynb" to select if you use "cpu" or "cuda".
2. Run "4.Relation-extraction.ipynb" to relation extraction between gene name and experimental method.


## Suggestion

### 5. Change the style for training a model

1. Run "5.py" to number the experiment.

### 6. Collect gene feature

To generate feature vector, we have to prepair two dictionary.
One is the key, another is the number.

1. Run "6.feature.py"

### 7. Training a suggestion model

1. Run "6. py"

### 8. Suggesting the gene in the next experiment

1.result-extract.py #XML  
2.Parsing.py #scispacy  
3.chikan.py #ahocorapy  
4.relation_extraction.py  #biobert  
5.feature.py  
6.XGboost.py  
7.app.py #flask & template htmls  
