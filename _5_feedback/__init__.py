from otree.api import *
import random

doc = """

"""

class C(BaseConstants):
    NAME_IN_URL = 'end'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    srsi_use_me = models.StringField(widget=widgets.RadioSelect, label="",
        choices=[
            ['yes', 'Yes'],
            ['no', 'No (please provide an explanation)'],
        ]
    )
    srsi_use_me_justification = models.StringField(blank=True, label="")
    ai_use = models.StringField(widget=widgets.RadioSelect, label="",
        choices=[
        ['yes', 'Yes, I have used AI.'],
        ['no', 'No, I have not used AI.']
        ])
    feedback = models.LongStringField(blank=True, label="")
    check = models.StringField(blank=True)
    prolific_id = models.StringField(label='')
    
    
class p9_srsi_use_me(Page):
    form_model = 'player'
    form_fields = ['srsi_use_me', 'srsi_use_me_justification']

    @staticmethod
    def error_message(player, values):
        if not values.get('srsi_use_me'):
            return 'Please answer this question.'
        if values.get('srsi_use_me') == 'no' and not values.get('srsi_use_me_justification'):
            return 'Please specify your answer.'
    

class p10_ai_use(Page):
    form_model = 'player'
    form_fields = ['ai_use']

    @staticmethod
    def error_message(player, values):
        if not values.get('ai_use'):
            return 'Please answer this question.'
    

class p11_feedback(Page):
    form_model = 'player'
    form_fields = ['feedback']

    @staticmethod
    def vars_for_template(player: Player):
        return dict()
    
    @staticmethod
    def error_message(player, values):
        if values['feedback'] == '':
            return 'Please answer this question.'


class p12_prolific_id(Page):
    form_model = 'player'
    form_fields = ['prolific_id', 'check']

    @staticmethod
    def vars_for_template(player: Player):
        return dict()
    
    @staticmethod
    def error_message(player, values):
        if values['prolific_id'] == '':
            return 'Please answer this question.'
        
class p13_thanks(Page):
    @staticmethod
    def is_displayed(player):
        return True

page_sequence = [p9_srsi_use_me, p10_ai_use, p11_feedback, p12_prolific_id, p13_thanks]