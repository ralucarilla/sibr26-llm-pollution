from otree.api import *
import random

doc = """

"""

class C(BaseConstants):
    NAME_IN_URL = 'demographics'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    age = models.IntegerField(label="How old are you?", min=18, max=100)
    gender = models.StringField(label="With which gender do you identify?", widget=widgets.RadioSelect,
        choices=[
            ['female', 'Female'],
            ['male', 'Male'],
            ['non_binary', 'Non-binary'],
            ['prefer_not_to_state', 'Prefer not to state'],
            ['self_describe', 'Prefer to self-describe'],
        ]
    )
    gender_self_describe = models.StringField(label="",blank=True)
    illusion_response = models.StringField(label="Is this the head of a duck or a rabbit?")


class p7_age(Page):
    form_model = 'player'
    form_fields = ['age']

class p8_gender(Page):
    form_model = 'player'
    form_fields = ['gender', 'gender_self_describe']

    @staticmethod
    def error_message(player, values):
        if values.get('gender') == 'self_describe' and not values.get('gender_self_describe'):
            return 'Please provide more details.'
        
class p0_illusion(Page):
    form_model = 'player'
    form_fields = ["illusion_response"]

    @staticmethod
    def error_message(player, values):
        if values['illusion_response'] is None:
            return 'Please answer the question.'

page_sequence = [p7_age, p8_gender, p0_illusion]