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

    url(regex=r"^api/v1/words$",
        view = views.WordCreateReadView.as_view(),
        name="word_rest_api",
    ),

    url(regex=r"^api/v1/words/(?P<id>[-\w]+)/$",
        view = views.WordReadUpdateDeleteView.as_view(),
        name="word_rest_api",
    ),
    
    url(regex=r"^wordlist$",
        view = views.WordListView.as_view(),
        name="wordlist",
    ),

    url(regex=r"^example$",
        view = views.ExampleListView.as_view(),
        name="example",
    ),

    url(regex=r"^examplecreate$",
        view = views.ExampleCreateView.as_view(),
        name="examplecreate",
    ),

    url(regex=r"^wordrelation$",
        view = views.WordRelationView.as_view(),
        name="wordrelation",
    ),

    url(regex=r"^wordexample$",
        view = views.WordExampleListView.as_view(),
        name="wordexample",
    ),
]