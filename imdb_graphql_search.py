

import requests
import json


class IMDbGraphQL:
    def __init__(self):
        """
        Initialize the IMDbGraphQL client.
        """
        self.suggestion_endpoint = "https://v3.sg.media-imdb.com/suggestion/x/"
        self.graphql_endpoint = "https://api.graphql.imdb.com/"
        self.headers = {
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Connection": "keep-alive",
            "DNT": "1",
            "Origin": "https://www.imdb.com",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        }

    def search_movie(self, movie_name):
        """
        Search for movies by name and return a list of movie details.

        Args:
            movie_name (str): The name of the movie to search.

        Returns:
            list: A list of movie details dictionaries.
        """
        # Format movie name for IMDb suggestion API
        formatted_name = movie_name.replace(" ", "_")
        url = f"{self.suggestion_endpoint}{formatted_name}.json?includeVideos=1"
        
        # Fetch suggestions
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        suggestions = response.json().get("d", [])

        movie_results = []

        # Loop through the suggestions and collect movie details
        for suggestion in suggestions:
            if suggestion.get("qid") == "movie":
                movie_id = suggestion.get("id")
                movie_title = suggestion.get("l")
                movie_image = suggestion.get("i", {}).get("imageUrl")
                release_year = suggestion.get("y")
                
                # Get additional movie details like rating
                movie_details = self.get_movie_details(movie_id)

                movie_results.append({
                    "id": movie_id,
                    "title": movie_title,
                    "rating": movie_details.get("rating"),
                    "image": movie_image,
                    "release_year": release_year
                })

        return movie_results

    def get_movie_details(self, movie_id):
        """
        Fetch detailed information about a movie by its ID.

        Args:
            movie_id (str): The IMDb ID of the movie (e.g., "tt10919420").

        Returns:
            dict: The movie's rating and other details.
        """
        query = f"""
        {{
            title(id: "{movie_id}") {{
                ratingsSummary {{
                    aggregateRating
                }}
            }}
        }}
        """
        response = requests.post(
            self.graphql_endpoint,
            headers=self.headers,
            json={"query": query},
        )
        response.raise_for_status()
        data = response.json().get("data", {}).get("title", {})
        return {
            "rating": data.get("ratingsSummary", {}).get("aggregateRating"),
        }


if __name__ == "__main__":
    movie_name = "stupid movie name"  # Replace this with a dynamic input if needed

    client = IMDbGraphQL()
    try:
        suggestions = client.search_movie(movie_name)

        for movie in suggestions:
            # Print formatted JSON result for each movie suggestion
            print(json.dumps(movie, indent=2))
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")