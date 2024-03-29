from dj_rest_auth.serializers import PasswordResetSerializer

from .forms import CustomResetForm


class CustomPasswordResetSerializer(PasswordResetSerializer):
    @property
    def password_reset_form_class(self):
        return CustomResetForm

    def validate_email(self, value):
        return super().validate_email(value)

    def get_email_options(self):
        return {
            'email_template_name': 'password_reset_email.html'
        }

    def save(self):
        request = self.context.get('request')
        # Set some values to trigger the send_email method.
        opts = {
            'use_https': request.is_secure(),
            'from_email': 'example@yourdomain.com',
            'request': request,
            # here I have set my desired template to be used
            # don't forget to add your templates directory in settings to be found
            'email_template_name': 'password_reset_email.html'
        }

        opts.update(self.get_email_options())
        self.reset_form.save(**opts)
