from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addcomment/<int:id>', views.addComment, name='addComment'),
    path('productdelete/<int:id>', views.product_delete, name='product_delete'),
]