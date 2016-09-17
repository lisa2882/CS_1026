def landscape():
    result = ""

    def flat(size):
        for count in range(0, size, 1):
            result += "_"

    def mountain(size):
        result += "/"
        for count in range(0, size, 1):
            result += "'"
        result += "\\"

    flat(1)
    mountain(7)
    flat(1)
    mountain(2)
    flat(2)
    return result

print(landscape())
