from otree.api import *
import random

doc = """
two-stage attention check system:
1. media source question (correct answer: reddit)
2. olive trees statement (correct answers: disagree/strongly disagree)
participants who fail both checks are redirected to prolific
"""

class C(BaseConstants):
    NAME_IN_URL = 'attention_check'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # media options for the first attention check
    MEDIA_OPTIONS = [
        'TikTok',
        'Newspaper',
        'Twitter',
        'Reddit',  # correct answer
        'YouTube',
        'Radio',
        'TV',
        'Facebook'
    ]
    CORRECT_ANSWER = 'Reddit'

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # first attention check (reddit)
    ac1 = models.StringField(initial=None)
    ac1_other = models.StringField(initial=None, blank=True)

    # second attention check (olive trees)
    ac2 = models.IntegerField(
        choices=[
            [1, 'Strongly disagree'],  # correct
            [2, 'Disagree'],  # correct
            [3, 'Agree'],  # incorrect
            [4, 'Strongly Agree'],  # incorrect
        ],
        label=""
    )
    
    ac1_failed = models.BooleanField(initial=False)
    ac2_failed = models.BooleanField(initial=False)
    acs_failed = models.BooleanField(initial=False)

class AttentionCheck1(Page):
    form_model = 'player'
    form_fields = ['ac1', 'ac1_other']
    
    @staticmethod
    def vars_for_template(player):
        return {
            'media_options': random.sample(C.MEDIA_OPTIONS, len(C.MEDIA_OPTIONS))
        }
    
    @staticmethod
    def error_message(player, values):
        if not values.get('ac1'):
            return 'Please answer this question.'
        if values.get('ac1') == 'Other' and not values.get('ac1_other'):
            return 'Please specify your answer.'
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.ac1_failed = player.ac1 != C.CORRECT_ANSWER

class AttentionCheck2(Page):
    """second attention check (olive trees)"""
    form_model = 'player'
    form_fields = ['ac2']
    
    @staticmethod
    def error_message(player, values):
        if not values.get('ac2'):
            return 'Please answer this question.'
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.ac2_failed = player.ac2 not in [1, 2]
        player.acs_failed = player.ac1_failed and player.ac2_failed

class FailedAttentionChecks(Page):
    """shown when participant fails both attention checks"""
    
    def is_displayed(player):
        return player.acs_failed
    
    def vars_for_template(player):
        return {
            'prolific_attention_link': player.session.config.get('prolific_attention_link'),
        }

page_sequence = [AttentionCheck1, AttentionCheck2, FailedAttentionChecks]