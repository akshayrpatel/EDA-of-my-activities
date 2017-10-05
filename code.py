import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set()
data= pd.read_csv('eda.csv',nrows=62)
data.set_index(['id', 'date'], append=True)
s = data.pivot("productivity_pulse", "social_networking_percentage","software_development_percentage")
f, ax = plt.subplots(figsize=(9, 6))
%matplotlib inline
sns.heatmap(data, annot=True, linewidths=.5, ax=ax)
plt.show()
#A heat plot that plots everyday productivity. the total time I Spend on Social Networking sites and Software development.

