# timesheet-todoist-example
An example of how I use the Todoist API for integration w/my timesheet

This is provided as an example of how I've used the Todoist API to integrate with my timesheet. It is highly customized to my needs, and would like need to be largely rewritten for anyone else's needs.

Here is how it works:

# Todoist Project Structure

My Todoist project structure is hierarchical. I have a top level project ("Work") and below that, I have four subprojects:

1. Projects
2. Support
3. Training
4. Management

Within each of the four subprojects are the projects that I actually work on. So for example, below Projects I have things like "CAP R1", "Presence Viewer", "EMS Discovery" all of which are projects that I actively charge my time to.

I have color-coded the four category projects so that I can easily see how much of each category I work on in the Todoist productivity screen. (Green is Projects, Yellow is support, etc.) It looks something like this:

![Todoist Project Colors](https://github.com/jamietr1/timesheet-todoist-example/blob/master/images/Todoist-Project-Colors.png)

The code is written to be aware of this structure.

# Control files

My code makes use of 2 text-based control files:

1. ~/.todoistprodrc: Lives in my home directory and contains my login information for the Todoist API (rights set to 700).
2. ~/.projects.txt: A comma-separated file used to store charge number information for the projects I work on. The projects in this file must have identical names to the projects in Todoist. A typical example looks like this:

`# Project | Charge number valid dates | Charge Number | Budget | Active`  
`CAP R1|2016-02-01,2016-09-30,XXX16-YYYY;2016-10-01,2017-09-30,XXX17-YYYY|5000|1`

# Adding an item to my Todoist list

When I add something project-related to Todoist, I am always sure to assign it to the correct project. When I complete the task, I append the time I spent on the task to the end of the task prior to completing it. A typical completed task might look like this:

![Time Spent](https://github.com/jamietr1/timesheet-todoist-example/blob/master/images/Todoist-Time-Spent.png)

# Displaying my work for any given day

At the command line, I run my "timesheet" command. Without any parameters, it assumes the current date. If I say "timesheet yesterday" it will pull data for yesterday. "timesheet Wednesday" will pull data from the previous Wednesday. I can also run "timesheet yyyy-mm-dd" to get data for a specific date. I've created an alias "ts" for my "timesheet" command to save keystrokes. The result looks something like this:

![Timesheet results](https://github.com/jamietr1/timesheet-todoist-example/blob/master/images/todoist-results.png)

If I have included the time spent for tasks, the total time will be automatically subtotaled for me in the output.

# Miscellaneous

I often include links in my tasks so that I can refer back to things I was working on. When pulled via the links are displayed in the task. I tend to copy and paste the output of my script into note boxes on my timesheet and I don't need to include the links there, so my code suppresses them by default. Adding a -l to the timesheet command will force the links to display.

I also suppress by default the time spent for each task and show only the subtotal. Adding a -t will display the time I spent on each line item.

# Summary

Once again, the code here is merely to provide an example of how I have used Todoist to manage my work tasks and provide some automation for logging my work in our timekeeping system. It works perfectly for me, but is highly customized to my style of work and my timekeeping system. Feel free to use it as an example, but expect to rewrite the code completely if you use it for your own system.

