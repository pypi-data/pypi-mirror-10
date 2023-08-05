  /*   Javascripts for the MLS Searchmask
  *    generates help divs and add functions to checkboxes
  *    generates Selection Indicator
  */
  // Set Fallback text

$(document).ready(function() {
  // wait till all pagecontent is loaded
  if($('#listing-search #search-form form#form').length !==0){
    //Include translations when the searchform is displayed
    $.getScript('translations_js.js', function(data, textStatus, jqxhr) {
    /*"""Execute Script when the translated parts are loaded"""*/

    for(var i=0, len=langs.length; i < len; i++){
      /* Loop through available languages and check which language is set in plone*/
      if($('body.site-' + langs[i]).length > 0 ){
        sitelanguage = langs[i];
      }
    }
    /*
      we get the "contents" array form plone
      structure: contents["en"]["text_All"] = 'all';
    */
    var text_UnselectAll = contents[sitelanguage]["text_UnselectAll"];
    var text_All = contents[sitelanguage]["text_All"];
    var text_Selected = contents[sitelanguage]["text_Selected"];
    var text_Default = contents[sitelanguage]["text_Default"];


    function generateHelpText(papa){
    /*"""Updates the display of the Selection Indicator Text.
    papa: Selector Reference String"""*/
      
      var outputstring = '';
      var outputlabel = text_Default + ' : ';
      var counter_all = 0;
      var counter_checked = 0;

    /* Loop over all checkboxes
        when a box is checked, add the label to the new outputstring
    */
    $(papa +' input[type=checkbox]').each(function () {
           counter_all++;
           if (this.checked) {
               outputlabel = text_Selected + ' : ';
               counter_checked++;
               if(outputstring.length>0){
                outputstring=outputstring +', ' +  String($(papa + " label[for='"+this.id+"']").text());
           } else{
               outputstring=String($(papa +" label[for='"+this.id+"']").text());
            }
           }
    });

    if (counter_all == counter_checked){
    /* when all checkboxes are selected, go back to default*/
        outputstring='';
        outputlabel=text_Default;
        $(papa +' input[type=checkbox]').attr('checked', false);
    }
    // Check if 'unselect all' Link should be displayed
    if(outputstring.length<1){
      outputstring = text_All;
      $(papa + ' .search_unselect').hide();
    }
    else{
      $(papa + ' .search_unselect').fadeIn();
    }
    //update the view
    $(papa + ' span.search_option').text(outputstring);
    $(papa + ' span.search_text').text(outputlabel);

}

function unselect_checkboxes(papa){
  /*"""Unselect all Checkboxes"""*/
  $(papa +' input[type=checkbox]').attr('checked', false);
  generateHelpText(papa);
}

function update_form(root){
  /*"""Update all different Areas with Selection Indicator Text"""*/
  /* Update the custom listing searchform*/
  var slot1 = root + ' .form-row-listing-type';
  var slot2 = root + ' .form-row-tabbed .enableFormTabbing dd.formPanel';

  generateHelpText(slot1);

  $(slot2).each(function () {
    generateHelpText('#' + this.id);

  });

}
      // add HTML for the helperbox and unselect button
      var help_div = '<div class="searchhelp"><span class="search_text">' + text_Default + '</span><span class="search_option"> ' + text_All + ' </span></div>';
      var unselect_div = '<div class="search_unselect"><span>' + text_UnselectAll + '</span></div>';
      
      // insert helperbox and unselect button before and after form div
      if ( $("#search-form .form-row-listing-type .searchhelp").length < 1 ) {
        $(help_div).insertBefore($('#search-form div#formfield-form-widgets-listing_type'));
        $(unselect_div).insertAfter($('#search-form div#formfield-form-widgets-listing_type'));
      }

      if ( $("#search-form .form-rows dl.enableFormTabbing dd.formPanel .searchhelp").length < 1 ) {
        // here the same for the tabbed forms
        $(help_div).insertBefore('#search-form .form-rows dl.enableFormTabbing dd.formPanel .field');
        $(unselect_div).insertAfter('#search-form .form-rows dl.enableFormTabbing dd.formPanel .field');
  
      }
      
      // show helperbox
      $('.searchhelp').fadeIn();
      update_form('#search-form #form');


      /* unselect all checked options in the current tab*/
      $('#listing-search #search-form .enableFormTabbing .search_unselect span').click(function (e) {
        /* add click handler on the 'unselect all' link in .enableFormTabbing area */
        papa=String('#listing-search #search-form .enableFormTabbing #' + e.target.parentElement.parentElement.id);
        
        $(papa + ' input[type=checkbox]').attr('checked', false);
        $(papa + ' .search_unselect').hide();
        $(papa + ' span.search_option').hide();
        $(papa + ' span.search_option').text(text_All);
        $(papa + ' span.search_text').text(text_Default + ' : ');
        $(papa + ' span.search_option').fadeIn();
      });

      $('#listing-search #search-form .form-row-listing-type .search_unselect span').click(function (e) {
        /* add click handler on the 'unselect all' link in .form-row-listing-type */
        unselect_checkboxes('#listing-search #search-form .form-row-listing-type');

      });

      /* Listing Type: add change function for checkbox fields */
      $('.form-row-listing-type .option input[type=checkbox]').change(function(e) {
      /* Get Parent Elements*/
        console.log('change ME');
        generateHelpText(String('#search-form #form .form-row-listing-type'));
      });
      /* Listing Type: add change function for checkbox fields */
      $('#listing-search #search-form .enableFormTabbing .option input[type=checkbox]').change(function(e) {
      /* Get Parent Elements*/ 
        generateHelpText(String('#search-form #form #' + e.target.parentNode.parentElement.parentElement.id));
      });  
  });
}

});
