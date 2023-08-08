import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
from collections import Counter
df = pd.read_csv('Cleaned_Combined_data.csv')

df['Order Date'] = pd.to_datetime(df['Order Date'])

#what was the best month for the sales?how much was earned that month.
df['sales']= df['Price Each']*df['Quantity Ordered']
df['month']= df['Order Date'].dt.month_name()
gdf =df.groupby('month')['sales'].sum().reset_index()


#2.what city sold the most product.
df['city']=df['Purchase Address'].str.split(',',expand=True)[1]
gdf= df.groupby('city')['sales'].sum().reset_index()
# sns.catplot(x='city', y='sales', data=gdf, kind='bar')
# plt.show()

# what time should we display advertisement to maximize the likelihod of customers buying product.
# hour
df['hour']= df['Order Date'].dt.hour
gdf =df.groupby('hour')['Quantity Ordered'].sum().reset_index()
# plt.plot(gdf['hour'],gdf['Quantity Ordered'])
# plt.show()
#
# what products are most often sold together.
df= df.loc[df['Order ID'].duplicated(keep=False)]
df['grouped']= df.groupby('Order ID')['Product'].transform(lambda X:','.join(X))
count= Counter()
row_list = []
for row in df['grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list,3)))
print(count.most_common(10))



