#####################################
########## Django settings ##########
#####################################
# See <https://docs.djangoproject.com/en/3.2/ref/settings/>
# for more info and help. If you are stuck, you can try Googling about
# Django - many of these settings below have external documentation about them.
#
# The settings listed here are of special interest in configuring the site.

# SECURITY WARNING: keep the secret key used in production secret!
# You may use this command to generate a key:
# python3 -c 'from django.core.management.utils import get_random_secret_key;print(get_random_secret_key())'
SECRET_KEY = 'This key is not very secure and you should change it.'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Change to False once you are done with runserver testing.

# Uncomment and set to the domain names this site is intended to serve.
# You must do this once you set DEBUG to False.
#ALLOWED_HOSTS = ['k23oj.io.vn']

CSRF_TRUSTED_ORIGINS = [
    'http://example.com',
    'https://example.com',
]

# Optional apps that DMOJ can make use of.
INSTALLED_APPS += (
    'discord_integration',
    'storages',
)

# Caching. You can use memcached or redis instead.
# Documentation: <https://docs.djangoproject.com/en/3.2/topics/cache/>
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}

# Your database credentials. Only MySQL is supported by DMOJ.
# Documentation: <https://docs.djangoproject.com/en/3.2/ref/databases/>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dmoj',
        'USER': 'dmoj',
        'PASSWORD': '<mariadb user password>',
        'HOST': '127.0.0.1',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'sql_mode': 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION',
        },
    },
}

# Sessions.
# Documentation: <https://docs.djangoproject.com/en/3.2/topics/http/sessions/>
#SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Internationalization.
# Documentation: <https://docs.djangoproject.com/en/3.2/topics/i18n/>
LANGUAGE_CODE = 'vi'
DEFAULT_USER_TIME_ZONE = 'Asia/Ho_Chi_Minh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

## django-compressor settings, for speeding up page load times by minifying CSS and JavaScript files.
# Documentation: <https://django-compressor.readthedocs.io/en/latest/>
COMPRESS_OUTPUT_DIR = 'cache'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'
STATICFILES_FINDERS += ('compressor.finders.CompressorFinder',)


#########################################
########## Email configuration ##########
#########################################
# See <https://docs.djangoproject.com/en/3.2/topics/email/#email-backends>
# for more documentation. You should follow the information there to define
# your email settings.

# Use this if you are just testing.
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# The following block is included for your convenience, if you want
# to use Gmail.
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = '<your account>@gmail.com'
#EMAIL_HOST_PASSWORD = '<your password>'
#EMAIL_PORT = 587

# To use Mailgun, uncomment this block.
# You will need to run `pip install django-mailgun-mime` to get `MailgunBackend`.
#EMAIL_BACKEND = 'django_mailgun_mime.backends.MailgunMIMEBackend'
#MAILGUN_API_KEY = '<your Mailgun access key>'
#MAILGUN_DOMAIN_NAME = '<your Mailgun domain>'

# You can also use SendGrid, with `pip install sendgrid-django`.
#EMAIL_BACKEND = 'sgbackend.SendGridBackend'
#SENDGRID_API_KEY = '<Your SendGrid API Key>'

# The DMOJ site is able to notify administrators of errors via email,
# if configured as shown below.

# A tuple of (name, email) pairs that specifies those who will be mailed
# when the server experiences an error when DEBUG = False.
ADMINS = (
    ('Your Name', 'your.email@example.com'),
)

# The sender for the aforementioned emails.
SERVER_EMAIL = 'online_judge@k23oj.io.vn'


################################################
########## Static files configuration ##########
################################################
# See <https://docs.djangoproject.com/en/3.2/howto/static-files/>.

# Change this to somewhere more permanent, especially if you are using a
# webserver to serve the static files. This is the directory where all the
# static files DMOJ uses will be collected to.
# You must configure your webserver to serve this directory as /static/ in production.
STATIC_ROOT = '/tmp/static'

# URL to access static files.
STATIC_URL = '/static/'

# Explicitly define compressor root to avoid relying on fallback to STATIC_ROOT.
COMPRESS_ROOT = STATIC_ROOT

