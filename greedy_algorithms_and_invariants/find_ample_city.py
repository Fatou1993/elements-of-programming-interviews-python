MPG = 20

def find_ample_city(gallons, distances):
    n = len(distances)
    totalSum = cumSum = 0
    for i in range(n):
        totalSum += gallons[i] - distances[i]/MPG
    idx=0
    for i in range(n):
        cumSum += gallons[i] - distances[i]/MPG
        if totalSum - cumSum > totalSum :
            idx=i+1
            cumSum = 0
    return idx

if __name__ == "__main__":
    gallons = [10,50,20,5,30,25,10]
    distances = [100,900,600,200,400,600,200]
    print(find_ample_city(gallons, distances))





