import os
import time
from tokenize import blank_re
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


def Binput(message="", Input_type=str, error_message="", clear=False, delay=0,
           func=False, **kwargs):
    """
    I recommend to write all arguments if you want to callback a func,
    for the function arguments you have to assign var to values, like :
    Binput(message=..., ..., delay=..., func=function to callback, func_args="hahahahahaha", other_func_args="test")
    For the Input_type and func argument, you have to write them without ""
    """
    try:
        return Input_type(input(message))
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
            print(f"You didn't write an {type(Input_type).__name__} !")
            
        if func:
            func(**kwargs)
        
def Bprint(text, speed=0):
    """
    BetterPrint : print(text, speed=0)
    text can be a str, so it will print letters by letters the text, with a waiting time
    (speed) between
    Or text can be a list, you can put several words, the last one is the delay between every printing of items of your list 
    If you want to remove the last item just write your can put just before the delay (in your list) "repalce"
    ex: Bprint(["First item in my list", "an other one", "other", "replace", 2])
    """
    
    if Btype(text) == "list":   # if you want to write some words and replace them one by one,
                                # or add a delay between every words
                                
        if Btype(text[-1]) == "int":
            delay = int(text[-1])
            text.pop(-1)
        
        if text[-1] == "replace":
            text.pop(-1)
            
            for i in text:
                blank = ""
                for _ in range(len(i)):
                    blank += " "
                p(blank, end="\r")
                for l in i:
                    p(l, end="", flush=True)
                    time.sleep(speed)
                    
                time.sleep(delay)
                p("", end="\r")
                
        else:
            for i in text:
                for l in i:
                    p(l, end="", flush=True)
                    time.sleep(speed)
                p(" ", end="")
                time.sleep(delay)
                
    else:
        for i in text:
            p(i, end="", flush=True)
            time.sleep(speed)
            
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
    return input(text)

def p(*objects, sep=' ', end='\n', flush=False):
    print(*objects, sep=sep, end=end, flush=flush)

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