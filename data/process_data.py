
import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """
    Load messages and categories datasets.

    Args:
    messages_filepath (str): Filepath to messages dataset.
    categories_filepath (str): Filepath to categories dataset.

    Returns:
    df (DataFrame): Merged DataFrame of messages and categories.
    """

    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    
    df = pd.merge(messages, categories)
    
    return df


def clean_data(df):
    """
    Clean DataFrame by splitting categories, converting category values to numbers,
    replacing categories column with new category columns, removing duplicates,
    and saving the clean dataset into an SQLite database.

    Args:
    df (DataFrame): Merged DataFrame of messages and categories.

    Returns:
    None
    """
    categories = df['categories'].str.split(';', expand=True)
    
    row = categories.iloc[0]
    category_colnames = row.apply(lambda x: x[:-2])
    
    categories.columns = category_colnames
    
    for column in categories:
        categories[column] = categories[column].str[-1]
        categories[column] = categories[column].astype(int)
        
    categories['related'] = categories['related'].replace(2, 1) 
    df.drop('categories', axis=1, inplace=True)
    df = pd.concat([df, categories], axis=1)
    
    df.drop_duplicates(inplace=True)

    engine = create_engine('sqlite:///DisasterResponsePipeline.db')
    df.to_sql('DisasterResponseTabel', engine, index=False, if_exists='replace')

    
def main(messages_filepath, categories_filepath):
    """
    Main function to run ETL pipeline.

    Args:
    messages_filepath (str): Filepath to messages dataset.
    categories_filepath (str): Filepath to categories dataset.

    Returns:
    None
    """

    print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'.format(messages_filepath, categories_filepath))
    df = load_data(messages_filepath, categories_filepath)

    print('Cleaning data...')
    clean_data(df)
    
    print('Data cleaned and saved to database!')


if __name__ == '__main__':
    if len(sys.argv) == 3:
        messages_filepath, categories_filepath = sys.argv[1], sys.argv[2]
        main(messages_filepath, categories_filepath)
    else:
        print("Please provide the file paths of the messages dataset and categories dataset.")
