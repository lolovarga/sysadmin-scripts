import sys, commands

''' {master} ~/sysadm/sysadmin-scripts$  python count_files.py /tmp
[('Laura', 13415098), ('csaba198', 40914), ('root', 2940), ('syntyma', 217)]
'''

def get_totals(rows):
    '''ls -l lines look like:
    -rw-rw-r-- 1 Laura Laura  356 Oct 14 12:12 input.py
    -rw-rw-r-- 1 Laura Laura   56 Oct 14 09:14 README.md
    -rw-rw-r-- 1 Laura Laura  230 Oct 14 11:26 search.py
    -rw-rw-r-- 1 Laura Laura 1048 Oct 14 09:14 tcp.py
    -rw-rw-r-- 1 Laura Laura  891 Oct 14 10:32 url_redirect.py
    '''
    users = {}
    for row in rows:
        if row.startswith('-'):
            fields = row.split()
            username, filesize = fields[2], fields[4]
            if username not in users:
                users[username] = 0
            users[username] += int(filesize)
        userlist = users.items()
        userlist = sorted(userlist, key=lambda x:x[1], reverse=True)
    return userlist

if __name__ == '__main__':
    file_rows = commands.getoutput('ls -l ' + sys.argv[1])
    user_totals = get_totals(file_rows.split('\n'))
    print user_totals
