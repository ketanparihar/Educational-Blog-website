from django.contrib.auth import login,authenticate
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, signup
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
# Create your views here


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return render(request, 'blog/post/detail.html', {'post':post, 'comments':comments,'new_comment':new_comment,'comment_form':comment_form})

    else:
      comment_form = CommentForm()
      return render(request, 'blog/post/detail.html', {'post':post, 'comments':comments,'new_comment':new_comment,'comment_form':comment_form})


def post_share(request, post_id):
  post = get_object_or_404(Post, id=post_id, status='published')
  sent = False

  if request.method == 'POST':
      form = EmailPostForm(request.POST)
      if form.is_valid():
          cd = form.cleaned_data
          post_url= request.build_absolute_uri(post.get_absolute_url())
          subject = '{} ({}) recommended you reading "{}"'.format(cd['name'] , cd['email'],post.title)
          message = 'Read "{}" at {}\n\n{}\'s comment:{}'.format(post.title, post_url,cd['name'],cd['comments'])
          send_mail(subject, message, 'admin@admin.com', [cd['to']])
          sent=True
  else:
    form = EmailPostForm()
  return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})


def home(request):
  return render(request, "blog/post/home.html")


def registerPage(request):
  return render(request, "registration/register.html")


def register(request):
    if request.method == "POST":
        FirstName = request.POST.get("FirstName")
        LastName = request.POST.get("LastName")
        password = request.POST.get("password")
        Email = request.POST.get("Email")
        country = request.POST.get("country")
        state = request.POST.get("state")
        city = request.POST.get("city")
        pincode = request.POST.get("pincode")
        auth = signup.objects.filter(Email=Email).count()
        if auth > 0:
            message = "User 2 Already Register"
            return render(request, "registration/register.html", {'message': message})
        else:
            signup(FirstName=FirstName, LastName=LastName, password=password, Email=Email, country=country, state=state,
                   city=city, pincode=pincode).save()
        return render(request, "registration/login.html")
    else:
        return render(request, "registration/login.html")


def loginUser(request):
    if request.method== "POST":
        UserEmail = request.POST.get("Email")
        password = request.POST.get("password")
        count = signup.objects.filter(Email=UserEmail, password=password)
        if count.count()>0:
            request.session['UserEmail'] = UserEmail
            return redirect('/', {'UserEmail': UserEmail})

        else:
            message = "invalid user or password"
            return render(request, "registration/login.html", {'message': message})
    else:
        return HttpResponse("invalid POST REQUEST")


def logout(request):
    request.session.flush()
    return redirect("/")