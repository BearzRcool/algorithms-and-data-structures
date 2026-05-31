


def reverse(n, text, ):
    if n == 0:
        return
    print(text[n-1], end = '')
    reverse(n-1,text)
reverse(5, "hello")

def reverse_answer(text):
    if len(text) <= 1:
        return text
    return reverse_answer(text[1:]) + text[0]

print("\n" + reverse_answer("hello"))
