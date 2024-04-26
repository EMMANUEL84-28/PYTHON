import pandas as pd
df1 = pd.read_csv('Bikes.csv')
df2 = pd.read_csv('orderlines.csv')
df3 = pd.read_csv('bikeshops.csv')

join_1 = pd.merge(df1, df2, left_on='bike.id', right_on='product.id')
final_join = pd.merge(join_1, df3, left_on='order.line', right_on='bikeshop.id')
print(final_join.head(30)) 

## Using description column divide data in two category 'road' and 'mountan' 
final_join['category'] = final_join['description'].str.split('-').str[0].str.strip()
print(final_join)

## Perform the total revenue 
final_join['revenue'] = final_join['price'] * final_join['quantity']
print(final_join)

##  Extract only Supersix model

final_join = final_join[final_join['model'].str.contains('Supersix')]
print(final_join)

## Extract only Florida state information

final_join = final_join[final_join['location'].str.contains('Miami, FL')]
print(final_join)

## generate quantiles from revenue and perfomr  a new column to conatined a revenue quantiles

quantiles = final_join['revenue'].quantile([0.25, 0.75])
def assign_quantile(revenue):
    if revenue > quantiles[0.75]:
        return 'Hight'
    elif revenue >= quantiles[0.25] and revenue <= quantiles[0.75]:
        return 'Medum'
    else:
        return 'Low'
final_join['revenue quantiles'] = final_join['revenue'].apply(assign_quantile)
print(final_join)    