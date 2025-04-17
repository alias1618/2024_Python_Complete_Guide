import Raise_Customized_Exception_01_2

try:
    num = "We"
    Raise_Customized_Exception_01_2.enter_age(num)
except Raise_Customized_Exception_01_2.NegativeNumberException as error:
    print(error)
except:
    print("Something we don't know went wrong...")