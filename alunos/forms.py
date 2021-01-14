# from django import forms
# from django.contrib.auth.models import User
#
# from alunos.models import Aluno
#
#
# class CadastrarAlunoForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class': 'form-control', 'placeholder': 'Password'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
#
#     dtNascimento = forms.DateField()
#     rg = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
#     nomeMae = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     nomePai = forms.CharField(widg et=forms.TextInput(attrs={'class': 'form-control'}))
#     nivelEnsino = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     anoConclusao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     observacoes = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'password', 'dtNascimento',
#                   'rg', 'nomeMae', 'nomePai', 'nivelEnsino', 'anoConclusao', 'observacoes']
#         widgets = {
#             'first_name': forms.TextInput(
#                 attrs={'class': 'form-control', 'placeholder': 'First Name', 'required': ''}),
#             'last_name': forms.TextInput(
#                 attrs={'class': 'form-control', 'placeholder': 'Last Name', 'required': ''}),
#             'username': forms.TextInput(
#                 attrs={'class': 'form-control', 'placeholder': 'Username', 'required': ''})
#         }
#
#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             return self.adiciona_erro("Password don't match")
#         return cd['password2']
#
#     def is_valid(self):
#         valid = True
#         if not super(CadastrarAlunoForm, self).is_valid():
#             valid = False
#
#         user_exists = User.objects.filter(username=self.data['username']).exists()
#         #email_exists = User.objects.filter(email=self.data['email']).exists()
#
#         if user_exists:
#             self.adiciona_erro('A user with that username already exists.')
#             valid = False
#
#         # if email_exists:
#         #     self.adiciona_erro('A user with that e-mail already exists.')
#         #     valid = False
#
#         return valid
#
#     def adiciona_erro(self, message):
#         erros = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
#         erros.append(message)
#
#     def save(self, commit=True):  # Metodo para encriptar password do formulario para enviar ao banco.
#         user = super(CadastrarAlunoForm, self).save(
#             commit=False)  # Não salva no banco ainda, tenho que fazer mais uma coisa
#         user.set_password(self.cleaned_data['password'])  # Encriptando password
#         if commit:
#             user.save()
#         return user