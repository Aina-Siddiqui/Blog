from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#each class isgoing to be its own table in the databases
from django.urls import reverse
class Post(models.Model):
    #lets add some attributesand each attribute is different field in the table
    title=models.CharField(max_length=100)
    content=models.TextField()
    #auto_now=True you can use it to update the post
    #auto_now_add will add the date when the post was created
    #default will  update the date when the post isupdated also it will add the date when post was created
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)# on delete is a function which tell what happen to the post if user got deleted
    #models.CASCADE will delete the post if user got delete but if you delete the post the user will not be deleted
    def __str__(self):
        return self.Title
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})