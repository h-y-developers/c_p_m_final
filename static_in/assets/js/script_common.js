$( document ).ready(function() {
    var w = window.innerWidth;

    if(w > 767){
        $('#menu-jk').scrollToFixed();
    }else{
        $('#menu-jk').scrollToFixed();
    }



})

$(document).ready(function(){
    
    $('.users').click(function(){

        $('.users').removeClass("user_active");
        $(this).addClass("user_active");
        localStorage.setItem('user',$(this).html())
        
        if($(this).html() == 'Student'){
            
            $('.faculty_form').css({"display":"none"});
            $('.company_form').css({"display":"none"});
            // $('.student_form').fadeIn(500,'swing');
            
            $('.student_form').css({"display":"block"});
            
        }
        else if($(this).html() == 'Faculty'){
            // localstorage.setItem("user", 'Faculty');
            $('.student_form').css({"display":"none"});
            $('.company_form').css({"display":"none"});
            // $('.faculty_form').fadeIn(500,'swing');
            $('.faculty_form').css({"display":"block"});
        }
        else if($(this).html() == 'Company'){
            // localstorage.setItem("user", 'Company');
            $('.student_form').css({"display":"none"});
            $('.faculty_form').css({"display":"none"});
            // $('.company_form').css({'transform' : 'rotateY(360deg)'});
            $('.company_form').css({"display":"block"});
        }
    })
    // $('.user_form').click(function(){
    //     $('.user_form').addClass("form_inactive");
    //     $('.user_form').removeClass('form_active');
    //     $(this).addClass("form_active");
    //     $(this).removeClass('form_inactive');
    // })
})
// $( document ).ready(function() {

//     $('.owl-carousel').owlCarousel({
//         loop:true,
//         margin:0,
//         nav:true,
//         autoplay: true,
//         dots: true,
//         autoplayTimeout: 5000,
//         navText:['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
//         responsive:{
//             0:{
//                 items:1
//             },
//             600:{
//                 items:1
//             },
//             1000:{
//                 items:1
//             }
//         }
//     })


// });


// var percentage = 0; 
  
//         function check(n, m) { 
//             if (n < 6) { 
//                 percentage = 0; 
//                 $(".progress-bar").css("background", "#dd4b39"); 
//             } else if (n < 8) { 
//                 percentage = 20; 
//                 $(".progress-bar").css("background", "#9c27b0"); 
//             } else if (n < 10) { 
//                 percentage = 40; 
//                 $(".progress-bar").css("background", "#ff9800"); 
//             } else { 
//                 percentage = 60; 
//                 $(".progress-bar").css("background", "#4caf50"); 
//             } 
  
//             // Check for the character-set constraints 
//             // and update percentage variable as needed. 
            
//             //Lowercase Words only 
//             if ((m.match(/[a-z]/) != null))  
//             { 
//                 percentage += 10; 
//             } 
            
//             //Uppercase Words only 
//             if ((m.match(/[A-Z]/) != null))  
//             { 
//                 percentage += 10; 
//             } 
            
//             //Digits only 
//             if ((m.match(/0|1|2|3|4|5|6|7|8|9/) != null))  
//             { 
//                 percentage += 10; 
//             } 
            
//             //Special characters 
//             if ((m.match(/\W/) != null) && (m.match(/\D/) != null)) 
//             { 
//                 percentage += 10; 
//             } 
  
//             // Update the width of the progress bar 
//             $(".progress-bar").css("width", percentage + "%"); 
//         } 
  
        // Update progress bar as per the input 
        $(document).ready(function() { 
            // Whenever the key is pressed, apply condition checks. 
            
            $(".change_password").focus(function(){
                $(".password_vali").css("display","block")
            })
            $(".change_password").blur(function(){
                $(".password_vali").css("display","none")
            })
            $(".change_password").keyup(function() { 
                var m = $(this).val(); 
                var n = m.length; 
  
                // // Function for checking 
                // check(n, m);
                var lowerCaseLetters = /[a-z]/g;
                var upperCaseLetters = /[A-Z]/g; 
                var numbers = /[0-9]/g;

                if(m.match(lowerCaseLetters)){
                    $('#letter').removeClass('invalid')
                    $('#letter').addClass('valid')
                }
                else{
                    $('#letter').removeClass('valid')
                    $('#letter').addClass('invalid')
                }
                if(m.match(upperCaseLetters)){
                    $('#capital').removeClass('invalid')
                    $('#capital').addClass('valid')
                }
                else{
                    $('#capital').removeClass('valid')
                    $('#capital').addClass('invalid')
                }
                if(m.match(numbers)){
                    $('#number').removeClass('invalid')
                    $('#number').addClass('valid')
                }
                else{
                    $('#number').removeClass('valid')
                    $('#number').addClass('invalid')
                }
                if(n>=8){
                    $('#length').removeClass('invalid')
                    $('#length').addClass('valid')
                }
                else{
                    $('#length').removeClass('valid')
                    $('#length').addClass('invalid')
                }

                if($('#letter').hasClass('valid') && ('#captial').hasClass('valid')&& $('#number').hasClass('valid') && ('#length').hasClass('valid')){
                    $(".password_vali").css("display","none")
                }
                else{
                    $(".password_vali").css("display","block")
                }
            }); 
        })

        $(document).ready(function(){
            $('.confirm_password').keyup(function(){
                var m = $(this).val();
                var n = $('.change_password').val()

                if(m.match(n)){
                    $('.password_re_vali').css('display',"none")
                    $('.submit_btn').removeAttr('disabled')
                }
                else{
                    $('.password_re_vali').css('display','block')
                    $('.submit_btn').prop('disabled','true')
                }
            })

            $('.show_password').click(function(){
                if($(this).prop('checked') == true){
                    $('.change_password').prop('type','text')
                    $('.confirm_password').prop('type','text')
                }
                else if($(this).prop('checked') == false){
                    $('.change_password').prop('type','password')
                    $('.confirm_password').prop('type','password')
                }
            })
        })