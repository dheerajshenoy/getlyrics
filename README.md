# getlyrics
CLI lyrics program using **Python**, **playerctl**

### Dependencies 
#### 1.Python libraries required 
- BeautifulSoup / bs4
- requests 
- subprocess (Pre-Installed with standard python library)
- getopt 

#### 2. Software required to be installed 
Playerctl 
#### On Arch and related distro use the following 
``` 
sudo pacman -S playerctl 
```
#### For the Debian/Ubuntu you need the deb package. (GOOGLE IT)


### Installation 
#### 1.Install the python library using pip
```
pip install beautifulsoup4 requests optspec 
```
#### 2.Clone this repo to a folder 
```
git clone https://www.github.com/dheerajshenoy/getlyrics.git
```
#### 3.Open the getlyrics folder and run the install.sh script 
```
chmod +x install.sh && ./install.sh 
```
#### 4. Installation is done

### Usage 
#### Getting lyrics for the currently playing spotify song 
```
getlyrics 
```
### Getting lyrics for specified song 
```
getlyrics "name of the song"
```
### Uninstalling 
#### Simply run the uninstall.sh script and you're done :)
