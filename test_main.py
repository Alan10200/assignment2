from inventory import Inventory
from product import Product

class TestInventory:
    def test_product_class(self):
        product = Product("Banana", 99, 100)
        assert product.stock == 99
        assert product.name == "Banana"
        assert product.price == 100

    def test_inventory_constructor(self):
        print("Running tests on inventory constructor")
        names = ["Apple", "Cucumber"]
        stocks = [55, 66]
        prices = [1.99, 2.99]
        inventory = Inventory(names, stocks, prices)

        assert inventory.get_total_products() == 2
        assert inventory.get_product(0).name == "Apple"
        assert inventory.get_product(0).stock == 55
        assert inventory.get_product(0).price == 1.99

        assert inventory.get_product(1).name == "Cucumber"
        assert inventory.get_product(1).stock == 66
        assert inventory.get_product(1).price == 2.99

        for i in range(inventory.get_total_products()):
            self.assert_product(inventory.get_product(i),names[i],stocks[i],prices[i])

    def assert_product(self, product, name, stock, price):
        print('Testing product attribute strings conversions')
        assert name in product.__str__()
        assert str(stock) in product.__str__()
        assert str(price) in product.__str__()

test = TestInventory()
test.test_inventory_constructor()
