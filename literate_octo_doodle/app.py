import argparse

from literate_octo_doodle import core
from literate_octo_doodle import utils
from literate_octo_doodle import configuration


def get_books(csv_output_file_path, field_names=None):
    with open(csv_output_file_path, "w") as fp:
        fp.write("")
    field_names = field_names or configuration.BOOK_FIELDS
    field_names = [f.strip() for f in field_names.split(",")]
    utils.write_csv_file(
        core.get_data({"TYPE": "Monograph"}, field_names),
        field_names, csv_output_file_path)


def get_chapters(csv_output_file_path, field_names=None):
    with open(csv_output_file_path, "w") as fp:
        fp.write("")
    field_names = field_names or configuration.CHAPTER_FIELDS
    field_names = [f.strip() for f in field_names.split(",")]
    utils.write_csv_file(
        core.get_data({"TYPE": "Part"}, field_names),
        field_names, csv_output_file_path)


def main():
    parser = argparse.ArgumentParser(description="Literate octo doodle")
    subparsers = parser.add_subparsers(
        title="Commands", metavar="", dest="command",
    )

    books_parser = subparsers.add_parser(
        "books",
        help=(
            "Get books data"
        )
    )
    books_parser.add_argument(
        "--fields",
        help=(
            "Inform field names. Use comma (,) as separator"
        )
    )
    books_parser.add_argument(
        "csv_output_file_path",
        help=(
            "/path/books.csv"
        )
    )

    chapters_parser = subparsers.add_parser(
        "chapters",
        help=(
            "Get chapters data"
        )
    )
    chapters_parser.add_argument(
        "--fields",
        help=(
            "Inform field names. Use comma (,) as separator"
        )
    )
    chapters_parser.add_argument(
        "csv_output_file_path",
        help=(
            "/path/chapters.csv"
        )
    )

    args = parser.parse_args()
    if args.command == "books":
        get_books(args.csv_output_file_path)

    elif args.command == "chapters":
        get_chapters(args.csv_output_file_path)

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
