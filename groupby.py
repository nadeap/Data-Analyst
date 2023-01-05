df1.groupby('col2').mean() #onekey

df1.groupby([df1['col2'], df1['col3']]).mean() #more than one key

grouped = df1['col1'].groupby(df1['col2']) #not conditions


