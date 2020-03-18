from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''
while True:
    product = input('What is your product : ')
    unit_price = Invoice().inputNumber("Please enter unit price : ")
    qnt = Invoice().inputNumber("Please enter quantity of product : ")
    discount = Invoice().inputNumber("Discount percent (%) : ")
    repeat = Invoice().inputAnswer("Another product? (y,n) : ")
    result = Invoice().addProduct(qnt, unit_price, discount)
    products[product] = result
    if repeat == "n":
        break

total_amount = Invoice().totalPurePrice(products)

print("Your total pure price is: ", total_amount)

print(Invoice().discountFormula({'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}))