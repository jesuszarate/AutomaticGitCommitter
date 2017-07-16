
def getPassword(file = 'Committer/password.txt'):
    with open(file, 'r') as f:
        p = f.readline().split(':')
        if p[0] == 'password':
            return p[1]
        else:
            raise ValueError('Incorrect format of file')