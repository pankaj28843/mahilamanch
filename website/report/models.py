from django.db import models
from report.widgets import *

class District(models.Model):
    name = models.CharField("Name", max_length=100)
    center = LocationField("Position of center", blank=False, max_length=255)
    
    def __unicode__(self):
        return self.name
    
class Block(models.Model):
    name = models.CharField("Name", max_length=100)
    district = models.ForeignKey(District)
    center = LocationField("Position of center", blank=True, max_length=255)
    
    def __unicode__(self):
        return self.name

class HealthCenter(models.Model):
    code = models.IntegerField("4 digit code", max_length=4, unique=True)
    name = models.CharField("Name", max_length=100)
    district = models.ForeignKey(District)
    block = models.ForeignKey(Block)
    center = LocationField("Position on map", blank=True, max_length=255)
    
    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    #objects = models.GeoManager()
    
    # So the model is pluralized correctly in the admin.
    class Meta:
        verbose_name = "Health Center"
        verbose_name_plural = "Health Centers"

    # Returns the string representation of the model.
    def __unicode__(self):
        return self.name

class Event(models.Model):
    CATEGORY_CHOICES = (
    (1, 'Category 1'),
    (2, 'Category 2'),
    (3, 'Category 3'),
    )

    reporting_date = models.DateField("Date of reporting")
    reporting_time = models.TimeField("Time of reporting", auto_now=False, auto_now_add=True)
    district = models.ForeignKey(District)
    block = models.ForeignKey(Block)
    target_health_center = models.ForeignKey(HealthCenter)
    category = models.IntegerField("Category", max_length=1, choices=CATEGORY_CHOICES)
    money = models.IntegerField("Amount of money")
    
    def __unicode__(self):
        return "Category = "+ str(self.category)+ ", Date = " + str(self.reporting_date) + ", Health Center = " + str(self.target_health_center)+", Money = " + str(self.money)
