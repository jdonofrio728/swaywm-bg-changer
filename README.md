# swaywm-bg-changer
Simple python program to rotate background images on sway outputs

## Usage
This program takes a directory as the only required input. That directory can have a number of images which the program will rotate through randomly. The program is quite alpha and does not do much of any sanity checking.
```
#: python swaywm-bg-changer --help
usage: swaywm-bg-changer [-h] [-d] [-t TIMEOUT] bg_dir

positional arguments:
  bg_dir                Path to directory containing images

optional arguments:
  -h, --help            show this help message and exit
  -d, --daemon          Daemonize the process
  -t TIMEOUT, --timeout TIMEOUT
                        How often to change background images in minutes
```
