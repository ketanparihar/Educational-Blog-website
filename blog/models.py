from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class PublishedManager(models.Manager):
     def get_quary(self):
          return super(PublishedManager,
                       self).get_queryset() \
                            .filter(status='published')

class Post(models.Model):
    STATUS_CHOICE = (
         ('draft' , 'Draft'),
         ('published', 'Published')
    )

    title   = models.CharField(max_length=250)
    slug    = models.SlugField(max_length=250,unique_for_date='publish')
    author  = models.ForeignKey(User , on_delete=models.CASCADE ,related_name='blog_posts' )
    body    = models.TextField()
    publish = models.DateTimeField( default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update  = models.DateTimeField(auto_now=True)
    status  = models.CharField(max_length=10 , choices=STATUS_CHOICE,default='draft')
    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
    
    class meta:
        ordering = ('-publish')

    def __str__(self):
        return self.title


class comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update  = models.DateTimeField(auto_now=True)
    active  = models.BooleanField(default=True)

    class meta:
        ordering = ('created',)

    def __str__(self):
        return 'comment by {} on {}'.format(self.name,self.post)


class signup(models.Model):
    FirstName = models.CharField(max_length=200, null=True, blank=True)
    LastName = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    country = models.CharField(max_length=100,null=True, blank=True)
    state = models.CharField(max_length=100,null=True, blank=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)

def __str__(self):
    return str(self.id)



     


