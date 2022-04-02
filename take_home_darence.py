

class Person:
    """
    Object of each person with his/her info, created and housed in WorkShop
    """
    def __init__(self, first: str, last: str, street: str, city: str, state: str, age: int):
        """
        Unpack list of info for Person attributes

        :param first: first name
        :param last: last name
        :param street: street address
        :param city: city address
        :param state: state abbreviation address
        :param age: Person's current age
        """
        self.__first_name = first
        self.__last_name = last
        self.__street = street
        self.__city = city
        self.__state = state
        self.__age = age
    
    @property
    def last_name(self) -> str:
        """
        Getter for age, accessed in Workshop.print_results()

        :return: person's last name
        :rtype: str
        """
        return self.__last_name
    
    @property
    def address(self) -> str:
        """
        Getter for age, accessed in Workshop.add_single_entry()

        :return: person's address
        :rtype: str
        """
        return ', '.join([self.__street, self.__city, self.__state])
        
    @property
    def age(self) -> int:
        """
        Getter for age, accessed in Workshop.print_results()

        :return: person's age
        :rtype: int
        """
        return self.__age
    
    def __lt__(self, other) -> bool:
        """
        Less than comparison overload to allow sorting by order of last name then first name

        :param other: another person being compared to
        :param type: Person
        :return: whether this object is less than another person by lexicographical order
        :rtype: bool       
        """    
        if not isinstance(other, Person): raise TypeError("Can only accept Person object")
        elif self.__last_name < other.__last_name: return True
        elif self.__last_name == other.__last_name and self.__first_name < other.__first_name: return True
        return False
    
    def __gt__(self, other) -> bool:
        """
        Greater than comparison overload to allow sorting by order of last name then first name

        :param other: another person being compared to
        :param type: Person
        :return: whether this object is greater than another person by lexicographical order
        :rtype: bool       
        """    
        if not isinstance(other, Person): raise TypeError("Can only accept Person object")
        elif self.__last_name > other.__last_name: return True
        elif self.__last_name == other.__last_name and self.__first_name > other.__first_name: return True
        return False

    def __str__(self) -> str:
        """
        For printing out attributes of Person

        :return: attributes in a string
        :rtype: str       
        """
        return f'{self.__last_name}, {self.__first_name}, {self.__street}, {self.__city}, {self.__state}, Age {self.__age}'

    def __repr__(self) -> str:
        """
        Attributes of Person

        :return: attributes in a string
        :rtype: str  
        """
        return f'{self.__last_name}, {self.__first_name}, {self.__street}, {self.__city}, {self.__state}, Age {self.__age}'


class WorkShop:
    """
    Shop for creating Person entries, sort and print
    """
    def __init__(self):
        """
        Constructor to house the dictionary of households:
        self.__households = {address: list[Person]} 
        """
        self.__households = {}

    @property
    def households(self) -> list:
        """
        Access households for testing purposes

        :return: dictionary of households by addresss
        :rtype: dict {str: list[str, int]}
        """
        return self.__households

    def add_single_entry(self, data: str) -> None:
        """
        Call parser to process data then create single Person object and 
        add to self.__households grouped by unique address

        :param data: string of information to create a Person
        :param type: str
        :return: None.
        """
        new_entry = self.__parser(data)
        person = Person(*new_entry)
        if person.address in self.__households:
            self.__households[person.address].append(person)
        else:
            self.__households[person.address] = [person]  

    def add_multiple_entries(self, data: str) -> None:
        """
        Separate raw string of multiple people's information

        :param data: multi-line str of multiple people's information
        :param type: str
        :return: None.
        """
        data_list = data.splitlines()
        for line in data_list:
            self.add_single_entry(line)      
            
    def __parser(self, data: str) -> list:
        """
        Verifies each part of an entry for correct formating and errors

        :param data: string of raw information about one person
        :param type: str
        :return: list of a person's information formatted appropriately
        :rtype: list [str, int]
        """
        data = data.strip('"').split('","')
        data_parsed = []
        for index, value in enumerate(data):
            # first name, last name, city
            if index in (0, 1, 3): value = value.capitalize()
            # street
            elif index == 2:
                value = value.split()
                # street name
                value[1] = value[1].capitalize()
                # St or Blvd
                value[2] = value[2].capitalize()
                    # includes apt
                if len(value) > 3 and value[2][-2:] != '.,':
                    value[2] = value[2].rstrip('.') + '.,'
                elif len(value) == 3 and value[2][-1] != '.': 
                    value[2] += '.'
                value = ' '.join(value)
            # state abbreviation
            elif index == 4: value = value.upper()
            # age
            elif index == 5: value = int(value)

            data_parsed.append(value)
        return data_parsed

    def print_results(self) -> None:
        """
        Create structure for printing solution, first header of household and & occupants,
        then each person over 18 in that household

        :return: None.
        """
        for family in self.__households.values():
            # last names for household title
            last_names = {}
            for person in family:
                if person.last_name not in last_names:
                    last_names[person.last_name] = 0
            last_names = ' and '.join(list(last_names))
            print(f'\n{last_names} household has {len(family)} occupants, person(s) over 18 are:')

            # only print persons over 18
            over_18 = [person for person in family if person.age > 18]
            if len(over_18) > 1: over_18 = WorkShop.heap_sort(over_18)
            elif over_18 == []: over_18 = ["None"]
            for person in over_18:
                print(person)

    @staticmethod
    def heap_sort(family: list) -> list:
        """
        Adapted heapsort from https://favtutor.com/blogs/heap-in-python

        :param family: list of family members
        :param type: list [Person]
        :return: sorted list of family members
        :rtype: list [Person]
        """
        array = family
        n = len(array)

        def heapify(array: list, n: int, i: int) -> None:
            """
            Part of heapsort. Heapify 'bubbles' values down to keep a heap structure with minimum root

            :param array: list of persons
            :param n: length of list
            :param i: root index
            """
            smallest = i  
            left_child = 2 * i + 1     
            right_child = 2 * i + 2     
            if left_child < n and array[smallest] < array[left_child]: smallest = left_child
            if right_child < n and array[smallest] < array[right_child]: smallest = right_child

            if smallest != i:
                array[i], array[smallest] = array[smallest], array[i] 
                heapify(array, n, smallest)

        for i in range(n // 2 - 1, -1, -1):
            heapify(array, n, i)

        for i in range(n-1, 0, -1):
            array[i], array[0] = array[0], array[i]  
            heapify(array, i, 0)
        return array

if __name__ == "__main__":
    input_data = '''"Dave","Smith","123 main st.","seattle","wa","43"
"Alice","Smith","123 Main St.","Seattle","WA","45"
"Bob","Williams","234 2nd Ave.","Tacoma","WA","26"
"Carol","Johnson","234 2nd Ave","Seattle","WA","67"
"Eve","Smith","234 2nd Ave.","Tacoma","WA","25"
"Frank","Jones","234 2nd Ave.","Tacoma","FL","23"
"George","Brown","345 3rd Blvd., Apt. 200","Seattle","WA","18"
"Helen","Brown","345 3rd Blvd. Apt. 200","Seattle","WA","18"
"Ian","Smith","123 main st ","Seattle","Wa","18"
"Jane","Smith","123 Main St.","Seattle","WA","13"'''

    w = WorkShop()
    w.add_multiple_entries(input_data)
    w.print_results()

# END