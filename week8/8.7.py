def album_creator(artist, title):
    album_creator = {'artist': artist.title(),
'title': title.title()}
    return album_creator

print(album_creator("SUPXR", "MISFIRE"))
print(album_creator("SUPXR", "High Five"))