$(document).ready(function(){
    $('.exam_nav_btn').click(function(){
        $('.exam_nav_btn').removeClass("exam_active");
        $(this).addClass("exam_active");
    });
    $('.assign_nav_btn').click(function(){
        $('.assign_nav_btn').removeClass("assign_active");
        $(this).addClass("assign_active");
    });

    $('.exam_nav_btn').click(function(){
        if($(this).html() == "SPI"){
            $('.external_exams').css({"display":"none"});
            $('.mid_exams').css({"display":"block"});
        }
        else{
            $('.external_exams').css({"display":"block"});
            $('.mid_exams').css({"display":"none"});
        }
    })

    $('.assign_nav_btn').click(function(){
        if($(this).html() == "Pending Assignments"){
            $('.completed_assign').css({"display":"none"});
            $('.pending_assign').css({"display":"block"});
        }
        else{
            $('.completed_assign').css({"display":"block"});
            $('.pending_assign').css({"display":"none"});
        }
    })
    // $('.user_form').click(function(){
    //     $('.user_form').addClass("form_inactive");
    //     $('.user_form').removeClass('form_active');
    //     $(this).addClass("form_active");
    //     $(this).removeClass('form_inactive');
    // })
})