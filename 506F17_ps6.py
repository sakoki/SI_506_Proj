import unittest
import requests
import json

## [PROBLEM 1]
print("\n*** PROBLEM 1 ***\n") # Print statements like this are to help you separate out the parts of the file that pertain to different problems in the problem set. You should leave them alone.
#------

## You should also have downloaded a file called nested_data_ps6.json. Use Python file operations and the json.loads function to save the data from that file, in a Python dictionary, to a variable called file_diction.

## Write your code to do so here.
with open('nested_data_ps6.json') as file1:
    file_diction = json.loads(file1.read())



## [PROBLEM 2]
print("\n*** PROBLEM 2 ***\n")

## We've provided some code below that creates a pretty complicated Python dictionary and saves it to a variable python_diction.

python_diction = {}
python_diction["items"] = []
python_diction["items"].append({"hello":1,"hi":2})
python_diction["items"].append({"hello":42,"hi":65})
python_diction["numbers"] = [1,2,3,5,7,8]

## Write Python code that uses the json.dumps function and Python file operations to write the data in the python_diction variable to a file called python_diction_saved.json.

## Write your code to do so here.
file2 = open('python_diction_saved.json', 'w')
file2.write(json.dumps(python_diction)) # To file2, load the contents of python_diction into a json format
file2.close()

#######

## NOTE: the rest of the problems in this Problem Set use the Federal Aviation Administration API, just like your reading in the APIs chapter of the textbook does. Note that these questions build on one another, so your answer to one will help you with problems later on!


## [PROBLEM 3] Encoding query parameters in a URL and making a request to an API, in several parts.
print("\n*** PROBLEM 3 ***\n")

## Create a dictionary to hold the FAA query parameters. It should be called called url_parameters. 
## You can do this in 2 lines of code (or even just one), just like dictionary creation you did earlier in the course!
## You should end up with a dictionary saved in the variable url_parameters with one key, "format", and its associated value should be a string, "json".

url_parameters = {'format': 'json'}



## Then write the assignment statement that makes a request to the FAA API and saves the result in a variable called airport_response.
## We've provided some code for you to rely on here (you could also refer to the textbook or FAA API documentation to decide that you needed this).
baseurl = 'http://services.faa.gov/airport/status/'
airport = 'DTW'

## Remember, you'll need to concatenate the airport code string ``"DTW"`` to the base url, and pass that as well as the ``url_parameters`` dictionary you already created to the ``requests.get`` function. Save the result in the variable airport_response.
## You can do this part in 1 line of code.

airport_response = requests.get(baseurl + airport, params = url_parameters)



## Finally, save the URL associated with the request you just made to a variable called airport_dtw_url. Do not hard code this by typing out the URL again.
## HINT: response objects have a .url attribute...

airport_dtw_url = airport_response.url



## [PROBLEM 4] Grabbing data off the web
print("\n*** PROBLEM 4 ***\n")

## Use the appropriate json module function and the attributes of a response object in order to write code to get the data from inside the airport_response variable into a Python dictionary called airport_data.

airport_data = json.loads(airport_response.text)

## Then, write Python code to save a LIST of the KEYS in the airport_data dictionary to a variable called airport_data_keys.
## Remember that you'll need to cast the result of .keys() to a list in Python 3!

airport_data_keys = airport_data.keys()

## [PROBLEM 5] Extracting relevant information from a dictionary
print("\n*** PROBLEM 5 ***\n")

## Write code to extract the following information from the airport_data dictionary: the airport code (e.g. DTW), the value of the 'reason' field from within the airport status, the current temperature at that airport, and the last time the data was updated. Save these pieces of info in variables called, respectively: airport_code, status_reason, current_temp, recent_update.

## You CAN do this in one line of code, but it may be easier to do this in 4 lines of code.
## HINT: jsoneditoronline.org and Understand/Extract/Repeat will be helpful here!

# Understand/Extract/Repeat
print(airport_data_keys)
for x1 in airport_data:
    print(x1)
    print(type(airport_data[x1]))
# This lets us know that key weather and status have pair values that are dictionaries.
print('***Values in weather***')
for x2 in airport_data['weather']:
    print(x2)
    print(type(airport_data['weather'][x2]))

