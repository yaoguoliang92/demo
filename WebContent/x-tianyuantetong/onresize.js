// 登录时间
function realSysTime(){ 
	var now = new Date(), //创建Date对象 
		year = now.getFullYear(), //获取年份 
		month = now.getMonth(), //获取月份 
		date = now.getDate(), //获取日期 
		day = now.getDay(), //获取星期 
		hour = now.getHours(), //获取小时 
		minu =now.getMinutes(), //获取分钟 
		sec = now.getSeconds(); //获取秒钟 
	month = month + 1; 
	if(month < 10){month = '0'+month;}
	if(date < 10){date = '0'+date;}
	if(hour < 10){hour = '0'+hour;}
	if(minu < 10){minu = '0'+minu;}
	if(sec < 10){sec = '0'+sec;}
	var time = year + '/' + month + '/' + date + ' ' + hour + ':' + minu + ':' + sec; //组合系统时间 
	$('#clock').text(time); //显示系统时间 
};

//设置iframe自动宽高
function autoIframe() {
	// 设置高度	
	$('.left-list-menu-box').css('height',$(window).height() - 90 + 'px');
	$('#left-list-menu').css('height',$(window).height() - 90 + 'px');
	
	
	$('.main-iframe').css('height',$(window).height() - 90 + 'px');
	//$('#main-iframe').css('height',$(window).height() - 90 + 'px');
	
	/*20161025注释
	var explorer = navigator.userAgent;
	if(explorer.indexOf('Firefox') >= 0){
		$('#main-iframe').css('height',$(window).height() - 105 + 'px');
	}else{
		$('#main-iframe').css('height',$(window).height() - 90 + 'px');
	}*/

	
	//设置 宽度
	if($(window).width()<=1260){
		$('.main-iframe').css('width','1093px');
		$('#main-iframe').css('width','1093px');	
	}else{
		$('.main-iframe').css('width',$(window).width() - 167 + 'px');
		$('#main-iframe').css('width',$(window).width() - 167 + 'px');
	};
};

// 窗口变化 调用设置iframe宽 高
window.onresize = function () {
	autoIframe();
};

// 菜单 控制
function go(n,m) {
	// top 菜单 控制
	var mainUrl = "",
		leftUrl = "";

	//右侧 MAIN 框架URL跳转	
	//if(n == 0) mainUrl = "App/group_stat.htm";
	if(n == 1) mainUrl = path + "/jsp/trafficsum/trafficsum.jsp";
	if(n == 2) mainUrl = path + "/jsp/flow_direction/flow_stat.jsp";
	if(n == 3) mainUrl = path + "/jsp/user_behavior/index.jsp";
	if(n == 4) mainUrl = "listroleURaction.do"; //path + "/jsp/user_behavior/index.jsp";       // "listroleURaction.do";

	//左菜单
	if(m == 0) leftUrl =  path+"/leftLogmenu.do";
	if(m == 1) leftUrl = path + "/jsp/menu_list_2.jsp";
	if(m == 2) leftUrl = path + "/jsp/menu_list_4.jsp";
	if(m == 3) leftUrl = path + "/jsp/menu_list_3.jsp";

	$("#main-iframe").attr("src",mainUrl);
	// 左侧 菜单 更换
	$("#left-list-menu").attr("src",leftUrl);
}

/*/左侧菜单点击定位
function usm() {
	setTimeout(function(){
		var cont =  $("#left-list-menu").contents().find("#um").text();
		if(cont == '') usm(); else $("#left-list-menu").contents().find("#um").click();	
	},15)

};

//信息探测 点击
function dec() {
	setTimeout(function(){
		var cont =  $("#left-list-menu").contents().find("#dec").text();
		if(cont == '') dec(); else $("#left-list-menu").contents().find("#dec").click();	
	},15)

};*/

$(function(){
	// 登录时间调用
	//realSysTime(); //解决刷新一秒空白
	//window.setInterval('realSysTime()',1000); //实时获取并显示系统时间

	//调用设置iframe宽 高
	autoIframe();

	// 定位top菜单 
	for(var i=0; i<$(".top-center a").length; i++){
		$(".top-center a:eq("+i+")").attr("index",i);
		$(".top-center a:eq("+i+")").click(function(){
			for(var j=0; j<$(".top-center a").length; j++){
				$(".top-center a:eq("+j+")").removeClass("ac-menu-" + j).addClass("menu-" + j);	
			}
			$(this).removeClass("menu-" + $(this).attr("index")).addClass("ac-menu-" + $(this).attr("index"));
		})
	}
})

function onrest(id) {
	if(!id)
		$(':input', 'form').not(':button,:submit,:reset,:hidden,.Wdate').val('');
	else
		$(':input', '#'+id).val('');
}