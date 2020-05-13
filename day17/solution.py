def solution(phone_book=None):
    answer = True
    if not isinstance(phone_book, list):
        return answer

    phone_book.sort()
    phone_book_size = len(phone_book)-1
    for i in range(phone_book_size):
        j = len(phone_book[i])
        if phone_book[i][:j] == phone_book[i+1][:j]:
            answer = False

    return answer
