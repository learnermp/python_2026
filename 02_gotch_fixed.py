# bad_append_demo.py
def bad_append(new_item, a_list=None):
    if a_list is None:
        a_list = []
    a_list.append(new_item)
    return a_list


if __name__ == "__main__":
    print(bad_append('one'))
    print(bad_append('two'))