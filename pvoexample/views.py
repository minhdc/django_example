from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView
from django.views.generic import TemplateView,View,CreateView,UpdateView

from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Word,Example,WordExampleRelation,WordRelation
from .forms import WordForm,ExampleForm

from .serializer import WordSerializer


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
    #fields = ('word','definition','pic_url')
    #cannot specify both fields and form_class

    @property
    def success_msg(self):
        return NotImplemented
    
    def form_valid(self,form):
        messages.info(self.request,self.success_msg)
        return super(WordActionMixin,self).form_valid(form)
        
class ExampleActionMixin(object):
    @property
    def success_msg(self):
        return NotImplemented
    
    def form_valid(self,form):
        messages.info(self.request,self.success_msg)
        return super(ExampleActionMixin,self).form_valid(form)


'''
    WORD 
'''

class WordCreateReadView(ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    lookup_field = 'word'

class WordReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    lookup_field = 'id'
'''
class WordCreateView(WordActionMixin,CreateView):
    model = Word
    success_msg = "Word created"
    template_name = 'pvoexample/word_form.html'
    form_class = WordForm
    success_url = '/pvoexample/wordlist' 
        
class WordUpdateView(WordActionMixin,UpdateView):
    model = Word
    success_msg = "Word updated"
    #fields = ('word','definition','pic_url')

class WordDetailView(DetailView):
    model = Word
'''


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
class ExampleCreateView(ExampleActionMixin,CreateView):
    model = Example
    success_msg = "Example created"
    template_name = 'pvoexample/example_form.html'
    form_class = ExampleForm
    success_url = '/pvoexample/example'
    
class ExampleListView(ListView):
    model = Example

    def get_example_list(request):
        return render(request,'pvoexample/example.html',model)

class WordExampleListView(ListView):
    model = WordExampleRelation

    def get_word_example_relation_list(request):
        return render(request,'pvoexample/wordexample.html',model)
