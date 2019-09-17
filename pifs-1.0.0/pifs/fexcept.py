import argparse

def ferror():
    try:
        parser = argparse.ArgumentParser(help= "help")
    except:
        print("> pifs-upload -f {filename}    use to upload file")
        print("> pifs-download -f {filename} -k {key}   use to downloadfile" + "\n")
        print("-f, --filename    use to input filename")
        print("-k, --key    use to input key" + "\n")
