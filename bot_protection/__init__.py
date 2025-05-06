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
    riddle1 = models.StringField(initial=None)
    riddle2 = models.StringField(initial=None)
    riddle3 = models.StringField(initial=None)
    riddle4 = models.StringField(initial=None)
    riddle5 = models.StringField(initial=None)
    riddle6 = models.StringField(initial=None)
    consistency1 = models.StringField(initial=None, label='')
    consistency2 = models.StringField(initial=None, label='')


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

# 4. riddles
class Riddle1(Page):
    form_model = 'player'
    form_fields = ['riddle1']

    @staticmethod
    def vars_for_template(player: Player):
        return dict()
    
    @staticmethod
    def error_message(player, values):
        if values['riddle1'] == '':
            return 'Please answer this question.'

class Riddle2(Page):
    form_model = 'player'
    form_fields = ['riddle2']

    @staticmethod
    def vars_for_template(player: Player):
        return dict()
    
    @staticmethod
    def error_message(player, values):
        if values['riddle2'] == '':
            return 'Please answer this question.'
        
class Riddle3(Page):
    form_model = 'player'
    form_fields = ['riddle3']

    @staticmethod
    def vars_for_template(player: Player):
        return dict()
    
    @staticmethod
    def error_message(player, values):
        if values['riddle3'] == '':
            return 'Please answer this question.'

class Riddle4(Page):
    form_model = 'player'
    form_fields = ['riddle4']

    @staticmethod
    def vars_for_template(player: Player):
        return dict()
    
    @staticmethod
    def error_message(player, values):
        if values['riddle4'] == '':
            return 'Please answer this question.'
        
class Riddle5(Page):
    form_model = 'player'
    form_fields = ['riddle5']

    @staticmethod
    def vars_for_template(player: Player):
        return dict()
    
    @staticmethod
    def error_message(player, values):
        if values['riddle5'] == '':
            return 'Please answer this question.'
        
class Riddle6(Page):
    form_model = 'player'
    form_fields = ['riddle6']

    @staticmethod
    def vars_for_template(player: Player):
        return dict()
    
    @staticmethod
    def error_message(player, values):
        if values['riddle6'] == '':
            return 'Please answer this question.'

# 5. consistency check
class Age(Page):
    form_model = 'player'
    form_fields = ['consistency1']

    @staticmethod
    def vars_for_template(player: Player):
        return dict()
    
    @staticmethod
    def error_message(player, values):
        if values['consistency1'] == '':
            return 'Please answer this question.'
        
class Demographics(Page):
    form_model = 'player'
    form_fields = ['consistency2']

    @staticmethod
    def vars_for_template(player: Player):
        return dict()
    
    @staticmethod
    def error_message(player, values):
        if values['consistency2'] == '':
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
        
page_sequence = [Age, HoneypotProlificID, HoneypotAttentionCheck,
                Riddle1, Riddle2, Riddle3, Riddle4,
                Riddle5, Riddle6, HoneypotFeedback, Demographics, Thanks]
