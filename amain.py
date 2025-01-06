import sys
import aiohttp
import asyncio
import json
from aimdb_graphql_search import IMDbGraphQL

# Код как выше...

async def main():
    if len(sys.argv) < 2:
        print("Movie name:")
        return

    movie_name = sys.argv[1]  # Получаем название фильма из аргументов командной строки
    client = IMDbGraphQL()
    try:
        suggestions = await client.search_movie(movie_name)
        for movie in suggestions:
            print(json.dumps(movie, indent=2))
    except aiohttp.ClientError as e:
        print(f"SOme error: {e}")

if __name__ == "__main__":
    asyncio.run(main())