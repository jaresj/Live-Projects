
from django.forms import ModelForm
from .models import Nutrition

# Create a form for Nutrition model
class NutritionForm(ModelForm):
    class Meta:
        model = Nutrition
        fields = '__all__' # food information fields