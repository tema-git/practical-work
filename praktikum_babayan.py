# -*- coding: utf-8 -*-
"""praktikum_babayan.ipynb"

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jkGqXxcaK5-dbFgJCuoKhCckjI4cHocH
"""

import io

path = '/content/qwerty.txt'
with io.open(path, 'r', encoding='windows-1251') as f:
    text = f.read()
text = text.replace('\n','',text.count('\n'))
text = text.replace(',','',text.count(','))
text = text.replace('.','',text.count('.'))
text = text.replace(':','',text.count(':'))
text = text.replace('!','',text.count('!'))
text = text.replace('\xa0','',text.count('\xa0'))

from collections import Counter

text = text.lower()

list_of_words = Counter(text.split(' '))

dict_words = {k: v for k, v in sorted(list_of_words.items(), key=lambda item: item[1], reverse = True)}

import seaborn as sns

import pandas as pd

df_words = pd.DataFrame([dict_words]).transpose()

df_words

df_words.rename(columns = {0:'count'}, inplace = True)

df_words.iloc[:25,:].plot.bar()

len(dict_words)

file1 = open('/content/qwerty.txt', 'r', encoding = 'windows-1251')
Lines = file1.readlines()

len(Lines)

filename = '/content/qwerty.txt'
with io.open(filename,'r',encoding='windows-1251') as f:
    text = f.read()
text = text.replace('\n','',text.count('\n'))
text = text.replace('\xa0','',text.count('\xa0'))

len(text)

text = text.replace(' ','',text.count(' '))

len(text)

