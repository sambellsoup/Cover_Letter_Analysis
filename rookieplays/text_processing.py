# library
import matplotlib.pyplot as plt
import pandas as pd
from rake_nltk import Rake
from tika import parser
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pickle


def document_to_text(document_path):
    parsed = parser.from_file(document_path)
    text = parsed['content']
    if parsed['content'] == None:
        print("The submitted document cannot be read.")
    try:
        text = text.replace('\n', '')
    except:
        pass
    return text

def compile_document_text(text):
    # job_descriptions = pd.read_csv('data/job_descriptions.csv', index_col=0)
    with open('rookieplays/pkl/job_descriptions.pkl', 'rb') as f:
        job_descriptions = pickle.load(f)
    data = [['resume', text]]
    basic_documentdf = pd.DataFrame(data, columns = ['title', 'description'])
    return basic_documentdf

def text_to_bagofwords(df):
    df['rake_key_words'] = ''
    r = Rake()
    for index, row in df.iterrows():
        r.extract_keywords_from_text(row['description'])
        key_words_dict_scores = r.get_word_degrees()
        row['rake_key_words'] = list(key_words_dict_scores.keys())
# Transform key words into bag of words
    df['bag_of_words'] = ''
    for index, row in df.iterrows():
        words = ''
        words += ' '.join(row['rake_key_words']) + ' '
        row['bag_of_words'] = words
    verbose_documentdf = df
    return verbose_documentdf

def join_and_condense(df):
    # job_descriptions = pd.read_csv('data/job_descriptions.csv', index_col=0)
    with open('rookieplays/pkl/job_descriptions.pkl', 'rb') as f:
        job_descriptions = pickle.load(f)
    job_descriptions = job_descriptions.append(df)
    recommend_df = job_descriptions[['title', 'bag_of_words']]
    recommend_df = recommend_df.reset_index(drop=True)
    return recommend_df

def vectorize_text(df):
    count = CountVectorizer()
    count_matrix = count.fit_transform(df['bag_of_words'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    return cosine_sim

def recommend_100(df, matrix):
    recommended_jobs = []
    indices = pd.Series(df['title'])
    idx = indices[indices == 'resume'].index[0]
    score_series = pd.Series(matrix[idx]).sort_values(ascending = False)
    top_100_indices = list(score_series.iloc[1:101].index)

    for i in top_100_indices:
        recommended_jobs.append(list(df['title'])[i])

    return recommended_jobs

def format_recommendations(recommendations):
    jobs10 = []
    for job in recommendations:
        job = job.lower().replace("_", " ").title()
        job = job.replace('Hr Manager', 'HR Manager')
        job = job.replace('Care Giver / Hha / Cna', 'Care Giver')
        jobs10.append(job)
    jobs10 = set(jobs10[0:100])
    format_jobs = list(jobs10)
    # final_jobs10 = jobs10[0:3]
    # for i, item in enumerate(final_jobs10, 1):
        # print(i, '. ' + item + '\n', sep='',end='')
    return format_jobs

def top_100_categories(recommendations):
    # df = pd.read_csv('data/job_descriptions.csv', index_col=0)
    with open('rookieplays/pkl/job_descriptions.pkl', 'rb') as f:
        df = pickle.load(f)
    user_titles = df[df.title.isin(recommendations)]
    user_titles = user_titles[['title', 'category']]
    category_list = list(user_titles.category)
    return category_list

def freq(list_of_categories):
    frequency = []
    unique_words = set(list_of_categories)
    for words in unique_words :
        frequency.append(list_of_categories.count(words))
    return frequency

def viz_data(list_of_categories, frequency_of_categories):
    unique_words = set(list_of_categories)
    unique_words = list(unique_words)
    category_values = dict(zip(unique_words, frequency_of_categories))
    category_dict = {key:val for key, val in category_values.items() if val >= 10}
    names=category_dict.keys()
    size=category_dict.values()
    return names, size

def make_viz(names_of_categories, size_of_categories):
# Create a circle for the center of the plot
    my_circle=plt.Circle( (0,0), 0.7, color='white')
# Give color names
    plt.title('Strength Summary')
    plt.pie(size_of_categories, labels=names_of_categories)
    p=plt.gcf()
    p.gca().add_artist(my_circle)
    plt.show()

def analyze(document_path):
    resume_text = document_to_text(document_path)
    basic_documentdf = compile_document_text(resume_text)
    verbose_documentdf = text_to_bagofwords(basic_documentdf)
    recommend_df = join_and_condense(verbose_documentdf)
    cosine_sim = vectorize_text(recommend_df)
    recommended_jobs = recommend_100(recommend_df, cosine_sim)
    final_jobs10 = format_recommendations(recommended_jobs)
    category_list = top_100_categories(recommended_jobs)
    frequency = freq(category_list)
    names, size = viz_data(category_list, frequency)
    strength_summary = make_viz(names, size)

def final_rec(document_path):
    text = document_to_text(document_path)
    basic_documentdf = compile_document_text(text)
    verbose_documentdf = text_to_bagofwords(basic_documentdf)
    recommend_df = join_and_condense(verbose_documentdf)
    cosine_sim = vectorize_text(recommend_df)
    recommended_jobs = recommend_100(document_path, 'resume', cosine_sim)
    recommendations = format_recommendations(recommended_jobs)
    return recommendations
