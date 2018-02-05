def majority_search(input_stream):
    candidate = None
    count = 0
    for it in input_stream :
        if it != candidate :
            count -= 1
            if count <= 0 :
                count = 1
                candidate = it
        else:
            count += 1
    return candidate

if __name__ == "__main__":
    input_stream = ["b","a","c","a","a","b","a","a","c","a"]
    print(majority_search(input_stream))




