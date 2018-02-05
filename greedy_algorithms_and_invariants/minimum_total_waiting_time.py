def minimum_total_waiting_time(service_times):
    waiting_time = 0
    n = len(service_times)
    service_times.sort()
    cummulativeTime = 0
    for i in range(n):
        waiting_time+=cummulativeTime
        cummulativeTime+=service_times[i]
    return waiting_time

if __name__ == "__main__":
    service_times = [2,5,1,3]
    print(minimum_total_waiting_time(service_times))