from django import forms

from .models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question


        fields = [
            "question_text",
            "pub_date",
        ]
        field_classes = {
            "pub_date": forms.DateTimeField,
        }
        labels = {
            "question_text": "",
            "pub_date": ""
        }
        widgets = {
            "question_text": forms.TextInput(
                {
                    "placeholder": "Your Question:",
                    "rows": 1,
                    "id": "QuestionTitle",
                }
            ),
            "pub_date": forms.DateTimeInput()
        }

        help_texts = {
            "pub_date": "Date published",
        }


class ChoiceForm(forms.Form):
    choice_text = forms.CharField(max_length=200, required=False, label="",
                                  widget=forms.TextInput(
                                      attrs={
                                          "placeholder": "",
                                          "size": 48,
                                      }
                                  ))
    votes = forms.IntegerField(min_value=0, initial=0, label="")
