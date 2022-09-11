from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Survey(Page):

    form_model = 'player'
    form_fields = ['why_accept','other_accept','why_reject','other_reject','age', 'gender','major','gpa','political']

page_sequence = [
    Survey,
]
