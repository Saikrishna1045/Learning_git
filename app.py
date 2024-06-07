import time
print("this is my fourth version in the cloud champ")
start = time.time()
word_list = ['Cristiano', ',', ' Ratan Tata',' and',' SK', ' are', ' my', ' inspiration.']
# for word in word_list:
#     new_list += word
new_list1 = "".join(word_list)
print(new_list1)
print(time.time() -start, 'seconds')