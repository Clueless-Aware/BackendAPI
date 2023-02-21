import pandas as pd

df = pd.read_csv('artwork.csv')
sample = df.head(50)

sample['jpg url'] = sample['ID'].apply(lambda id: f'images/artworks/{id}.jpg')

print(sample)

sample.to_csv(index=False)
