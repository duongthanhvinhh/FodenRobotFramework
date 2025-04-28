
# Just image you have some code here, to add 2 items to your cart
total_items_in_cart = 2
assert(total_items_in_cart == 2)
if  total_items_in_cart != 2:
    raise Exception("Product cart count not matching")

# try catch
try:
    with open('data/text.txt') as reader:
        reader.read()
except Exception as e:
    print(e)

# Or can custom exception
# except:
#     print("Something went wrong, could not open the file")
finally:
    print("Cleaning up resources")