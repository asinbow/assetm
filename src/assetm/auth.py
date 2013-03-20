
from django.contrib.auth.models import User

# username => (challenge, expiration)
challenges = {

}


class UserBackend:
    def authenticate(self, username=None, password=None):
        return User.objects.get(pk=1)
        #return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
