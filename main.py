def parse(string, i=0):
    letters = list(set(string))
    estring = ""
    aword = ""
    pword = ""

    while i < len(string):
        s = string[i]

        if s == "(":
            if len(aword) > 1:
                pword = "(" + " and ".join(aword) + ")"
            else:
                pword = aword

            estring += "(" + pword + " and ("
            aword = ""

            rstring, i = parse(string, i+1)

            estring += rstring

        if s == ")":
            if len(aword) > 1:
                pword = "(" + " and ".join(aword) + ")"
            else:
                pword = aword

            estring += pword + "))"
            return estring, i
        
        if s.isalpha():
            aword += s

        if s == "+":
            estring += aword + " or "
            aword = ""

        i += 1

    for s in " +()":
        letters.remove(s)

    return estring, sorted(letters)


def get_lambda(string, string_lambda=False):
    lambda_code, letters = parse(string)

    args = ", ".join(letters)

    code = f"lambda {args}: {lambda_code}"

    if string_lambda:
        return code
    else:
        return eval(code)


print(get_lambda("abd(b(c + d) + e)", string_lambda=True))
