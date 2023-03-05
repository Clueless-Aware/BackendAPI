from dj_rest_auth.forms import AllAuthPasswordResetForm
from django.contrib.sites.shortcuts import get_current_site
from allauth.account.forms import default_token_generator
from allauth.account.adapter import get_adapter
from allauth.account.utils import user_pk_to_url_str

class CustomResetForm(AllAuthPasswordResetForm):
    def save(self, request, **kwargs):
        current_site = get_current_site(request)
        email = self.cleaned_data['email']
        token_generator = kwargs.get('token_generator', default_token_generator)

        for user in self.users:

            temp_key = token_generator.make_token(user)
            uid = user_pk_to_url_str(user)

            context = {
                'current_site': current_site,
                'user': user,
                'key': temp_key,
                'uid': uid,
            }
            get_adapter(request).send_mail(
                'account/email/password_reset_key', email, context
            )
        return self.cleaned_data['email']