from otree.api import *
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'secure'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    media = models.StringField(initial=None)
    media_other = models.StringField(initial=None, blank=True)
    prolific_id = models.StringField(label='')
    check = models.StringField(blank=True)
    feedback = models.LongStringField(blank=True)
    bot_check = models.StringField(initial=None)


#### bot protection options ####
# 1. Prolific ID + honeypot
class HoneypotProlificID(Page):
    form_model = 'player'
    form_fields = ['prolific_id', 'check']

    @staticmethod
    def vars_for_template(player: Player):
        return dict()
    
    @staticmethod
    def error_message(player, values):
        if values['prolific_id'] == '':
            return 'Please answer this question.'

# 2. attention check + honeypot
class HoneypotAttentionCheck(Page):
    form_model = 'player'
    form_fields = ['media', 'media_other']

    OPTIONS = [
        'TikTok',
        'Newspaper',
        'Twitter',
        'Reddit',
        'YouTube',
        'Radio',
        'TV',
        'Facebook'
    ]

    CORRECT_ANSWER = 'TikTok'

    @staticmethod
    def vars_for_template(self):
        return dict(media_options=random.sample(HoneypotAttentionCheck.OPTIONS, len(HoneypotAttentionCheck.OPTIONS)))
    
    @staticmethod
    def error_message(player, values):
        if values['media'] == '':
            return 'Please answer this question.'
        if values['media_other'] == '' and values['media'] == "Other":
            return 'Please answer this question.'

# 3. open-ended question + honeypot
class HoneypotFeedback(Page):
    form_model = 'player'
    form_fields = ['feedback']

    @staticmethod
    def vars_for_template(player: Player):
        return dict()
    
    @staticmethod
    def error_message(player, values):
        if values['feedback'] == '':
            return 'Please answer this question.'
        
class HoneypotBreton(Page):
    form_model = 'player'
    form_fields = ['bot_check']

    @staticmethod
    def vars_for_template(player: Player):
        return dict()
    
    @staticmethod
    def error_message(player, values):
        if values['bot_check'] == '':
            return 'Please answer this question.'

class Thanks(Page):
    form_model = 'player'
    form_fields = []

    @staticmethod
    def vars_for_template(player: Player):
        return dict()

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        pass
        
page_sequence = [HoneypotProlificID, HoneypotAttentionCheck, HoneypotFeedback,
                 HoneypotBreton, Thanks]
