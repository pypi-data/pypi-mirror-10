"""
Dummy email backend that does nothing.
"""

from google.appengine._internal.django.core.mail.backends.base import BaseEmailBackend

class EmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        return len(email_messages)