# Uncomment to use hashed filenames with the cache framework.
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


############################################
########## DMOJ-specific settings ##########
############################################

## DMOJ site display settings.
SITE_NAME = 'K23OJ'
SITE_FULL_URL = 'https://k23oj.io.vn'
SITE_LONG_NAME = 'K23OJ: ITK23 Online Judge'
SITE_ADMIN_EMAIL = 'online_judge@k23oj.io.vn'
TERMS_OF_SERVICE_URL = None

## Media files settings.
# This is the directory where all the media files are stored.
# Change this to somewhere more permanent.
# You must configure your webserver to serve this directory in production.
MEDIA_ROOT = '/tmp/media'

## Problem data settings.
# This is the directory where all the problem data are stored.
# Change this to somewhere more permanent.
DMOJ_PROBLEM_DATA_ROOT = '/tmp/problem_data/'

## Bridge controls.
# The judge connection address and port; where the judges will connect to the site.
# You should change this to something your judges can actually connect to
# (e.g., a port that is unused and unblocked by a firewall).
BRIDGED_JUDGE_ADDRESS = [('localhost', 9999)]

# The bridged daemon bind address and port to communicate with the site.
#BRIDGED_DJANGO_ADDRESS = [('localhost', 9998)]

## DMOJ features.
# Set to True to enable full-text searching for problems.
ENABLE_FTS = False

# Set of email providers to ban when a user registers, e.g., {'throwawaymail.com'}.
BAD_MAIL_PROVIDERS = set()

# The number of submissions that a staff user can rejudge at once without
# requiring the permission 'Rejudge a lot of submissions'.
# Uncomment to change the submission limit.
#DMOJ_SUBMISSIONS_REJUDGE_LIMIT = 10

# Event server.
# Uncomment to enable live updating.
EVENT_DAEMON_USE = True

# Uncomment this section to use websocket/daemon.js included in the site.
#EVENT_DAEMON_POST = '<ws:// URL to post to>'

# If you are using the defaults from the guide, it is this:
EVENT_DAEMON_POST = 'ws://127.0.0.1:15101/'

# These are the publicly accessed interface configurations.
# They should match those used by the script.
#EVENT_DAEMON_GET = '<public ws:// URL for clients>'
#EVENT_DAEMON_GET_SSL = '<public wss:// URL for clients>'
#EVENT_DAEMON_POLL = '<public URL to access the HTTP long polling of event server>'
# i.e. the path to /channels/ exposed by the daemon, through whatever proxy setup you have.

# Using our standard nginx configuration, these should be.
EVENT_DAEMON_GET = 'ws://k23oj.io.vn/event/'
EVENT_DAEMON_GET_SSL = 'wss://k23oj.io.vn/event/' # Optional
EVENT_DAEMON_POLL = 'ws://k23oj.io.vn/poll/'
# EVENT_DAEMON_GET = 'ws://k23oj.io.vn/event/'
# EVENT_DAEMON_GET_SSL = 'wss://k23oj.io.vn/event/'  # Optional
# EVENT_DAEMON_POLL = '/channels/'

# If you would like to use the AMQP-based event server from <https://github.com/DMOJ/event-server>,
# uncomment this section instead. This is more involved, and recommended to be done
# only after you have a working event server.
#EVENT_DAEMON_AMQP = '<amqp:// URL to connect to, including username and password>'
#EVENT_DAEMON_AMQP_EXCHANGE = '<AMQP exchange to use>'

## Celery
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'

## CDN control.
# Base URL for a copy of Ace editor.
# Should contain ace.js, along with mode-*.js.
ACE_URL = '//cdnjs.cloudflare.com/ajax/libs/ace/1.2.3/'
JQUERY_JS = '//cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js'
SELECT2_JS_URL = '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/js/select2.min.js'
SELECT2_CSS_URL = '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/css/select2.min.css'

# A map of Earth in equirectangular projection, for timezone selection.
# Please try not to hotlink this poor site.
TIMEZONE_MAP = 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Blue_Marble_2002.png/1024px-Blue_Marble_2002.png'

