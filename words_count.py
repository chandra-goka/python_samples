def word_count(string):
    counts = dict()
    words = string.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else :
            counts[word] = 1
    return counts
# Opening data.txt file in read only mode
document_text = open('data','r')
text_string = document_text.read().lower()
print("Distinct Words and their frequency")
print(word_count(text_string))