from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,TemplateView,View
from .models import Word,Example,WordExampleRelation,WordRelation
# Create your views here.
'''
    Using CBV - allow us to rspond to HTTP request methods with 
    different class instance METHOD, instead of branching code inside
    a single view function
'''
class IndexView(TemplateView):
    template_name = 'pvoexample/index.html'
    

'''
    WORD - CONCEPT
'''
class WordListView(ListView):       
    model = Word
    
    def get_word_list(request):
        return render(request,'pvoexample/word_list.html',model)

class WordDetailView(DetailView):
    model = Word

class WordRelationView(DetailView):
    model = WordRelation

'''
    EXAMPLE
'''
class ExampleListView(ListView):
    model = Example

class WordExampleRelationListView(ListView):
    model = WordExampleRelation
