SITE_ID = 1

# 利用するユーザモデル
AUTH_USER_MODEL = 'orders.CustomUser'
# ログイン用アクション
LOGIN_URL = 'account_login'
# ログイン後に遷移するアクション
LOGIN_REDIRECT_URL = 'orders:dashboard'
# ログアウト後に遷移するアクション
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# 認証に利用するフィールド
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False

# メールを認証する
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = ""

ACCOUNT_LOGOUT_ON_GET = True

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

DEFUALT_FROM_EMAIL = "admin@example.com"

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
