import sys, doctest, os, glob
from getopt import gnu_getopt as getopt

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CUR_DIR)

if __name__ == '__main__':
    run_level = None
    optlist, args = getopt(sys.argv[1:], "l:", ['--level='])
    
    for opt, arg in optlist:
        if opt in ("-l", "--list"):
            run_level = arg.zfill(2)
    
    # Test each package
    if run_level is None:
        test_files = glob.glob('%s/*.txt' % os.path.join(CUR_DIR, 'tests'))        
    else: 
        test_files = glob.glob('%s/%s-*.txt' % \
            (os.path.join(CUR_DIR, 'tests'), run_level))
    
    test_files = map(lambda i: i[len(CUR_DIR)+1:], test_files)

    # Run the tests
    for fname in test_files:
        print 'Running "%s"...'%(os.path.splitext(os.path.split(fname)[-1])[0])
        doctest.testfile(fname)

    print 'Finished!'

