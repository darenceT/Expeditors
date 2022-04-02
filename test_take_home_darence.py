from take_home_darence import Person, WorkShop
from io import StringIO
import sys

"""
Unit tests written to be executed by using PyTest
"""

def test_single_person_object():
    data = ['Dave', 'Smith', '123 Main St.', 'Seattle', 'WA', 43]
    p = Person(*data)
    assert isinstance(p, Person)

def test_create_single_person_entry():
    data = '"Dave","Smith","123 main st.","seattle","wa","43"'
    w = WorkShop()
    w.add_single_entry(data)
    assert len(w.households) == 1

def test_create_two_person_entry_using_single_entry():
    data1 = '"Dave","Smith","123 main st.","seattle","wa","43"'
    w = WorkShop()
    w.add_single_entry(data1)
    data2 = '"Bob","Williams","234 2nd Ave.","Tacoma","WA","26"'
    w.add_single_entry(data2)
    assert len(w.households) == 2

def test_create_two_person_entry_using_multiple_entries():
    data = '''"Dave","Smith","123 main st.","seattle","wa","43"
"Bob","Williams","234 2nd Ave.","Tacoma","WA","26"'''
    w = WorkShop()
    w.add_multiple_entries(data)
    assert len(w.households) == 2

def test_print_one_entry():
    data = '"Dave","Smith","123 main st.","seattle","wa","43"'
    w = WorkShop()
    w.add_single_entry(data)
    output = StringIO()
    sys.stdout = output
    w.print_results()
    sys.stdout = sys.__stdout__
    expected = '''\nSmith household has 1 occupants, person(s) over 18 are:
Smith, Dave, 123 Main St., Seattle, WA, Age 43'''.strip()
    assert output.getvalue().strip() == expected

def test_print_two_entry_different_address():
    data = '''"Dave","Smith","123 main st.","seattle","wa","43"
"Bob","Williams","234 2nd Ave.","Tacoma","WA","26"'''
    w = WorkShop()
    w.add_multiple_entries(data)
    output = StringIO()
    sys.stdout = output
    w.print_results()
    sys.stdout = sys.__stdout__
    expected = '''Smith household has 1 occupants, person(s) over 18 are:
Smith, Dave, 123 Main St., Seattle, WA, Age 43

Williams household has 1 occupants, person(s) over 18 are:
Williams, Bob, 234 2nd Ave., Tacoma, WA, Age 26'''.strip()
    assert output.getvalue().strip() == expected

def test_print_two_entry_same_address():
    data = '''"Dave","Smith","123 main st.","seattle","wa","43"
"Eve","Smith","123 main st.","seattle","WA","25"'''
    w = WorkShop()
    w.add_multiple_entries(data)
    output = StringIO()
    sys.stdout = output
    w.print_results()
    sys.stdout = sys.__stdout__
    expected = '''Smith household has 2 occupants, person(s) over 18 are:
Smith, Dave, 123 Main St., Seattle, WA, Age 43
Smith, Eve, 123 Main St., Seattle, WA, Age 25'''.strip()
    assert output.getvalue().strip() == expected