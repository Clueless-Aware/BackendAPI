import pandas as pd

df = pd.read_csv('artwork_source.csv')
sample = df.head(500)

sample['jpg url'] = sample['ID'].apply(lambda id: f'images/artworks/{id}.jpg')

print(sample)

sample.to_csv('./artwork.csv', index=False, )
