#!/usr/bin/env python3

#Adam Hostin
#21.4.2018
#proj č.7 ISJ(skriptovacie jazyky)

class Log(object):
    """ zapisuje do súboru """

    def __init__(self, file):
        """ inicializuje súbor """
        self.file = file

    def __enter__(self):
        """ otvára súbor pre zapisovanie a na začiatok súboru napíše Begin"""
        self.openedfile = open(self.file, "w")
        self.logging("Begin")

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ na koniec súboru napíše End a zavrie súbor """
        self.logging("End")
        self.openedfile.close()

    def logging(self, text):
        """ zapíše text do súboru a pridá znak konca riadku """
        self.openedfile.write(text + "\n")

def ordered_merge(*args,**selector):
    """ vracia list podla selectoru, ktorý udáva z ktorého objektu má byť prvok na danej pozicii a prvky sú vyberané v poradí """

    result=[]
    tmp=[]
    tmp=list(selector.values())
    if len(tmp)!=1:
        return []

    selector=(tmp[0])

    tmp=[]
    for x in selector:
        result.append(args[x][tmp.count(x)])
        tmp.append(x)
    return result

class TooManyCallsError(Exception):
    """ specifikacia chyby """
    pass

def limit_calls(max_calls=2, error_message_tail='called too often'):
    """ Limit calls. """

    # Define counter (dictionary) for function calling.
    pocitadlo_call = dict()


    def decorate(func):
        """ Decorator """

        def wrapper(*args, **kwargs):
            """ vola funkciu s danymi argumeentami alebo vypise error """
            # Get function name and count calling. => Save to dictionary.
            call = "function \"{}\" - {}".format(func.__name__, error_message_tail)
            pocitadlo_call[call] = pocitadlo_call.get(call, 0) + 1
            if pocitadlo_call[call] > max_calls:
                raise TooManyCallsError(call)

            # Call function with its arguments.
            return func(*args, *kwargs)

        return wrapper


    return decorate


print(list(ordered_merge('abcde', [1, 2, 3], (3.0, 3.14, 3.141), range(11, 44, 11), selector = [2,3,0,1,3,1])))