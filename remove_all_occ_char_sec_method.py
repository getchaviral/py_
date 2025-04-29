def remove_all_occ_of_char(s,char_to_remove):
    result=""
    for i in s:
        if i != char_to_remove:
            result +=i
    return result

print(remove_all_occ_of_char("abababa","b"))
