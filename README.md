# BlockTheSpot Applier
A simple program written in Python 3.9 to apply the latest version of BlockTheSpot to the latest release of Spotify. 

## What is it?

This basic Python program makes it so when you run it, it downloads the latest version from the [BlockTheSpot repo](https://github.com/mrpond/BlockTheSpot), saves it in your Spotify folder (assumes it will be in `%AppData%/Spotify`), kills the current running Spotify process(es) and then unzips the file and reopens Spotify. All of this happens within seconds.


## Requirements

- Python 3.9 (though it may work with older versions)
- psutil (installed via CMD using command `pip install psutil`)
- Admin permissions (will automatically have them if your account is admin, this is to kill processes)
- Have the shipping release of Spotify installed to AppData (the default)


## Why?

I get annoyed when I open Spotify and the ads are back, you are supposed to update BlockTheSpot's files each time Spotify updates manually but who would want to do that? You can make this script automatically run with Spotify or you can just run it when you get the advertisements again all within seconds. 


## Disclaimer

I did NOT write / maintain the BlockTheSpot repo, this program simply access the latest release posted to the [BlockTheSpot repo](https://github.com/mrpond/BlockTheSpot) and automatically unzips it. 
