from django.urls import path
from django.conf.urls import url

from django.views.generic import TemplateView

from . import views
app_name = "pvoexample"

urlpatterns = [    
    url(
        regex=r'^$',
        #view = views.IndexView.as_view(),
        view = TemplateView.as_view(template_name="pvoexample/index.html"),
        name="index",
    ),
    #WORD 
    url(regex=r"^api/v1/words$",
        view = views.WordCreateReadView.as_view(),
        name="word_rest_api_create",
    ),

    url(regex=r"^api/v1/words/(?P<id>[-\w]+)/$",
        view = views.WordReadUpdateDeleteView.as_view(),
        name="word_rest_api_rud",
    ),

    #WORD-WORD RELATION
    url(regex=r"^api/v1/wordrelationdetail/(?P<word1_id>[-\w]+)/(?P<word2_id>[-\w]+)$",        
        view = views.WordRelationReadUpdateDeleteView.as_view(),
        name="word_relation_rest_api_rud",
    ), 

    url(regex=r"^api/v1/wordrelation$",
        view = views.WordRelationCreateReadView.as_view(),
        name="word_relation_rest_api_create",
    ),


    #WORD_EXAMPLE RELATION
    url(regex=r"^api/v1/wordexample/(?P<id>[-\w]+)/$",
        view = views.WordExampleRelationReadUpdateDeleteView.as_view(),
        name="word_example_relation_rest_api_rud",
    ),

    url(regex=r"^api/v1/wordexample$",
        view = views.WordExampleRelationCreateReadView.as_view(),
        name="word_example_relation_rest_api_create",
    ),


    #EXAMPLE 
    url(regex=r"^api/v1/example/(?P<id>[-\w]+)/$",
        view = views.ExampleReadUpdateDeleteView.as_view(),
        name="example_relation_rest_api_rud",
    ),

    url(regex=r"^api/v1/example$",
        view = views.ExampleCreateReadView.as_view(),
        name="example_relation_rest_api_create",
    ),
   
]