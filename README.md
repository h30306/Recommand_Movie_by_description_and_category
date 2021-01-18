# Recommand_Movie_by_description_and_category
Recommend favorite movies based on user input description and favorite movie category

### Author

[Howard W. Chung](https://github.com/h30306)

## Introduction

This Library implements Movie Recommandation website, by using sentence embedding model BERT & text feature extraction method TF-IDF, to select the movies that users might be interested in. We build this system with two flask model for Predict Vector ModelEnd and Website WebEnd.

## Requirement

- python>=3
- flask>=1.0
- numpy>=1.15
- pandas=0.24.2
- bert-serving-client=1.10.0
- requests=2.21
- json=0.9.2
- pickle=0.7.5
- os

## Start Up

Start Flask of Model End<br>
1. Setup output port in line 20 in RecommandMovie.py<br>
2. Start ModelEnd Flask<br>
```
$ python3 RecommandMovie.py
```
Deploy BERT Serving client<br>
3. [Download BERT base model](https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-12_H-768_A-12.zip)<br>
4. Start BERT Serving client<br>
```
$ PTHNAME="./uncased_L-12_H-768_A-12" #Path of Model
$ bert-serving-start -model_dir ${PTHNAME} -num_worker=1
```
Start Flask of Website End<br>
5. Setup ModelEnd IP and port in line 71 in app.py<br>
6. Start WebEnd Flask<br>
```
$ python3 app.py
```
