$(document).ready(function(){

	$('.fresh').stop().animate({
        left: 0    
    }, 900);   

    $('.story').stop().animate({
        marginTop: 0    
    }, 800); 

    $('.community').slideToggle(800);

    $('.mood').stop().animate({
        right: 0    
    }, 1200);          
    	
   
   $('.fresh').mouseenter(function() {
   		$('.fresh-text').textillate('in');
   }).mouseleave(function() {
   		$('.fresh-text').textillate('out');
   });

   $('.community').mouseenter(function() {
    	$('ul.community-text-list li').each(function(index) {
    		$(this).delay(80*index).fadeTo(400, 1);
    	});
   }).mouseleave(function() {
    	$('ul.community-text-list li').each(function(index) {
    		$(this).delay(80*index).fadeTo(400, 0);
    	});
   });

    $('.story').mouseenter(function() {
   		$('.story-text1').textillate('in');
   		$('.story-text2').textillate('in');
   }).mouseleave(function() {
   		$('.story-text1').textillate('out');
   		$('.story-text2').textillate('out');
   });

     $('.mood').mouseenter(function() {
   		$('.mood-text1').textillate('in');
   		$('.mood-text2').textillate('in');
   }).mouseleave(function() {
   		$('.mood-text1').textillate('out');
   		$('.mood-text2').textillate('out');

   });

}) 