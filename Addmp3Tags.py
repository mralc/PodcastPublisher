import eyed3

Podcast_Number = 5555

Podcast_Number_Formatted = str( Podcast_Number )
Number_Length = len( Podcast_Number_Formatted )
Zero_Padding = 3 - Number_Length
if Zero_Padding < 0 : 
	Zero_Padding = 0
Podcast_Number_Formatted = ( "0" * Zero_Padding ) + Podcast_Number_Formatted

Podcast_Title = 'Jerry is Back!'
Podcast_File_Name = "aap" + Podcast_Number_Formatted + ".mp3"
Podcast_FullTitle = "#" + Podcast_Number_Formatted + " - " + Podcast_Title
Podcast_Artist = "Admin Admin Podcast"
Podcast_Album = "www.AdminAdminPodcast.co.uk"
Podcast_Year = "2017"
Podcast_Track = Podcast_Number # This is never used, Podcast_Number is used in the tag
print(Podcast_FullTitle)
print(Podcast_File_Name)

audiofile = eyed3.load(Podcast_File_Name)
if (audiofile.tag == None):
    audiofile.initTag()
audiofile.tag.artist = unicode(Podcast_Artist)
audiofile.tag.album_artist = unicode(Podcast_Album)
audiofile.tag.title = unicode(Podcast_FullTitle)
audiofile.tag.track_num = Podcast_Number
audiofile.tag.images.set(3, open('adminadminlogo.png','rb').read(), 'image/jpeg')
audiofile.tag.save()
