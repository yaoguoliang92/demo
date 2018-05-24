(function($){
	var Branch = function(t,gl_i,speed){
		this.tree = t;
		this.gl_i = gl_i;
		this.speed = speed;
		//this.draw();
	}
	Branch.prototype = {
		draw: function () {
			
			var context = this.tree.ctx;
			var gl_i = this.gl_i;
			var gl_i = 2;
			context.beginPath();
			context.moveTo(0+(gl_i*30),0);
			context.lineTo(25+(gl_i*30),0);
			context.lineTo(50+(gl_i*30),50);
			context.lineTo(25+(gl_i*30),50);
			if(this.gl_i<12){
				context.fillStyle="rgb(17,179,210)";//绿色
				context.fill();
				context.closePath();/*可选步骤，关闭绘制的路径*/
				gl_i=this.gl_i+1;  
			}else if(this.gl_i>=12&&this.gl_i<18){
				context.fillStyle="rgb(240,49,49)";//红色
				context.fill();
				context.closePath();/*可选步骤，关闭绘制的路径*/
				this.gl_i=this.gl_i+1;  
			}else{
				this.gl_i=19;
				context.fillStyle="rgb(40,49,49)";//黑色
				context.fill();
				context.closePath();
			}
		}
	}
	
	var Tree = function(){
		this.init = function (ctx) {
			this.ctx = ctx;
		};
	}

	
	function init(){
		var canvas = document.getElementById('canvas');
		var width = canvas.width;
   		var  height = canvas.height;
		var ctx = canvas.getContext("2d");
		var t = new Tree();
		t.init(ctx);
		var b = new Branch(t);
		b.draw();
	}
	
	$(function(){
		init();
//		var s = setInterval(init,1000);
		
	})
	
	
})(jQuery);
