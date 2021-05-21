#!/usr/bin/env python3

# Created by: Ethan Gravelle
# Created on: May 19, 2021
# This program gives all the RGB numbers


def main():
   # this function gives all the RGB numbers
   red = 0
   green = 0
   blue = 0
   
   # process & output
   for red in range(0, 256):
        for green in range(0, 256):
            for blue in range(0, 256):
                print("RGB ({0}, {1}, {2})".format(red, green, blue))


if __name__ == "__main__":
    main()
