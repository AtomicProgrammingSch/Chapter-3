quotations = []
finished = False
while True:
    print("Please enter one of your favourite quotations:")
    quote = input()
    quotations.append(quote)
    resp = False
    while True:
        print("Do you have another favourite quotation? (y/n)")
        reply = input()
        if reply == "y":
            break
        elif reply == "n":
            quote_string = ""
            count = 1
            for quote in quotations:
                quote_string += "\n" + str(count) + ") " + quote
                count += 1
            print("Your favourite quote(s) are:" + quote_string)
            finished = True
            break
    if finished:
        break
