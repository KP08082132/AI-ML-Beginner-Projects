from pathlib import Path

import scipy
import pandas as pd
def load_user_artists(user_artists_file: Path) -> scipy.sparse.csr_matrix:
    
    user_artists = pd.read_csv(user_artists_file)
    user_artists.set_index(["user_id", "artist_id"], inplace=True)
    coo = scipy.sparse.coo_matrix(
        (
            user_artists.scrobbles.astype(float),
            (
                user_artists.index.get_level_values(0),
                user_artists.index.get_level_values(1),
            ),
        )
    )
    return coo.tocsr()


class ArtistRetriever:
    

    def __init__(self):
        self._artists_df = None

    def get_artist_name_from_id(self, artist_id: int) -> str:
        
        return self._artists_df.loc[artist_id, "artist_name"]

    def load_artists(self, artists_file: Path) -> None:
        
        artists_df = pd.read_csv(artists_file)
        artists_df = artists_df.set_index("artist_id")
        self._artists_df = artists_df


if __name__ == "__main__":
    user_artists_matrix = load_user_artists(Path("C:/Users/Aashu/Downloads/SongRec/lastfm_user_scrobbles.csv"))
    print(user_artists_matrix)

    artist_retriever = ArtistRetriever()
    artist_retriever.load_artists(Path("C:/Users/Aashu/Downloads/SongRec/lastfm_artist_list.csv"))
    artist = artist_retriever.get_artist_name_from_id(1)
    print(artist)