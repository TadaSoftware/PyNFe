import sys, doctest, os, glob

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CUR_DIR)

PACKAGES = ('robvm','robsim','robparser','robide')

if __name__ == '__main__':
    # Packages to test
    packages = len(sys.argv) > 1 and sys.argv[1:] or PACKAGES

    # Test each package
    test_files = []
    for pkg in packages:
        test_files.append(glob.glob('%s/*.txt' % os.path.join(CUR_DIR, pkg, 'tests')))

    test_files = reduce(lambda a,b: a+b, test_files)
    test_files = map(lambda i: i[len(CUR_DIR)+1:], test_files)

    # Run the tests
    for fname in test_files:
        doctest.testfile(fname)

