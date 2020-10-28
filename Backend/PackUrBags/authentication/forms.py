from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from authentication.models import UserData


class UserDataCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = UserData
        fields = ('email', )


class UserDataChangeForm(UserChangeForm):

    class Meta:
        model = UserData
        fields = ('email', )
