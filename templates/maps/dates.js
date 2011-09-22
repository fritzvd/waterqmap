var enabledDays = [{% for i in date %}'{{ i.date|date:"n-j-Y" }}',{% endfor %}];

function enableDates(date) {
          var m = date.getMonth(), d = date.getDate(), y = date.getFullYear();
          for (i = 0; i < enabledDays.length; i++) {
            if($.inArray((m+1) + '-' + d + '-' + y,enabledDays) != -1) {
	            return [true];
            }
          }
          return [false];
        }; 
