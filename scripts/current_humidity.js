// load current humidity values pushed from pi every ten mins											
var humid1 =Papa.parse("current_internal_conditions.csv", {
	download: true,
	complete: function(results) {
		var str2 = "%"
		document.getElementById("live-humid").innerHTML = results.data[1][3].concat(str2);
		var str1 = " o"
		var str1a = str1.sup()
		var str2 = "C"
		var str3 = str1a.concat(str2)
		document.getElementById("live-temp").innerHTML = results.data[1][2].concat(str3); 
		
		var str4 =" Lux"
		document.getElementById("live-lux").innerHTML = results.data[1][4].concat(str4); 
		var str5 = " ppm"		
		document.getElementById("live-co2").innerHTML = results.data[1][5].concat(str5); 
	}
});

// load external conditions pushed from pi every hour after being called from api											
var humid_out =Papa.parse("current_external_conditions.csv", {
	download: true,
	complete: function(results) {
		
		var str2a = "%"
		document.getElementById("outside-humid").innerHTML = results.data[1][4].concat(str2a); 
		var str1 = " o"
		var str1a = str1.sup()
		var str2 = "C"
		var str3 = str1a.concat(str2)
		document.getElementById("outside-temp").innerHTML = results.data[1][5].concat(str3); 	
		document.getElementById("outside-conditions").results.data[1][6];
	}
});

// load external conditions pushed from pi every hour after being called from api											
var pollution_out =Papa.parse("outside_air_pollution.csv", {
	download: true,
	complete: function(results) {
		document.getElementById("outside-no2-name").innerHTML = results.data[1][1];
		document.getElementById("outside-no2-index").innerHTML = results.data[1][2];
		document.getElementById("outside-no2-band").innerHTML = results.data[1][3];
		document.getElementById("outside-ozone-name").innerHTML = results.data[2][1];
		document.getElementById("outside-ozone-index").innerHTML = results.data[2][2];
		document.getElementById("outside-ozone-band").innerHTML = results.data[2][3];
		document.getElementById("outside-pm10-name").innerHTML = results.data[3][1];
		document.getElementById("outside-pm10-index").innerHTML = results.data[3][2];
		document.getElementById("outside-pm10-band").innerHTML = results.data[3][3];	
		document.getElementById("outside-pm2.5-name").innerHTML = results.data[4][1];
		document.getElementById("outside-pm2.5-index").innerHTML = results.data[4][2];
		document.getElementById("outside-pm2.5-band").innerHTML = results.data[4][3];
		document.getElementById("outside-sulphur-name").innerHTML = results.data[5][1];
		document.getElementById("outside-sulphur-index").innerHTML = results.data[5][2];
		document.getElementById("outside-sulphur-band").innerHTML = results.data[5][3];
	}
});

