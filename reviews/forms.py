from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Username", max_length=100, error_messages={
        "required": "Username is reqired",
        "max_length": "Please enter a shorter name"
    })
