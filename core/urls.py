from django.urls import path

from .views import BoardCreateView, BoardDeleteView, BoardDetailView, BoardEditView, BoardIndexView, BoardRubricView

urlpatterns = [
    path('add/', BoardCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BoardDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', BoardDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/', BoardEditView.as_view(), name='edit'),
    path('<int:rubric_id>/', BoardRubricView.as_view(), name='rubric'),
    path('', BoardIndexView.as_view(), name='index'),
]
