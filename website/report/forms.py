from django.forms import ModelForm, ChoiceField, Select
from report.models import HealthCenter, District, Block, Event

class HealthCenterForm(ModelForm):
    block = ChoiceField(choices=(('-1', 'Select Block'),))
    class Meta:
        model = HealthCenter

class DistrictForm(ModelForm):
    class Meta:
        model = District

class BlockForm(ModelForm):
    class Meta:
        model = Block
        
class EventForm(ModelForm):
    class Meta:
        model = Event