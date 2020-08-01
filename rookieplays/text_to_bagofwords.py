import pandas as pd
from rake_nltk import Rake

def job_descriptions_download():
# Upload and consolidate new job descriptions
    new_jobsdf = pd.read_csv('data/new_job_descriptions.csv')
    new_jobsdf = new_jobsdf.dropna()

# Extract key words and phrases with RAKE. Pass the dataframe and the uncleaned text column to be bagged.
def text_to_bagofwords(df, column_name):
    df['rake_key_words'] = ''
    r = Rake()
    for index, row in df.iterrows():
        r.extract_keywords_from_text(row[column_name])
        key_words_dict_scores = r.get_word_degrees()
        row['rake_key_words'] = list(key_words_dict_scores.keys())

# Transform key words into bag of words
    df['bag_of_words'] = ''
    for index, row in df.iterrows():
        words = ''
        words += ' '.join(row['rake_key_words']) + ' '
        row['bag_of_words'] = words

def compile_job_descriptions():
# Combine new jobs dataframe with main job description dataframe
    job_descriptions = pd.read_csv('data/job_descriptions.csv', index_col=0)
    job_descriptions = job_descriptions.append(new_jobsdf, ignore_index=True)
    job_descriptions.to_csv('data/job_descriptions.csv')
