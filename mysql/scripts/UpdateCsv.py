import pandas as pd

HEAD_SIZE = 500

df = pd.read_csv('../data/artwork_source.csv', nrows=HEAD_SIZE)

df['jpg url'] = df['ID'].apply(
    lambda image_id: f'images/artworks/{image_id}.jpg')

df[['date', 'type', 'size', 'museum']
   ] = df['picture_data'].str.split(', ', expand=True, n=3)

df[['resolution', 'color', 'file_dimension']
   ] = df['file_info'].str.split(', ', expand=True, n=2)

df.drop(['picture_data', 'file_info'], axis=1, inplace=True)

# TODO
# .apply(lambda x: x.str.strip())

# print(df.to_string())

df.to_csv('./artwork.csv', index=False)

print(f'Successfully created a csv file with {HEAD_SIZE} elements')
