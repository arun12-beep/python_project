str=input("enter a string:")
alpha_count=0
digit_count=0
sp_char_count=0
alpha_lst=[]
digit_lst=[]
sp_char_lst=[]
for s in str:
    if s.isalpha():
        alpha_count+=1
        alpha_lst.append(s)
    elif s.isdigit():
        digit_count+=1
        digit_lst.append(s)
    else:
        sp_char_count+=1
        sp_char_lst.append(s)

print("Input string:",str)
print(f"alphabets in string are:",alpha_lst)
print(f"No of alphabets count in string: {alpha_count}")
print(f"digits in string are: {digit_lst}")
print(f"No of digits count in string: {digit_count}")
print(f"special characters in string are: {sp_char_lst}")
print(f"No of special character count in string: {sp_char_count}")
