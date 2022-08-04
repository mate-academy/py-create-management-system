# Management System
**Please note:** read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md)
before starting.


The Technical Lyceum plans to create a system for managing information about groups and students. 
You have to implement the above system using the `dataclasses` module.


You can import the module in such way:
 
```python
import dataclasses
```
 
Let`s implement 3 classes:
 
1. **Specialty**

It has the following attributes:

- `name`;
- `number`.
 
2. **Student**

It has the following attributes:

- `first_name`;
- `last_name`;
- `birth_date` ;
- `average_mark` — average score of the previous year (or average score of entrance exams for the first-course students), float number;
- `has_scholarship` — information on whether the student receives a scholarship. This is a bool value;
- `phone_number`;
- `address`.

**Please note:** to import datetime, use the following syntax:

```python
from datetime import datetime
```

3. **Group**

It has the following attributes:

- `specialty` - instance of the `Specialty`class;
- `course` - course number/year of study;
- `students` - list of students studying in this group. This should be a list of instances of the `Student` class.


Also implement 4 functions, using module `pickle` in this way:

```python
import pickle
```
 
1. **write_groups_information**

This function writes all inputted information about the Lyceum groups to the file named `"groups.pickle"`. 
The input is a list of the `Group` class instances. 
This function returns the maximum number of students from all the groups.


2. **write_students_information**

This function writes information about students to the `"students.pickle"` file. 
You should store all the students in one file. The input is a list of the `Student` class instances. 
This function returns the number of students.
 
3. **read_groups_information**

This function reads data from the `"groups.pickle"` file. 
It returns all group's specialties' names without repetition.

4. **read_students_information** 

This function reads data from the `"students.pickle"` file. 
It returns a list of all the `Student` class instances.

<details>
  <summary><strong>Hint</strong></summary>
  
   The `pickle` module returns only one recorded object.
   It is necessary to implement the reading of each instance from the file for the `read_students_information` and `read_groups_information` functions.

</details>

Implement the described task [here](app/main.py)
