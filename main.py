import re

#function for tokenizing a sentence based on spaces
def tokenize(text): 
    return re.findall(r'\w+', text.lower())

#opening the text file consisting of Instagram comments and reading them into a list
with open('comments.txt') as f:
    lines=[line.rstrip() for line in f]


# list of racial slurs supplied to us
racial_slurs = ["dumbfuck","bitch","moron","shit","stupid"]

for i in lines:
    count = 0
    profanity_degree = 0
    comment_token=tokenize(i)
    for word in comment_token:
        if word.lower() in racial_slurs:
            count = count + 1    
	# degree:number of occurrences normalized by total number
    profanity_degree = profanity_degree + count/len(comment_token)
    print("Comment: "+i+" profanity_degree: " + str(profanity_degree))

    	



