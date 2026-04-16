def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx <len(L) #What is the value of test on each call first: false second:true
    if test: #what is this check preventing the continuation of the code when idx is not greater than zero and less than 3
        return L[idx]
    else:
        return None
first = checked_access([1,0,1], 9) #what is the value none
second = checked_access([1,0,1], 2) #what is the value 3
print(second)

def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2]) #which call will this statement be evaluated: when the length of the list is greater than 2
    elif len(L) > 1: #what values are being added:the length of the specific values called in the list based on the index
        result = len(L[0]) + len(L[1]) # is called when the length of the list is greater than 1 and not greater than 2 and adds the length of the term called in the list based on the index called
    elif len(L) > 0: #statement is used when the length of the list is greater than zero and less than 1
        result = len(L[0]) #the result is the length of the 0th term
    else:
        result = 0
        return result

first = length = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another, call"])
print(first)


def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L
words = ["this", "is", "confusing", "code"]
first = surprising(words,"Avoid")
second = surprising(words, "such")
print(first)
print(second)
#what is the values of words at this point: all uppercase for AVOID and SUCH
#what are the values of the first and the second at this point: the lists are combined so the list becomes the words and the capital AVOID and SUCH
#what happened: created all caps for the "other" work avoid and such and combined to the list words.