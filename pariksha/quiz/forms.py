# from __future__ import absolute_import
# from django import forms
# from quiz.models import Question
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout
# from crispy_forms.bootstrap import InlineCheckboxes
#
# form_fields = []
# class QuestionResponseForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         choices_set = Question.objects.get(pk=1).choices.all()
#         field_names = ['choice'+str(i) for i in range(1, len(choices_set)+1)]
#         fields = field_names
#         form_fields = fields
#
#     def __init__(self, *args, **kwargs):
#         super(QuestionResponseForm, self).__init__(*args, **kwargs)
#
#         self.helper = FormHelper
#         self.helper.layout = Layout(
#             [InlineCheckboxes(form_field) for form_field in form_fields ]
#         )
