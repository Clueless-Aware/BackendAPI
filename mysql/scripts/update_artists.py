import pandas as pd


def remove_parenthesis(born_died):
    born_died = born_died.rstrip().lstrip()
    # print(born_died[0], born_died[-1])
    if (born_died[0] != '(' or born_died[-1] != ')'):
        print(f"Record {born_died} dosen't match the pattern")
        return born_died

    born_died = born_died[1:]
    born_died = born_died[:-1]

    born_died = born_died.replace('b.', 'Born')
    born_died = born_died.replace('d.', 'Died')

    return born_died


def load():
    return pd.read_csv('../data/bio_catalog.csv')


def save(df):
    df.to_csv('new_artists.csv', header=True, index=False)


def main():
    df = load()

    df['BIRTH DATA'] = df['BIRTH DATA'].apply(remove_parenthesis)

    print(df['BIRTH DATA'].to_string())

    save(df)


if __name__ == "__main__":
    main()
