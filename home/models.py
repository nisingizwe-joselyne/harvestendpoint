from django.db import models
from django.contrib.auth.models import User,auth
# Create your models here.


class Cooperative(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    harvesttype=models.CharField(max_length=255)
    district=models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Recorder(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.username  

class Regfarmer(models.Model):
    firstname= models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    dateofbirth = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    regCooperative=models.CharField(max_length=255)
    farmercode=models.CharField(max_length=255)
    def __str__(self):
        return self.firstname
class Insurance(models.Model):
    farmercode=models.ForeignKey(Regfarmer, on_delete=models.CASCADE)
    insurancetype = models.CharField(max_length=255,choices=(('imyaka15','imyaka15'),('imyaka10','imyaka10'),('imyaka itanu','imyaka itanu'),('umwaka umwe','umwaka umwe'),))
    def __str__(self):
        return self.farmercode  
class Harvestrecord(models.Model):
    usered=models.ForeignKey(Regfarmer, on_delete=models.CASCADE)
    Quantity=models.CharField(max_length=255)
    farmercode=models.CharField(max_length=255)
    donedate=models.DateField(auto_now=True)
    donetime=models.TimeField(auto_now=True)


class Loan(models.Model):
    farmercode = models.ForeignKey(Regfarmer, on_delete=models.CASCADE)
    loan_amount= models.CharField(max_length=255)
    def __str__(self):
        return self.farmercode

class Payharvest(models.Model):
    farmercode = models.ForeignKey(Regfarmer, on_delete=models.CASCADE)
    pay_amount= models.CharField(max_length=255)
    def __str__(self):
        return self.farmercode

class Cooperativesreg(models.Model):
    name=models.CharField(max_length=255)
    leadername=models.CharField(max_length=255)
    leaderphone=models.CharField(max_length=255)
    harvesttype=models.CharField(max_length=255)
    Cooperativedistrict=models.CharField(max_length=255) 
    Cooperativesector=models.CharField(max_length=255) 
    def __str__(self):
        return self.name

class Profilecooperative(models.Model):
    farmer=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='Instute cooperative Logo',null=True,blank=True)
    cooperativename=models.CharField(max_length=255)
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url       

class Site(models.Model):
    name= models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    Cell = models.CharField(max_length=255)
    def __str__(self):
        return self.name