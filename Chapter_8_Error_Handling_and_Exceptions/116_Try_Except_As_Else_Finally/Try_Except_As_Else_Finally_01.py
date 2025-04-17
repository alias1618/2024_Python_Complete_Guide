try:
    result = 10 + "10"
except:
    print("Error... something went wrong")
finally:
    print(result)