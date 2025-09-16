from otree.api import *
import random

doc = """
exit questions about AI
"""

class C(BaseConstants):
    NAME_IN_URL = 'eqs'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    ai_trust = models.IntegerField(min=0, max=10)
    ai_risk = models.IntegerField(min=0, max=10)
    daily_ai_use = models.IntegerField(min=0, max=10)
    ai_expertise = models.IntegerField(min=0, max=10)
    ai_expertise_justification = models.LongStringField(blank=True, label="")


class p2_ai_trust(Page):
    form_model = 'player'
    form_fields = ['ai_trust']
    
    @staticmethod
    def error_message(player, values):
        if values.get('ai_trust') is None:
            return 'Please answer this question.'
        
class p3_ai_risk(Page):
    form_model = 'player'
    form_fields = ['ai_risk']
    
    @staticmethod
    def error_message(player, values):
        if values.get('ai_risk') is None:
            return 'Please answer this question.'
        
class p4_daily_ai_use(Page):
    form_model = 'player'
    form_fields = ['daily_ai_use']
    
    @staticmethod
    def error_message(player, values):
        if values.get('daily_ai_use') is None:
            return 'Please answer this question.'
        
class p5_ai_expertise(Page):
    form_model = 'player'
    form_fields = ['ai_expertise']
    
    @staticmethod
    def error_message(player, values):
        if values.get('ai_expertise') is None:
            return 'Please answer this question.'
        
class p6_ai_expertise_justification(Page):
    form_model = 'player'
    form_fields = ['ai_expertise_justification']
    
    @staticmethod
    def error_message(player, values):
        if values.get('ai_expertise_justification') is None:
            return 'Please answer this question.'


page_sequence = [p2_ai_trust, p3_ai_risk, p4_daily_ai_use, p5_ai_expertise, p6_ai_expertise_justification]