import wfdb
import pandas as pd

record = wfdb.rdsamp('16272')
df = pd.DataFrame(record[0], columns=record[1]['sig_name'])
df.to_csv('16272.csv', index=False)
