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
    with open('exitq/exit_survey.csv') as questions_file:
        questions = list(csv.DictReader(questions_file))

    num_rounds = len(questions)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['questions'] = Constants.questions.copy()
            ## ALTERNATIVE DESIGN:
            ## to randomize the order of the questions, you could instead do:

            # import random
            # randomized_questions = random.sample(Constants.questions, len(Constants.questions))
            # self.session.vars['questions'] = randomized_questions

            ## and to randomize differently for each participant, you could use
            ## the random.sample technique, but assign into participant.vars
            ## instead of session.vars.

        for p in self.get_players():
            question_data = p.current_question()
            p.question_id = int(question_data['id'])
            p.question = question_data['question']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_id = models.IntegerField()
    question = models.StringField()
    submitted_answer = models.StringField()

    def submitted_answer_choices(self):
        qd = self.current_question()
        return [
            qd['choice1'],
            qd['choice2'],
            qd['choice3'],
            #qd['choice4'],
        ]

    def current_question(self):
        return self.session.vars['questions'][self.round_number - 1]

