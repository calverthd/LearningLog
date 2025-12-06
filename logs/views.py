from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# ----- Static pages -----
def home(request):
    return render(request, 'logs/home.html')

def about(request):
    return render(request, 'logs/about.html')

def contact(request):
    return render(request, 'logs/contact.html')


# ----- Dynamic pages: Topics and Entries -----
@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    return render(request, 'logs/topics.html', {'topics': topics})

@login_required
def topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if topic.owner != request.user:
        return redirect('topics')
    entries = topic.entry_set.order_by('-date_added')
    return render(request, 'logs/topic.html', {'topic': topic, 'entries': entries})

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('topics')
    return render(request, 'logs/new_topic.html', {'form': form})

@login_required
def new_entry(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if topic.owner != request.user:
        return redirect('topics')
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.topic = topic
            entry.save()
            return redirect('topic', topic_id=topic.id)
    return render(request, 'logs/new_entry.html', {'topic': topic, 'form': form})

@login_required
def edit_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        return redirect('topics')
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('topic', topic_id=topic.id)
    return render(request, 'logs/edit_entry.html', {'entry': entry, 'topic': topic, 'form': form})
