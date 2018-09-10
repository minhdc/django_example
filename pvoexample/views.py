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
    WORD RELATION
'''

class WordRelationCreateReadView(ListCreateAPIView):
    queryset = WordRelation.objects.all()
    serializer_class = WordRelationSerializer    
    lookup_field = 'word1_id'

class WordRelationReadUpdateDeleteView(MultipleFieldLookupMixin,RetrieveUpdateDestroyAPIView):    
    queryset = WordRelation.objects.all()
    serializer_class = WordRelationSerializer
    lookup_fields = ('word1_id','word2_id')


'''
    WORD_EXAMPLE
'''
class WordExampleRelationCreateReadView(ListCreateAPIView):
    queryset = WordExampleRelation.objects.all()
    serializer_class = WordExampleRelationSerializer
    lookup_field = 'word_id'

class WordExampleRelationReadUpdateDeleteView(MultipleFieldLookupMixin,RetrieveUpdateDestroyAPIView):
    queryset = WordExampleRelation.objects.all()
    serializer_class = WordExampleRelationSerializer
    lookup_field = ('word_id','example_id')

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



