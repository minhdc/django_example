from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,TemplateView,View,CreateView,UpdateView

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
   ACTION MIXIN
'''
class WordActionMixin(object):
    fields = ('word','definition','pic_url')

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self,form):
        messages.info(self.request,self.success_msg)
        return super(WordActionMixin,self).form_valid(form)

'''
    WORD 
'''
class WordCreateView(WordActionMixin,CreateView):
    model = Word
    success_msg = "Word created"
    #fields = ('word','definition','pic_url')


class WordUpdateView(WordActionMixin,UpdateView):
    model = Word
    success_msg = "Word updated"
    #fields = ('word','definition','pic_url')

class WordDetailView(DetailView):
    model = Word
    

'''
    WORD - CONCEPT
'''
class WordListView(ListView):       
    model = Word
    
    def get_word_list(request):
        return render(request,'pvoexample/word_list.html',model)

class WordRelationView(ListView):
    model = WordRelation

    def get_word_relation_list(request):
        return render(request,'pvoexample/wordrelation.html',model)
    

'''
    EXAMPLE
'''
class ExampleListView(ListView):
    model = Example

    def get_example_list(request):
        return render(request,'pvoexample/example.html',model)

class WordExampleListView(ListView):
    model = WordExampleRelation

    def get_word_example_relation_list(request):
        return render(request,'pvoexample/wordexample.html',model)
