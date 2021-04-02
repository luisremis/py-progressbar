import time

# In the root of the repo,
# do "pip3 install ." to make the module/package available
from progressbar import ProgressBar

def main():

    pb = ProgressBar.ProgressBar()
    # pb = ProgressBar("progres.txt")

    total = 10
    for x in range(total):
        pb.update(x/total)
        time.sleep(1)
    pb.update(1)

if __name__ == "__main__":
    main()
