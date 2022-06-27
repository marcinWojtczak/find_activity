from django.urls import path
from . views import(
    home,
    PostListView,
)
urlpatterns = [
    path('', home, name='home-page'),
    path('posts', PostListView.as_view(), name='posts-view'),
]
