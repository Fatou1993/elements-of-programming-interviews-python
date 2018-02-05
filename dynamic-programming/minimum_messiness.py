def minimum_messiness(words, line_length):
    n = len(words)
    num_remaining_blanks = line_length - len(words[0])
    min_messiness = ([num_remaining_blanks*num_remaining_blanks] + [float('inf')]*(n-1))
    for i in range(1,n):
        num_remaining_blanks = line_length - len(words[i]) #place words[i] in new line
        min_messiness[i] = num_remaining_blanks**2 + min_messiness[i-1]
        #try to move some previous words
        for j in reversed(range(i)):
            num_remaining_blanks -= (len(words[j]) + 1)
            if num_remaining_blanks < 0 :
                break
            first_j = 0 if j - 1 < 0 else min_messiness[j-1]
            current_line_mesiness = num_remaining_blanks ** 2
            min_messiness[i] = min(min_messiness[i], first_j + current_line_mesiness)
    return min_messiness[-1]

def solution_minimum_messiness(words, line_length):
    num_remaining_blanks = line_length - len(words[0])
    min_messiness = ([num_remaining_blanks**2] + [float('inf')]*(len(words)-1))
    for i in range(1,len(words)):
        num_remaining_blanks = line_length - len(words[i])
        min_messiness[i] = min_messiness[i-1]+num_remaining_blanks**2
        for j in reversed(range(i)):
            num_remaining_blanks -= len(words[j]) + 1
            if num_remaining_blanks < 0 :
                break
            first_j_messiness = 0 if j - 1 < 0 else min_messiness[j-1]
            current_line_mesiness = num_remaining_blanks**2
            min_messiness[i] = min(min_messiness[i], first_j_messiness+current_line_mesiness)
    return min_messiness[-1]


if __name__ == "__main__":
    words = ["I", "have", "inserted", "a", "large", "number", "of", "new", "examples", "from", "the", "papers",
             "for", "the", "Mathematical", "Tripes", "during", "the", "last", "twenty", "years,", "which", "should",
             "be", "useful", "to", "Cambridge", "students."]
    line_length = 36
    print(minimum_messiness(words, line_length))
    print(solution_minimum_messiness(words, line_length))


