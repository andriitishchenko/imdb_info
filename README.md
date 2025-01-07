# imdb_info
imdb playground


**Server enpoint**: https://api.graphql.imdb.com/

Search query:
```
{
  suggestionSearch(
    first: 8
    searchTerm:"robocop"
  ) {
    edges {
      node {
        id
        titleTypeId
        videoCount
        rank
        displayLabels{
          primaryLabel
          secondaryLabel
        }
        releaseYear{
          year
        }
        image{
          url
        }
      }
    }
  }
}
```

Get info by ID query:
```
{
  title(id: "tt0093870") {
    id
    originalTitleText {
      text
    }
    releaseYear {
      year
    }  
    ratingsSummary{
      aggregateRating
    }
    titleText{
      text
    }
  }
}
```

### Examples

```
#!/bin/sh
movie_name="robocop"

curl 'https://api.graphql.imdb.com/' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Connection: keep-alive' \
  -H 'DNT: 1' \
  --data-binary "{\"query\":\"{ suggestionSearch(first: 8, searchTerm:\\\"$movie_name\\\") { edges { node { id titleTypeId videoCount rank displayLabels { primaryLabel secondaryLabel } releaseYear { year } image { url } } } } }\"}" \
  --compressed
```

```
#!/bin/sh
movie_id="tt0093870"

curl 'https://api.graphql.imdb.com/' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Connection: keep-alive' \
  -H 'DNT: 1' \
  --data-binary "{\"query\":\"{ title(id: \\\"$movie_id\\\") { id originalTitleText { text } releaseYear { year } ratingsSummary { aggregateRating } titleText { text } } }\"}" \
  --compressed
```

### alternative suggestions

```
#!/bin/sh

stupid_movie_name="Your Movie Name Here"
formatted_movie_name=$(echo "$stupid_movie_name" | sed 's/ /_/g')
curl "https://v3.sg.media-imdb.com/suggestion/x/${formatted_movie_name}.json?includeVideos=1"
```
