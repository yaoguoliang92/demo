/**将表单序列化成 json，并清除空值项**/  
$.fn.serializeObject = function() {  
    var o = {};  
    var a = this.serializeArray();  
    $.each(a, function() {  
        if(this.value != -1 && this.value.length > 0){  
            if (o[this.name]) {  
                if (!o[this.name].push) {  
                    o[this.name] = [ o[this.name] ];  
                }  
                o[this.name].push(this.value || '');  
            } else {  
                o[this.name] = this.value || '';  
            }  
        }  
  
    });  
    return o;  
}  


serializeGridData:function(postData){ //序列化参数  
            return  $.extend($("#searchForm").serializeObject(),postData);  
        }  