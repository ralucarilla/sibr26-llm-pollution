from otree.api import *
import os

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'fat'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    prolific_completion_link = models.StringField()
    prolific_no_consent_link = models.StringField()

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

# PAGES
class p1_associations(Page):
    form_model = 'player'
    form_fields = ['association1','association2','association3','association4','association5']

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.vars['associations'] = {
            'association1': player.association1,
            'association2': player.association2,
            'association3': player.association3,
            'association4': player.association4,
            'association5': player.association5,
        }


page_sequence = [p1_associations]
