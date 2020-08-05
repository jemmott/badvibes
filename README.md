# Bad Vibes

During the excellent [Cultured Data Symposium](https://cultureddata.net/) 2020, [Tobin Chodos](http://www.tobinchodos.com/) said something like "since there is no mathematically coherent measure of a "success" in music recommendation, since human love of music is so strange and capricious, you could probably reverse the logic of Spotify's recommender engine and get similarly satisfying results, perhaps more satisfying"

### Challenge Accepted!

Make a bad Spotify recommender. Like, the worst. Bad vibes anti-recommendations.

This is currently very much a proof of concept.  It grabs your top 50 songs (long-term), and then does a "farthest neighbor recommendation" based on the audio features Spotify provides.  I restricted myself to the [2019 global most streamed tracks](https://www.kaggle.com/prasertk/spotify-global-2019-moststreamed-tracks), so I couldn't pick total shit.  In other words, it is a recommender system that tries to find music that is popular, but you won't like.

Though, to be honest, that *NYSYNC Christmas song is pretty rough.

You can play with it at http://badplaylist.com

## Future <s>Plans</s> Ideas

* Non-collaborative filtering.  (Adversarial Filtering?)
* Use [Spotify's recommendation API]((https://developer.spotify.com/documentation/web-api/reference/browse/get-recommendations/)) with a bad seed?
* Alphabetical by name of band.


### Links

* [Spotipy: python SDK](https://spotipy.readthedocs.io/en/2.7.0/)
* [Authorization Scopes](https://developer.spotify.com/documentation/general/guides/scopes/)

## April 2020 Update

"The point is this.  Even if there were some objective criteria that make one artwork better than another, as long as context plays a role in our aesthetic appreciation of art, it's not possible to create a tangible measure for aesthetic quality that works for all places in all times.  Whatever statistical techniques, or artificial intelligence tricks, or machine-learning algorithms you deploy, trying to use numbers to latch on to the essence of artistic excellence is like clutching at smoke with your hands."

- Hannah Fry, "[Hello World](http://www.hannahfry.co.uk/helloworld)"
