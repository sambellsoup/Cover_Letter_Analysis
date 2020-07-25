from django.shortcuts import render
from djang.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm

# Create your views here.
def index(request):
    """Rookieplay's Job Matchmaking"""
    return render(request, 'rookieplays/index.html')

def topics(request):
    """Show a single topic and all its entries."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'rookieplays/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'rookieplays/topic.html', context)

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
    return render(request, 'rookieplays/new_topicc.html', context)
