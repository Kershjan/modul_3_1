
calls = 0
def count_calls():
     global calls
     calls += 1
def string_info(string):
    print(tuple([len(string), string.upper(), string.lower()]))
    count_calls()

def is_contains(string, list_to_search):
    count_calls()
    if string.lower() in tuple(map(str.lower, list_to_search)):
        print(True)
    else:
        print(False)


is_contains('Apple', ['BaNana', 'ApPLe', 'kiwi'])
is_contains('cycle', ['recycling', 'cyclic'])
string_info('Paris')
string_info('Orange')
print(calls)