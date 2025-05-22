class bank:
    bank_name = "my bank"  # Class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name


if __name__ == "__main__":
   
   user1 = bank()
   user2 = bank()
   
   print("before change bank_name")
   print(user1.bank_name)  # Output: my bank

   bank.change_bank_name("sindh bank")

   print("after change bank_name")
   print(user1.bank_name)  # Output: sindh bank