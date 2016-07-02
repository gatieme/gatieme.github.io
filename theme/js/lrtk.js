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

<script type="text/javascript">
<!--
//分别是奇数行默认颜色,偶数行颜色,鼠标放上时奇偶行颜色
var aBgColor = ["#FFFFFF","#f2faff","#FFFFCC","#FFFFCC"];
//从前面iHead行开始变色，直到倒数iEnd行结束
function addTableListener(o,iHead,iEnd)
{
o.style.cursor = "normal";
iHead = iHead > o.rows.length?0:iHead;
iEnd = iEnd > o.rows.length?0:iEnd;
for (var i=iHead;i<o.rows.length-iEnd ;i++ )
{
o.rows[i].onmouseover = function(){setTrBgColor(this,true)}
o.rows[i].onmouseout = function(){setTrBgColor(this,false)}
}
}
function setTrBgColor(oTr,b)
{
oTr.rowIndex % 2 != 0 ? oTr.style.backgroundColor = b ? aBgColor[3] : aBgColor[1] : oTr.style.backgroundColor = b ? aBgColor[2] : aBgColor[0];
}
window.onload = function(){addTableListener(document.getElementById("tbColor"),0,0);}
//-->
</script>
