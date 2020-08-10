from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
# from django.views.generic import TemplateView

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# recommendation packages
from .text_processing import document_to_text, compile_document_text, text_to_bagofwords, join_and_condense, vectorize_text, recommend_100, format_recommendations, top_100_categories, freq, viz_data, make_viz
# from io import BytesIO
# import base64
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from rake_nltk import Rake
from tika import parser
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer



# Create your views here.
def index(request):
    """Rookieplay's Job Matchmaking"""
    return render(request, 'rookieplays/upload.html')

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

        # document_to_text(uploaded_file)
        # text_to_bagofwords(document_df)
        # document_df = compile_document_text()
        # title = 'resume'
        # cosine_sim = vectorize_text()
        # recommend_100(title, cosine_sim)
        # categories = top_100_categories()
        # freq(categories)
        # viz_data()
        # top10_recs = format_recommendations()
        # strength_summary = make_viz()
    return render(request, 'rookieplays/upload.html', context)

def analyze(request):
    uploaded_file = request.FILES['document']
    document_to_text(uploaded_file)
    text_to_bagofwords(document_df)
    document_df = compile_document_text()
    title = 'resume'
    cosine_sim = vectorize_text()
    recommend_100(title, cosine_sim)
    categories = top_100_categories()
    freq(categories)
    viz_data()
    top10_recs = format_recommendation()
    strength_summary = make_viz()
    context = {'Top 10 Job Title Recommendations': top10_recs, 'Strength Summary': strength_summary}
    return render(request, 'rookieplays/upload.html', context)

@login_required
def topics(request):
    """Show a single topic and all its entries."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'rookieplays/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'rookieplays/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('rookieplays:topics'))

    context = {'form': form}
    return render(request, 'rookieplays/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()

    else:
        # POST data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('rookieplays:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'rookieplays/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('rookieplays:topic', args=[topic.id]))

    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'rookieplays/edit_entry.html', context)
