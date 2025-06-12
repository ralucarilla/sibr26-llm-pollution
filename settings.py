from os import environ

SESSION_CONFIGS = [
    dict(
         name='otree_template',
         display_name="Otree Starter Pack",
         num_demo_participants=12,
         app_sequence=['consent', 'attention_check','basics', 'bot_protection'],
         # set up prolific paths for completion, attention checks, etc.
         # replace YOUR_CODE with your actual Prolific code for each path
         prolific_completion_link='https://app.prolific.com/submissions/complete?cc=YOUR_CODE',
         prolific_attention_link='https://app.prolific.com/submissions/complete?cc=YOUR_CODE',
         prolific_no_consent_link='https://app.prolific.com/submissions/complete?cc=YOUR_CODE',
         prolific_comprehension_link='https://app.prolific.com/submissions/complete?cc=YOUR_CODE',
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, # if USE_POINTS is True, this is the conversion rate
    participation_fee=0.00, # replace with base fee for participating in the experiment
    doc=""
)

# for deployment, initialize rooms:
ROOMS = [dict(name='testing', display_name='Testing'), ]

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

LANGUAGE_CODE = 'en' # ISO-639 code

REAL_WORLD_CURRENCY_CODE = 'USD' # e.g. EUR, GBP, CNY, JPY
USE_POINTS = False # if True, points are used instead of real world currency

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '6393255297089'
