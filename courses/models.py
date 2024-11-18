from django.db import models
class AccessRequirement(models.TextChoices):
      ANYONE = "any", "Anyone"
      EMAIL_REQUIRED = "email_required" , "Email_Required"
     

class PublishStatus(models.TextChoices):
      PUBLISHED = "Publish", "Published"
      COMING_SOON = "soon" , "Coming Soon"
      DRAFT= "draft","Draft"

def handle_upload(instance,filename):
      return f"{filename}"      

class Course(models.Model):
      title = models.CharField(max_length=120)
      description = models.TextField(blank=True,null=True)
      status = models.CharField(max_length=50, choices=PublishStatus.choices, default=PublishStatus.DRAFT)
      access = models.CharField(max_length=50, choices=AccessRequirement.choices, default=AccessRequirement.EMAIL_REQUIRED)
      image = models.ImageField(upload_to=handle_upload,blank=True, null=True)


      @property
      def is_published(self):
            return self.status == PublishStatus.PUBLISHED