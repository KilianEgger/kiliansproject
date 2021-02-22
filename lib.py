#function checks if you get which is the best football club in the world

def try_me():
    x = input("What's the most amazing football club in the word (by far!)? ")
    y = x.lower()
    if len(x) < 4:
        x = input("Which football club do you mean? Please enter its full name. ")
        y = x.lower()
    if 'bayern' not in y:
        return f"No way! {x} sucks so much! And you know that! Bayern München is a 100 times better. "
    else:
        return "Yeah Baby, Bayern München is the greatest club ever!!!"
