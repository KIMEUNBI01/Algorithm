# 백준 1181 김은비

import sys

N = int(input()) #단어의 개수
Word = [input() for i in range(N)] #알파벳 소문자로 이루어진 단어

Word = list(set(Word)) #중복 단어 제거
Word.sort(key=lambda x: (len(x), x)) #길이순 -> 사전순 정렬 

for i in Word:
    print(i)