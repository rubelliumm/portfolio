$(document).ready(function(){
	
	/*----- Getting Current Time -----*/
	var currentTime = new Date();
	var currentSec = currentTime.getSeconds();
	var currentMin = currentTime.getMinutes();
	var currentHr = currentTime.getHours();
	if(currentHr>12){
		currentHr = currentHr - 12;
	}
	
	/*---- Calculating Needle Angle ----*/
	//Deg for 1sec is 360deg/60=6deg | 1sec=1sec
	var degPerSec = 360/60; 								//6
	var secDeg_PerSec = degPerSec/1; 						//Deg of Sec Needle per Sec = 6
	/*Deg for 1min is 360deg/60=6deg | 1min=60sec*/
	var degPerMin = 360/60; 								//6
	var minDeg_PerSec = degPerMin/60;						//Deg of Min Needle per Sec = 0.1
	/*Deg for 1hr is 360deg/12=30deg | 1hr=3600sec*/
	var degPerHr = 360/12; 									//30
	var hrDeg_PerSec = degPerHr/3600;						//Deg of Hr Needle per Sec = 0.00833
	
	$.fn.rotate = function(degrees) {
		$(this).css({'-webkit-transform' : 'rotate('+ degrees +'deg)',
					 '-moz-transform' : 'rotate('+ degrees +'deg)',
					 '-ms-transform' : 'rotate('+ degrees +'deg)',
					 'transform' : 'rotate('+ degrees +'deg)'});
	};
	var clockInterval;
	function clock(a,b,c){
		var holdSec = a;
		var holdMin = b;
		var holdHr = c;
		
		var secRotation = holdSec*6;
		var minRotation = (holdMin*6)+(holdSec*0.1);
		var hrDeg_PerMin = 30/60; //0.5
		var hourRotation = (holdHr*30)+(holdMin*0.5)+(holdSec*hrDeg_PerSec); //Hr Deg Per Min = 30/60 = 0.5
		if(hourRotation>=360){
			hourRotation = hourRotation-360;
		}
		
		$('.wtb__needle--sec').rotate(secRotation);
		$('.wtb__needle--min').rotate(minRotation);
		$('.wtb__needle--hour').rotate(hourRotation);
	
		clockInterval = setInterval(function(){
			if(secRotation>=360){
			secRotation = 0;
			}
			/*Increasing "1 sec deg" for every second*/
			secRotation += secDeg_PerSec;
			$('.wtb__needle--sec').rotate(secRotation);
			
			if(minRotation>=360){
				minRotation = 0;
			}
			/*Increasing "1 sec deg" for every second*/
			minRotation += minDeg_PerSec;
			$('.wtb__needle--min').rotate(minRotation);
			
			if(hourRotation>=360){
				hourRotation = 0;
			}
			/*Increasing "1 sec deg" for every second*/
			hourRotation += hrDeg_PerSec;
			$('.wtb__needle--hour').rotate(hourRotation);
		},1000);
		
	}
	clock(currentSec,currentMin,currentHr);
	
	var clockEditorInterval;
	function clockEditor(a,b,c){
		var holdSec = a;
		var holdMin = b;
		var holdHr = c;
		
		$('.clockEditor__input--sec').val(holdSec);
		$('.clockEditor__input--min').val(holdMin);
		$('.clockEditor__input--hr').val(holdHr);
		
		clockEditorInterval = setInterval(function(){
			holdSec++;
			if(holdSec==60){
				holdSec = 0;
				holdMin++;
				if(holdMin==60){
					holdMin = 0;
					holdHr++;
					if(holdHr==13){
						holdHr = 1;
					}
				}
			}
			$('.clockEditor__input--sec').val(holdSec);
			$('.clockEditor__input--min').val(holdMin);
			$('.clockEditor__input--hr').val(holdHr);
		},1000);
	}
	clockEditor(currentSec,currentMin,currentHr);
	
	//var rollerInterval;
	
	
	
	$('.clockEditor__plus, .clockEditor__minus').on('mousedown',function(){
		$('.clockEditor__setTime').prop('disabled',false);
		clearInterval(clockEditorInterval);
		var thisOne = $(this);
		var inputVal;
		//rollerInterval = setInterval(function(){
			if(thisOne.hasClass('clockEditor__plus')){
				inputVal = thisOne.siblings('input').val();
				inputVal++;
				if(thisOne.closest('.clockEditor__tile').hasClass('clockEditor__sec')||thisOne.closest('.clockEditor__tile').hasClass('clockEditor__min')){
					if(inputVal==60){
						inputVal = 0;
						thisOne.siblings('input').val(inputVal);
					}
					else {
						thisOne.siblings('input').val(inputVal);
					}
				}
				else {
					if(inputVal==13){
						inputVal = 1;
						thisOne.siblings('input').val(inputVal);
					}
					else {
						thisOne.siblings('input').val(inputVal);
					}
				}
			}
			else {
				inputVal = thisOne.siblings('input').val();
				inputVal--;
				if(thisOne.closest('.clockEditor__tile').hasClass('clockEditor__sec')||thisOne.closest('.clockEditor__tile').hasClass('clockEditor__min')){
					if(inputVal==-1){
						inputVal = 59;
						thisOne.siblings('input').val(inputVal);
					}
					else {
						thisOne.siblings('input').val(inputVal);
					}
				}
				else {
					if(inputVal===0){
						inputVal = 12;
						thisOne.siblings('input').val(inputVal);
					}
					else {
						thisOne.siblings('input').val(inputVal);
					}
				}
			}
		//},100);
	});
	/*$('.clockEditor .ct .plus, .clockEditor .ct .minus').on('mouseup',function(){
		clearInterval(rollerInterval);
	});*/
	
	$('.clockEditor__setTime').click(function(){
		var setSec = $('.clockEditor__input--sec').val();
		var setMin = $('.clockEditor__input--min').val();
		var setHr = $('.clockEditor__input--hr').val();
		$('.wta').addClass('smoothMove');
		clearInterval(clockInterval);
		clock(setSec,setMin,setHr);
		clockEditor(setSec,setMin,setHr);
		$(this).prop('disabled',true);
		setTimeout(function(){
			$('.wta').removeClass('smoothMove');
		},1000);
	});
	
	$('.clockEditor__resetTime').click(function(){
		$('.wta').addClass('smoothMove');
		clearInterval(clockInterval);
		clearInterval(clockEditorInterval);
		var currentTime = new Date();
		var currentSec = currentTime.getSeconds();
		var currentMin = currentTime.getMinutes();
		var currentHr = currentTime.getHours();
		if(currentHr>12){
			currentHr = currentHr - 12;
		}
		clock(currentSec,currentMin,currentHr);
		clockEditor(currentSec,currentMin,currentHr);
		$('.clockEditor__setTime').prop('disabled',true);
		setTimeout(function(){
			$('.wta').removeClass('smoothMove');
		},1000);
	});
	
	// -------------------------------
	function digitalclock() {// We create a new Date object and assign it to a variable called "time".
		var time = new Date(),
			
			// Access the "getHours" method on the Date object with the dot accessor.
			hours = time.getHours() % 12 || 12,
			
			// Access the "getMinutes" method with the dot accessor.
			minutes = time.getMinutes(),
			
			
			seconds = time.getSeconds();
		
		  
		  function harold(standIn) {
			if (standIn < 10) {
			  standIn = '0' + standIn
			}
			return standIn;
		  }
		}
		setInterval(digitalclock, 1000);
});