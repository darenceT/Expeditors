

class Person:
    """

    """
    def __init__(self, first, last, street, city, state, age):
        """
    
        """
        self.__first_name = first
        self.__last_name = last
        self.__street = street
        self.__city = city
        self.__state = state
        self.__age = age
    
    @property
    def first_name(self) -> str:
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        return self.__last_name
    
    @property
    def street(self) -> str:
        return self.__street
    
    @property
    def city(self) -> str:
        return self.__city

    @property
    def state(self) -> str:
        return self.__state
    
    @property
    def address(self) -> str:
        return ', '.join([self.__street, self.__city, self.__state])
        
    @property
    def age(self) -> int:
        return self.__age
    
    def is_household(self, person) -> str:
        return self.address == person.address
    
    def __eq__(self, other) -> bool:
        pass
    
    def __lt__(self, other) -> bool:
        """
        :param other:
        :param type:
        :return:
        :rtype: bool       
        """    
        if not isinstance(other, Person):
            raise TypeError("Can only accept Person object")
        elif self.age > other.age:
            return True
        # elif self.last_name > other.last_name:
        #     return True
        # elif self.last_name == other.last_name:
        #     if self.first_name > other.first_name:
        #         return True
        #     elif self.age < other.age:
        #         return True
        # return False
    
    def __gt__(self, other) -> bool:
        """
        :param other:
        :param type:
        :return:
        :rtype: bool       
        """       
        if not isinstance(other, Person):
            raise TypeError("Can only accept Person object")
        elif self.age < other.age:
            return True
        # elif self.last_name < other.last_name:
        #     return True
        # elif self.last_name == other.last_name:
        #     if self.first_name < other.first_name:
        #         return True
        #     elif self.age > other.age:
        #         return True
        # return False

    def __str__(self) -> str:
        """

        :return:
        :rtype:        
        """
        return f'{self.__last_name}, {self.__first_name}, {self.__street}, {self.__city}, {self.__state}, Age {self.__age}'

    def __repr__(self) -> str:
        """
        
        :return:
        :rtype:
        """
        return f'{self.__last_name}, {self.__first_name}, {self.__street}, {self.__city}, {self.__state}, Age {self.__age}'

class WorkShop:
    """

    """
    def __init__(self):
        """
        
        """
        self.__households = {}

    @property
    def households(self):
        return self.__households

    def add_single_entry(self, data):
        """
        :param data:
        :param type:
        :return: None.
        """
        new_entry = self.__parser(data)
        person = Person(*new_entry)
        if person.address in self.__households:
            self.__households[person.address].append(person)
        else:
            self.__households[person.address] = [person]  

    def add_multiple_entries(self, data):
        """
        :param data:
        :param type:
        :return: None.
        """
        data_list = data.splitlines()
        for line in data_list:
            self.add_single_entry(line)      
            
    def __parser(self, data):
        """
        Verifies each part of an entry for correct formating and errors

        :param data:
        :param type:
        :return:
        :rtype:
        """
        data = data.strip('"').split('","')
        data_parsed = []
        for index, value in enumerate(data):

            # first name, last name, city
            if index in (0, 1, 3):
                value = value.capitalize()
            
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
            elif index == 4:
                value = value.upper()
            data_parsed.append(value)
        return data_parsed

    def print_results(self):
        """

        :return: None.
        """
        for family in self.__households.values():

            last_names = {}
            for person in family:
                if person.last_name not in last_names:
                    last_names[person.last_name] = 0

            last_names = ' and '.join(list(last_names))

            print(f'\n{last_names} household has {len(family)} occupants:')

            if len(family) > 1:
                family = WorkShop.heap_sort(family)
            for person in family:
                print(person)

    @staticmethod
    def heap_sort(family):
        """
        Adapted heapsort from https://www.youtube.com/watch?v=Q_eia3jC9Ts

        :param family:
        :param type:
        :return:
        :rtype: 
        """
        array = family
        n = len(array)

        def heapify(array, n, i):
            """
            Part of heapsort. Heapify 'bubbles' values down to keep a heap structure with minimum root
            """
            smallest = i  # Initialize smallest as root
            l = 2 * i + 1     # left = 2*i + 1
            r = 2 * i + 2     # right = 2*i + 2

            # See if left child of root exists and is
            # greater than root
            if l < n and array[i] < array[l]:
                smallest = l

            # See if right child of root exists and is
            # greater than root
            if r < n and array[smallest] < array[r]:
                smallest = r

            # Change root, if needed
            if smallest != i:
                array[i], array[smallest] = array[smallest], array[i]  # swap

                # Heapify the root.
                heapify(array, n, smallest)
        
        # Build a max heap.
        # Start at last parent location ((n//2)-1) and go to root.
        for i in range(n // 2 - 1, -1, -1):
            heapify(array, n, i)

        # Sort by removing last element, decreasing size n
        for i in range(n-1, 0, -1):
            array[i], array[0] = array[0], array[i]   # swap
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
    
    # w.add_single_entry('"Dave","Smith","123 main st.","seattle","wa","43"')
    w.add_multiple_entries(input_data)
    # for address, family in w.households.items():
    #     print('address:', address)
    # for address, family in w.households.items():
    #     print('family: ')
    #     for person in family:
    #         print('person:', person)

    w.print_results()






# END