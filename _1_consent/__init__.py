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
    consent = models.BooleanField(
        label="",
        choices=[
            [True, "I agree with this declaration of consent and the processing of my personal data"],
            [False, "I do not agree with this declaration of consent, the processing of my personal data and do not want to participate"],
        ],
        widget=widgets.RadioSelect,
    )


class p0_consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if not player.consent:
            player.participant.vars['consent_failed'] = True


class pEnd_no_consent(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.vars.get('consent_failed', False)

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'prolific_no_consent_link': player.session.config.get('prolific_no_consent_link'),
        }


page_sequence = [p0_consent, pEnd_no_consent]