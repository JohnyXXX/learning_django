from django.urls import path

from .views import BoardCreateView, BoardDeleteView, BoardDetailView, BoardEditView, BoardIndexView, BoardRubricView, \
    register, user_login, user_logout

urlpatterns = [
    path('add/', BoardCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BoardDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', BoardDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/', BoardEditView.as_view(), name='edit'),
    path('<int:rubric_id>/', BoardRubricView.as_view(), name='rubric'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', BoardIndexView.as_view(), name='index'),
]
