data.dropna() #drop all NaN
data.dropna(axis=1) #drop kolom

#Fillna
data.fillna({'col1':0, 'col2':2})
data.isnull()
data.isnull().sum()