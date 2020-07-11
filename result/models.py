from django.db import models

# Create your models here.
class Gender(models.Model):
    g_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=200)
    
    def  __str__(self):
        return self.gender

class MatricResult(models.Model):
    s_id = models.AutoField(primary_key=True)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    father_name = models.CharField(max_length=200)
    dob = models.DateField()
    img = models.ImageField(upload_to = "media/")
    roll_no = models.IntegerField()
    roll_code = models.IntegerField()
    sst = models.IntegerField(default=0)
    sci = models.IntegerField(default=0)
    math = models.IntegerField(default=0)
    hindi = models.IntegerField(default=0)
    eng = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class InterResult(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    i_gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    dob = models.DateField()
    img = models.ImageField(upload_to="media/")
    roll_no = models.IntegerField()
    roll_code = models.IntegerField()
    phy = models.IntegerField(default=0)
    che = models.IntegerField(default=0)
    math = models.IntegerField(default=0)
    bio = models.IntegerField(default="ex")
    hindi = models.IntegerField(default=0)
    eng = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    
class BeResult(models.Model):
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    email = models.EmailField()
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    img = models.ImageField(upload_to ="media/")
    dob = models.DateField()
    roll_no = models.IntegerField()
    roll_code = models.IntegerField()
    marks = models.IntegerField(default=0)
    renk = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    