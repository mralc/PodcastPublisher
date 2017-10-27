import ftplib
import os
Podcast_Number = "59"
curdir = "podcasts"
Podcast_File_Name = "aap0" + Podcast_Number + ".mp3"
print("Uploading:")
print(Podcast_File_Name)
ftp = ftplib.FTP("remotehost")
ftp.login("ftpaccount", "Password")
ftp.cwd(curdir)
ftp.storbinary("STOR " + Podcast_File_Name , file(Podcast_File_Name, "rb"))a
ftp.sendcmd('SITE CHMOD 640 ' + Podcast_File_Name)
ftp.quit()
