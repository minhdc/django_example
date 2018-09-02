from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView
from django.views.generic import TemplateView,View,CreateView,UpdateView

from rest_framework.generics import ListCreateAPIView,ListAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView
from rest_framework.generics import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend


from .models import Word,Example,WordExampleRelation,WordRelation
from .forms import WordForm,ExampleForm

from .serializer import WordSerializer,WordRelationSerializer
from .serializer import ExampleSerializer,WordExampleRelationSerializer


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

class MultipleFieldLookupMixin(object):
    def get_object(self):
        queryset = self.get_queryset()  # Get the base queryset
        queryset = self.filter_queryset(queryset)
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:  # Ignore empty fields.
                filter[field] = self.kwargs[field]
        return get_object_or_404(queryset,**filter)

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

class WordRelationLookupMixin(object):
    
        handle mulitple field filtering based on a lookup_fields
    
    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:
                filter[field] = self.kwargs[field]
        obj = get_object_or404(queryset,**filter)
        self.check_object_permission(self.request,obj)

        return obj
'''

class WordRelationCreateReadView(ListCreateAPIView):
    queryset = WordRelation.objects.all()
    serializer_class = WordRelationSerializer    
    lookup_field = 'word1_id'

class WordRelationReadUpdateView(MultipleFieldLookupMixin,RetrieveUpdateAPIView):    
    queryset = WordRelation.objects.all()
    serializer_class = WordRelationSerializer
    lookup_fields = ('word1_id','word2_id')



  
'''
    WORD - CONCEPT

class WordListView(ListView):       
    model = Word
    
    def get_word_list(request):
        return render(request,'pvoexample/word_list.html',model)

class WordRelationView(ListView):
    model = WordRelation

    def get_word_relation_list(request):
        return render(request,'pvoexample/wordrelation.html',model)
'''    

'''
    EXAMPLE
'''

class ExampleCreateReadView(ListCreateAPIView):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
    lookup_field = 'id'

class ExampleReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
    lookup_field = 'id'

    
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
'''

'''
WORD_EXAMPLE
'''
class WordExampleRelationCreateReadView(ListCreateAPIView):
    queryset = WordExampleRelation.objects.all()
    serializer_class = WordExampleRelationSerializer
    lookup_field = 'word_id'

class WordExampleRelationReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = WordExampleRelation.objects.all()
    serializer_class = WordExampleRelationSerializer
    lookup_field = 'word_id'

