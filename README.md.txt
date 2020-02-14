# Bad Vibes

During the excellent [Cultured Data Symposium](https://cultureddata.net/) 2020, [Tobin Chodos](http://www.tobinchodos.com/) said something like "Spotify's recommenders are so random that I think you could throw a negative sign in front and end up with similar quality."

### Challenge Accepted!

Make a bad Spotify recommender. Like, the worst. Bad vibes anti-recommendations.

This is currently very much a proof of concept.  It grabs your top 50 songs (long-term), and then does a "farthest neighbor recommendation" based on the audio features Spotify provides.  I restricted myself to the [2019 global most streamed tracks](https://www.kaggle.com/prasertk/spotify-global-2019-moststreamed-tracks), so I couldn't pick total shit.

Though, to be honest, that *NYSYNC Christmas song is pretty rough.

You can play with it at http://badplaylist.com

## Future <s>Plans</s> Ideas

* Non-collaborative filtering.  (Adversarial Filtering?)
* Use [Spotify's recommendation API]((https://developer.spotify.com/documentation/web-api/reference/browse/get-recommendations/)) with a bad seed?


### Links

* [Spotipy: python SDK](https://spotipy.readthedocs.io/en/2.7.0/)
* [Authorization Scopes](https://developer.spotify.com/documentation/general/guides/scopes/)