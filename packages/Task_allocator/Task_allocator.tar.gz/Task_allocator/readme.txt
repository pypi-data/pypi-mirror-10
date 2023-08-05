This program takes commandline input for the datafile from where configuration will be fetched.
Example:- python task_allocator config.txt

Configuration file template looks like this=>

Task_type   User_Name    Country    Start Time(Local)   End Time(Local)
Email       U1          India      May/17/2015-00:00    May/17/2015-01:00
Call        U1          India      May/17/2015-08:00    May/17/2015-09:00
Sms         U1          India      May/17/2015-21:00    May/17/2015-22:00
.           .           .               .                   .
.           .           .               .                   .   
.           .           .               .                   .



There are two functions present in the code.
1. status_check
2. enhanced_search


The input argument for the two function are same.
But outputs are different.status_check printsout "True" if the task should be executed immediately (If the
current time is between start time and end time).Prints 'False' otherwise
   
    Whereas, enhanced_search serach printssout "True" if the task should be executed immediately, but if not, 
it also prints out when the task would be picked up next.

Sample Input(status_check):-Email       U1          India      May/17/2015-00:00    May/17/2015-01:00
Output:- True

Sample Input(status_check):-Sms         U1          India      May/17/2015-00:00    May/17/2015-01:00
Output:- False

Sample Input(enhanced_search):-Email    U1          India      May/17/2015-00:00    May/17/2015-01:00
Output:- True

Sample Input(enhanced_search):-Sms      U1          India      May/17/2015-00:00    May/17/2015-01:00
Output:- Task will be picked up between: May/17/2015-21:00  to  May/17/2015-22:00