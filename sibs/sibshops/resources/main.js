jQuery(function($){

  $('form #formfield-form-widgets-IDublinCore-title label').addClass('field_online');
  $('form #formfield-form-widgets-IDublinCore-description label').addClass('field_online');
  $('form #formfield-form-widgets-sponsor_contact label').addClass('field_online');
  $('form #formfield-form-widgets-agency label').addClass('field_online');
  $('form #formfield-form-widgets-address1 label').addClass('field_online');
  $('form #formfield-form-widgets-address2 label').addClass('field_online');
  $('form #formfield-form-widgets-city label').addClass('field_online');
  $('form #formfield-form-widgets-state label').addClass('field_online');
  $('form #formfield-form-widgets-zip label').addClass('field_online');
  $('form #formfield-form-widgets-country label').addClass('field_online');
  $('form #formfield-form-widgets-other_country label').addClass('field_online');
  $('form #formfield-form-widgets-sponsor_phone label').addClass('field_online');
  $('form #formfield-form-widgets-sponsor_email label').addClass('field_online');
  $('form #formfield-form-widgets-agency_site label').addClass('field_online');
  $('form #formfield-form-widgets-facilitator_training label').addClass('field_plain');

  $('form #formfield-form-widgets-bool_standards label').html(
      'We have reviewed and endorsed the <a target="_blank" href="https://www.siblingsupport.org/about-sibshops/for-sibshop-providers/sibshops-standards-of-practice">Sibshop Standards of Practice</a>'
   );

  $('form #formfield-form-widgets-bool_sibgroup label').html(
      'We have asked to join the Sibshop Facilitator Forum Facebook group.'
   );

  $('form #formfield-form-widgets-facilitator_training label').html(
      "<b>Training.</b> Please provide the name(s) of facilitator(s) who became first-generation facilitators by attending the Sibling Support Project’s two-day Sibshop Facilitator Training:"
   );
  $('form #formfield-form-widgets-facilitator_training_date').after(
      '<p><strong><em>Please note:</em></strong> If none of your Sibshop facilitators attended the Sibling Support Project’s two-day Sibshop Facilitator Training please contact us at 206-297-6368 or at <a href="mailto:info@siblingsupport.org">info@siblingsupport.org</a> before proceeding.  <strong>Registering with second-generation facilitators requires prior approval from the Sibling Support Project.</strong></p>'
   );
  $('form #formfield-form-widgets-bool_sibgroup').before(
      '<p>The Sibshop Facilitator Forum (SFF) is a closed Facebook group JUST for facilitators from registered Sibshops.  <strong>It is a requirement that each registered Sibshop have at least one facilitator who is a member of SFF.</strong>  You can easily request to join <a target="_blank" href="https://www.facebook.com/groups/SibshopFacilitatorForum/">here</a>:</p>'
   );
});

