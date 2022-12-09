from django.shortcuts import render, get_object_or_404


# Create your views here.
from blog.forms import CommentForm
from blog.models import Post

def home_view(request):
    posts= Post.objects.filter(status="published").order_by("-created_on")[:6]
    return render(request,
                  template_name='post/index.html',
                  context={
                      'posts':posts,
                  })
def posts_view(request):
    posts= Post.objects.filter(status="published").order_by("-created_on")
    return render(request,
                  template_name='post/post.html',
                  context={
                      'posts': posts,
                  })

def post_detail(request,slug):
    template_name = "post/post_detail.html"
    post = get_object_or_404(Post,slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )