$(function(){
	var arrjson = [{'div':[
		{
			"dt":"2.1权限管理",
			"li":[
				{"_link":"iframe2.html","text":"2.1权限管理"}
			]
		},{
			"dt":"2.2测试区测试资源管理",
			"li":[
				{"_link":"iframe1.html","text":"2.2.1.测试设备管理"},
				{"_link":"iframe4.html","text":"2.2.2.易耗测试材料管理"},
				{"_link":"iframe3.html","text":"2.2.3.专业测试人员资源"},
				{"_link":"iframe3.html","text":"2.2.4.测试服务车辆管理"}
			]
		},{
			"dt":"2.3.客户信息管理",
			"li":[
				{"_link":"iframe1.html","text":"2.3.客户信息管理"}
			]
		},{
			"dt":"2.4.测试业务管理",
			"li":[
				{"_link":"iframe1.html","text":"2.4.测试业务管理"}
			]
		}
	]},{'div':[
		{
			"dt":"2.4.测试业务管理",
			"li":[
				{"_link":"iframe1.html","text":"2.4.测试业务管理"}
			]
		}
	]}]
	
	var left_menu = '<div class="left_menu"></div>';
	for(var i=0;i<arrjson.length;i++){
		if(i==0){
			$(".nav").append(left_menu);
		}else{
			$(".nav").append('<div class="left_menu" style="display:none;"></div>');
		}
	}
	
	for(var i=0;i<arrjson.length;i++){
		var str = "";
		for(var j=0;j<arrjson[i].div.length;j++){
			console.log(arrjson[i].div[j].dt);
			str+='<dl class="yin">';
			str+='<dt>'+arrjson[i].div[j].dt+'<i class="fa fa-angle-down" style="font-size:24px"></i></dt>';
			for(var k=0;k<arrjson[i].div[j].li.length;k++){
				str+='<li><a href="javascript:;" _link="'+arrjson[i].div[j].li[k]._link+'">'+arrjson[i].div[j].li[k].text+'</a></li>';
			}
			str+='</dl>';
		}
		$(".left_menu").eq(i).append(str);
	}
	
	$(".headnva").eq(0).trigger("click");
	
//	var str = "";
//	//str+='<div class="left_menu">';
//	for(var i=0;i<arr.length;i++){
//		str+=''
//		str+='<dl class="yin">';
//		str+='<dt>'+arr[i].dt+'<i class="fa fa-angle-down" style="font-size:24px"></i></dt>';
//		for(var j=0;j<arr[i].li.length;j++){
//			str+='<li><a href="javascript:;" _link="'+arr[i].li[j]._link+'">'+arr[i].li[j].text+'</a></li>';
//		}
//		str+='</dl>';
//	}
//	$(".left_menu").eq(0).append(str);
//	str+='</div>';
	//左侧菜单权限显示数据-----end
	
//	//左侧菜单权限显示数据------start
//	var arr = [{
//		"dt":"2.1权限管理",
//		"li":[
//			{"_link":"iframe2.html","text":"2.1权限管理"}
//		]
//	},{
//		"dt":"2.2测试区测试资源管理",
//		"li":[
//			{"_link":"iframe1.html","text":"2.2.1.测试设备管理"},
//			{"_link":"iframe4.html","text":"2.2.2.易耗测试材料管理"},
//			{"_link":"iframe3.html","text":"2.2.3.专业测试人员资源"},
//			{"_link":"iframe3.html","text":"2.2.4.测试服务车辆管理"}
//		]
//	},{
//		"dt":"2.3.客户信息管理",
//		"li":[
//			{"_link":"iframe1.html","text":"2.3.客户信息管理"}
//		]
//	},{
//		"dt":"2.4.测试业务管理",
//		"li":[
//			{"_link":"iframe1.html","text":"2.4.测试业务管理"}
//		]
//	}]
//	//左侧菜单权限显示数据-----end
//	
//	//菜单权限显示json--------------------------------start------------------------------
//	//测试业务管理。
//	var str = "";
//	//str+='<div class="left_menu">';
//	for(var i=0;i<arr.length;i++){
//		str+=''
//		str+='<dl class="yin">';
//		str+='<dt>'+arr[i].dt+'<i class="fa fa-angle-down" style="font-size:24px"></i></dt>';
//		for(var j=0;j<arr[i].li.length;j++){
//			str+='<li><a href="javascript:;" _link="'+arr[i].li[j]._link+'">'+arr[i].li[j].text+'</a></li>';
//		}
//		str+='</dl>';
//	}
//	$(".left_menu").eq(0).append(str);
//	str+='</div>';
//	//菜单权限显示json--------------------------------end------------------------------
	
})
