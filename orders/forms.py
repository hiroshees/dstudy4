from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm

from django.contrib.auth import get_user_model

class UserUpdateForm(ModelForm):
    """
    ユーザー情報更新フォーム
    """

    class Meta:
        model = get_user_model()
        fields = ('last_name', 'first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    last_name = forms.CharField(
        label="姓",
        widget=forms.TextInput(attrs={
            'autofocus': True,
            "placeholder":"姓を入力してください"
        }),
        error_messages={
            "required" : "入力してください",
        }
    )
    
    first_name = forms.CharField(
        label="名",
        widget=forms.TextInput(attrs={
            "placeholder":"名を入力してください"
        }),
        error_messages={
            "required" : "入力してください",
        }
    )


from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator

from .models import Item

class ItemForm(ModelForm):
    """
    商品用フォーム
    """
    class Meta:
        model = Item
        fields = ('name','price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    price = forms.IntegerField(
        label="金額",
        validators=[
            MinValueValidator(0,"0以上にしてね"),
        ],
    )

