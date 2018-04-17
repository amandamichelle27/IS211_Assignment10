DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS songs;

CREATE TABLE artists(
    artist_name     TEXT,
    artist_id       INT
);

CREATE TABLE albums(
    album_title     TEXT,
    album_id        INT,
    artist_id       INT,
    FOREIGN KEY ([artist_id]) REFERENCES [artists] ([artist_id]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE songs(
    song_title      TEXT,
    track_num       INT,
    length          INT,
    album_id        INT,
    FOREIGN KEY ([album_id]) REFERENCES [albums] ([album_id]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);
