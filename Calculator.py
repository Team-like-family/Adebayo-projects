#!/usr/bin/env python
# coding: utf-8

# # calculator

# In[150]:


def calculator():
    count = 0
    while True:
        try:
            fill_box1 = float(input("FIRST NUMBER: "))
            fill_box2 = float(input("SECOND NUMBER: "))
        except:
            print("You are not entry number!")
            break
        calculate = input("+, -, *, /? ENTERED: ")
        if (calculate == calculate):
            if calculate == "+":
                addition = fill_box1 + fill_box2
                print(f"ADDITION ANSWER >>> {addition}")
            elif calculate == "-":
                subtraction = fill_box1 - fill_box2
                print(f"SUBTRACTION ANSWER >>> {subtraction}")
            elif calculate == "*":
                multiplication = fill_box1 * fill_box2
                print(f"MULTIPLICATION ANSWER >>> {multiplication}")
            elif calculate == "/":
                division = fill_box1 / fill_box2
                print(f"DIVISION ANSWER >>> {division}")                  
            else:
                print("You have input invalid operation!!")
        condition = input("Do you want to do calculate again? ").upper()
        if condition == "YES":
            count += 1
            print(f"Done calculation {count}")
        else:
            break
                


calculator()


# In[ ]:




