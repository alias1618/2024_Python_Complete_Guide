# LBYL approach

# def safe_divide_1(x, y):
#     if y == 0:
#         print("Divide by 0 attempt detected.")
#         return None
#     else:
#         return x / y
    
# EAFP (Easier to ask forgiveness then permission)

# def safe_divide_2(x, y):
#     try:
#         return x / y
#     except ZeroDivisionError:
#         print("Divide by 0 attempt detected.")
#         return None
    
# This is not real codes

#LBYL approach

# def save_a_file():
#     result = safe_prefd()
#     if result == 'error':
#         print("Preference not saved.")
#         return
#     result = save_text()
#     if result == 'error':
#         print("Not enough memory")
#         return
#     result = save_format()
#     if result == 'error':
#         print("Format not saved.")
#         return
    
# EAFP

# def save_a_file():
#     try:
#         save_prefs()
#         save_text()
#         save_format()
#     except:
#         print("Something went wrong...")