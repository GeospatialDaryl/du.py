#!/usr/bin/python3
# from:
#https://stackoverflow.com/questions/1392413/
import subprocess

def du(path):
    """disk usage in human readable format (e.g. '2,1GB')"""
    return subprocess.check_output(['du','-sh', path]).split()[0].decode('utf-8')

if __name__ == "__main__":
    print(du('.'))
# from:
#https://stackoverflow.com/questions/1392413/