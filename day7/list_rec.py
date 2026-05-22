xoxo=[11,22,33,44,55,66,77,88,99,110]
def print_list(list,idx):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
#xoxo=[11,22,33,44,55,66,77,88,99,110]
print_list(xoxo,0)