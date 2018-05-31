/*(function($){*/
	var obj = {gl_i:0,speed:10}
	
	var Branch = function(speed,context){
		this.speed = speed;
		this.context = context;
	}
	Branch.prototype.draw= function(){
		console.log(this.speed);
//		speed = Math.random()*15+5;
	    var canvas = document.getElementById('canvas');
	    context = canvas.getContext('2d');
	    width = canvas.width;
	    height = canvas.height;
	    obj.gl_i = 0;
	    canvas.height = canvas.height;//重置canvas
	    clearInterval(this.painting);
	    setInterval(Branch.painting,100);
	    console.log(obj.gl_i);
	}
	
	Branch.painting = function(){
	     // context.fillStyle = "green";
	      //context.fillRect(i,10,10,10);
	     //gl_i = this.gl;
		if(obj.gl_i>obj.speed){
		 	obj.gl_i=0;
		}
		context.beginPath();
		context.moveTo(0+(obj.gl_i*30),0);
		context.lineTo(25+(obj.gl_i*30),0);
		context.lineTo(50+(obj.gl_i*30),50);
		context.lineTo(25+(obj.gl_i*30),50);
		if(obj.gl_i<12){
			context.fillStyle="rgb(17,179,210)";//绿色
			context.fill();
			context.closePath();/*可选步骤，关闭绘制的路径*/
			obj.gl_i=obj.gl_i+1;  
		}else if(obj.gl_i>=12&&obj.gl_i<18){
			context.fillStyle="rgb(240,49,49)";//红色
			context.fill();
			context.closePath();/*可选步骤，关闭绘制的路径*/
			obj.gl_i=obj.gl_i+1;  
		}else{
			obj.gl_i=19;
			context.fillStyle="rgb(40,49,49)";//黑色
			context.fill();
			context.closePath();
		}
	//  i=i+20;
	}
	
	function init(){
//		var speed = math
		var b = new Branch(11,"")
		b.draw();
	}
	$(function(){
//		init();
		var s = setInterval(init,1000);
	})
	
/*})(jQuery);*/
function chngespeed(){
	var speed = Math.random()*15+5;
	obj.speed = speed;
}
