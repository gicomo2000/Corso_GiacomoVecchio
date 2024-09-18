import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


numeri = np.random.randint(0, 30, 30)
giorni=np.arange(1,31)
df = pd.DataFrame({"Giorni":giorni,"temperatura":numeri})
print(df)
print(df["temperatura"].describe()) #mediana è il 50%



x = df["temperatura"]
y = df["Giorni"]

#grafico a linee
plt.figure()
plt.plot(y, x)
plt.title('Grafico a Linee')
plt.xlabel('Giorni del mese')
plt.ylabel('Temperatura')
plt.show()

categories = x
values = y

#grafico a barre
plt.figure()
plt.bar(values,categories)
plt.title('Grafico a Barre')
plt.xlabel('Giorni del mese')
plt.ylabel('Temperature')
plt.show()

#scatterplot
plt.figure()
plt.scatter(y, x)
plt.title('Scatter Plot')
plt.xlabel('Giorni del mese')
plt.ylabel('Temperature')
plt.show()

