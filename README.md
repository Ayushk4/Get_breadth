# Get_breadth
This is repository to extract breadth courses from erp and their grades. The data could also be added to the wiki because it lacks pages on such courses.

# Installation guide

- [Install pip](https://pip.pypa.io/en/stable/installing/)
- [Install pipenv](https://github.com/pypa/pipenv/blob/master/docs/install.rst)
- `pipenv shell --two`

# Running the app

This has two steps:

##### Adding cookie:

  1. Login to your erp account. Go to Student Academic Activities (UG) section in Academic. This gives you a cookie for accesing the /Acad route. You will not be able to mine the grades without this.

  2. Get the content of the JSID#/Acad named cookie set by ERP. Most web browsers enable you to view cookies from settings . It should be something like '0101E89CA7F3BDDE983B34912BDFFA08.worker3'. Update this in get_breadth.py under the cookie variable.
  
  3.  Open your terminal and run the program by `python2 get_breadth.py`

##### Using with Chillzone

The project assists [Chillzone](https://www.github.com/metakgp/chillzone). 

To use with it, copy the generated `breadth_schedule.json` to the root directory of chillzone and follow the instructions mentioned in chillzone README.