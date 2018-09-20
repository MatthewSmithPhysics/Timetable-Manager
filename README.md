# Matthew Smith Timetable Manager
## Introduction
This is my own Python script for managing an academic timetable. The default version of the script supports a 5 day (9 am to 6 pm) schedule for 30 weeks, but this is quite easily changed in the source code. 
## Dependencies
Running this script currently requires installation of:
* **Python 3** ([project website](https://www.python.org/)); platform licensed [here](https://docs.python.org/3/license.html).
* **numpy** ([project website](http://www.numpy.org/), [GitHub repository](https://github.com/numpy/numpy)); library provided under the BSD license.
* **tabulate** ([PyPI project page](https://pypi.org/project/tabulate/), [GitHub repository](https://github.com/gregbanks/python-tabulate)); library provided under the MIT license.  


Both are easily installed with **pip**:  
`pip install numpy`  
`pip install tabulate`    
or  
`pip3 install numpy`  
`pip3 install tabulate`
## License
This software is provided under the MIT license.
## Installation
With the above dependencies installed, installation is as easy as downloading **timetable.py** and placing it in your working folder.
## Running
With Python 3 installed, running from the command line is elementary:  
`python timetable.py`  
or  
`python3 timetable.py`
## Use
The manager is based in the command line and a user has the following commands at their disposal:
* **exit()**;  Exits the script.
* **cls**; Clears the terminal. 
* **addClass(** _name_, _lecturer_, _room_ **)**; Adds a class to the list of classes able to be placed in the timetable; _name_ (str) is the name of the class, _lecturer_ is the name of the lecturer, and _room_ is the room name. 
* **setClass(** _name_, _week_, _day_, _time_ **)**; Sets a class to be in a named slot; _name_ (str) is the name of the class, _week_ (int) is the week number (from 1 to 30 default), _day_ (str) is the relevant day ("Mon", "Tue", "Wed", "Thur", "Fri"), and _time_ (str) is the relevant time ("9 am", "10 am", "11 am", "12 pm", "1 pm", "2 pm", "3 pm", "4 pm", 5 pm"). 
* **setClass(** _name_, [_a_, _b_], _day_, _time_ **)**; Sets a class to be in a named slot; _name_ (str) is the name of the class, _a_ (int) is the first week number (from 1 to 30 default), _b_ is the last week number (from 1 to 30 by default), [_a_, _b_] is a closed interval of weeks, _day_ (str) is the relevant day ("Mon", "Tue", "Wed", "Thur", "Fri"), and _time_ (str) is the relevant time ("9 am", "10 am", "11 am", "12 pm", "1 pm", "2 pm", "3 pm", "4 pm", 5 pm").
* **showTable(** _week_, _showList_ = False **)**; Shows the timetable for a particular week and optionally shows a list of class details; _week_ (int) is the week numeber (1 to 30 default), and _showList_ (bool, optional) is whether or not the user wishes to see a list of classes and their details. 
* **save(** _name_ **)**; saves the current timetable; _name_ is the non-extended filename. 
* **load(** _name_ **)**; loads a named timetable; _name_ is the non-extended filename.
Due to the nature of the input system (essentially allowing the execution of user-defined Python within the script), there are other commands at the user's disposal. The prior listed are however all that is thought needed for the intended purpose. 
## Future Work
Future ammendments to this project may include:
* Custom boundaries on the weeks, days, and times supported by a particular timetable
* Command to change details of a class
* An inbult 'help' section


