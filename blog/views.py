from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from .models import Blog, BlogAuthor, BlogComment

# Create your views here.
from django.views import generic


def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html
    return render(
        request,
        'index.html',
    )

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5
    template_name = ('/blog/blog_list')

class AuthorsListView(generic.ListView):
    model = BlogAuthor
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    """
    Generic class-based detail view for a blog.
    """
    model = Blog

class AuthorDetailView(generic.DetailView):
    model = BlogAuthor

class BlogCommentCreate(CreateView):
    """
    creates a comment object
    """
    model = BlogComment #specify which model can be created here
    fields = ['description', ] # which fields can be openly editted

    def get_context_data(self, **kwargs):
        """
        attach parent blog so I can display it on the comment template
        :param kwargs:
        :return:
        """
        #refer to the super view to generate context base
        context = super(BlogCommentCreate,self).get_context_data(**kwargs)
        #set 'blog' to equal queryset of Blog objects matching pk
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        #this will return a blog object
        return context

    def form_valid(self, form):
        """
        add associate blog and author to form.
        """
        #this is setting the author of the form
        form.instance.author = self.request.user
        #associate comment with blog based on passed
        form.instance.blog = get_object_or_404(Blog, pk = self.kwargs['pk'])
        #the super class carried the validator function
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('blog_detail', kwargs={'pk': self.kwargs['pk'], })





