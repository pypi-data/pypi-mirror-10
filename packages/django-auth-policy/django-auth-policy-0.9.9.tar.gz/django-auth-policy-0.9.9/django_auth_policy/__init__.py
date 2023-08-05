default_app_config = 'django_auth_policy.apps.DjangoAuthPolicyConfig'


class BasePolicy(object):
    def __init__(self, **kwargs):
        """ Policy configuration happens at init
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
