from django.db import models
from orderable.models import Orderable
from django.utils import timezone


#class Tiles(models.Model):
#    title = models.CharField(max_length=100)
#    description = models.TextField()
#    technology = models.CharField(max_length=20)
#    image = models.FilePathField(path="/img")


# - head of page - myself and description
#
# 5 tiles:
# - 1 - Work and science - cv
# - 2 - tech and expertise
# - 3 - artistic vein 
# - 4 - blog
# - 5 - contact me

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# - 1 - professional experience
class Job(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    skills = models.ManyToManyField('Skill', related_name='skills')
    #image = models.FilePathField(path="/img")

    def __str__(self):
        return self.job_title + ' / ' + self.company_name


# - 2 - technologies used
class Technology(models.Model):
    name = models.CharField(max_length=255)
    dev_icon = models.CharField(max_length=255, help_text="name of corresponding devicon.")

    class Meta():
        unique_together = ['name', 'dev_icon']

    def __str__(self):
        return self.name


# - 3 - Art
class ArtWork(models.Model):
    title = models.CharField(max_length=100)
    openseaLink = models.TextField(null=True,help_text="opensea link")
    openseaImage = models.TextField(null=True,help_text="opensea image")
    #technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

# - 4 - blog and papers
#class Papers(models.Model):
    #title = models.CharField(max_length=100)
    #description = models.TextField()
    #technology = models.CharField(max_length=20)
    #image = models.FilePathField(path="/img")


class Project(Orderable):
    index = models.CharField(max_length=20, null=True, default=1)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta(Orderable.Meta):
        ordering = ['index']

    def __str__(self):
        return self.title


# rom projects.models import Job
# jobs = Job.objects.all()
# job_list = ''
# for job in jobs:
#   job_list += job.job_title + '\n\t' + job.description
# p1 = Project( title='Jobs', description=job_list, technology='' )
# p1.save()