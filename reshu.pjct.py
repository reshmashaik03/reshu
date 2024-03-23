class CarShowroom:
    def _init_(self):
        self.company_name = ""
        self.models = {
            "Toyota": ["Camry", "Corolla", "Prius"],
            "Honda": ["Civic", "Accord", "CR-V"],
            "Hyundai": ["Elantra", "Tucson", "Santa Fe"]
        }
        self.showroom_prices = {
            "Toyota": {"Camry": 3000000, "Corolla": 2000000, "Prius": 2500000},
            "Honda": {"Civic": 2200000, "Accord": 2800000, "CR-V": 3200000},
            "Hyundai": {"Elantra": 1800000, "Tucson": 2400000, "Santa Fe": 2900000}
        }
        self.insurance = 100000

    def company(self, company_name):
        self.company_name = company_name
        print("Welcome to the", company_name, "family")

    def model(self):
        if self.company_name in self.models:
            print("Available models for", self.company_name, "are:")
            for model in self.models[self.company_name]:
                print("-", model)
        else:
            print("Company not found.")

    def price(self, selected_model):
        if self.company_name in self.showroom_prices and selected_model in self.showroom_prices[self.company_name]:
            x_showroom_price = self.showroom_prices[self.company_name][selected_model]
            CGST = 0.18 * x_showroom_price
            SGST = 0.18 * x_showroom_price
            price = x_showroom_price + CGST + SGST + self.insurance
            print("Final on-road price for", selected_model, "is:", price)
        else:
            print("Model not found for the selected company.")


# Example usage:
showroom = CarShowroom()
showroom.company("Toyota")
showroom.model()
showroom.price("Camry")