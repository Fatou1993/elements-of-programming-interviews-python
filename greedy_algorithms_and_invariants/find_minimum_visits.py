from collections import namedtuple

def find_minimum_visits(intervals):

    intervals.sort(key=lambda x : x.end)
    n = len(intervals)
    idx = 0
    minimum_set = []
    while idx < n :
        hour = intervals[idx].end
        idx+=1
        while idx < n and intervals[idx].start <= hour <= intervals[idx].end :
            idx+=1
        minimum_set.append(hour)
    return minimum_set

if __name__ == "__main__":
    Interval = namedtuple("Interval", ("start", "end"))
    intervals = [Interval(1,2), Interval(2,3), Interval(3,4), Interval(2,3), Interval(3,4), Interval(4,5)]
    print(find_minimum_visits(intervals))