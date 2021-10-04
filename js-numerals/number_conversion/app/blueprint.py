from flask import Blueprint, render_template, request
import numpy
import requests, re 

calculate_number = Blueprint('calculate_number', __name__, static_folder='static', template_folder='numbers/templates')


@calculate_number.route('/', methods=['POST', 'GET'])
def api():
    # Method to render the html page
    if request.method == 'GET':
        return render_template("index.html")
    else:
        num1 = request.form['numbers']
        result = convert_number(num1)
        return render_template('index.html', result=result)


def convert_number(number):
    number = number.strip(' ')
    number = list(number)
    print(number)
    word = []
    if len(number) > 6:
        number2 = number[:-6]
        print(number2)
        if len(number2) == 3:
            hundred = test_hundreds(number2[0])
            print('here3')
            word.append(hundred)
        elif len(number2) == 2:
            number2.insert(0,0)
        else:
            number2.insert(0,0)
            number2.insert(0,0)
        if int(number2[1]) != 0:
            print(number2[0])
            print('here4')
            if int(number2[0]) != 0:
                word.append(' and ')
                print('here')
            if int(number2[2]) != 0:
                decimals = test_decimals(number2[-2:])
                print(number2[-2:])
                word.append(decimals)
            else:
                decimals = test_round_decimals(number2[1])
                print(number2[1])
                word.append(decimals)
        if int(number2[1]) == 0 and int (number2[2]) != 0 and int(number2[0]) != 0:
            word.append(' and ')
            print('here2')
        if int(number2[2]) != 0 and int(number2[1]) != 1:
            units = test_units(number2[2])
            print(number2[2])
            word.append(units)
        word.append(' million ')
    if len(number) > 3:
        if len(number) == 9:
            number3 = number[3:9]
        elif len(number) == 8:
            number3 = number[2:8]
        elif len(number) == 7:
            number3 = number[1:7]
        elif len(number) == 5:
            number3 = number
            number3.insert(0,0)
        elif len(number) == 4:
            number3 = number
            number3.insert(0,0)
            number3.insert(0,0)
        else:
            number3 = number
        number3 = number3[:-3]
        print(number3)
        print('here9')
        if int(number[0]) != 0:
            hundred = test_hundreds(number3[0])
            print(number3)
            word.append(hundred)
        print(number3)
        if int(number3[1]) != 0:
            if int(number3[0]) != 0 and int(number3[1]) != 0 and int(number3[2]) != 0:
                word.append(' and ')
                print('here7')
                print(number3)
            if int(number3[2]) != 0:
                decimals = test_decimals(number3[-2:])
                print(number3[-2:])
                print('here8')
                word.append(decimals)
            else:
                decimals = test_round_decimals(number3[1])
                print(number3[1])
                print('here9')
                word.append(decimals)
        if int(number3[2]) != 0 and int(number3[1]) == 0 and int(number3[0]) != 0:
            word.append(' and ')
            print('here5')
            print(number3[2])
            units = test_units(number3[2])
            word.append(units)
        if int(number3[2]) != 0 and int(number3[1]) != 1:
            print(number3[2])
            units = test_units(number3[2])
            word.append(units)
        if int(number3[0]) !=0 or int(number3[1]) or int(number3[2]):
            word.append(' thousand ')
    if len(number) >= 3:
        number4 = number[-3:]
        print(number4[0])
        if number4[0] != 0:
            hundred = test_hundreds(number4[0])
            print(hundred)
            word.append(hundred)
    elif len(number) == 2:
        number4 = number
        number4.insert(0,0)
        print('here10')
        print(number4)
    else:
        number4 = number
        number4.insert(0,0)
        number4.insert(0,0)
    if int(number4[1]) != 0:
        if number4[0] != 0:
            word.append(' and ')
        if int(number4[2]) != 0:
            decimals = test_decimals(number4[-2:])
            number4[-2:]
            print('here11')
            word.append(decimals)
        else:
            decimals = test_round_decimals(number4[1])
            word.append(decimals)
    
    values = ''.join(map(str, number))

    if int(number4[1]) == 0 and int(number4[2]) != 0 and int(values) > 9:
        print(number4[0:1])
        word.append(' and ')
    if int(number4[2]) != 0 and int(number4[1]) != 1:
        units = test_units(number4[2])
        word.append(units)
    print(word)
    sentence = ''.join(word)
    return sentence


            
def test_units(number):
    print(number)
    if number == '0':
        return ''
    elif number == '1':
        return 'one'
    elif number == '2':
        return 'two'
    elif number == '3':
        return 'three'
    elif number == '4':
        return 'four'
    elif number == '5':
        return 'five'
    elif number == '6':
        return 'six'
    elif number == '7':
        return 'seven'
    elif number == '8':
        return 'eight'
    elif number == '9':
        return 'nine'


def test_round_decimals(number):
    print(number)
    if number == '0':
        return ''
    elif number == '1':
        return 'ten'
    elif number == '2':
        return 'twenty'
    elif number == '3':
        return 'thirty'
    elif number == '4':
        return 'forty'
    elif number == '5':
        return 'fifty'
    elif number == '6':
        return 'sixty'
    elif number == '7':
        return 'seventy'
    elif number == '8':
        return 'eighty'
    elif number =='9':
        return 'ninety'

def test_decimals(number):
    print(number)
    if number[0] == '0':
        return ''
    elif number[0] == '1':
        result = test_tens(number)
        return result
    elif number[0] == '2':
        return 'twenty-'
    elif number[0] == '3':
        return 'thirty-'
    elif number[0] == '4':
        return 'forty-'
    elif number[0] == '5':
        return 'fifty-'
    elif number[0] == '6':
        return 'sixty-'
    elif number[0] == '7':
        return 'seventy-'
    elif number[0] == '8':
        return 'eighty-'
    elif number[0] == '9':
        return 'ninety-'

def test_tens(number):
    print(number)
    if number[1] == '0':
        return ''
    if number[1] == '1':
        return 'eleven'
    elif number[1] == '2':
        return 'twelve'
    elif number[1] == '3':
        return 'thirteen'
    elif number[1] == '4':
        return 'fourteen'
    elif number[1] == '5':
        return 'fifteen'
    elif number[1] == '6':
        return 'sixteen'
    elif number[1] == '7':
        return 'seventeen'
    elif number[1] == '8':
        return 'eighteen'
    elif number[1] == '9':
        return 'nineteen'

def test_hundreds(number):
    print(number)
    print(type(number))
    if number == '0':
        return ''
    elif number == '1':
       return 'one hundred'
    elif number == '2':
        return 'two hundred'
    elif number == '3':
        return 'three hundred'
    elif number == '4':
        return 'four hundred'
    elif number == '5':
        return 'five hundred'
    elif number == '6':
        return 'six hundred'
    elif number == '7':
        return 'seven hundred'
    elif number == '8':
        return 'eight hundred'
    elif number == '9':
        return 'nine hundred'