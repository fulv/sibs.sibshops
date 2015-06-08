from five import grok

from zope.schema.interfaces import IVocabularyFactory, IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from sibs.sibshops import MessageFactory as _

class StateVocab(object):
    """
    Return a vocab of U.S. states
    """
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        return SimpleVocabulary([SimpleTerm(value=None, title=_(u'-- Select --')),
                                 SimpleTerm(value=u'NA', title=_(u'Not Applicable')),
                                 SimpleTerm(value=u'American States', title=_(u'-- States of the USA --')),
                                 SimpleTerm(value=u'AL', title=_(u'Alabama')),
                                 SimpleTerm(value=u'AK', title=_(u'Alaska')),
                                 SimpleTerm(value=u'AZ', title=_(u'Arizona')),
                                 SimpleTerm(value=u'AR', title=_(u'Arkansas')),
                                 SimpleTerm(value=u'CA', title=_(u'California')),
                                 SimpleTerm(value=u'CO', title=_(u'Colorado')),
                                 SimpleTerm(value=u'CT', title=_(u'Connecticut')),
                                 SimpleTerm(value=u'DE', title=_(u'Delaware')),
                                 SimpleTerm(value=u'DC', title=_(u'District of Columbia')),
                                 SimpleTerm(value=u'FL', title=_(u'Florida')),
                                 SimpleTerm(value=u'GA', title=_(u'Georgia')),
                                 SimpleTerm(value=u'HI', title=_(u'Hawaii')),
                                 SimpleTerm(value=u'ID', title=_(u'Idaho')),
                                 SimpleTerm(value=u'IL', title=_(u'Illinois')),
                                 SimpleTerm(value=u'IN', title=_(u'Indiana')),
                                 SimpleTerm(value=u'IA', title=_(u'Iowa')),
                                 SimpleTerm(value=u'KS', title=_(u'Kansas')),
                                 SimpleTerm(value=u'KY', title=_(u'Kentucky')),
                                 SimpleTerm(value=u'LA', title=_(u'Louisiana')),
                                 SimpleTerm(value=u'ME', title=_(u'Maine')),
                                 SimpleTerm(value=u'MT', title=_(u'Montana')),
                                 SimpleTerm(value=u'NE', title=_(u'Nebraska')),
                                 SimpleTerm(value=u'NV', title=_(u'Nevada')),
                                 SimpleTerm(value=u'NH', title=_(u'New Hampshire')),
                                 SimpleTerm(value=u'NJ', title=_(u'New Jersey')),
                                 SimpleTerm(value=u'NM', title=_(u'New Mexico')),
                                 SimpleTerm(value=u'NY', title=_(u'New York')),
                                 SimpleTerm(value=u'NC', title=_(u'North Carolina')),
                                 SimpleTerm(value=u'ND', title=_(u'North Dakota')),
                                 SimpleTerm(value=u'OH', title=_(u'Ohio')),
                                 SimpleTerm(value=u'OK', title=_(u'Oklahoma')),
                                 SimpleTerm(value=u'OR', title=_(u'Oregon')),
                                 SimpleTerm(value=u'MD', title=_(u'Maryland')),
                                 SimpleTerm(value=u'MA', title=_(u'Massachusetts')),
                                 SimpleTerm(value=u'MI', title=_(u'Michigan')),
                                 SimpleTerm(value=u'MN', title=_(u'Minnesota')),
                                 SimpleTerm(value=u'MS', title=_(u'Mississippi')),
                                 SimpleTerm(value=u'MO', title=_(u'Missouri')),
                                 SimpleTerm(value=u'PA', title=_(u'Pennsylvania')),
                                 SimpleTerm(value=u'RI', title=_(u'Rhode Island')),
                                 SimpleTerm(value=u'SC', title=_(u'South Carolina')),
                                 SimpleTerm(value=u'SD', title=_(u'South Dakota')),
                                 SimpleTerm(value=u'TN', title=_(u'Tennessee')),
                                 SimpleTerm(value=u'TX', title=_(u'Texas')),
                                 SimpleTerm(value=u'UT', title=_(u'Utah')),
                                 SimpleTerm(value=u'VT', title=_(u'Vermont')),
                                 SimpleTerm(value=u'VA', title=_(u'Virginia')),
                                 SimpleTerm(value=u'WA', title=_(u'Washington')),
                                 SimpleTerm(value=u'WV', title=_(u'West Virginia')),
                                 SimpleTerm(value=u'WI', title=_(u'Wisconsin')),
                                 SimpleTerm(value=u'WY', title=_(u'Wyoming')),
                                 SimpleTerm(value=u'American Territories', title=_(u'-- American Territories --')),
                                 SimpleTerm(value=u'AS', title=_(u'American Samoa')),
                                 SimpleTerm(value=u'GU', title=_(u'Guam ')),
                                 SimpleTerm(value=u'MP', title=_(u'Northern Mariana Islands')),
                                 SimpleTerm(value=u'PR', title=_(u'Puerto Rico')),
                                 SimpleTerm(value=u'VI', title=_(u'U.S. Virgin Islands')),
                                 SimpleTerm(value=u'Canadian provinces', title=_(u'-- Canadian provinces --')),
                                 SimpleTerm(value=u'AB', title=_(u'Alberta')),
                                 SimpleTerm(value=u'BC', title=_(u'British Columbia')),
                                 SimpleTerm(value=u'MB', title=_(u'Manitoba')),
                                 SimpleTerm(value=u'NB', title=_(u'New Brunswick')),
                                 SimpleTerm(value=u'NL', title=_(u'Newfoundland and Labrador')),
                                 SimpleTerm(value=u'NT', title=_(u'Northwest Territories')),
                                 SimpleTerm(value=u'NS', title=_(u'Nova Scotia')),
                                 SimpleTerm(value=u'NU', title=_(u'Nunavut')),
                                 SimpleTerm(value=u'ON', title=_(u'Ontario')),
                                 SimpleTerm(value=u'PE', title=_(u'Prince Edward Island')),
                                 SimpleTerm(value=u'QC', title=_(u'Quebec')),
                                 SimpleTerm(value=u'SK', title=_(u'Saskatchewan')),
                                 SimpleTerm(value=u'YT', title=_(u'Yukon')),
                               ])
grok.global_utility(StateVocab, name=u"sibs.sibshops.vocab.state")

class CountryVocab(object):
    """
    Return a vocab of countries
    """
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        return SimpleVocabulary([SimpleTerm(value=None, title=_(u'-- Select --')),
                                 SimpleTerm(value=u'United States', title=_(u'United States')),
                                 SimpleTerm(value=u'Canada', title=_(u'Canada')),
                                 SimpleTerm(value=u'Japan', title=_(u'Japan')),
                                 SimpleTerm(value=u'New Zealand', title=_(u'New Zealand')),
                                 SimpleTerm(value=u'Argentina', title=_(u'Argentina')),
                                 SimpleTerm(value=u'Iceland', title=_(u'Iceland')),
                                 SimpleTerm(value=u'Ireland', title=_(u'Ireland')),
                                 SimpleTerm(value=u'Other', title=_(u'Other')),
                                 ])
grok.global_utility(CountryVocab, name=u"sibs.sibshops.vocab.country")

