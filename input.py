import sys

'''getting raw input from console, interactively'''
r = raw_input('type smt:')
print r
r = int(raw_input('int now!'))
print r

'''printing out all the command line arguments'''
print 'called with arguments: '
for i in sys.argv[1:]:
    print i

'''getting the data from a file given as a parameter'''
data = open(sys.argv[1]).read()
print data
