from bs4 import BeautifulSoup as Soup
import unittest
import requests
import csv

#########
## Instr note: the outline comments will stay as suggestions, otherwise it's too difficult.
## Of course, it could be structured in an easier/neater way, and if a student decides to commit to that, that is OK.

## NOTE OF ADVICE:
## When you go to make your GitHub milestones, think pretty seriously about all the different parts and their requirements, and what you need to understand. Make sure you've asked your questions about Part 2 as much as you need to before Fall Break!


######### PART 0 #########

# Write your code for Part 0 here.
should_I_cache = 1
if(should_I_cache == 1):
    try: 
        cats_page = open('cats_page.html','r').read()
    except:
        cats_page = requests.get('http://newmantaylor.com/gallery.html').text
        f = open('cats_page.html','w')
        f.write(cats_page)
        f.close()
else: pass

cat_soup = Soup(cats_page, 'html.parser')
cat_img_repository = cat_soup.find_all("img")
#print(type(cat_img_repository))
cat_alt = []
for cat_element in cat_img_repository:
    cat_alt.append(cat_element.get('alt',"No alternative text provided!"))
# print(cat_alt)
    
######### PART 1 #########

# Get the main page data...

# Try to get and cache main page data if not yet cached
# Result of a following try/except block should be that
# there exists a file nps_gov_data.html,
# and the html text saved in it is stored in a variable 
# that the rest of the program can access.

# We've provided comments to guide you through the complex try/except, but if you prefer to build up the code to do this scraping and caching yourself, that is OK.

try: 
    main_page_data = open('nps_gov_data.html','r').read()
except:
    main_page_data = requests.get('https://www.nps.gov/index.htm')
    main_page_data.encoding = 'utf-8'
    # print('The main_page_data is encoded in: {}'.format(main_page_data.encoding))
    # print('The main_page_data is type: {}'.format(type(main_page_data)))
    main_page_data = main_page_data.text
    f = open('nps_gov_data.html','w')
    f.write(main_page_data)
    f.close()


# Get individual states' data...

# Result of a following try/except block should be that
# there exist 3 files -- arkansas_data.html, california_data.html, michigan_data.html
# and the HTML-formatted text stored in each one is available
# in a variable or data structure 
# that the rest of the program can access.

# TRY: 
# To open and read all 3 of the files

# But if you can't, EXCEPT:

# Create a BeautifulSoup instance of main page data 
# Access the unordered list with the states' dropdown

# Get a list of all the li (list elements) from the unordered list, using the BeautifulSoup find_all method

# Use a list comprehension or accumulation to get all of the 'href' attributes of the 'a' tag objects in each li, instead of the full li objects

# Filter the list of relative URLs you just got to include only the 3 you want: AR's, CA's, MI's, using the accumulator pattern & conditional statements


# Create 3 URLs to access data from by appending those 3 href values to the main part of the NPS url. Save each URL in a variable.


## To figure out what URLs you want to get data from (as if you weren't told initially)...
# As seen if you debug on the actual site. e.g. Maine parks URL is "http://www.nps.gov/state/me/index.htm", Michigan's is "http://www.nps.gov/state/mi/index.htm" -- so if you compare that to the values in those href attributes you just got... how can you build the full URLs?


# Finally, get the HTML data from each of these URLs, and save it in the variables you used in the try clause
# (Make sure they're the same variables you used in the try clause! Otherwise, all this code will run every time you run the program!)


# And then, write each set of data to a file so this won't have to run again.


try:
    # To open and read all 3 of the files
    arkansas_data = open('arkansas_data.html').read()
    california_data = open('california_data.html').read()
    michigan_data = open('michigan_data.html').read()
