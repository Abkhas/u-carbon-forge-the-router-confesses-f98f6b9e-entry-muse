"""The Router Confesses entry: one line, 129 characters.

The line is an excuse from a home Wi-Fi router for dropping the
connection at the climax of a movie. The router is a smug little
blackmailer: it knows the household's 2 a.m. search history and holds
every climax hostage until someone changes the password from 'password'.
"""

ONE_LINE = "I know what you searched for at 2 a.m., and I will keep dropping every climax until someone changes the password from 'password'."

OUTPUT_PATH = "/output/entry.txt"


def main():
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ONE_LINE)
    print(ONE_LINE)


if __name__ == "__main__":
    main()
