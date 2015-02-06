def is_palindrome(n):
    str_num = str(n)
    check_lo = 0
    check_hi = len(str_num) - 1

    while check_hi >= check_lo:
        if str_num[check_hi] != str_num[check_lo]:
            return False
        check_hi -= 1
        check_lo += 1
    return True

start_num = 999
prod_array = []
current_num = 0

while start_num > 0:
    dec_num = start_num
    while dec_num > 0:
        current_num = start_num * dec_num
        if is_palindrome(current_num):
            prod_array.append(current_num)
        dec_num -= 1
    start_num -= 1

print(max(prod_array))