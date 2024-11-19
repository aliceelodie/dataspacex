import pandas as pd
data = {
    'rocket' : [
        'Falcon 1',
        'Falcon 9',
        'Falcon Heavy',
    ],
    'launches': [5, 100, 3 ],
}
df = pd.DataFrame(data)
print(df)
print('nnnnnnnnnnnnnnnnnnn')
print(df['rocket'])
falcon9_df = df[df['rocket'] == 'Falcon 9']
print('nnnnnnnnnnnnnnnnnnnnnn')
print( falcon9_df)
launches5_df = df[df['launches'] == 5]
print ('nnnnnnnnnnnnnnnnnnnnnnnnn')
print (launches5_df)
df [ 'success_rate'] = [0.4, 0.98, 1.0]
print ('nnnnnnnnnnnnnnnnnnnnnnnnn')
print (df)