from django.forms import ModelForm
from shrimps.models import Shrimp


class ShrimpForm(ModelForm):
    """Shrimp model form"""

    class Meta:
        model = Shrimp
        fields = "__all__"
