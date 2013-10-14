import sys
import commands

def find(pattern):
    res = commands.getoutput('/usr/bin/find ' + pattern)
    return res
    
if __name__ == '__main__':
    pattern = ' '.join(sys.argv[1:])
    files = find(pattern)
    print files
