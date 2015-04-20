from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.views import generic

from core.models import Journal



class IndexView(generic.ListView):
    template_name = 'core/index.html'

    def get_queryset(self):
        return Journal.objects.all()


class DetailView(generic.DetailView):
    model = Journal
    template_name = 'core/detail.html'


class EditView(generic.DetailView):
    model = Journal
    template_name = 'core/edit.html'


def delete(request, pk):
    print pk
    try:
        entry = Journal.objects.get(id=pk)
        entry.delete()
    except:
        return HttpResponseRedirect(reverse('index'))

    return HttpResponseRedirect(reverse('index'))

def new_form(request):
    return render(request, 'core/new_entry.html', {})


def new(request):
    try:
        entry = Journal(title=request.POST['title'], content=request.POST['content'])
        entry.save()
    except ValidationError as e:
        return render(request, 'core/new_entry.html', {
            'error_message': 'Please fill out both title and content',
            'entry': entry
        })    
    else:
        return HttpResponseRedirect(reverse('detail', args=(entry.id,)))

def update(request, pk):
    try:
        entry = Journal.objects.get(id=pk)
        entry.title = request.POST['title']
        entry.content = request.POST['content']
        print entry
        entry.save()
    except ValidationError as e:
        return render(request, 'core/edit.html', {
            'error_message': 'Please fill out both title and content',
            'entry': entry
        })    
    else:
        return HttpResponseRedirect(reverse('detail', args=(entry.id,)))    