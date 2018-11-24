$(document).ready(function(){
	var imgItems = $('.slider li').length;
	var imgPos = 1;
	//puntitos debajo de la imagen
	for(i = 1; i <= imgItems; i++){
		$('.pagination').append('<li><span class="fa fa-circle"></span></li>');
	}
	//ejecutables
	$('.slider li').hide();
	$('.slider li:first').show();
	$('.pagination li:first').css({'color':'#000000'});
	
	$('.pagination li').click(pagination);
	$('.right span').click(nextSlider);
	$('.left span').click(prevSlider);
	//funciones
//--
	function pagination(){
		var paginationPosition = $(this).index()+1;

		$('.slider li').hide();
		$('.slider li:nth-child('+paginationPosition+')').fadeIn();
		$('.pagination li').css({'color':'#969696'});
		$(this).css({'color':'#000000'});

		imgPos = paginationPosition;
	}

	function nextSlider(){
		if(imgPos >= imgItems){
			imgPos = 1;
		}else{
			imgPos++;
		}
		$('.pagination li').css({'color':'#969696'});
		$('.pagination li:nth-child('+imgPos+')').css({'color':'#000000'});

		$('.slider li').hide();
		$('.slider li:nth-child('+imgPos+')').fadeIn();
	}

	function prevSlider(){
		if(imgPos <= 1){
			imgPos = imgItems;
		}else{
			imgPos--;
		}
		$('.pagination li').css({'color':'#969696'});
		$('.pagination li:nth-child('+imgPos+')').css({'color':'#000000'});

		$('.slider li').hide();
		$('.slider li:nth-child('+imgPos+')').fadeIn();
	}

	
	/*
	//automatico --no necesario
	setInterval(function(){
		nextSlider();
	},5000);
	*/
});
