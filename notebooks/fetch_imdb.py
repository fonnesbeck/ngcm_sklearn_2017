import os

try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen

import tarfile


IMDB_URL = "http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
IMDB_ARCHIVE_NAME = "aclImdb_v1.tar.gz"


def check_imdb(datasets_folder = "../data/"):
    print("\nChecking availability of the IMDb dataset")
    archive_path = os.path.join(datasets_folder, IMDB_ARCHIVE_NAME)
    imdb_path = os.path.join(datasets_folder, 'IMDb')

    train_path = os.path.join(imdb_path, 'aclImdb', 'train')
    test_path = os.path.join(imdb_path, 'aclImdb', 'test')

    if not os.path.exists(imdb_path):
        if not os.path.exists(archive_path):
            print("Downloading dataset from %s (84.1MB)" % IMDB_URL)
            opener = urlopen(IMDB_URL)
            open(archive_path, 'wb').write(opener.read())
        else:
            print("Found archive: " + archive_path)

        print("Extracting %s to %s" % (archive_path, imdb_path))

        tar = tarfile.open(archive_path, "r:gz")
        tar.extractall(path=imdb_path)
        tar.close()
        os.remove(archive_path)

    print("Checking that the IMDb train & test directories exist...")
    assert os.path.exists(train_path)
    assert os.path.exists(test_path)
    print("=> Success!")


if __name__ == "__main__":
    check_imdb("../data/")
