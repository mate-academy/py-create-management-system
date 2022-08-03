# Management System

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start


The Technical Lyceum plans to create a system for managing information about groups and students.
You have to implement the above system, using the `dataclasses` module.

You can import the module in such way:
 
```
Import dataclasses
```
 
Let`s implement 3 classes:
 
**Specialty**

It has the following attributes:

- `name`
- `number`
 
**Student**

- `first_name`
- `last_name`
- `birth_date` - student's date of birth.
- `average_mark` -  average score of the previous year (or average score of entrance exams for the first course students), float number
- `has_scholarship` - information on whether the student receives a scholarship. This is a bool value
- `phone_number`
- `address`

_Important! To import datetime use the following syntax:_

```from datetime import datetime ```

**Group**

- `specialty` - a specialty, has be an instance of  the class “Specialty”
- `course` - course number/year of study
- `students` - a list of students studying in this group. This should be a list of instances of the class “Student”. 


Also implement 4 functions, using module `pickle`.

You can import this module at this way:

```Import pickle```
 
1. **write_groups_information**

This function writes all inputted information about the Lyceum groups to the file named `“groups.pickle”`.
The input is a list of class `Group` instances.
The function returns the maximum number of students from all groups.


2. **write_students_information**

Writes information about students to the file `“students.pickle”`.
All students should be stored in one file. The input is a list of class `Student` instances.
This function returns the number of students.
 
3. **read_groups_information**

Function reads data from the file `“groups.pickle”`.
Returns all groups specialties' names without repetition.
 
4. **read_students_information** - 

Reads data from the file `“students.pickle”`.
Returns a list of all class `Student` instances.

> Hint!
> The module `pickle` returns only one recorded object. 
> 
>It is necessary to implement the reading of each instance from the file for the functions `read_students_information` and `read_groups_information`

Implement the task described [here](app/main.py)
