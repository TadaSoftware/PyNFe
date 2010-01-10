import sys, doctest, os, glob

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CUR_DIR)

if __name__ == '__main__':
    # Test each package
    test_files = glob.glob('%s/*.txt' % os.path.join(CUR_DIR, 'tests'))
    test_files = map(lambda i: i[len(CUR_DIR)+1:], test_files)

    # Run the tests
    for fname in test_files:
        doctest.testfile(fname)

