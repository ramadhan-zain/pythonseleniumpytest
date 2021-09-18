items_in_cart = 0
# 2 items will be added to cart

if items_in_cart != 2:
    # raise Exception("Product Cart Count not matched")
    pass

# assert(items_in_cart == 2)

# try, catch
try:
    with open('filelog.txt', 'r') as reader:
    # with open('test.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(f"failure no file\n python error message: {e}")

finally:
    print("cleaning up records")
    # we can delete the cookies here
    # even the task failed and or succeed