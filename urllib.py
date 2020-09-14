# Retrieving an image over HTTP with urllib is much simpler than with socket
import urllib.request
import urllib.parse
import urllib.error

# This code reads all of the data in at once. However if this is a large file,
# this program may crash or at least run extremely slowly when your computer runs out of memory.
# img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
# fhand = open('cover3.jpg', 'wb')
# fhand.write(img)
# fhand.close()

# In order to avoid running out of memory, we retrieve the data in blocks (or buffers)
# and then write each block to your disk before retrieving the next block.
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1:
        break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()
