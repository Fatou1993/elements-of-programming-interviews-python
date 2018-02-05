def is_match(regex, s):
    if not regex :
        return True
    n = len(s)
    regex_end_index = len(regex)
    if regex[-1] == "$": #we will look to elements up to end
        regex_end_index -= 1
    regex_start_index, string_end_index = 0, n
    if regex[0] == "^":
        regex_start_index += 1
        string_start_index = 0
        return is_match_helper(regex, s, regex_start_index, regex_end_index, string_start_index, string_end_index)
    else:
        for i in range(n):
            string_start_index = i
            if is_match_helper(regex, s, regex_start_index, regex_end_index, string_start_index, string_end_index):
                return True
        return False


def is_match_helper(regex, s, regex_start_index, regex_end_index, string_start_index, string_end_index):
    
    if regex_start_index == regex_end_index : #regex totally matched
        return regex[-1] != "$" or string_start_index == string_end_index

    if string_start_index == string_end_index : #regex not matched
        return False

    if regex[regex_start_index] == "^" or regex[regex_start_index] == "$" :
        raise ValueError("invalid regex expression")

    if regex[regex_start_index] == "*" and (regex_start_index == 0 or (regex[regex_start_index-1] != "." and not regex[regex_start_index-1].isalnum())):
        raise ValueError("invalid regex expression")

    if regex_start_index + 1 < len(regex) and regex[regex_start_index+1] == "*":
        return (regex[regex_start_index] == "." or regex[regex_start_index] == s[string_start_index]) and is_match_helper(regex, s, regex_start_index, regex_end_index, string_start_index+1, string_end_index) \
               or is_match_helper(regex, s, regex_start_index+2, regex_end_index, string_start_index, string_end_index)
    else:
        return (regex[regex_start_index] == "." or regex[regex_start_index] == s[string_start_index]) and is_match_helper(regex, s, regex_start_index+1, regex_end_index, string_start_index+1, string_end_index)

if __name__ == "__main__":
    regex = "aW9"
    candidate_strings = ["aW9", "aW9bcW", "ab8aW9", "cc2aW9raW9z", "aW8", "bcd8", "xy"]
    for string in candidate_strings :
        print string, regex, is_match(regex, string)
    print ""
    regex = "a.9."
    candidate_strings = ["ab9w", "ac9bcW", "ab8a999", "cc2aW9r", "az9", "a989a", "bac9"]
    for string in candidate_strings:
        print string, regex, is_match(regex, string)

    print ""
    regex = "aW*9"
    candidate_strings = ["a9", "aW9", "aWW9b9cW", "aU9aWW9", "ab8aWWW9W9aa", "aWWU9", "baX9", "aXW9Wa"]
    for string in candidate_strings:
        print string, regex, is_match(regex, string)

    print ""
    regex = "a.*9"
    candidate_strings = ["a9", "aZ9", "aZW9b9cW", "aU9a9", "b8aWUW9W", "cc2a9raU9z", "9UWaW8", "b9aaaX", "XUq8"]
    for string in candidate_strings:
        print string, regex, is_match(regex, string)

    print ""
    regex = "^aW.9"
    candidate_strings = ["aW99zer", "aWW9", "aWP9GA", "baWx9", "aW9", "aWcc90"]
    for string in candidate_strings:
        print string, regex, is_match(regex, string)

    print ""
    regex = "aW.9$"
    candidate_strings = ["aWW9abcaWz9", "aWW9", "baaWX9", "abcaWP9", "aWW99", "aW", "aWcc90"]
    for string in candidate_strings:
        print string, regex, is_match(regex, string)

    print ""
    regex = "^aW9$"
    candidate_strings = ["aW99zer", "aWW9", "aWP9GA", "baWx9", "aW9", "aWcc90"]
    for string in candidate_strings:
        print string, regex, is_match(regex, string)