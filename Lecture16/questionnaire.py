#!/usr/bin/python3

def main():
    dict_answers = {}

    while True:
        try:
            prompt_name = str(input("What's your name? ").strip()).title()
            dict_answers["name"] = prompt_name
            break
        except ValueError:
            print("Invalid name")
    
    while True:
        try:
            prompt_age = int(input("How old are you? ").strip())
            if prompt_age <= 0:
                raise ValueError
            dict_answers["age"] = prompt_age
            break
        except ValueError:
            print("Invalid age")
    
    while True:
        try:
            prompt_colour = str(input("What is your favourite colour? ").strip()).title()
            dict_answers["favourite_colour"] = prompt_colour
            break
        except ValueError:
            print("Invalid colour")
    
    while True:
        try:
            prompt_py = str(input("Do you like Python? ").strip()).lower()
            if prompt_py not in ["yes", "no"]:
                raise ValueError
            prompt_py = prompt_py == "yes"
            dict_answers["like_python"] = prompt_py
            break
        except ValueError:
            print("Yes or No?")

    while True:
        try:
            prompt_bool = str(input("The world is flat: True or False? ").strip()).lower()
            if prompt_bool not in ["true", "false"]:
                raise ValueError
            prompt_bool = prompt_bool == "true"
            dict_answers["world_flat"] = prompt_bool
            break
        except ValueError:
            pass

    print(f"Your name is {dict_answers['name']}")
    print(f"You are {dict_answers['age']} years old")
    print(f"Your favourite colour is {dict_answers['favourite_colour']}")
    print(f"You like Python!") if dict_answers["like_python"] else print(f"You do NOT like Python.")
    print(f"You are a flat-earther.") if dict_answers["world_flat"] else print(f"You are NOT a flat-earther!")


if __name__ == "__main__":
    main()