print('***Values in status***')
for x3 in airport_data['status']:
    print(x3)
    print(type(airport_data['status'][x3]))

# The previous search showed that key meta have a pair value that is a dictionary. 
print('***Values in meta***')
for x4 in airport_data['weather']['meta']:
    print(x4)
    print(type(airport_data['weather']['meta'][x4]))

airport_code = airport_data['IATA']
status_reason = airport_data['status']['reason']
current_temp = airport_data['weather']['temp']
recent_update = airport_data['weather']['meta']['updated']

## Uncomment the following lines if you want to see the printed reps of what's in these variables.
print(airport_code)
print(status_reason)
print(current_temp)
print(recent_update)


## [PROBLEM 6] Generalizing your code
print("\n*** PROBLEM 6 ***\n")

## At this point, you'll consider the code you've written so far in your file, and make it generalizable. Which means... defining a function.

## Define a function called get_airport() that accepts a three-letter airport code string as input to the function, and returns a Python dictionary (like the one you saved in airport_data above) with data about that airport.

## This function should work no matter where it is called, with just the input of an airport code like "DTW" or "PDX" or "LAX", etc. It should NOT depend upon global variables. (So, if a programmer like you input "DTW" into your get_airport function, you should get a different result returned than from invoking the function with the input "LAX", and so on.)

## You can assume that the requests module is available at the top of your file, though (you do not have to import it again in your function definition of get_airport).

## Note: You should NOT put any try/except clauses inside this function.

## Define your get_airport() function below.






## [PROBLEM 7] More code generalization
print("\n*** PROBLEM 7 ***\n")

## Now, write another function called extract_airport_data() that accepts an airport code string as input, like "LAX", and returns a tuple: of the airport code, status reason, current temp, and recent update. 
## This function should invoke the get_airport() function from problem 6 inside it.
## HINT: What you did for problem 5 may be helpful here!






## [PROBLEM 8] Examples of using your newly defined functions with real data
print("\n*** PROBLEM 8 ***\n")

fav_airports = ['PIT', 'BOS', 'LGA', 'DCA']

## Write code here to iterate over the fav_airports list, invoke your extract_airport_data function on each element of the list, and append all of the results to a new list in a variable airport_tuples.
## The airport_tuples variable should end up being a list of 4 tuples, each of which contains information about a different airport.





## [PROBLEM 9] Dealing with real live data
print("\n*** PROBLEM 9 ***\n")

possible_airports = ["LAX","PHX","PPT","BOS","JAC","PDX","DTW"]

## Write code to iterate over the list in possible_airports and invoke the extract_airport_data function on each element of the list, appending each result to a list called poss_airport_tuples, similar to Problem 8.

## HOWEVER, your code should include a try/except clause such that if any element in the possible_airports list is NOT a valid airport to invoke the function on, your code should NOT create an error, just print out "Sorry, [whatever airport code] didn't work." 

## For example, if the string "XYZ" were in the list, you should see: "Sorry, XYZ didn't work." in the console, and all the valid data should still be accumulated into the list poss_airport_tuples.




## [PROBLEM 10] Using real live data to write a CSV file
print("\n*** PROBLEM 10 ***\n")


## Now, you'll iterate over the fav_airports list again, but you'll write the data to a CSV file.

## Iterate over the list fav_airports from Problem 8 again, but this time, write code to write to a CSV file called airport_temps.csv with 4 columns: airport_code, status_reason, current_temp, recent_update.

## Your resulting CSV file should have at least 5 lines: 4 lines for real airport data, and 1 line for the column headers. The content of each cell should have well-formatted data: no extra parentheses, just the specific value that corresponds to that header!

##MAKE SURE THE CSV FILE YOU CREATE IS CALLED EXACTLY airport_temps.csv. We will run tests on the CSV files post-submission, and we depend on the name of the file being correct.
## Open the document in Excel or in Google Drive to make sure that it is properly formatted.
## Since you are iterating over fav_airports in this problem, not possible_airports, you probably do not need to use a try/except clause in THIS problem if you do all the ones it relies upon correctly!

## Write the code to write your CSV file airport_temps.csv here:



