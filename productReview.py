#The aim of this assignment is to extract insights from product reviews by using
#string manipulation to categorize and summarize customer feedback for a SaaS product.

#Task 1: Keyword Highlighter

#Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average".
#Print out each review with the keywords in uppercase so they stand out.

reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ] 
keywords = ['good', 'excellent', 'bad', 'poor', 'average']
nice = ['good', 'excellent']
not_nice = ['bad', 'poor', 'average']


for review in reviews:
    modified_review = review
    for keyword in keywords:
        if keyword in modified_review:
            modified_review = modified_review.replace(keyword, keyword.upper())
        elif keyword.upper() in modified_review.upper():
            modified_review = modified_review.replace(keyword.title(), keyword.upper())
    print(modified_review)

    #Two checks for keyword as "Poor" being capitalized trips up the logic.


def posneg(choice):
    pos_tally = 0
    neg_tally = 0


    for review in reviews:
            if choice == 1:
                cur_review = review
                for keyword in nice:
                    if keyword.upper() in cur_review.upper():
                        pos_tally = pos_tally + 1
            if choice == 2:
                cur_review = review
                for keyword in not_nice:
                    if keyword.upper() in cur_review.upper():
                        neg_tally = neg_tally + 1
    return pos_tally, neg_tally

def summary(choice):
    print("\nReview", choice, "has been summarized: ")
    review = reviews[choice - 1]
    if len(review) <= 30:
        print(review)
    else:
        summary = review[:30]
        lspace = summary.rfind(' ')
        if lspace != -1:
            summary = summary[:lspace]
        print(summary + '...')

        # Found rfind() on w3schools.



#Task 2: Sentiment Tally

#Develop a function that tallies the number of positive and negative words in each review.
#Use a predefined list of positive and negative words to check against.
#The function should return the count of positive and negative words for each review.

pos_reviews = posneg(1)
neg_reviews = posneg(2)

print('\nThere are', pos_reviews[0], 'positive reviews and', neg_reviews[1], 'negative reviews. ')


#Task 3: Review Summary

#Implement a script that takes the first 30 characters of a review and appends "…" to create a summary.
#Ensure that the summary does not cut off in the middle of a word.

print("\nThe following reviews have been left: ")
for review in range(len(reviews)):
    indexnum = review
    print(indexnum+1, '.', reviews[review])

while True:
    index_choice = int(input("\nPlease enter the number of the review you wish to summarize. "))
    if index_choice <= len(reviews):
        summary(index_choice)
        break
    else:
        print("There aren't that many reviews.")
