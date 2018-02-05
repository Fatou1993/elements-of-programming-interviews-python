def get_max_trapped_water(heights):
    max_water = 0
    start, end = 0, len(heights)-1
    while start < end :
        max_water = max(max_water, (end-start)*min(heights[start], (heights[end])))
        if heights[start] < heights[end]:
            start+=1
        else:
            end-=1
    return max_water

if __name__ == "__main__":
    heights = [1,1]
    print(get_max_trapped_water(heights))