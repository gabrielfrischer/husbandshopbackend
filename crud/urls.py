from django.urls import path
from .views import ListItems, DetailItem, current_user, UserList

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('', ListItems.as_view()),
    path('<int:pk>/', DetailItem.as_view())
]