## When you're finished, upload your 506W17_ps6.py file to Canvas. Please DO NOT upload the files that your code generates -- your code should generate them when we run it!
## Remember that we do not grade files that do not run.

##### BELOW THIS LINE IS CODE FOR PROBLEM SET TESTS #####
######## DO NOT CHANGE CODE BELOW THIS LINE #########
print("\n*** BELOW THIS LINE ARE TESTS FOR YOUR PROBLEM SET; DO NOT CHANGE CODE BELOW THIS LINE ***\n***********************\n")

class Problem1(unittest.TestCase):
    def test1(self):
        self.assertEqual(sorted(file_diction.items()),sorted({"python":{"ruby":["yay","ok","rails","whatever","yay"],"js":22},"umsi":{"ux":582,"research":674,"tsi":534,"ci":501,"python":[506,507,601]}}.items()))

class Problem2(unittest.TestCase):
    def test1(self):
        print("Trying to open the file you should have created to test it...")
        fptest = open("python_diction_saved.json","r")
        s = fptest.read()
        fptest.close()
        self.assertEqual(json.loads(s),python_diction)

class Problem3(unittest.TestCase):
    def test1(self):
        self.assertEqual(url_parameters,{"format":"json"},"Make sure you have the correct dictionary saved in url_parameters")
    def test2(self):
        self.assertEqual(type(airport_response),type(requests.get("http://www.google.com")),"airport_response is not a response object, check out what's being assigned to it")
    def test3(self):
        self.assertEqual(airport_dtw_url,"http://services.faa.gov/airport/status/DTW?format=json")

class Problem4(unittest.TestCase):
    def test1(self):
        self.assertEqual(sorted(airport_data_keys),sorted([u'status', u'ICAO', u'name', u'city', u'IATA', u'delay', u'state', u'weather']),"Perhaps something's wrong with your dictionary or you aren't getting the keys with a dictionary method properly?")

class Problem5(unittest.TestCase):
    def test1(self):
        print("Printing P5 data output to check:",(airport_code, status_reason, current_temp))
        self.assertEqual(airport_code,"DTW","airport_code does not have the correct value, OR you have a problem with your airport_data variable. Check out what's going on.")

class Problem6(unittest.TestCase):
    def test1(self):
        self.assertIsInstance(get_airport("DTW"),dict,"get_airport does not return a dictionary")
    def test2(self):
        self.assertEqual(get_airport("DTW")["IATA"],u"DTW","get_airport definitely does not return all of the right data right now -- check it out")

class Problem7(unittest.TestCase):
    def test1(self):
        self.assertIsInstance(extract_airport_data("DTW"),tuple,"extract_airport_data does not return a tuple")
        self.assertEqual([type(extract_airport_data("DTW")[0]),type(extract_airport_data("DTW")[1]), type(extract_airport_data("DTW")[2]), type(extract_airport_data("DTW")[3])], [type(u""),type(u""),type(u""),type(u"")], "Check out the return value of extract_airport_data. Is it a tuple of Unicode strings (Unicode strings get returned from the web)?")
        self.assertEqual(extract_airport_data("SFO")[0],u"SFO","check what your extract_airport_data function returns!")
    def test2(self):
        print("Printing the result of your extract_airport_data function because it's live data:")
        print(extract_airport_data("PHX"))

class Problem8(unittest.TestCase):
    def test1(self):
        self.assertIsInstance(airport_tuples[0], tuple, "Checking that airport_tuples is a list of tuples.")
        self.assertEqual(airport_tuples[-1][0], "DCA", "Checking that airport_tuples contains correct values.")

class Problem9(unittest.TestCase):
    def test1(self):
        self.assertIsInstance(poss_airport_tuples[0], tuple, "Checking that poss_airport_tuples is a list of tuples.")
        self.assertEqual(poss_airport_tuples[3][0], "PDX", "Checking that airport_tuples is a list of tuples with correct values.")

class Problem10(unittest.TestCase):
    def setUp(self):
        self.csv_file_temps = open("airport_temps.csv",'r')

    def test1(self):
        file_text= self.csv_file_temps.read()
        self.assertTrue(file_text,"Testing whether the airport_temps.csv file can be opened and read. NOT testing its formatting!")

    def tearDown(self):
        self.csv_file_temps.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
