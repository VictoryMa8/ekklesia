from django.urls import path
from .views import Home, ArticleDetailView

urlpatterns = [
    path('', Home.as_view(), name="home"),
    # Here, the <int:pk> parameter matches any integer and gives it to our view which tries to identify the article based on its primary key (pk)

    # We didn't specify a pk though, so it'll just go by oldest article incrementing from there
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article_detail")
]