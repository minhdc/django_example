from django.urls import path
from django.conf.urls import url
from . import views
app_name = "pvoexample"

urlpatterns = [    
    url(
        regex=r'^$',
        view = views.IndexView.as_view(),
        name="index",
    ),

    url(regex=r"^word$",
        view = views.WordDetailView.as_view(),
        name="worddetail",
    ),

    url(regex=r"^wordlist$",
        view = views.WordListView.as_view(),
        name="wordlist",
    ),

    url(regex=r"^example$",
        view = views.ExampleListView.as_view(),
        name="example",
    ),

    url(regex=r"^wordrelation$",
        view = views.WordRelationView.as_view(),
        name="wordrelation",
    ),
]