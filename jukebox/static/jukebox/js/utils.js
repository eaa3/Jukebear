

function setPlayerCallbacks(playlist){

	   var doCallback = function(youtube_player){


        //playVideo(youtube_player,"http://www.youtube.com/v/L9iY6yPrSzY");

        playVideo(youtube_player,playlist[playIdx]);

      };


      var onPlayerStateChange = function(youtube_player, event){

         if (event.data == YT.PlayerState.PLAYING && !done) {
            //setTimeout(stopVideo, 6000);
            //console.log("LOL what?")
            //done = true;
          }
          if( event.data == YT.PlayerState.ENDED ){
            playIdx = (playIdx+1)%playlist.length;
            playVideo(youtube_player,playlist[playIdx]);
            //setTimeout( function() { changeVideoId("50690pyEd9I"); }, 6000);
          }

      }

      initPlayer(doCallback, onPlayerStateChange)
}


            // /href="http://localhost:8000/jukebox/update_playlist" 
function updatePlaylist(jukebox_id, csrf_token){
  textfield = document.getElementById("add_song")
  xhr = new XMLHttpRequest();
  var url = "http://localhost:8000/jukebox/update_playlist";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-type", "application/json");
  xhr.setRequestHeader('X-CSRF-Token', csrf_token);

  xhr.onreadystatechange = function () { 
      if (xhr.readyState == 4 && xhr.status == 200) {
          var json = JSON.parse(xhr.responseText);
          console.log("Received: " + json.playlist);
          playlist = json.playlist;
          var list = document.getElementById("plist");
          while (list.hasChildNodes()) {
              list.removeChild(list.childNodes[0]);
          }
          //list.style.display = "block";
          for(var i = 0; i < json.playlist.length; i++){
            var item = document.createElement("li");
            item.style = list.style;
            //item.style.float = "bottom";
            //item.innerHTML = json.playlist[i];
            item.appendChild(document.createTextNode(json.playlist[i]));
            list.appendChild(item);
          }
          if(playlist.length == 1){
            playVideo(getPlayer(),playlist[playIdx]);
          }
      }
  }
  var data = JSON.stringify({"id": jukebox_id,
                           "link": textfield.value});
  xhr.send(data);
  textfield.value="";
}

function updateStats(UpDown,jukebox_id,csrf_token){
  xhr = new XMLHttpRequest();
  var url = "http://localhost:8000/jukebox/update_stats";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-type", "application/json");
  xhr.setRequestHeader('X-CSRF-Token', csrf_token);

  xhr.onreadystatechange = function () { 
      if (xhr.readyState == 4 && xhr.status == 200) {
          var json = JSON.parse(xhr.responseText);
       console.log("I am updating the stats: " + json.SomeData);
      }
  }
  var data = JSON.stringify({"stat": UpDown,"id": jukebox_id});
  xhr.send(data);
}