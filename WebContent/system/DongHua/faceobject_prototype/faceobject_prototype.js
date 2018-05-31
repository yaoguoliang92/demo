function Father(){  
    this.name = "姓名";  
    this.age = "20";  
    this.setName = function(str){this.name=str};  
    this.getName = function(){return this.name;};  
}  
//Father.prototype.setAge = function(age){this.age = age;};  
//Father.prototype.getAge = function(){return this.age;};  
//这俩相同。

Father.prototype = {
	setAge:function(age){
		this.age = age;
	},
	getAge:function(){
		return this.age;
	}
}

console.log(new Father().getAge());  