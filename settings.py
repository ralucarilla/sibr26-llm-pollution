from os import environ

SESSION_CONFIGS = [
    dict(
         name='ai_fat_2025',
         display_name="AI FAT 2025",
         num_demo_participants=12,
         app_sequence=['_1_consent', '_2_main','_3_exit_questions', '_4_demographics', '_5_feedback'],
         prolific_completion_link='https://app.prolific.com/submissions/complete?cc=C1BZPBSV',
         prolific_no_consent_link='https://app.prolific.com/submissions/complete?cc=C3YAIOZN',
         recaptcha_site_key=environ.get('RECAPTCHA_SITE_KEY'),
         recaptcha_secret_key=environ.get('RECAPTCHA_SECRET_KEY'),
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00, # replace with base fee for participating in the experiment
    doc=""
)

# for deployment, initialize rooms:
ROOMS = [dict(name='ai_fat_2025', display_name='AI FAT 2025'), ]

PARTICIPANT_FIELDS = ['associations']
SESSION_FIELDS = []

LANGUAGE_CODE = 'en' # ISO-639 code

REAL_WORLD_CURRENCY_CODE = 'USD' # e.g. EUR, GBP, CNY, JPY
USE_POINTS = False # if True, points are used instead of real world currency

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '6393255297089'
