# version = 1.0

# SHADOWpy

# sys_xmath
# sys_xmetric
# sys_xdate
# sys_xrefer
# sys_xfile



####    math   ####
import math# for sys_xmath
import pyautogui # for sys_metrics
from datetime import date # for date access
import random # for sys_xrandom function
from collections import namedtuple
from os import *
###################

class sys_xmath():

    ###############   BIT   ################

        def x_NOT(value):
            return ~ value

        def x_OR(value_1,  value_2):
            return value_1 | value_2

        def x_XOR(value_1, value_2):
            return value_1 ^ value_2

        def x_LS(value_1, value_2):
            return value_1 << value_2

        def x_RS(value_1, value_2):
            return value_1 >> value_2 

        def x_AND(value_1, value_2):
            return value_1 & value_2

    #############   num_sys   ##############

        def x_bin(value):
            return bin(value) [2:]

        def x_oct(value):
            return oct(value) [2:]

        def x_hex(value):
            return hex(value) [2:]

    ##############   basic   ##############

        def x_sum(*value):
            num = 0
            for number in value:
               num = num + number
            return num

        def x_sub(value_1, value_2):
            return value_1 - value_2
            

        def x_mul(value_1, value_2):
            return value_1 * value_2

        def x_div(value_1, value_2):
            return value_1 /  value_2

        def x_rem(value_1, value_2):
            return value_1 % value_2

    ##############  ADV  ###############
        def x_sq(value):
            return value * value
        
        def x_sqrt(value):
            return math.sqrt(value)

        def x_isqrt(value):
            return math.isqrt(value)

        def xceil(value):
            return math.ceil(value)

        def x_floor(value):
            return math.floor(value)

        def x_factorial(value):
            return math.factorial(value)

        def x_gcd(value_1,  value_2):
            return math.gcd(value_1, value_2)

        def x_exp(value):
            return math.exp(value)

        def x_fmod(value_1, value_2):
            return math.fmod(value_1, value_2)

        def x_copysign(value_1, value_2):
            return math.copysign(value_1, value_2)

        def x_fabs(value):
            return  math.fabs(value)

        def x_pow(value_1, value_2):
            return math.pow(value_1, value_2)

        def x_fsum(value, *value_1):
            return math.fsum(value)

        def x_prod(value):
            return math.prod(value)

        def x_isnan(value):
            return math.isnan(value)

        def x_isfinite(value):
            return math.isfinite(value)

        def x_isclose(value_1, value_2):
            return math.isclose(value_1, value_2)

        def x_degrees(value):              # 1
            return math.degrees(value)

    ##################################

class sys_xmetrics():
  
    def x_metrics():
         width, height = pyautogui.size()
         metrics = namedtuple('metrics', 'width, height')
         tuple = metrics._make([width,  height])
         return tuple
        
    def x_width():
        width, height = pyautogui.size()
        metrics = namedtuple('metrics', 'width')
        tuple = metrics._make([width])
        return tuple
    def x_height():
        width, height = pyautogui.size()
        metrics = namedtuple('metrics','height')
        tuple = metrics._make([height])
        return tuple

    def x_height_single():
        width, height = pyautogui.size()
        return height

    def x_width_single():
        width, height = pyautogui.size()
        return width

############################################


#############   EXPLAIN  ###################

class sys_xrefer():

    def x_properties():
        classes = "anchor = ['sys_xmath()','sys_xmetrics()', 'sys_xdate()', 'sys_xrefer()', 'sys_xrandom()']"
        return classes

    def x_method(class_name):
        return dir(class_name)

############################################
############################################

class sys_xdate():
    def x_date():
        today  = date.today()
        return today

    def x_year():
        today = date.today()
        return today.year

    def x_month():
        today = date.today()
        return today.month

    def x_day():
        today = date.today()
        return today.day

    def x_age(birth_year, current_year):
        if birth_year > current_year:
            format = birth_year - current_year
            return format

        else:
            default = current_year - birth_year
            return default

###########################################
###########################################

class sys_xrandom():
    def x_choice(list):
        return random.choice(list) 

    def x_randint(value_1, value_2):
        return random.randint(value_1, value_2)

    def x_shuffle(lst):
        return random.shuffle(lst)
 
    def x_randrange(start, end):
        return random.randrange(start, end)
    
    def x_uniform(float_num_1, float_num_2):
        return random.uniform(float_num_1, float_num_2)

    def x_random():           # 2
        return random.random()

    def x_choices(lst):            # 3
        return random.choices(lst)
###########################################