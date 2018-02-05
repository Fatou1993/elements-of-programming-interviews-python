from collections import namedtuple

Segment = namedtuple("Segment", ("start", "end", "color", "height"))
def view_from_above(segments):
    n = len(segments)
    result = []
    if not n :
        return result
    interval_start = interval_end = segments[0]
    for i in range(1,n):
        if segments[i].start < interval_start.end : #overlap
            if segments[i].height > interval_start.height:
                result.append(Segment(interval_start.start, segments[i].start, interval_start.color, interval_start.height))
                interval_start = segments[i]
        else:
            result.append(Segment(interval_start.start, interval_start.end, interval_start.color, interval_start.height))
            if interval_start.end < interval_end.end : #there is space to fill
                if interval_start.end !=  min(segments[i].start, interval_end.end):
                    result.append(Segment(interval_start.end, min(segments[i].start, interval_end.end), interval_end.color, interval_start.height))
                if interval_end.end > segments[i].start and interval_end.height > segments[i].height :
                    interval_end = Segment(segments[i].start, interval_end.end, interval_end.color, interval_end.height)
                    interval_start = interval_end
                else:
                    interval_start = segments[i]
        if segments[i].end > interval_end.end :
                interval_end = segments[i]
        result.append(interval_start)
        if interval_end.end > interval_start.end :
            result.append(Segment(interval_start.end, interval_end.end, interval_end.color, interval_end.height))
    return result


if __name__ == "__main__":
    segments = [Segment(0,4,"A",1), Segment(1,3,"B",3), Segment(2,7,"C",2), Segment(4,5,"D",4),
                Segment(5, 7, "E", 1), Segment(6,10,"F",3), Segment(8,9,"G",2), Segment(9,18,"H",1),
                Segment(11, 13, "I",3), Segment(12,15,"J",2), Segment(14,15,"K",3), Segment(16,17,"L",3)]
    res = view_from_above(segments)
    for s in res :
        print s