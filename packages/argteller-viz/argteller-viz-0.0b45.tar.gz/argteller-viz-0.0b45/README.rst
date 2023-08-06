Argteller
=========

The argteller package provides the class and method decorators for visual and interactive class object constructor. It frees the user from needing to constantly refer to documentations to figure out what arguments are required and what parameter values are valid inputs. It lists required arguments parsimoniously by only asking the parameters as needed, depending on the previously provided argument values. You can easily encode them in the custom DSL (domain specific language) script. 

This tool is useful in the Jupyter interface. It thus caters to the Python's interactive development capability. It also helps with code reproducibility by providing an easy way to share the parameter configurations.

Install
-------

::

	pip3 install argteller-viz

What does it do?
----------------

Let's take an example use case. Let's say you have two classes ``Vehicle`` and ``Rider``. Each class has the following ``__init__`` signatures:

::

	class Vehicle():

	    def __init__(self, vehicle_type, n_doors=None, car_name=None, n_motors=None, boat_name=None):
	    	"""
	    	Parameters
	    	----------
	    	vehicle_type : str
	    	    Valid inputs: "car" or "boat"

	    	n_doors : int
	    	    Only used when vehicle_type is "car". Valid inputs: 2 or 4

	    	car_name : str
	    	    Only used when vehicle_type is "car". 

	    	n_motors : int
	    	    Only used when vehicle_type is "boar". Valid inputs: 1, 2, or 3

	    	boat_name : str
	    	    Only used when vehicle_type is "boar"
	    	"""

		# ...Vehicle class definition

::

	class Rider():

	    def __init__(self, rider_name, rider_height, rider_weight):
	    	"""
	    	Parameters
	    	----------
	    	rider_name : str

	    	rider_height : float

	    	rider_weight : float
	    	"""

		# ...Rider class definition

Note the following: (1) there may be predefined list of valid input values for a given parameter and (2) some arguments are required only conditionally (e.g. ``n_doors`` is not needed if ``vehicle_type`` is set to "boat"). As the number of parameters grow, these will become harder to keep track of, requiring the user to constantly refer to the documentation to figure out the signature requirements.

Without going into code details, let us see what argteller can do for us. The argteller lets us define a separate class, say, ``CoolConstructor``. If you initialize ``CoolConstructor`` you will see interactive widgets that will help you fill out the required arguments:

::

	cool_constructor = CoolConstructor()

.. image:: https://github.com/mozjay0619/argteller-viz/blob/master/media/cool_constructor_2.png

If you click "car", the argteller will show you the conditionally required parameters, which you can fill in likewise.

.. image:: https://github.com/mozjay0619/argteller-viz/blob/master/media/cool_constructor_4.png

You can fill in the parameter values for the ``Rider`` class by clicking on the ``Rider`` tab. 

Argteller solves the problem of needing to know (1) the (potentially very long) list of parameters, (2) which parameters are required conditionally, and (3) what argument values are valid inputs, where it helps reduce time and hassle to type them in by making them into buttons that you can simply click on to choose. 

But how does this work, and how can we use the ``cool_constructor`` object to initialize our classes? In sections below, we will explain those details. Also, argteller can do so much more than the short sneak peek demo we just saw. We will slowly get into the rest of the functionalities that argteller has to offer as well. 

DSL
---








