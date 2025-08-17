from django import forms



class LoginForm(forms.Form):
    usuario = forms.CharField(
        label='Usuario',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Usuario',
                'class':'form-control',
                'usuario':'usuario'
            }
        )
    )

    password = forms.CharField(
        label='Password',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Senha',
                'class':'form-control',
                'password':'password'
            }
        )
    )