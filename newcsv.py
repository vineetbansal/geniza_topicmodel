import numpy as np
import pandas as pd

df1 = pd.read_csv('geniza-documents-20220714T131650.csv')
print(df1.shape)
print(df1.columns)

df2 = pd.read_csv('geniza-footnotes-20220715T143619.csv')
print(df2.shape)
print(df2.columns)
footnote_document_ids = df2.document_id.unique()
print(len(footnote_document_ids))