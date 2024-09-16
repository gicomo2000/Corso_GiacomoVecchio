import numpy as np
import pandas as pd
giorni = 365
media_visitatori = 2000
deviazione_standard = 500
trend_crescente = np.linspace(0, 1000, giorni).astype(int)  

visitatori = media_visitatori + np.random.randint(-deviazione_standard, deviazione_standard + 1, giorni) + trend_crescente

intervallo_date = pd.date_range(start='2023-01-01', periods=giorni, freq='D')

df_visitatori = pd.DataFrame({'Data': intervallo_date, 'Visitatori': visitatori})
df_visitatori.set_index('Data', inplace=True)

media_mensile = df_visitatori.resample('ME').mean().astype(int)  
dev_std_mensile = df_visitatori.resample('ME').std().astype(int)  


print("Numero medio di visitatori per mese:")
print(media_mensile)

print("\nDeviazione standard dei visitatori per mese:")
print(dev_std_mensile)
