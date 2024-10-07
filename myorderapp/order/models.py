from django.db import models

# Create your models here.

class Order(models.Model):
    student_name = models.CharField(max_length=100,verbose_name='Student Name',null=False)
    job_title = models.CharField(max_length=100,verbose_name='Job Title',null=False)
    sent_date = models.DateField(auto_now_add=True,verbose_name='Day task was sent')
    due_date = models.DateField(verbose_name='due date',null=False)
    completed = models.BooleanField(verbose_name='Completed or Not',default=False)
    cancelled = models.BooleanField(verbose_name='cancelled or not', default=False)
    page_count = models.PositiveIntegerField(null=True,blank=True)
    word_count = models.PositiveIntegerField(null=True,blank=True)
    additional_notes = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return f"Order by {self.student_name}, Title {self.job_title}"