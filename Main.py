from pytube import YouTube
import androidhelper

droid = androidhelper.Android()
download_list = []
downloaded_list = []
downloads = 0
link = list(droid.getClipboard()[1])
l = list(link)

p360_list = ['1', '3', '36', '360', '360p'] #list of acceptable inputs for 360p
p480_list = ['2', '4', '48', '480', '480p'] #list of acceptable inputs for 480p

while True:
    if l[0:17] == ['h','t','t','p','s',':','/','/','y','o','u','t','u','.','b','e','/']: #check if its a youtube link😉
        #print(f'{downloads} is a youtube link 👍')
        if droid.getClipboard()[1] not in downloaded_list:
             yt = YouTube(droid.getClipboard()[1])
             #print(yt.streams)
             downloaded_list.append(droid.getClipboard()[1])
             try: #try getting 360p pr 480p
                try:
                    p360 = yt.streams.get_by_resolution('360p')
                    print('got 360p')
                except:
                    p480 = yt.streams.get_by_resolution("480p")
                    p480.download() #download 480p if 360p is not available
                    
                try:
                    p480 = yt.streams.get_by_resolution("480p")
                    print('got 480p')
                except:
                    p360 = yt.streams.get_by_resolution("360p")
                    p360.download() #download 360p if 480p is not available
             except:
                 droid.makeToast(f'No preferred resolutions for {yt.title} 😔')
                 
                 
             try:
                 #print(f'360: {p360.filesize/(1024*1024)}mb')
                 #print(f'480: {p480.filesize/(1024*1024)}mb')
                 if p480 == None:
                     p360.download()
                     droid.makeToast(f'downloaded {yt.title} [{downloads}]😊')
                 elif p360 == None:
                     p480.download()
                     droid.makeToast(f'downloaded {yt.title} [{downloads}]😊')
                 elif p360 == None and p480 == None:
                     droid.makeToast(f'could not download {yt.title} [{downloads}]😔')
                 elif p360.filesize >= p420.filesize:
                    p420.download()
                    print(f'downloaded {yt.title}')
                    droid.makeToast(f'downloaded {yt.title} [{downloads}]😊')
                 else:
                    if ((p420.filesize/(1024*1024)) - (p360.filesize/(1024*1024))) <= 3: #if size difference is less than or equals 3mb
                        p420.download()
                        droid.makeToast(f'downloaded {yt.title} [{downloads}]😊')
                    else:
                        res = droid.dialogGetInput('res', 'p360:  {p360.filesize}/np420:  {p420.filesize}/np360 or p420?') #ask pf preferrence
                        while res not in p360_list or res not in p420_list:
                            res = droid.dialogGetInput('res', 'p360:  {p360.filesize}/np420:  {p420.filesize}/np360 or p420?')
                        if res in p360_list:
                            p360.download()
                            print(f'downloaded {yt.title}')
                            droid.makeToast(f'downloaded {yt.title} [{downloads}]😊')
                        if res in p420_list:
                            p420.download()
                            print(f'downloaded {yt.title}')
                            droid.makeToast(f'downloaded {yt.title} [{downloads}]😊')
             except:
                 droid.makeToast(f'An error occurred while trying to download {yt.title}') #display in case of error
                 #break #choose to stop the code or keep running it🤷‍♂️
