$(document).ready(function () {

  $('.save-icon i, .save-icon').click(function (e) {
    const csrftoken = getCookie('csrftoken');
    e.preventDefault();
    var cur_el = this;
    var link = $(this).parent().attr('href');
    //make a ajax request to server
    $.ajax({
      type: "POST",
      url: link,
      headers:{'X-CSRFtoken':csrftoken},
      success: function (response) {
        if(response.statusCode==1){ // save successfull for statuscode 1;
          $(cur_el).removeClass('fa-regular');
          $(cur_el).addClass('fa-solid');
          $(cur_el).parent().attr('href', link.replace('/save/', '/unsave/'));
        }
        else if (response.statusCode == 10){ // unsave successfull for statuscode 10;
          $(cur_el).removeClass('fa-solid');
          $(cur_el).addClass('fa-regular');
          $(cur_el).parent().attr('href', link.replace('/unsave/', '/save/'));
        }
        else{
          console.log('operation failed with statusCode ',response.statusCode);
          console.log(response.statusText);

        }
      }
    });
    // end of ajax request
    // function for getting csrf token
    function getCookie(name) {
          var cookieValue = null;
          if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
              var cookie = cookies[i].trim();
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
              }
            }
          }
          return cookieValue;
        }
        //end of function for getting csrf token
  }); // end for onclick event for save-icon

//navbar dropdown behaviour
$('.navbar-dropdown i.fa-caret-down').click(function (e) { 
  e.preventDefault();
  $('.navbar-dropdown .dropdown-content').toggle();
});
$(document).on("click", function(event){
  var $trigger = $(".navbar-dropdown");
  if($trigger !== event.target && !$trigger.has(event.target).length){
      $(".dropdown-content").slideUp("fast");
  }            
});//end of dropdown toggle.

//jobappnavbar toggler
$('.jobnavbar-toggle').click(function(event){
  $('.jobnavbar ul').toggleClass('active');
  hasClass();
});
function hasClass(){
  if ($('.jobnavbar ul').hasClass('active')) {
    $('.jobapp-nav-heading').css("display",'none');
  }
else{
    $('.jobapp-nav-heading').css("display","block");
}
}

//user modal 
$(document).on("click", function(event){
  var $trigger = $("#userId");
  if($trigger !== event.target && !$trigger.has(event.target).length){
      $(".dropdown-content").slideUp("fast");
  }            
});
// var s = document.getElementsByClassName('pdf-file')[0]
// if(s == ""){
//   s.css({'display':'none'})
// }
// else{

// }
var s = $('.pdf-file').attr('data');
console.log(s);
}); //end document ready



















