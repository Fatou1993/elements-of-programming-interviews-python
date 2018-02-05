def calculate_largest_rectangle(heights):
    n = len(heights)
    stack = []
    maxArea = 0
    stack_length = 0
    for i in range(n) :
        if stack and heights[stack[-1]] > heights[i]:
            while stack and heights[stack[-1]] > heights[i] :
                lastIndex = stack.pop()
                stack_length -= 1
                if not stack :
                    currArea = heights[lastIndex] * (i - lastIndex) + heights[lastIndex] * lastIndex
                else:
                    currArea = heights[lastIndex]*(i - lastIndex)
                    if stack_length == 1 and lastIndex - stack[0] - 1 != 0:
                        currArea += heights[lastIndex] * (lastIndex - stack[0] - 1)
                maxArea = max(maxArea, currArea)
        stack.append(i)
        stack_length += 1
        #print(stack, maxArea)
    i = n
    while stack :
        lastIndex = stack.pop()
        if not stack:
            currArea = heights[lastIndex] * (i - lastIndex) + heights[lastIndex] * lastIndex
        else:
            currArea = heights[lastIndex] * (i - lastIndex)
        maxArea = max(maxArea, currArea)
    return maxArea

def naiveImplementation(heights):
    n = len(heights)
    maxArea = 0
    for i in range(n):
        left, right = i, i
        while left >= 0 and heights[left] >= heights[i]:
            left -= 1
        left += 1
        while right < n and heights[right] >= heights[i]:
            right += 1
        right -= 1
        # print(i, (right-left+1)*heights[i])
        maxArea = max(maxArea, (right - left + 1) * heights[i])
    return maxArea

if __name__ == "__main__":
    heights = [1,4,2,5,6,3,2,6,6,5,2,1,3]
    print(calculate_largest_rectangle(heights))