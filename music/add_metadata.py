import eyed3


def add_metadata(title):

    audiofile = eyed3.load("output/final.mp3")
    audiofile.initTag()

    audiofile.tag.artist = "Tech Star Podcast"
    audiofile.tag.album = "Mock Interviews in the Tech Industry"
    audiofile.tag.album_artist = "Tech Star Podcast"
    audiofile.tag.title = title
    audiofile.tag.track_num = 1

    audiofile.tag.save()
