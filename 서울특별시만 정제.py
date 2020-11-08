import pandas as pd
df = pd.read_csv("delivery.csv")
A= df[df['DLVR_DSTN_SIDO']=='서울특별시']
A.to_csv('newdelivery.csv', index=False, encoding='cp949')
print(A)