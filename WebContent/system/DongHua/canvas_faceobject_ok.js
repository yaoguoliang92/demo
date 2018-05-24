//闭包的写法   
//AMD、CMD、UMD 模块的写法？
var Tool = (function($){
	var context;
	var width,height;
	var gl_i;
	var speed;
	var s = setInterval(draw,1000);
	
	function draw(){
		speed = Math.random()*15+5;
		console.log(speed);
	    var canvas = document.getElementById('canvas');
	    context = canvas.getContext('2d');
	    width = canvas.width;
	    height = canvas.height;
	    gl_i = 0;
	    canvas.height = canvas.height;//重置canvas
	    clearInterval(painting);
	    setInterval(painting,100);
	   
	}
	function painting(){
	     // context.fillStyle = "green";
	      //context.fillRect(i,10,10,10);
		if(gl_i>speed){
		 	gl_i=0;
		}
		context.beginPath();
		context.moveTo(0+(gl_i*30),0);
		context.lineTo(25+(gl_i*30),0);
		context.lineTo(50+(gl_i*30),50);
		context.lineTo(25+(gl_i*30),50);
		if(gl_i<12){
			context.fillStyle="rgb(17,179,210)";//绿色
			context.fill();
			context.closePath();/*可选步骤，关闭绘制的路径*/
			gl_i=gl_i+1;  
		}else if(gl_i>=12&&gl_i<18){
			context.fillStyle="rgb(240,49,49)";//红色
			context.fill();
			context.closePath();/*可选步骤，关闭绘制的路径*/
			gl_i=gl_i+1;  
		}else{
			gl_i=19;
			context.fillStyle="rgb(40,49,49)";//黑色
			context.fill();
			context.closePath();
		}
	
	//  i=i+20;
	}
	
	return {
		drawfuc:draw
	}
	
})(jQuery);
