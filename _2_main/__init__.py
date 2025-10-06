from otree.api import *
import itertools
import requests
import os

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'fat'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    RECAPTCHA_SECRET_KEY = os.environ.get('RECAPTCHA_SECRET_KEY')

class Subsession(BaseSubsession):
    prolific_completion_link = models.StringField()
    prolific_attention_link = models.StringField()
    prolific_no_consent_link = models.StringField()
    prolific_comprehension_link = models.StringField()

def creating_session(subsession):
    """
    This function is called when the session is created.
    You can use it to assign participants to different conditions, to set up Prolific
    completion paths.
    """
    expected_fields = [
        "prolific_completion_link",
        "prolific_attention_link",
        "prolific_no_consent_link",
        "prolific_comprehension_link"
    ]
    
    for field in expected_fields:
        if field not in subsession.session.config:
            raise Exception(f"You must set a {field} in settings.py")
        setattr(subsession, field, subsession.session.config[field])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    association1 = models.StringField(label="", blank=True)
    association2 = models.StringField(label="", blank=True)
    association3 = models.StringField(label="", blank=True)
    association4 = models.StringField(label="", blank=True)
    association5 = models.StringField(label="", blank=True)
    recaptcha_score = models.FloatField(blank=True)
    is_bot = models.BooleanField(blank=True)
    page_load_time = models.FloatField(blank=True)
    total_time_on_page = models.FloatField(blank=True)


# PAGES
class p1_associations(Page):
    form_model = 'player'
    form_fields = ['association1', 'association2', 'association3', 'association4', 'association5']

    def live_method(player, data):
        if 'page_load_time' in data:
            player.page_load_time = data['page_load_time']
            return {player.id_in_group: {'received': True}}
        
        if 'total_time_on_page' in data:
            player.total_time_on_page = data['total_time_on_page']
            return {player.id_in_group: {'time_logged': True}}

        if 'recaptcha_response' in data:
            verification_data = {
                'secret': C.RECAPTCHA_SECRET_KEY,
                'response': data['recaptcha_response']
            }
            
            try:
                response = requests.post(
                    'https://www.google.com/recaptcha/api/siteverify', 
                    data=verification_data
                )
                result = response.json()
                
                player.recaptcha_score = result.get('score')
                player.is_bot = result.get('score', 1) < 0.5 
                
                if player.is_bot:
                    print(f"Potential bot detected: Player {player.id_in_group}, Score: {player.recaptcha_score}")
                
                return {player.id_in_group: {'recaptcha_verified': True, 'is_bot': player.is_bot}}
            
            except Exception as e:
                print(f"reCAPTCHA verification error: {e}")
                return {player.id_in_group: {'error': str(e)}}
        
        return {player.id_in_group: {'received': True}}

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.vars['associations'] = {
            'association1': player.association1,
            'association2': player.association2,
            'association3': player.association3,
            'association4': player.association4,
            'association5': player.association5
        }


page_sequence = [p1_associations]
