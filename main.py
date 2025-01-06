import argparse
from imdb_graphql_search import IMDbGraphQL
import json

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Search for a movie on IMDb")
parser.add_argument("movie_name", type=str, help="The name of the movie to search for")
args = parser.parse_args()

# Create an instance of IMDbGraphQL
client = IMDbGraphQL()

# Search for the movie and get the result
try:
    result = client.search_movie(args.movie_name)
    print("Formatted Movie Data:")
    print(json.dumps(result, indent=2))
except Exception as e:
    print(f"An error occurred: {e}")