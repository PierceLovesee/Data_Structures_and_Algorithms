# python3
# Pierce Lovesee
# February 15th, 2021

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    """  Implementation of Rabin-Karp algorithm for searching text for matching
    key words
    Inputs:
    pat: pattern of text you are searching for
    txt: entire text being searched

    Outputs:
    list of integers corisponding to the index values in 'txt' where 'pat'
    matches at the first letter of 'pat'	"""

    matches = []  # empty list for holding indexes of matching words
    P = 13441  # large prime number
    d = 256  # num. chars in english alphabet
    h = pow(d, len(pattern) - 1, P)

    # Calculate the hash value of pattern and first window of text
    p = 0
    t = 0
    for i in range(len(pattern)):
    	p = (d*p + ord(pattern[i])) % P
    	t = (d*t + ord(text[i])) % P

    # slide the pattern over text one by one
    for i in range(len(text)-len(pattern)+1):
    	if p==t: # compare hash values
    		if pattern == text[i:i+len(pattern)]:  # compare actual strings
    			matches.append(i)  # if a match, record index of first char
    	if i < (len(text) - len(pattern)):
    		t = (d*(t-ord(text[i])*h) + ord(text[i+len(pattern)])) % P
    		if t < 0:  # ensure positive hash value
    			t = t + P
    return(matches)

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
