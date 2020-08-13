# library
import matplotlib.pyplot as plt
import pandas as pd
from rake_nltk import Rake
from tika import parser
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def document_to_text(document_path):
    # document = request.FILES['document']
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
    job_descriptions = pd.read_csv('data/job_descriptions.csv', index_col=0)
    """Use this variable for production?"""
    # resume = request.FILES['document']
    """Use this variable for development"""
#     document_path = (r"C:\Users\sambe\Projects\Cover_Letter_Analysis\data\documents\ResumeBrittanyMouzoon.pdf")
#     text = document_to_text(document_path)
    data = [['resume', text]]
#     print(data)
    basic_documentdf = pd.DataFrame(data, columns = ['title', 'description'])
    return basic_documentdf

def text_to_bagofwords(basic_documentdf):
    document_path = (r"C:\Users\sambe\Projects\Cover_Letter_Analysis\data\documents\ResumeBrittanyMouzoon.pdf")
#     text = document_to_text(document_path)
#     basic_documentdf = compile_document_text(text)
    basic_documentdf['rake_key_words'] = ''
    r = Rake()
    for index, row in basic_documentdf.iterrows():
        r.extract_keywords_from_text(row['description'])
        key_words_dict_scores = r.get_word_degrees()
        row['rake_key_words'] = list(key_words_dict_scores.keys())
    # Transform key words into bag of words
    basic_documentdf['bag_of_words'] = ''
    for index, row in basic_documentdf.iterrows():
        words = ''
        words += ' '.join(row['rake_key_words']) + ' '
        row['bag_of_words'] = words
    verbose_documentdf = basic_documentdf
    return verbose_documentdf

def join_and_condense(verbose_documentdf):
    # Slices
    job_descriptions = pd.read_csv('data/job_descriptions.csv', index_col=0)
    job_descriptions = job_descriptions.append(verbose_documentdf)
    recommend_df = job_descriptions[['title', 'bag_of_words']]
    return recommend_df

def vectorize_text(recommend_df):
    count = CountVectorizer()
#     recommend_df = join_and_condense()
    count_matrix = count.fit_transform(recommend_df['bag_of_words'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    return cosine_sim

def recommend_100(title, cosine_sim):
    document_path = (r"C:\Users\sambe\Projects\Cover_Letter_Analysis\data\documents\ResumeBrittanyMouzoon.pdf")
    text = document_to_text(document_path)
    basic_documentdf = compile_document_text(text)
    verbose_documentdf = text_to_bagofwords(basic_documentdf)
    recommend_df = join_and_condense(verbose_documentdf)
    cosine_sim = vectorize_text(recommend_df)
    recommended_jobs = []
    indices = pd.Series(recommend_df['title'])
    idx = indices[indices == title].index[0]
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)
    top_10_indices = list(score_series.iloc[1:101].index)

    for i in top_10_indices:
        recommended_jobs.append(list(recommend_df['title'])[i])

    return recommended_jobs

def format_recommendations(recommended_jobs):
#     jobs100 = recommend_100('resume')
    jobs10 = []
    for job in recommended_jobs:
        job = job.lower().replace("_", " ").title()
        job = job.replace('Hr Manager', 'HR Manager')
        jobs10.append(job)
    jobs10 = set(jobs10[0:20])
    jobs10 = list(jobs10)
    final_jobs10 = jobs10[0:10]

    for i, item in enumerate(final_jobs10,1):
        print(i, '. ' + item + '\n', sep='',end='')

def top_100_categories(recommended_jobs):
    df = pd.read_csv('data/job_descriptions.csv', index_col=0)
#     jobs100 = recommend_100('resume')
    user_titles = df[df.title.isin(recommended_jobs)]
    user_titles = user_titles[['title', 'category']]
    user_titles.drop_duplicates(subset="title", keep="last")
    category_list = list(user_titles.category)
    return category_list

def freq(category_list):
    frequency = []
    document_path = (r"C:\Users\sambe\Projects\Cover_Letter_Analysis\data\documents\ResumeBrittanyMouzoon.pdf")
    text = document_to_text(document_path)
    basic_documentdf = compile_document_text(text)
    verbose_documentdf = text_to_bagofwords(basic_documentdf)
    recommend_df = join_and_condense(verbose_documentdf)
    cosine = vectorize_text(recommend_df)
    title = 'resume'
    recommended_jobs = recommend_100(title, cosine)
    categories = top_100_categories(recommended_jobs)
    # gives set of unique words
    unique_words = set(categories)
    for words in unique_words :
        frequency.append(category_list.count(words))
    return frequency

def viz_data(category_list, frequency):
#     categories = top_100_categories()
#     frequency = freq(categories)
    unique_words = set(category_list)
    unique_words = list(unique_words)
    category_values = dict(zip(unique_words, frequency))
    category_dict = {key:val for key, val in category_values.items() if val >= 10}
    # create data
    names=category_dict.keys()
    size=category_dict.values()
    return names, size

def make_viz(names, size):
#     categories = top_100_categories()
#     freq(categories)
#     names, size = viz_data()
# Create a circle for the center of the plot
    my_circle=plt.Circle( (0,0), 0.7, color='white')
# Give color names
    plt.title('Strength Summary')
    plt.pie(size, labels=names)
    p=plt.gcf()
    p.gca().add_artist(my_circle)
    plt.show()

def analyze(document_path):
    document_path = (r"C:\Users\sambe\Projects\Cover_Letter_Analysis\data\documents\ResumeBrittanyMouzoon.pdf")
    text = document_to_text(document_path)
#     print("Extracting text from document...")
    basic_documentdf = compile_document_text(text)
#     print("Creating dataframe...")
    verbose_documentdf = text_to_bagofwords(basic_documentdf)
#     print("Extracting key words from text...")
    recommend_df = join_and_condense(verbose_documentdf)
#     print("Compiling data...")
    cosine_sim = vectorize_text(recommend_df)
#     print("Calculating similarities...")
    recommended_jobs = recommend_100('resume', cosine_sim)
#     print("Retrieving top recommendations...")
    top10 = format_recommendations(recommended_jobs)
#     print("Formatting top recommendations...")
    category_list = top_100_categories(recommended_jobs)
#     print("Retrieving relevant job categories...")
    frequency = freq(category_list)
#     print("Calculating the most common job categories...")
    names, size = viz_data(category_list, frequency)
#     print("Compiling data...")
    strength_summary = make_viz(names, size)
