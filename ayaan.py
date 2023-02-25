import os, platform

def Run():

        bit = platform.architecture()[0]

        if bit == '64bit':

            import ARYAN64

        elif bit == '32bit':

            import BD32

Run()
