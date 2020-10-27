from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from authentication.models import UserData
# YEARS = [x for x in range(1940, 2021)]


class UserDataCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = UserData
        fields = ('email', )


class UserDataChangeForm(UserChangeForm):

    class Meta:
        model = UserData
        fields = ('email', )


# class RegistrationForm(UserCreationForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
#     dob = forms.DateField(label='Date of birth', widget=forms.SelectDateWidget(years=YEARS))
#
#     class Meta(UserCreationForm):
#         model = UserData
#         fields = ('email', 'username', 'first_name', 'last_name', 'dob', 'phone_number', 'password1', 'password2',)
#
#
# class AccountAuthenticationForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = UserData
#         fields = ('email', 'password')
#
#     def clean(self):
#         if self.is_valid():
#             email = self.cleaned_data['email']
#             password = self.cleaned_data['password']
#             if not authenticate(email=email, password=password):
#                 raise forms.ValidationError("Invalid login")
