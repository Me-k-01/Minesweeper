
def save(data) :
    from pickle import dump as pDump

    try:
        with open('data.dem', 'wb') as formater:
            pDump(data, formater)
            formater.close()
    except:
        return -1 # Access error

def load():
    from pickle import load as pLoad
    try:
        with open('data.dem', 'rb') as formater:
            data = pLoad(formater)
            formater.close()
        return data
    except:
        return -1  # Didn't found the file
