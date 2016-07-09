
var player = null;
var done = false;

function initPlayer(do_callback, on_player_state_change){



  var tag = document.createElement('script');
  tag.src = "https://www.youtube.com/iframe_api";
  var firstScriptTag = document.getElementsByTagName('script')[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);


  window.onYouTubeIframeAPIReady = function() {
    player = new YT.Player('player', {
      height: '390',
      width: '640',
      origin: '',
      events: {
        'onReady': onPlayerReady,
        'onStateChange': onPlayerStateChange
      }
    });

  }

  // 4. The API will call this function when the video player is ready.
  function onPlayerReady(event) {
    //event.target.playVideo();

    // That's where we do the stuff
    do_callback(player);

  }

  // 5. The API calls this function when the player's state changes.
  //    The function indicates that when playing a video (state=1),
  //    the player should play for six seconds and then stop.

  function onPlayerStateChange(event) {

    on_player_state_change(player,event);

  }

  function stopVideo() {
    player.stopVideo();
  }
}


// Jukebear player API (temporary)
function playVideo(player,vid){

    //player.loadVideoByUrl({mediaContentUrl:vid});
    player.loadVideoById({videoId: vid});

}

function getPlayer(){
  return player;
}






