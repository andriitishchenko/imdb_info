# imdb_info
imdb playground



### Suggestions:


```
#!/bin/sh

stupid_movie_name="Your Movie Name Here"
formatted_movie_name=$(echo "$stupid_movie_name" | sed 's/ /_/g')
curl "https://v3.sg.media-imdb.com/suggestion/x/${formatted_movie_name}.json?includeVideos=1"
```

Extract movie ID
```
curl -s "https://v3.sg.media-imdb.com/suggestion/x/The_Dark_Knight.json?includeVideos=1" | jq -r '.d[] | select(.qid == "movie") | .id' | head -n 1
```


```
curl "https://v3.sg.media-imdb.com/suggestion/x/stupid_movie_name.json?includeVideos=1"
{"d":[{"i":{"height":1800,"imageUrl":"https://m.media-amazon.com/images/M/MV5BMTg2MjkwMTM0NF5BMl5BanBnXkFtZTcwMzc4NDg2NQ@@._V1_.jpg","width":1215},"id":"tt1570728","l":"Crazy, Stupid, Love.","q":"feature","qid":"movie","rank":742,"s":"Steve Carell, Ryan Gosling","v":[{"i":{"height":478,"imageUrl":"https://m.media-amazon.com/images/M/MV5BMjA0MTY2NzgwMl5BMl5BanBnXkFtZTcwMzYzNDg4NA@@._V1_.jpg","width":640},"id":"vi3722091801","l":"Crazy, Stupid, Love.","s":"2:32"},{"i":{"height":720,"imageUrl":"https://m.media-amazon.com/images/M/MV5BYzUyM2M2N2EtYTA3Ni00YjVhLTkxZjUtMTczNGMyNjMxZTEzXkEyXkFqcGdeQXRyYW5zY29kZS13b3JrZmxvdw@@._V1_.jpg","width":1280},"id":"vi208977945","l":"'Crazy, Stupid, Love.' | Anniversary Mashup","s":"1:34"}],"vt":24,"y":2011},{"i":{"height":1344,"imageUrl":"https://m.media-amazon.com/images/M/MV5BNDUxY2RlODctNTc0Ni00NDcyLTk4NDQtMjQyYmJiOTJlYjFkXkEyXkFqcGc@._V1_.jpg","width":1078},"id":"tt21652514","l":"Stupid Wife","q":"TV series","qid":"tvSeries","rank":28098,"s":"Priscila Reis, Priscila Buiar","v":[{"i":{"height":676,"imageUrl":"https://m.media-amazon.com/images/M/MV5BMjE4NTQ4Y2QtODY4My00NzczLWEyMDEtMGY2YTAzYWViMmFjXkEyXkFqcGdeQXRyYW5zY29kZS13b3JrZmxvdw@@._V1_.jpg","width":1280},"id":"vi243253785","l":"Trailer Season 1 [OV]","s":"1:47"}],"vt":1,"y":2022,"yr":"2022-2024"},{"i":{"height":2048,"imageUrl":"https://m.media-amazon.com/images/M/MV5BMTg3OTQyODAwOF5BMl5BanBnXkFtZTgwMDY1MDM0NDM@._V1_.jpg","width":1382},"id":"tt5566790","l":"A Futile and Stupid Gesture","q":"feature","qid":"movie","rank":12269,"s":"Frank Gingerich, Morgan Gingerich","y":2018},{"i":{"height":675,"imageUrl":"https://m.media-amazon.com/images/M/MV5BNDM4OWIxMDktMDEwMC00NzIyLWIwYjQtZTFmN2VjYTM1YzcyXkEyXkFqcGc@._V1_.jpg","width":1200},"id":"tt0499408","l":"Stupid","q":"TV series","qid":"tvSeries","rank":66565,"s":"Rusty Goffe, Travis Yates","y":2004,"yr":"2004-2006"},{"i":{"height":819,"imageUrl":"https://m.media-amazon.com/images/M/MV5BNzFjNzZmODQtZDBlZC00YmI3LTkxOTUtOTViOGMwMmQzMzcwXkEyXkFqcGc@._V1_.jpg","width":1024},"id":"tt1842178","l":"Stupid for Dexter","q":"TV series","qid":"tvSeries","rank":34049,"s":"Kat Steel, Mike Rotman","y":2010,"yr":"2010-2011"},{"i":{"height":6000,"imageUrl":"https://m.media-amazon.com/images/M/MV5BNjhmZjE2YzMtYjhhYy00N2I3LWE1MmQtYTU0OTMzNzg5Zjg0XkEyXkFqcGc@._V1_.jpg","width":4000},"id":"tt27703758","l":"Stupid Games","q":"feature","qid":"movie","rank":39697,"s":"Saad Rolando, Gage Robinson","y":2024},{"i":{"height":1200,"imageUrl":"https://m.media-amazon.com/images/M/MV5BMmJhY2VhY2EtZmQzNS00ZGEwLWFiZTMtMzRmNWJiYjE1ZWQ3XkEyXkFqcGc@._V1_.jpg","width":800},"id":"tt0101821","l":"Ernest Scared Stupid","q":"feature","qid":"movie","rank":18002,"s":"Jim Varney, Eartha Kitt","y":1991},{"i":{"height":750,"imageUrl":"https://m.media-amazon.com/images/M/MV5BYjY3MzhjYjMtZTg2Yi00NjU5LThkNDMtNDJiNWMxNGI4NGY2XkEyXkFqcGc@._V1_.jpg","width":500},"id":"tt0058265","l":"Kiss Me, Stupid","q":"feature","qid":"movie","rank":26427,"s":"Dean Martin, Kim Novak","y":1964}],"q":"stupid","v":1}% 
```
##### Filter by "qid":"movie"


### GraphQL
```
curl 'https://api.graphql.imdb.com/' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Connection: keep-alive' -H 'DNT: 1' -H 'Origin: chrome-extension://kjhjcgclphafojaeeickcokfbhlegecd' --data-binary '{"query":"{\n  title(id: \"tt10919420\") {\n    id\n    originalTitleText {\n      text\n    }\n    releaseYear {\n      year\n    }  \n    ratingsSummary{\n      aggregateRating\n    }\n    titleText{\n      text\n    }\n  }\n}"}' --compressed
{"data":{"title":{"id":"tt10919420","originalTitleText":{"text":"Ojing-eo geim"},"releaseYear":{"year":2021},"ratingsSummary":{"aggregateRating":8},"titleText":{"text":"Squid Game"}}},"extensions":{"disclaimer":"Public, commercial, and/or non-private use of the IMDb data provided by this API is not allowed. For limited non-commercial use of IMDb data and the associated requirements see https://help.imdb.com/article/imdb/general-information/can-i-use-imdb-data-in-my-software/G5JTRESSHJBBHTGX#","experimentalFields":{"janet":[]}}}
```



```
#!/bin/sh
movie_id="tt0468569"

curl 'https://api.graphql.imdb.com/' \
  -H 'Accept-Encoding: gzip, deflate, br' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Connection: keep-alive' \
  -H 'DNT: 1' \
  -H 'Origin: chrome-extension://kjhjcgclphafojaeeickcokfbhlegecd' \
  --data-binary "{\"query\":\"{\n  title(id: \\\"$movie_id\\\") {\n    id\n    originalTitleText {\n      text\n    }\n    releaseYear {\n      year\n    }  \n    ratingsSummary{\n      aggregateRating\n    }\n    titleText{\n      text\n    }\n  }\n}\"}" \
  --compressed
```

