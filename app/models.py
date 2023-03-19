from django.db import models

# Create your models here.
class Immunization(models.Model):
    g = models.FloatField() #Hepa
    h = models.FloatField() #measles
    k = models.FloatField() #Polio
    m = models.FloatField() #Diptheria

class Health(models.Model):
    i = models.FloatField() #BMI
    q = models.FloatField() #Thinnes 5-9
    r = models.FloatField() #Thinnes 1-19

class Mortality(models.Model):
    c = models.FloatField() #adult mortality
    d = models.FloatField() #infant deaths
    e = models.FloatField() #alcohol
    j = models.FloatField() #under 5 deaths
    n = models.FloatField() #HIV


class Economic(models.Model):
    b = models.FloatField() #status
    f = models.FloatField() #percentage expenditure
    l = models.FloatField() #total
    o = models.FloatField() #GDP
    s = models.FloatField() #Income Composition

class Social(models.Model):
    p = models.FloatField() #population
    t = models.FloatField() # schooling
    u = models.CharField(max_length=255) # country




