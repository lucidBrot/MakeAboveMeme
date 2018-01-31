# MakeAboveMeme
An attempt to combine commandline inputs and images into a meme of simple format

And to learn how to use git submodules

## Dependencies
* `sudo apt-get install xvfb` or your standard x-server running
* [webkit2png](https://stackoverflow.com/a/48537053/2550406)

## Notes
To get the X-server to run with xvfb, run `Xvfb :1 &` followed by `export DISPLAY=:1` (or any other number than `:1`, as long as it is in both).
