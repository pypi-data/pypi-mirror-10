function hoverme(state){
  var img_url ='++resource++customer.mlscrcom.images/map' + state +'.png';
  $('#map-image').attr('src', img_url);
}

function clearbg(){
  $('#map-image').attr('src', '++resource++customer.mlscrcom.images/map.png');
}

function fillselect(state){
  //unset all selected options
  $("#form-widgets-location_state").find('option').selected(false);
  //find the one to select
  $("#form-widgets-location_state option").each(function()
  {
    if($(this).val() == state){
      $(this).attr("selected","selected");
    }
    if(state == 'SanJose' && escape($(this).val())=='San%20Jos%5Cxe9') $(this).attr("selected","selected");
    if(state == 'Limon' && escape($(this).val())=='Lim%5Cxf3n') $(this).attr("selected","selected");
  });

return false;
}


$(document).ready(function() {

/* add class-name to every last li of a list */
  $("ul li:last-child").addClass("last-item");
  $("#tab-menu li:first-child").addClass("active");

  var defaultText_Min = 'MIN';
  var defaultText_Max = 'MAX';
  var defaultValue_Location ='--NOVALUE--';

  /* Preparation not make the side no-skript safe */
  /* turn off onbeforeunload dialog for pages with #home-search-map  */
  if($('#home-search-map').length !==0){
    window.onbeforeunload = null;
    
  /*Unselect ALL checkboxes in homesearchmap*/
  $('#home-search-map input[type=checkbox]').attr('checked', false);

  if($('#form-widgets-location_state option:selected').val()==defaultValue_Location){
    $('#form-widgets-location_state option:selected').text(' ');
  }

  $('#form').removeClass('rowlike enableUnloadProtection');
  $('#form').submit(function() {
    
    if($("#form-widgets-price_min").val() == defaultText_Min){
        $("#form-widgets-price_min").text("");
        $("#form-widgets-price_min").val("");
    }
    if($("#form-widgets-price_max").val() == defaultText_Max){
        $("#form-widgets-price_max").val("");
        $("#form-widgets-price_max").text("");
    }

    });
  }  

});
