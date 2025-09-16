from otree.api import *

doc = """
Asks for consent and ends experiment if not given.
"""

class C(BaseConstants):
    NAME_IN_URL = 'consent'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    participation_consent = models.BooleanField(label="",
        choices=[
            [True, "Yes, I agree"],
            [False, "No, I don't agree"]
        ],
        widget=widgets.RadioSelect
    )
    data_consent = models.BooleanField(label="",
        choices=[
            [True, "Yes, I agree"],
            [False, "No, I don't agree"]
        ],
        widget=widgets.RadioSelect
    )

class p0_consent(Page):
    form_model = 'player'
    form_fields = ['participation_consent', 'data_consent']
    
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        if not player.participation_consent or not player.data_consent:
            player.participant.vars['consent_failed'] = True

class pEnd_no_consent(Page):
    @staticmethod
    def is_displayed(player):
        return player.participant.vars.get('consent_failed', False)
    
    def vars_for_template(player):
        return {
            'prolific_no_consent_link': player.session.config.get('prolific_no_consent_link'),
        }

page_sequence = [p0_consent, pEnd_no_consent]