## Camo (https://github.com/atmos/camo) usage.
#DMOJ_CAMO_URL = '<URL to your camo install>'
#DMOJ_CAMO_KEY = '<The CAMO_KEY environmental variable you used>'

# Domains to exclude from being camo'd.
#DMOJ_CAMO_EXCLUDE = ('https://dmoj.ml', 'https://dmoj.ca')

# Set to True to use https when dealing with protocol-relative URLs.
# See <https://www.paulirish.com/2010/the-protocol-relative-url/> for what they are.
#DMOJ_CAMO_HTTPS = False

# HTTPS level. Affects <link rel='canonical'> elements generated.
# Set to 0 to make http URLs canonical.
# Set to 1 to make the currently used protocol canonical.
# Set to 2 to make https URLs canonical.
#DMOJ_HTTPS = 0

## PDF rendering settings.

# Enable PDF generation.
#DMOJ_PDF_PDFOID_URL = '<URL to your pdfoid install>.'

# Directory to cache the PDF.
#DMOJ_PDF_PROBLEM_CACHE = '/home/dmoj-uwsgi/pdfcache'

# Path to use for nginx's X-Accel-Redirect feature.
# Should be an internal location mapped to the above directory.
#DMOJ_PDF_PROBLEM_INTERNAL = '/pdfcache'

## Data download settings.
# Uncomment to allow users to download their data.
DMOJ_USER_DATA_DOWNLOAD = True

# Directory to cache user data downloads.
# It is the administrator's responsibility to clean up old files.
DMOJ_USER_DATA_CACHE = '/home/dmoj-uwsgi/userdatacache'

# Path to use for nginx's X-Accel-Redirect feature.
# Should be an internal location mapped to the above directory.
#DMOJ_USER_DATA_INTERNAL = '/userdatacache'

# How often a user can download their data.
#DMOJ_USER_DATA_DOWNLOAD_RATELIMIT = datetime.timedelta(days=1)

# Uncomment to allow contest authors to download contest data
DMOJ_CONTEST_DATA_DOWNLOAD = True

# Directory to cache contest data downloads.
# It is the administrator's responsibility to clean up old files.
DMOJ_CONTEST_DATA_CACHE = '/home/dmoj-uwsgi/contestdatacache'

# Path to use for nginx's X-Accel-Redirect feature.
# Should be an internal location mapped to the above directory.
#DMOJ_CONTEST_DATA_INTERNAL = '/contestdatacache'

# How often contest data can be exported.
# This applies per contest, not per user.
#DMOJ_CONTEST_DATA_DOWNLOAD_RATELIMIT = datetime.timedelta(days=1)

