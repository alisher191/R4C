from django import forms

from .models import Robot


class RobotForm(forms.ModelForm):
    class Meta:
        model = Robot
        fields = ['model', 'version', 'created']

    def clean_version(self):
        version = self.cleaned_data['version']
        if Robot.objects.filter(version=version).exists():
            raise forms.ValidationError("Модель уже существует.")
        return version

