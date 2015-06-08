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
      'We have joined <a target="_blank" href="https://www.siblingsupport.org/about-sibshops/for-sibshop-providers/sibgroup-a-yahoogroup-for-sibshop-providers">SibGroup</a>'
   );

  $('form #formfield-form-widgets-facilitator_training label').html(
      "Please read Standard 10 of the Sibshops Standards of Practice and describe your agency's efforts to obtain training on the Sibshop model. Specifically, please note whether your Sibshop facilitators are first-generation or second-generation facilitators and <b>where and when</b> they received their training. <b>Registering with second-generation facilitators requires prior approval from the Sibling Support Project.</b>"
   );
});