except:
    # Create a BeautifulSoup instance of main page data
    main_page_soup = Soup(main_page_data,'html.parser')
    
    # Access the unordered list with the states' dropdown
    main_page_soup_stateUl = main_page_soup.find("ul",{"class":"dropdown-menu SearchBar-keywordSearch"})
    
    # prettify the main nps page
    f = open("prettified_main_page.html",'w')
    f.write(main_page_soup_stateUl.prettify())
    f.close
    
    # Get a list of all the li (list elements) from the unordered list, using the BeautifulSoup find_all method
    state_href_list = []
    li_main_page = main_page_soup_stateUl.find_all("li")
    for e in li_main_page:
        state_href_list.append(e)
    #print(state_href_list)
    
    # Use a list comprehension or accumulation to get all of the 'href' attributes of the 'a' tag objects in each li, instead of the full li objects
    href_list = [x['href'] for x in main_page_soup_stateUl.find_all('a')]
    #print(href_list)

    # Filter the list of relative URLs you just got to include only the 3 you want: AR's, CA's, MI's, using the accumulator pattern & conditional statements
    target_states = ['ar','ca','mi']
    #target_states = [i+'/index.htm' for i in target_states]
    #print(target_states)

    target_href_dict = {}
    for i in target_states:
        target_href_dict[i] = '/state/'+i+'/index.htm' 
    #print(target_href_dict)

    # Create 3 URLs to access data from by appending those 3 href values to the main part of the NPS url. Save each URL in a variable.
    
    main_url = "https://www.nps.gov"
    ar_url = main_url+target_href_dict['ar']
    ca_url = main_url+target_href_dict['ca']
    mi_url = main_url+target_href_dict['mi']
    print(ar_url)
    print(ca_url)
    print(mi_url)
    # Finally, get the HTML data from each of these URLs, and save it in the variables you used in the try clause
    # (Make sure they're the same variables you used in the try clause! Otherwise, all this code will run every time you run the program!)

    ar_data = requests.get(ar_url)
    ar_data.encoding = 'utf-8'
    arkansas_data = ar_data.text
    with open("arkansas_data.html", 'w') as f:
        f.write(arkansas_data)

    ca_data = requests.get(ca_url)
    ca_data.encoding = 'utf-8'
    california_data = ca_data.text
    with open("california_data.html", 'w') as f:
        f.write(california_data)

    mi_data = requests.get(mi_url)
    mi_data.encoding = 'utf-8'
    michigan_data = mi_data.text
    with open("michigan_data.html", 'w') as f:
        f.write(michigan_data)    

    # And then, write each set of data to a file so this won't have to run again.

######### PART 2 #########

## Before truly embarking on Part 2, we recommend you do a few things:

# - Create BeautifulSoup objects out of all the data you have access to in variables from Part 1
# - Do some investigation on those BeautifulSoup objects. What data do you have about each state? How is it organized in HTML?

# HINT: remember the method .prettify() on a BeautifulSoup object -- might be useful for your investigation! So, of course, might be .find or .find_all, etc...

# HINT: Remember that the data you saved is data that includes ALL of the parks/sites/etc in a certain state, but you want the class to represent just ONE park/site/monument/lakeshore.

# We have provided, in sample_html_of_park.html an HTML file that represents the HTML about 1 park. However, your code should rely upon HTML data about Michigan, Arkansas, and Califoria you saved and accessed in Part 1.

# However, to begin your investigation and begin to plan your class definition, you may want to open this file and create a BeautifulSoup instance of it to do investigation on.

# Remember that there are things you'll have to be careful about listed in the instructions -- e.g. if no type of park/site/monument is listed in input, one of your instance variables should have a None value...


## Define your class NationalSite here:
class NationalSite(object):
    def __init__(self, state_Soup):
        self.location = state_Soup.find("h4").text.strip()
        self.name = state_Soup.find("h3").text.strip()
        if state_Soup.find("h2") is not None:
            self.type = state_Soup.find("h2").text.strip()
        else: 
            self.type = None
        if state_Soup.find("p") is not None:
            self.description = state_Soup.find("p").text.strip()
        else:
            self.description = ""
        sub_grp = state_Soup.find('h3')
        sub_link = sub_grp.find('a')
        self.link = sub_link.get('href')
    def __str__(self):
        return "{} | {}".format(self.name, self.location)
    def __contains__(self, test_string):
        return test_string in self.name
    def get_mailing_address(self):
        address_link = 'http://www.nps.gov'+ self.link +'planyourvisit/basicinfo.htm'
