from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
      #If Method is POST 
    if request.method == 'POST':
        form = PostForm(request.POST)
        #If the form is valid
        if form.is_valid():
            # If yes, Save
            form.save()
            #Redirect to Home
            return HttpResponseRedirect('/')          
        else:
            #If no, Show Error
            return HttpResponseRedirect(form.erros.as_json)
    # Get all posts, limit = 20
    posts = Post.objects.all()[:20]
    # Show
    return render(request, 'posts.html',
                    {'posts': posts})


def delete(request, post_id):
    #Find the post
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')