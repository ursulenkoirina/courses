def check_dict_by_id(value_id,data):
    new_dict = None
    for i in data:
        if i.get('id') == value_id:
            new_dict = i
    return new_dict

if __name__ =="__main__":
    pass