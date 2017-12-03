from django.db import models
from django.core.urlresolvers import reverse

class Hub(models.Model):
    hub_id = models.IntegerField(primary_key=True, default=0)
    population = models.IntegerField(default=0)
    current_storage = models.IntegerField(default=0)

    def _get_days_to_exhaustion():
        return round(self.current_storage/self.population,0)
    days_to_exhaustion = property(_get_days_to_exhaustion)
    def _get_priority_score():
       return round(self.population/self.current_storage*10,0)
    priority_score = property(_get_priority_score)

    def __str__(self):
        return("Hub ID: {hub_id}  ".format(hub_id=self.hub_id))

class household(models.Model):
    household_id = models.IntegerField(default=0)

    def _get_hub():
        if(self.household_id>0 and self.household_id<6):
            return()
        elif(self.household_id>5 and self.household_id<11):
            return(2)
        else:
            return(3)
    from_hub = property(_get_hub)
    house_population = models.IntegerField(default=0)

    def __str__(self):
        return("House ID: {household_id}  ".format(household_id=self.household_id))
