import pandas as pd
import numpy as np
città=["milano","lecce","taranto","palermo","roma","torino","verona","bari","pescara","bologna"]
prodotti=["telefono","mouse","tablet","computer","televisione","tastiera"]

df=pd.DataFrame({
    "città":np.random.choice(città,size=10),
    "prodotti":np.random.choice(prodotti,size=10),
    "data": np.random.choice(['2023-01-31', '2023-12-30', '2022-05-10', '2023-07-18', '2023-02-04','2022-12-31'],10),
    "vendite":np.random.randint(10,100,10)
})

print(df)

df_medie= df.pivot_table(values="vendite", index="prodotti", columns="città", aggfunc='mean')
df_group=df.groupby("prodotti").sum()

print(df_medie)
print(df_group)