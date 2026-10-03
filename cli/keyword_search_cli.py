import argparse
import json

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()
    
    with open("data/movies.json") as file:
        movies = json.load(file)
    match args.command:
        case "search":
            print(f'Searching for: {args.query}')
            results = []
            for movie in movies["movies"]:
                if args.query in movie["title"]:
                    results.append(movie)
            for i, movie in enumerate(results, start=1):
                print(f"{i}.{movie['title']}")
                if i == 5:
                    break
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()