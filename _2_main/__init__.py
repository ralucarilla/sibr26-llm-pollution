from otree.api import *
import os

class C(BaseConstants):
    NAME_IN_URL = 'fat'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    prolific_completion_link = models.StringField()
    prolific_no_consent_link = models.StringField()

def creating_session(subsession: Subsession):
    for field in ["prolific_completion_link", "prolific_no_consent_link"]:
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

    association1_timer = models.IntegerField(initial=0, blank=True)
    association2_timer = models.IntegerField(initial=0, blank=True)
    association3_timer = models.IntegerField(initial=0, blank=True)
    association4_timer = models.IntegerField(initial=0, blank=True)
    association5_timer = models.IntegerField(initial=0, blank=True)


class p1_associations(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        return [
            'association1','association2','association3','association4','association5',
            'association1_timer','association2_timer','association3_timer',
            'association4_timer','association5_timer'
        ]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(timing_storage_key=f"assoc_timing_{player.participant.code}_{player.round_number}")

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['associations'] = {
            'association1': player.association1,
            'association2': player.association2,
            'association3': player.association3,
            'association4': player.association4,
            'association5': player.association5,
        }
        player.participant.vars['association_timers'] = {
            'association1_timer': player.association1_timer,
            'association2_timer': player.association2_timer,
            'association3_timer': player.association3_timer,
            'association4_timer': player.association4_timer,
            'association5_timer': player.association5_timer,
        }

page_sequence = [p1_associations]
