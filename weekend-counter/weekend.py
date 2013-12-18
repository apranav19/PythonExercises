from datetime import date, timedelta

def checkio(from_date, to_date):
    tot_days = (to_date - from_date).days + 1
    return len(filter(is_weekend, [(from_date + timedelta(d)).weekday() for d in xrange(tot_days)]))

def is_weekend(weekday):
    return (weekday == 5 or weekday == 6)
        

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2
    print checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8
    print checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2