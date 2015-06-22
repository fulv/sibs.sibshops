import copy

from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.component import getMultiAdapter
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.site.hooks import getSite

from zope.interface import Interface, invariant, Invalid, implements, directlyProvides
from zope.app.content.interfaces import IContentType

from z3c.form import group, field
from z3c.form.interfaces import HIDDEN_MODE
from z3c.form.interfaces import IAddForm


from Products.CMFCore.utils import getToolByName

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

#from sibs.sibshops.vocabularies import equipment_required_binder
from sibs.sibshops import MessageFactory as _

from plone.dexterity.browser import edit
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

# Interface class; used to define content-type schema.

class ISibshop(form.Schema, IImageScaleTraversable):
    """
    This is used to propose a new sibshop and for the board to review and decide.  When approved the sibshop will be available to the campers to sign up
    """

    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/sibshop.xml to define the content type
    # and add directives here as necessary.

    form.model("models/sibshop.xml")

directlyProvides(ISibshop, IContentType)

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Sibshop(dexterity.Item):
    grok.implements(ISibshop)

    # Add your class methods and properties here
    name = schema.Text(
        title=_(u"Your Name"),
        required=True,
    )
    agency = schema.Text(
        title=_(u"Agency"),
        required=True,
    )
    address1 = schema.Text(
        title=_(u"Address 1"),
        required=True,
    )


#class EditForm(edit.DefaultEditForm):
    #grok.context(ISibshop)
    #template = ViewPageTemplateFile('sibshop_templates/sibshop_edit.pt')

class ISibshopAddForm(IAddForm):
    pass

class SibshopAddForm(dexterity.AddForm):
    implements(ISibshopAddForm)
    grok.name('sibs.sibshops.sibshop')
    grok.require('sibs.sibshops.AddSibshop')

    label = _(u'Register Your Sibshop')
    description = _(u"""
                    Please provide the following information.  Some of the
                    information you provide will be used in the <a
                    target='_blank'
                    href='https://www.siblingsupport.org/about-sibshops/find-a-sibshop-near-you'>
                    online directory of registered Sibshops</a>.
                    <span class="field_online">The information needed for
                    the online directory is in blue type.</span>
                    """)
    buttons = copy.deepcopy(dexterity.AddForm.buttons)
    buttons['save'].title = u'Submit'


    def nextURL(self):
        return getSite().absolute_url() + '/about-sibshops/thanks'


#    template = ViewPageTemplateFile('sibshop_templates/sibshop_add.pt')

    def updateWidgets(self):
        """ """
        dexterity.AddForm.updateWidgets(self)

        self.widgets['IDublinCore.title'].label = u'Name of your Sibshop (e.g., Springfield County Sibshops)'
        self.widgets['IDublinCore.description'].label = u'Brief description of your Sibshop (optional)'

        # autofill 'your name' and 'your email' based on login
        #portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        #member = portal_state.member()
        #if not self.widgets['your_name'].value:
        #    self.widgets['your_name'].value = member.getProperty('fullname')
        #if not self.widgets['your_email'].value:
        #    self.widgets['your_email'].value = member.getProperty('email')
        # hide all other fieldsets except default one
        #self.groups = ["registration"]


# View class
# The view will automatically use a similarly named template in
# sibshop_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class View(grok.View):
    grok.context(ISibshop)
    grok.require('zope2.View')

#class SibshopListingView(grok.View):
#    # available on all context
#    grok.context(Interface)
#    # should be only Authenticated members can see this page
#    grok.require('sibs.sibshops.ViewSibshop')
#
#    grok.name('sibshop_listing')
#
#    def renderEquipmentRequiredValues(self, obj, value):
#        """ convert a list of EquipmentRequired to string separated by comma """
#        if type(value) == list:
#            vocab = equipment_required_binder(obj)
#            terms = []
#            for v in value:
#                try:
#                    term = vocab.getTerm(v)
#                except LookupError:
#                    terms.append(v)
#                terms.append(term.title)
#            return ', '.join(terms);
#        return value
