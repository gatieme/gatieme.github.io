jQuery(document).ready(function($){
	// browser window scroll (in pixels) after which the "back to top" link is shown
	var offset = 300,
		//browser window scroll (in pixels) after which the "back to top" link opacity is reduced
		offset_opacity = 1200,
		//duration of the top scrolling animation (in ms)
		scroll_top_duration = 700,
		//grab the "back to top" link
		$back_to_top = $('.cd-top');

	//hide or show the "back to top" link
	$(window).scroll(function(){
		( $(this).scrollTop() > offset ) ? $back_to_top.addClass('cd-is-visible') : $back_to_top.removeClass('cd-is-visible cd-fade-out');
		if( $(this).scrollTop() > offset_opacity ) {
			$back_to_top.addClass('cd-fade-out');
		}
	});

	//smooth scroll to top
	$back_to_top.on('click', function(event){
		event.preventDefault();
		$('body,html').animate({
			scrollTop: 0 ,
		 	}, scroll_top_duration
		);
	});

});


/* 当鼠标移到表格上是，当前一行背景变色 */
$(document).ready(function(){
		$(".data_list tr td").mouseover(function(){
				$(this).parent().find("td").css("background-color","#d5f4fe");
		});
})
/* 当鼠标在表格上移动时，离开的那一行背景恢复 */
$(document).ready(function(){
		$(".data_list tr td").mouseout(function(){
				var bgc = $(this).parent().attr("bg");
				$(this).parent().find("td").css("background-color",bgc);
		});
})

$(document).ready(function(){
		var color="#ffeab3"
		$(".data_list tr:odd td").css("background-color",color);  //改变偶数行背景色
		/* 把背景色保存到属性中 */
		$(".data_list tr:odd").attr("bg",color);
		$(".data_list tr:even").attr("bg","#fff");
})
