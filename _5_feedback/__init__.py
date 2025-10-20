from otree.api import *
import requests

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
    include_data = models.StringField(widget=widgets.RadioSelect, label="",
        choices=[['yes', 'Yes'], ['no', 'No (please provide an explanation)']]
    )
    include_data_justification = models.StringField(blank=True, label="")

    ai_use_survey = models.StringField(widget=widgets.RadioSelect, label="",
        choices=[['yes', 'Yes, I have used AI.'], ['no', 'No, I have not used AI.']]
    )
    ai_use_details = models.LongStringField(blank=True, label="")

    feedback = models.LongStringField(label="")
    check = models.StringField(blank=True)
    prolific_id = models.StringField(label='')
    recaptcha_token = models.StringField(blank=True)
    recaptcha_score = models.FloatField(blank=True)
    participant_metrics_json = models.LongStringField(blank=True, label="")


class p9_srsi_use_me(Page):
    form_model = 'player'
    form_fields = ['include_data', 'include_data_justification']

    @staticmethod
    def error_message(player, values):
        if not values.get('include_data'):
            return 'Please answer this question.'
        if values.get('include_data') == 'no' and not values.get('include_data_justification'):
            return 'Please specify your answer.'


class p10_ai_use(Page):
    form_model = 'player'
    form_fields = ['ai_use_survey', 'ai_use_details']

    @staticmethod
    def error_message(player, values):
        if not values.get('ai_use_survey'):
            return 'Please answer this question.'
        if values.get('ai_use_survey') == 'yes' and not (values.get('ai_use_details') or '').strip():
            return 'Please provide a short description of how you used AI.'


class p11_feedback(Page):
    form_model = 'player'
    form_fields = ['feedback', 'participant_metrics_json']

    @staticmethod
    def error_message(player, values):
        if values['feedback'] == '':
            return 'Please answer this question.'


class p12_prolific_id(Page):
    form_model = 'player'
    form_fields = ['prolific_id', 'check', 'recaptcha_token']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        token = player.recaptcha_token
        if not token:
            player.recaptcha_score = None
            return
        secret = player.session.config.get('recaptcha_secret_key')
        try:
            resp = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                data={'secret': secret, 'response': token},
                timeout=5
            ).json()
            player.recaptcha_score = float(resp.get('score', 0) or 5)
        except Exception as e:
            print('[reCAPTCHA] verify error:', e)
            player.recaptcha_score = None

class p13_thanks(Page):
    @staticmethod
    def is_displayed(player):
        return True

page_sequence = [p9_srsi_use_me, p10_ai_use, p11_feedback, p12_prolific_id, p13_thanks]