## ======== Logging Settings ========
# Documentation: https://docs.djangoproject.com/en/3.2/ref/settings/#logging
#                https://docs.python.org/3/library/logging.config.html#configuration-dictionary-schema
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'file': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    'handlers': {
        # You may use this handler as an example for logging to other files.
        'bridge': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/home/huythedev/bridge.log',
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'file',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'dmoj.throttle_mail.ThrottledEmailHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'file',
        },
    },
    'loggers': {
        # Site 500 error mails.
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Judging logs as received by bridged.
        'judge.bridge': {
            'handlers': ['bridge', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        # Catch all logs to stderr.
        '': {
            'handlers': ['console'],
        },
        # Other loggers of interest. Configure at will.
        #  - judge.user: logs naughty user behaviours.
        #  - judge.problem.pdf: PDF generation log.
        #  - judge.html: HTML parsing errors when processing problem statements etc.
        #  - judge.mail.activate: logs for the reply to activate feature.
        #  - event_socket_server
    },
}

## ======== Integration Settings ========
## Python Social Auth
# Documentation: https://python-social-auth.readthedocs.io/en/latest/
# You can define these to enable authentication through the following services.
#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''
#SOCIAL_AUTH_FACEBOOK_KEY = ''
#SOCIAL_AUTH_FACEBOOK_SECRET = ''
#SOCIAL_AUTH_GITHUB_SECURE_KEY = ''
#SOCIAL_AUTH_GITHUB_SECURE_SECRET = ''

## ======== Custom Configuration ========
# You may add whatever Django configuration you would like here.
# Do try to keep it separate so you can quickly patch in new settings.

DMOJ_CANONICAL = 'k23oj.io.vn'
DMOJ_REQUIRE_STAFF_2FA = False

DMOJ_PP_STEP = 0.995
DMOJ_PP_ENTRIES = 2000

VNOJ_ORG_PP_STEP = 0.995
VNOJ_ORG_PP_ENTRIES = 2000

DATA_UPLOAD_MAX_NUMBER_FIELDS = int(1e6)
DATA_UPLOAD_MAX_MEMORY_SIZE = None
FILE_UPLOAD_MAX_MEMORY_SIZE = None

##############################################
# MATHOID CONFIGURATION (DISABLED: NO SERVER)
##############################################

MATHOID_URL = False
MATHOID_GZIP = False
MATHOID_MML_CACHE = None
MATHOID_CSS_CACHE = 'default'
MATHOID_DEFAULT_TYPE = 'auto'
MATHOID_MML_CACHE_TTL = 86400

# Mathoid local cache directory
MATHOID_CACHE_ROOT = '/tmp/.cache/mathoid'
MATHOID_CACHE_URL = False


##############################################
# TEXOID CONFIGURATION (ENABLE SERVER-SIDE LATEX)
##############################################

TEXOID_URL = 'http://localhost:12346/'
TEXOID_GZIP = False
TEXOID_META_CACHE = 'default'
TEXOID_META_CACHE_TTL = 86400

# Texoid local cache directory (REQUIRED)
TEXOID_CACHE_ROOT = '/tmp/.cache/texoid'
TEXOID_CACHE_URL = False


##############################################
# ENABLE LATEX PROCESSOR IN DMOJ
##############################################

RENDER_LATEX = True

POST_PROCESSORS = {
    'latex': 'dmoj.post_processors.latex',
}

############################################
# Cloudflare R2 – MEDIA
############################################

# STORAGES = {
#     'default': {
#         'BACKEND': 'storages.backends.s3.S3Storage',
#     },
#     'staticfiles': {
#         'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage',
#     },
# }

# AWS_ACCESS_KEY_ID = 'your aws access key ID'
# AWS_SECRET_ACCESS_KEY = 'your aws access key'
# AWS_STORAGE_BUCKET_NAME = 'your aws bucket name'

# AWS_S3_ENDPOINT_URL = 'your aws endpoint url'
# AWS_S3_REGION_NAME = 'auto'
# AWS_S3_SIGNATURE_VERSION = 's3v4'

# AWS_DEFAULT_ACL = None
# AWS_QUERYSTRING_AUTH = False

# Prefix inside bucket
# AWS_LOCATION = 'media'

# MEDIA_URL = 'https://cdn.k23oj.io.vn/media/'
# PDF_STATEMENT_UPLOAD_URL_PREFIX = 'https://cdn.k23oj.io.vn/media/pdf/'
# VNOJ_ENABLE_API = True

REGISTRATION_OPEN = True

# reCAPTCHA v3 for registration anti-spam.
# Get keys from https://www.google.com/recaptcha/admin and use score-based v3 keys.
# RECAPTCHA_V3_SITE_KEY = 'Recaptcha site key'
# RECAPTCHA_V3_SECRET_KEY = 'Recaptcha secret key'
# RECAPTCHA_V3_MIN_SCORE = 0.7

# Use recaptcha.net when browsers cannot reach google.com reCAPTCHA endpoints.
RECAPTCHA_V3_API_DOMAIN = 'www.recaptcha.net'
FILE_UPLOAD_TEMP_DIR = None
# Disk workspace for AutoProblem's uploaded package and staged testcase ZIPs.
# Set this to a directory with enough free space; it must not be a small /tmp tmpfs.
# AUTOPROBLEM_TEMP_DIR = '/home/huythedev/media/upload_tmp'
AUTOPROBLEM_UPLOAD_DISK_MULTIPLIER = 2.15
AUTOPROBLEM_UPLOAD_DISK_RESERVE_BYTES = 1024 * 1024 * 1024
AUTOPROBLEM_MAX_CONCURRENCY = 10
