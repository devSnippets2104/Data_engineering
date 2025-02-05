import time
string="""Hello my name is Aditya and I'm a developer having 3.5 years of experience want to lear data engineering"""


def streamLetters(letter):
    for word in letter:
        yield word


gen=streamLetters(string)

for l in gen:
    print(l, end='', flush=True)
    time.sleep(0.2)