

class Person:
    """
    """
    def __init__(self, first, last, street, city, state, age):
        self.__first_name = first
        self.__last_name = last
        self.__street = street
        self.__city = city
        self.__state = state
        self.__age = age
    
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def street(self):
        return self.__street
    
    @property
    def city(self):
        return self.__city

    @property
    def state(self):
        return self.__state

    @property
    def age(self):
        return self.__age
    
    def __eq__(self):
        pass
    
    def __lt__(self):
        pass
    
    def __gt__(self):
        pass

class WorkShop:

    def __init__(self):
        self.__storage = []

    @property
    def storage(self):
        return self.__storage

    def add_single_entry(self, data):
        
        new_entry = self.__parser(data)
        self.__storage.append(Person(*new_entry))

    def add_multiple_entries(self, data):
        data_list = data.splitlines()

        for line in data_list:
            new_entry = self.__parser(line)
            self.__storage.append(Person(*new_entry))            
            
    def __parser(self, data):
        """
        Verifies each part of an entry for correct formating and errors
        """
        data = data.strip('"').split('","')
        # print(data)                                       DELETE
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
        # print(data_parsed)                                       DELETE
        # print(' '.join(data_parsed))                             DELETE

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
    print(w.storage)
