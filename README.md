# lexas
LEXAS: Lifescience EXperiments seArch and Suggestion

## Introduction

## Google drive data repository

## Contents

### 0. Downloading required data

1. Downlods all files in <<google drive>>

### 1. Extracting the result sections

1. Run "1.result-extract.py"

### 2. Sentence segmentation

1. Run "2.sentence_segmentation.py"

### 3. Extracting the sentences descibing gene-related experiments

1. Run "3.Sentence-extraction.py"

### 4. Relation extraction between gene names and experimental methods

1. Run "4.Relation-extraction.py"

### 5. Change the style for training a model

1. Run "5..py"

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
