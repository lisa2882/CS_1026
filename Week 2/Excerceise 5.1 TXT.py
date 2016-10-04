#exploring concept of scope
x = 1
if :
    y = 2
    if :
        print("block 2")
    print("block1")
else: print("block 0")

# note that the """ means that every new line of code
# within the string will by default be printed on a new line
# The """ creates a triple quoted block
big = """This is
... a multi line block
... of text; Python puts
... an end-of-line marker
... after each line."""
print(big)
print( "And then he said,  \"No way\" when I told him''" )
