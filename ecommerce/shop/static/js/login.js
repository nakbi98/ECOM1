(function( $ ){
	   
    // Easing equation based on
    // EaseInOutExpo by Robert Penner (c) 2001
    // robertpenner.com/easing_terms_of_use.html
    
    $.fn.extend( jQuery.easing, {
      eioe: function( ø, t, b, c, d ) {
        if(t==0) return b;
        if(t==d) return b+c;
        if( (t /= d/2) < 1 ) return c/2 * Math.pow( 2, 10 * (t - 1) ) + b;
        return c/2 * ( -Math.pow( 2, -10 * --t ) + 2 ) + b;
      }
    });
    
    // Toggle disabled
    // http://stackoverflow.com/questions/4702000/jquery-toggle-input-disabled-attribute#comment5189637_4702086
    
    $.fn.toggleDisabled = function() {
      return this.each(function() {
        this.disabled = !this.disabled;
      });
    };
    
    // Toggle attribute value
    // Anders Grimsrud, 2013
    
    $.fn.toggleAttr = function(a, v1, v2) {
      return this.each(function() {
        var $t = $(this),
            v  = $t.attr(a) === v1 ? v2 : v1;
        $t.attr(a, v)
          });
    };
    
    // Toggle login/register form

    
  })(jQuery);