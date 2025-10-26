def album_creator(artist, title, tracks=None):
    album = {'artist': artist.title(),
'title': title.title()}
    if tracks:
        album['tracks'] = tracks
    return album

print(album_creator("SUPXR", "MISFIRE", 1))
print(album_creator("SUPXR", "High Five"))