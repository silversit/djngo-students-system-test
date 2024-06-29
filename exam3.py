store = input().split(", ")

def add_phone(phone):
    if phone in store:
        pass
    else:
        store.append(phone)

def remove_phone(phone):
    if phone not in store:
        pass
    else:
        store.remove(phone)

def bonus(phone,oldphone):
    if oldphone in store:
        index = store.index(oldphone)
        store.insert(index+1,phone)
def last_phone(phone):
    if phone in store:
        store.remove(phone)
        store.append(phone)

while True:
    commands = input()
    if "End" in commands:
        break
    else:
        command_name,phones = commands.split(" - ")
        if command_name == "Bonus phone":
            oldphone, new_phone = phones.split(":")
            bonus(new_phone,oldphone)
        if command_name == "Add":
            add_phone(phones)

        if command_name == "Remove":
            remove_phone(phones)
        if command_name == "Last":
            last_phone(phones)


print(*store, sep=", ")




