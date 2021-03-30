from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import BoardForm
from .models import Board, Rubric


# Create your views here.
class BoardIndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'boards'

    def get_queryset(self):
        return Board.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BoardCreateView(CreateView):
    template_name = 'add.html'
    form_class = BoardForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BoardDetailView(DetailView):
    template_name = 'detail.html'
    model = Board

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BoardRubricView(ListView):
    template_name = 'rubrics.html'
    context_object_name = 'boards'

    def get_queryset(self):
        return Board.objects.filter(rubric=self.kwargs['rubric_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['cur_rubric'] = Rubric.objects.get(pk=self.kwargs['rubric_id'])
        return context


class BoardEditView(UpdateView):
    template_name = 'edit.html'
    model = Board
    form_class = BoardForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BoardDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Board
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
