def strbin(s):
        return ''.join(format(ord(i),'0>8b') for i in s)
