from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from . import models
from . import forms

def index(request):
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    # topics = models.Topic.objects.order_by('date_added') # o mais antigo para o mais recente
    topics = models.Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {
        'topics' : topics,
    }
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    # topic = models.Topic.objects.get(id = topic_id)
    topic = get_object_or_404(models.Topic, id = topic_id)

    if topic.owner != request.user: # se o usuário que está acessando for diferente do usuário dono do tópico
        raise Http404

    entries = topic.entry_set.order_by('-date_added') # mais recente para o mais antigo
    context = {
        'topic' : topic,
        'entries' : entries,
    }
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        # nenhum dado enviado: cria um formulário em branco
        form = forms.TopicForm()
    else:
        # dados via post enviados
        form = forms.TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('topics')
        
    context = {
        'form' : form
    }

    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic = models.Topic.objects.get(id = topic_id)

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = forms.EntryForm()
    else:
        form = forms.EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('topic', topic_id = topic_id)
    
    context = {
        'topic': topic,
        'form': form,
    }
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = models.Entry.objects.get(id = entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = forms.EntryForm(instance = entry)
    else:
        form = forms.EntryForm(instance = entry, data = request.POST)
        if form.is_valid():
            form.save() 
            return redirect('topic', topic_id = topic.id)
    
    context = {
        'entry': entry,
        'topic': topic,
        'form': form,
    }

    return render(request, 'learning_logs/edit_entry.html', context)    
