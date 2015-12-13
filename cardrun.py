#!/usr/bin/python

def safe_float(obj):
    'safe version of float()'
    try:
        retval = float(obj)
    except (ValueError, TypeError), diag:
        retval = str(diag)
    return retval

def main():
    'handle all the data processing'
    log = open('cardlog.txt', 'w')
    try:
        ccfile = open('carddata.txt', 'r')
    except IOError, e:
        ccfile.write('no txns this month\n')
        ccfile.close()
    tnxs = ccfile.readlines()
    ccfile.close()
    total = 0.0
    log.write('account log\n')
    for eachTnx in tnxs:
        result = safe_float(eachTnx)
        if isinstance(result, float):
            total += result 
            log.write('data processed\n')
        else:
            log.write('ignored %s\n' % result)
    print '$%.2f (new balance)' % total
    log.close()

if __name__ == '__main__':
    main()


