# Small program written by Fums to auto install BlockTheSpot over new Spotify version

import zipfile, os, requests, psutil


for proc in psutil.process_iter():

    if proc.name() == "Spotify.exe":
        proc.terminate()
        

zipPath = os.getenv('APPDATA')+ "\Spotify" + "\chrome_elf.zip"
spotifyPath = os.getenv('APPDATA')+ "\Spotify"
spotifyExePath = os.getenv('APPDATA')+ "\Spotify" + "\Spotify.exe"
print (f"Loaded Spotify directory: {zipPath}")

r = requests.get("https://github.com/mrpond/BlockTheSpot/releases/latest/download/chrome_elf.zip")  
with open(zipPath, 'wb') as f:
    f.write(r.content)
print ("Downloaded new release from GitHub repo (mrpond/BlockTheSpot)")


with zipfile.ZipFile(zipPath, 'r') as zip_ref:
    zip_ref.extractall(spotifyPath)
print ("Applied BlockTheSpot, starting Spotify")

os.remove(zipPath)
os.startfile(spotifyExePath)
print ("Finished! BlockTheSpot is now ready, you're good to go!")
