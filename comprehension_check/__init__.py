from otree.api import *

doc = """
Attention checks to ensure participants are paying attention."""


class C(BaseConstants):
    NAME_IN_URL = 'instructions1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    attention_check_daylight = models.StringField(label="")
    attention_check_color = models.StringField(
        choices=[
            'Red',
            'Green',
            'Blue',
            'Yellow',
        ]
    )

    failed_both_attention_checks = models.BooleanField(initial=False)

class p2_attn(Page):
    form_model = 'player'
    form_fields = ['attention_check_daylight', 'attention_check_color']

    @staticmethod
    def before_next_page(player, timeout_happened):
        len_att_check_daylight = len(player.attention_check_daylight.split())
        # check if the player entered at least 10 words and if the selected color is 'Green'
        if len_att_check_daylight >= 10 and player.attention_check_color == 'Green':
            player.failed_both_attention_checks = False
        else:
            player.failed_both_attention_checks = True


class pEnd_attn(Page):
    def is_displayed(player):
        return player.failed_both_attention_checks
    
    def vars_for_template(player):
        return {
            'prolific_attention_link': player.session.config.get('prolific_attention_link'),
        }

page_sequence = [p2_attn, pEnd_attn]
