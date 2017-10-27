import eyed3
Podcast_Number = "59"
Podcast_Number2 = 59
Podcast_Title = 'Jerry is Back!'

Podcast_File_Name = "aap0" + Podcast_Number + ".mp3"
Podcast_FullTitle = "#0" + Podcast_Number + " - " + Podcast_Title
Podcast_Artist = "Admin Admin Podcast"
Podcast_Album = "www.AdminAdminPodcast.co.uk"
Podcast_Year = "2017"
Podcast_Track = Podcast_Number
print(Podcast_FullTitle)
print(Podcast_File_Name)

audiofile = eyed3.load(Podcast_File_Name)
if (audiofile.tag == None):
    audiofile.initTag()
audiofile.tag.artist = unicode(Podcast_Artist)
audiofile.tag.album_artist = unicode(Podcast_Album)
audiofile.tag.title = unicode(Podcast_FullTitle)
audiofile.tag.track_num = Podcast_Number2
audiofile.tag.images.set(3, open('adminadminlogo.png','rb').read(), 'image/jpeg')
audiofile.tag.save()
