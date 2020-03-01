def firstrun():
    return "success"


def area(r):
    return 3.14 * r * r


def list(l):
    if (len(l) >= 2):
        return (l[0], l[len(l) - 1])
    elif (len(l) == 1):
        return (l[0], None)
    else:
        return (None, None)


def date(date1, date2):
    date_diff = abs(date2 - date1)
    return date_diff.days
