from json import load
import os
import time
import sys

"""
    TODO:
        ->  Bprint() with speed option
        ->  function to setup arguments that will always be the same for a function
        ->  Update docs
"""


def cls():
    """
    Function to clear console, work on Windows, MacOS and some other
    """
    if os.name in ('nt', 'dos'):
        os.system("cls")
    else:
        os.system("clear")


def Binput(Input_message = "", Input_type = "str", error_message = "", clear = False, delay = 0,
           func = False, **kwargs):
    """
    I recommend to write all arguments if you want to callback a func,
    for the function arguments you have to assign var to values, like :
    Binput(Input_message=..., ..., delay=..., func=function to callback, func_args="hahahahahaha", other_func_args="test")
    """
    try:
        return Input_type(input(Input_message))
    except:
        if clear:
            cls()
        if error_message:
            print(error_message)
            if delay > 0:
                time.sleep(delay)
        else:
            if delay > 0:
                time.sleep(delay)
            print(f"You didn't write an {Input_type.__name__} !")
        if func:
            func(**kwargs)
            
def Btype(var, print=False):
    """
    Like type()function but return the name only name of a var like: int, not <class 'int'>
    But can print automatically, or return
    """
    if print:
        print(type(var).__name__)
    else:
        return type(var).__name__

# some function to make coding faster, but not more easier to understand
def i(text):    
    input(text)

def p(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    print(*objects, sep, end, file, flush)

def loading(percentage: int):
    if percentage > 100 or percentage < 0:
        print(f"Percentage need to be between 0 and 100 !")
    else:
        load = ""
        for _ in range(int(percentage/10)):
            load += "██"
        for _ in range(20-len(load)):
            load += " "
        print(f"| {load} | {percentage}%", end="\r")