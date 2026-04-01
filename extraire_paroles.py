import argparse
import os
import lyricsgenius

genius = lyricsgenius.Genius(Token)


def exporter_contenu(fichier: str, contenu) -> None:
    with open(fichier, "w") as f:
        f.write(contenu)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("artiste", help="L'artiste dont l'on récupère les paroles")
    parser.add_argument(
        "dossier",
        help="Le chemin vers le dosser où vont être créés les différents fichies",
    )

    args = parser.parse_args()

    artist = genius.search_artist(args.artiste, max_songs=100, sort="title")

    for song in artist.songs:
        titre = song.title
        split = titre.split()
        clean_title = "_".join(split)

        fichier = clean_title + ".txt"
        chemin = os.path.join(args.dossier, fichier)

        if os.path.isfile(chemin):
            print(f"Ce fichier existe déjà: {fichier}")
            continue
        else:
            lyrics = song.lyrics
            exporter_contenu(chemin, lyrics)

    print(f"L'exportation a été effectuée vers le dossier {args.dossier} !")


if __name__ == "__main__":
    main()
