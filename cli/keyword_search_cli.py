import argparse
import json
import string

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()
    table = str.maketrans("", "", string.punctuation)

    with open("data/movies.json") as file:
        movies = json.load(file)

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            results = []

            stop=[]
            with open("stopwords.txt") as file:
                stop = file.read().split()
            
            for movie in movies["movies"]:
                new_query = args.query.lower().translate(table).split()
                new_title = movie["title"].lower().translate(table).split()

                match_found = False

                for query_word in new_query:
                    for title_word in new_title:
                        if query_word in title_word:
                            match_found = True
                            break

                    if match_found:
                        break

                if match_found:
                    results.append(movie)

            for i, movie in enumerate(results, start=1):
                print(f"{i}. {movie['title']}")

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()