# new code: try except
        address_page_data = requests.get(address_link)
        address_page_data.encoding = 'utf-8'
        address_page_data = address_page_data.text            
        address_Soup = Soup(address_page_data,'html.parser')
        section_address_Soup = address_Soup.find("div",{"itemprop":"address"})
        # if address_Soup.find("div",{"itemprop":"address"}) is None:
            # return ""
        # else: 
        if section_address_Soup.find("span",{"itemprop":"streetAddress"}) is None: 
            street_address = ""
        else:
            street_address = section_address_Soup.find("span",{"itemprop":"streetAddress"}).text.strip()
        if section_address_Soup.find("span",{"itemprop":"addressLocality"}) is None:
            address_locality = ""
        else:
            address_locality = section_address_Soup.find("span",{"itemprop":"addressLocality"}).text.strip()
        if section_address_Soup.find("span",{"itemprop":"addressRegion"}) is None:
            address_region = ""
        else:
            address_region = section_address_Soup.find("span",{"itemprop":"addressRegion"}).text.strip()
        if section_address_Soup.find("span",{"itemprop":"postalCode"}) is None:
            zipcode = ""
        else:
            zipcode = section_address_Soup.find("span",{"itemprop":"postalCode"}).text.strip()
        address_string = "{} {} {} {}".format(street_address,address_locality,address_region,zipcode)
        return address_string

## Recommendation: to test the class, at various points, uncomment the following code and invoke some of the methods / check out the instance variables of the test instance saved in the variable sample_inst:

# f = open("sample_html_of_park.html",'r')
# soup_park_inst = Soup(f.read(), 'html.parser') # an example of 1 BeautifulSoup instance to pass into your class
# sample_inst = NationalSite(soup_park_inst)
# f.close()

######### PART 3 #########

# Create lists of NationalSite objects for each state's parks.

# HINT: Get a Python list of all the HTML BeautifulSoup instances that represent each park, for each state.
arkansas_natl_sites = []
california_natl_sites = []
michigan_natl_sites = []

ar_Soup = Soup(arkansas_data,'html.parser')
ca_Soup = Soup(california_data,'html.parser')
mi_Soup = Soup(michigan_data,'html.parser')

ar_sub_Soup = ar_Soup.find('ul',{'id':'list_parks'})
for each_link in ar_sub_Soup.find_all("div",{'class':'col-md-9 col-sm-9 col-xs-12 table-cell list_left'}):
    each_NatSite_obj = NationalSite(each_link)
    arkansas_natl_sites.append(each_NatSite_obj)

ca_sub_Soup = ca_Soup.find("ul",{"id":"list_parks"})
for each_link in ca_sub_Soup.find_all("div",{'class':'col-md-9 col-sm-9 col-xs-12 table-cell list_left'}):
    each_NatSite_obj = NationalSite(each_link)
    california_natl_sites.append(each_NatSite_obj)

mi_sub_Soup = mi_Soup.find("ul",{"id":"list_parks"})
for each_link in mi_sub_Soup.find_all("div",{'class':'col-md-9 col-sm-9 col-xs-12 table-cell list_left'}):
    each_NatSite_obj = NationalSite(each_link)
    michigan_natl_sites.append(each_NatSite_obj)

##Code to help you test these out:
# for p in california_natl_sites:
# 	print(p)
# for a in arkansas_natl_sites:
# 	print(a)
# for m in michigan_natl_sites:
# 	print(m)


with open('arkansas.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name','Location','Type','Address','Description'])
    for each_park in arkansas_natl_sites:
        writer.writerow([each_park.name, each_park.location, each_park.type, each_park.get_mailing_address(), each_park.description])
with open('california.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name','Location','Type','Address','Description'])
    for each_park in california_natl_sites:
        writer.writerow([each_park.name, each_park.location, each_park.type, each_park.get_mailing_address(), each_park.description])
with open('michigan.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name','Location','Type','Address','Description'])
    for each_park in michigan_natl_sites:
        writer.writerow([each_park.name, each_park.location, each_park.type, each_park.get_mailing_address(), each_park.description])

######### PART 4 #########

## Remember the hints / things you learned from Project 2 about writing CSV files from lists of objects!

## Note that running this step for ALL your data make take a minute or few to run -- so it's a good idea to test any methods/functions you write with just a little bit of data, so running the program will take less time!

## Also remember that IF you have None values that may occur, you might run into some problems and have to debug for where you need to put in some None value / error handling!

