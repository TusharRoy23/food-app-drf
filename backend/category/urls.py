from django.urls import path
from . import views

app_name = "Category"

urlpatterns = [
    path("", views.CategoryListViewForVisitor.as_view(), name="category-list-view-for-public"),
]