import pandas as pd
import numpy as np
import random

nomi=["giacomo","francesca","cosimo","carlo","antonio","roberta","chiara","angelo","salvatore","alessia"]
città=["milano","lecce","taranto","palermo","roma","torino","verona","bari","pescara","bologna"]

df= pd.DataFrame({
    "nome":np.random.choice(nomi,size=8),
    "città":np.random.choice(città,size=8),
    "salario":np.random.randint(15000,50000,8),
    "eta":np.random.randint(18,80,8)
})

prime5=df.head()
print(prime5)

ultime5=df.tail()
print(ultime5)

tipo_dati=df.info()
print(tipo_dati)

statistiche_descrittive=df.describe()
print(statistiche_descrittive)

duplicati=df.isna()
print(duplicati)
df_senza_duplicati=df.drop_duplicates()
print(df_senza_duplicati)