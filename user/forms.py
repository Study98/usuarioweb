from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserDados

class CustomUserDadosCreateForm(UserCreationForm):
    
    class Meta:
        model = UserDados
        fields = ('username','luser','suser', 'cpf', 'pis','pais','estado',
                   'municipio','cep','rua','numero','complemento')
        labels = {'username': 'E-mail'}
        
    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user

class CustomUserDadosChangeForm(UserChangeForm):
    class Meta:
        model = UserDados
        fields  = ('username','luser','suser', 'cpf', 'pis','pais','estado',
                   'municipio','cep','rua','numero','complemento')
        exclude = ('password',)