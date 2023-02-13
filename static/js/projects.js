var Expand = (function() {
  var tile = $('.strips__strip');
  var tileLink = $('.strips__strip > .strip__content');
  var tileText = tileLink.find('.strip__inner-text');
  var stripClose = $('.strip__close');

  //console.log(tile);
  
  var expanded  = false;

  var open = function() {

    if (this.innerText.toLowerCase().startsWith('contact')) {
      window.location.href="/contact";
    } else {      
      var tile = $(this).parent();
        if (!expanded) {
          tile.addClass('strips__strip--expanded');
          // add delay to inner text
          tileText.css('transition', 'all .6s .5s cubic-bezier(0.23, 1, 0.32, 1)');
          stripClose.addClass('strip__close--show');
          stripClose.css('transition', 'all .6s .5s cubic-bezier(0.23, 1, 0.32, 1)');
          expanded = true;
          listenToButtons();
        } 
    }
  };

  var listenToButtons = function() {
    var coll = document.getElementsByClassName("collapsible");
    var i;

    //console.log("!!!", coll.length, "!!!")

    for (i = 0; i < coll.length; i++) {

      //content.style.display = "none";
      //closebutton(parseInt(this.classList.value[12]))
    
      coll[i].addEventListener("click", handleCollapsible)
    }
  };

  var handleCollapsible = function() {
    //console.count();

    this.classList.toggle("active");
    var content = this.nextElementSibling;

    //console.log(content.style.display, this.classList);
    if (content.style.display === "block") {
      content.style.display = null;
    }
    else {
      // open button
      content.style.display = "block";
      // close all other buttons
      closebutton(parseInt(this.classList.value[12]))
    } 
  }
  
  var close = function() {
    if (expanded) {
      tile.removeClass('strips__strip--expanded');
      // remove delay from inner text
      tileText.css('transition', 'all 0.15s 0 cubic-bezier(0.23, 1, 0.32, 1)');
      stripClose.removeClass('strip__close--show');
      stripClose.css('transition', 'all 0.2s 0s cubic-bezier(0.23, 1, 0.32, 1)')
      expanded = false;
      closebutton();
    }
  }

  var bindActions = function() {
    tileLink.on('click', open);
    stripClose.on('click', close);
  };

  var init = function() {
    bindActions();
  };

  return {
    init: init
  };

  }());
  

var PicExpand = (function() {
    var pictile = $('.picstrips__picstrip');
    var pictileLink = $('.picstrips__picstrip > .picstrip__content');
    var pictileText = pictileLink.find('.picstrip__inner-text');
    var picstripClose = $('.picstrip__picclose');
    
    var picexpanded  = false;
  
    var picopen = function() {
        
      var pictile = $(this).parent();
  
        if (!picexpanded) {
          pictile.addClass('picstrips__picstrip--picexpanded');
          // add delay to inner text
          pictileText.css('transition', 'all .5s .3s cubic-bezier(0.23, 1, 0.32, 1)');
          picstripClose.addClass('picstrip__picclose--picshow');
          picstripClose.css('transition', 'all .6s 1s cubic-bezier(0.23, 1, 0.32, 1)');
          picexpanded = true;
        } 
    };
    
    var picclose = function() {
      if (picexpanded) {
        pictile.removeClass('picstrips__picstrip--picexpanded');
        // remove delay from inner text
        pictileText.css('transition', 'all 0.15s 0 cubic-bezier(0.23, 1, 0.32, 1)');
        picstripClose.removeClass('picstrip__picclose--picshow');
        picstripClose.css('transition', 'all 0.2s 0s cubic-bezier(0.23, 1, 0.32, 1)')
        picexpanded = false;
      }
    }
  
    var picbindActions = function() {
      pictileLink.on('click', picopen);
      picstripClose.on('click', picclose);
    };

    var picinit = function() {
      picbindActions();
    };

    return {
      init: picinit
    };
  
    }());


Expand.init();
PicExpand.init();

function closebutton(selected = null){
  //console.log("closing all buttons but:", selected)
  var coll_ii = document.getElementsByClassName("collapsible");
  var ii;
  for (ii = 0; ii < coll_ii.length; ii++){

    var content_ii = coll_ii[ii].nextElementSibling;
    if (parseInt(coll_ii[ii].classList.value[12]) != selected){
      if (coll_ii[ii].classList.contains("active")) { 
        content_ii.style.display = null
        coll_ii[ii].classList.remove("active") 
      }
    } 
  }
}