from django.db import models

# Create your models here.
    # title, pub_date, body, image
# Create A blog models
# Add the blog app to the settings
# migrate
#Add to the admin

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Published Date')
    b_content = models.TextField()
    image = models.ImageField(upload_to='images/')
