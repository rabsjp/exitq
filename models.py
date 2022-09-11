from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv

author = 'Your name here'

doc = """
Survey exit
"""


class Constants(BaseConstants):
    name_in_url = 'exitq'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):

    why_accept = models.StringField(
        choices=[['To help other participants ', 'To help other participants '],
                 [' To increase my own earnings', ' To increase my own earnings'],
                 ['To ensure fair payoffs', 'To ensure fair payoffs'],
                 ['Other reason (specify bellow)', 'Other reason (specify bellow)']],
        label='What is the main reason for you to ACCEPT the proposal?',
        widget=widgets.RadioSelect,
    )

    other_accept = models.CharField(blank=True,label='Other reason for accepting')

    why_reject = models.StringField(
        choices=[['To help other participants ', 'To help other participants '], [' To increase my own earnings', ' To increase my own earnings'],
                 ['To ensure fair payoffs', 'To ensure fair payoffs'], ['Other reason (specify below)', 'Other reason (specify below)']],
        label='What is the main reason for you to REJECT the proposal?',
        widget=widgets.RadioSelect,
    )


    other_reject = models.CharField(blank=True,label='Other reason for rejecting')

    age = models.IntegerField(label='What is your age?', min=17, max=125)

    gender = models.StringField(
        choices=[['Man', 'Man'], ['Woman', 'Woman'], ['Non-binary/gender diverse', 'Non-binary/gender diverse']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )

    major = models.StringField(
        choices=[['Not a student', 'Not a student'], ['Science, technology, engineering and mathematics', 'Science, technology, engineering and mathematics'],
                 ['Social sciences', 'Social sciences'], ['Business, Finance', 'Business, Finance'], ['Art and humanities', 'Art and humanities']],
        label='What is your major?',
        widget=widgets.RadioSelect,
    )

    political = models.StringField(
        choices=[['Left', 'Left'], ['Center', 'Center'], ['Right', 'Right']],
        label='What is your political orientation?',
        widget=widgets.RadioSelect,
    )

    gpa = models.DecimalField(label='What is your GPA?', min=0.0, max=4.0, decimal_places=1, max_digits=2)


