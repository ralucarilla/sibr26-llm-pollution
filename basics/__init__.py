from otree.api import *
import itertools

doc = """
Your app description
"""

# here, you should define any constants that you want to be able to flexibly change
# for instance, if you want to change the bonus payment in all parts of the experiment,
# you can define it here and use the variable name throughout your app
class C(BaseConstants):
    NAME_IN_URL = 'basics' # will appear in the URL; try to avoid informative names
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1 # should be 1 in most cases, but number of attempts for comp/attention checks
    BONUS_PAYMENT = 0.50  # replace with the bonus payment for the experiment
    CONDITIONS = ['disclosure', 'no_disclosure']  # example conditions

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

    # assigning participants to conditions
    def creating_session(subsession: Subsession):
        # assign conditions to players, aiming for a balanced distribution
        conditions = itertools.cycle(C.CONDITIONS)
        for player in subsession.get_players():
            player.condition = next(conditions)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, Results]
