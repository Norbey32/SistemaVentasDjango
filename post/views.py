from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

# Vista para listar todos los puestos de trabajo.
class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

# Vista para crear un nuevo puesto de trabajo.
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_form.html'
    success_url = reverse_lazy('post-list')

# Vista para actualizar un puesto de trabajo existente.
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_form.html'
    success_url = reverse_lazy('post-list')

# Vista para eliminar un puesto de trabajo.
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')