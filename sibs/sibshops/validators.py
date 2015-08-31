import re
import pprint

from z3c.form.validator import SimpleFieldValidator

from zope.interface import Invalid

from sibs.sibshops import MessageFactory as _

class EmailValidator(SimpleFieldValidator):
    regex = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"

    def validate(self, value):
        super(EmailValidator, self).validate(value)
        if value:
            if not re.match(self.regex, value.lower()) or value.endswith('.'):
                raise Invalid(_("Not a valid e-mail address"))

class BooleanValidator(SimpleFieldValidator):

    def validate(self, value):
        if not value == True:
            raise Invalid(_("You must check this option"))

