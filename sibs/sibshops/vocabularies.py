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
                                 SimpleTerm(value=u'CA', title=_(u'California')),
                                 SimpleTerm(value=u'NV', title=_(u'Nevada'))])
grok.global_utility(StateVocab, name=u"sibs.sibshops.vocab.state")

class CountryVocab(object):
    """
    Return a vocab of countries
    """
    grok.implements(IVocabularyFactory)
    
    def __call__(self, context):
        return SimpleVocabulary([SimpleTerm(value=None, title=_(u'-- Select --')),
                                 SimpleTerm(value=u'CA', title=_(u'United States')),
                                 SimpleTerm(value=u'NV', title=_(u'Canada'))])
grok.global_utility(CountryVocab, name=u"sibs.sibshops.vocab.country")

