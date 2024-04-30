"""Every good & perfect gift is from above, coming down from the Father of 
heavenly lights, who does not change like shifting shadows."""

'''I have changed the user.txt to not only store the username and password for
each user, but also add the user role that I use to view all tasks. '''

# List of variables and dictionaries
# Add some new variables that I use in the program.
user_name = ""
user_pass = ""
user_role = ""
user_pass_c = ""
user_role_dec = {'admin': 'IT Administrator',
                 'manag': 'Manager',
                 'clerk': 'Clerk',
                 'sales': 'Sales Rep',
                 'finad': 'Finance Admin',
                 'offad': 'Office Admin',
                 'hradm': 'HR Admin'
                 }

#=====importing libraries===========
from datetime import date


#====Login Section====
print("\t\tWelcome to Blaauwboch task manager programme")
print("\n\n")
print("Please Login:\n\n")

user_details = open("user.txt", "r")

# Create a dictionary to check if the user does exits
user_n = []
user_p = []
user_r = []       
for idata in user_details:
    a,b,c = idata.split(", ") 
    b = b.strip()
    user_n.append(a)
    user_p.append(b)

user_data = dict(zip(user_n, user_p))

login_user_name = input("Please enter your username: \n\tUsername: ").upper()

# Create a while loop to check the username is valid
while login_user_name not in user_n:
    print("The username enter is invalid:")
    login_user_name = input("Please enter your username: \n\tUsername: ").upper()
    if login_user_name in user_n:
        continue

user_pass = input("Please enter your password: \n\tPassword: ")
 
# Create a while loop to verify the password
while user_pass != user_data[login_user_name]:
    print("The password you enter is incorrected.")
    user_pass = input("Please enter your password: \n\tPassword: ")
    if user_pass == user_data[login_user_name]:
        continue

today1 = date.today()
formatted_date = today1.strftime('%d %B %Y')

print(f"\n\n\n\t\tWelcome, {login_user_name}")

print(f"\nWhat would you like to do today the {formatted_date}?:\n")

while True:
    # If the login user is admin, manager, or HR they can access Statistics.
    # Creat dictionary to check the user role
    user_role_c = open("user.txt", "r")
    user_n = []
    user_p = []  
    user_r = []      
    for idata in user_role_c:
        a,b,c = idata.split(", ") 
        c = c.strip()
        user_n.append(a)
        user_p.append(b)
        user_r.append(c)

    user_roledata = dict(zip(user_n, user_r))
    
    user_role = user_roledata[login_user_name]
            
    if user_role == "admin" or user_role == "manag" or user_role == "hradm":
        # Present the menu to the admin, managers & hr user and 
        # make sure that the user input is converted to lowercase.
        menu = input('''Select one of the following options:
                r - register a user
                a - add task
                va - view all tasks
                vm - view my tasks
                s - Statistics        
                e - exit
                : ''').lower()

    else:
        # Present the menu to the other user and 
        # make sure that the user input is converted to lowercase.
        menu = input('''Select one of the following options:
                r - register a user
                a - add task
                va - view all tasks
                vm - view my tasks
                e - exit
                : ''').lower()


    if menu == 'r':
       
        # Setup only that Admin can register a new user
        if login_user_name == "ADMIN":
            """ Ask how many new users is required to add. That helps not to go 
                back into menu or start over to add more users.""" 
            num_new_user = int(input('''Please enter the number of new user to 
                                     be added: \n'''))
            num_new_user_p = num_new_user + 1
            num_new_user_n = num_new_user - 1

            for i in range(1, num_new_user_p):
                with open('user.txt', 'a+' ) as new_userfile:
                    if i <= num_new_user_p:
                        user_details = open("user.txt", "r")

                        user_name = input('''Please enter new user name \n
                                        (Username must be at least 4 characters): \n
                                          ''').upper() 
                        
                        # Create a dictionary to check if the user does exits
                        user_n = []
                        user_p = []  
                        user_r = []      
                        for idata in user_details:
                            a,b,c = idata.split(", ") 
                            c = c.strip()
                            user_n.append(a)
                            user_p.append(b)
                            user_r.append(c)

                        user_data = dict(zip(user_n, user_p))

                        """Create 2 while loop to make sure the input is more 
                        than 4 characters and that the user name do not exist 
                        all ready."""
                        while len(user_name) < 4:
                            print("Username must be at least 6 characters.")
                            user_name = input("Please enter new user name: \n").upper()
                            continue

                        while user_name in user_n:
                            print("Username all ready exist")
                            user_name = input("Please enter new user name: \n").upper()
                            continue

                    # user to input new password     
                        user_pass = input('''Please enter new password 
                                          \n(Password needs to be at least 6 
                                          characters): \n''')
                        
                        while len(user_pass) < 6:
                            print("The password you have enter is smaller than 6 Characters.")
                            user_pass = input("Please re-enter new password: \n")
                            continue
                        
                        """user to re-enter password to confirm it match and 
                        use a while loop to for the process to go on"""
                        user_pass_c = input("Please re-enter the password to confirm: \n")
                        
                        while user_pass != user_pass_c:
                            print("The passwords do not match")
                            user_pass = input("Please re-enter new password: \n")
                            user_pass_c = input("please re-confirm the new password: \n")
                            if user_pass == user_pass_c:
                                continue
                        
                        # add a user role as require it for task view or to add task.
                        user_role = input('''Select one of the following user role from below:
                                        Admin - IT Administrator
                                        Manag - Manager
                                        Clerk - Clerk
                                        Sales - Sales Rep
                                        FinAd - Finance Admin
                                        OffAd - Office Admin
                                        HRAdm - HR Admin
                                        : \n''').lower()    
                        
                        new_userfile.write("\n" + user_name + ", " + user_pass + ", " + user_role)
                        print("User details created successful.")

                new_userfile.close
        
        else:
           print("\n\nYou are not able to register new users.\n\n")


    elif menu == 'a':
        print(f"\n\n\n\t{login_user_name}, please complete the below to add new task.\n")

        with open('tasks.txt', 'a+' ) as add_task:
            user_details = open("user.txt", "r")
            
            ntask_user_name = input("Enter the username for the new task: \nUsername: ").upper()

            # creat dictionary to check if the user does exits
            user_n = []
            user_p = []  
            user_r = []      
            for idata in user_details:
                a,b,c = idata.split(", ") 
                c = c.strip()
                user_n.append(a)
                user_p.append(b)
                user_r.append(c)

            user_data = dict(zip(user_n, user_p))

            # create a while loop for check the username is valid
            while ntask_user_name not in user_n:
                print("The username enter is invalid.")
                ntask_user_name = input("Please enter your username: \n\tUsername: ").upper()
                if ntask_user_name in user_n:
                    continue
                
            ntask_title = input("Enter the title of the new task:\nTask Title: ")
            ntask_desc = input("Enter the new task descrription:\nTask Description: ")
            print('''You will need to enter the due date in three steps:
                  1st Day, 2nd Month, 3rd The Year.''')
            ntask_due_day = input("Enter the due date Day:\nDay: ")
            ntask_due_month = input("Enter the due date Month(eg Jan):\nMonth: ")
            ntask_due_year = input("Enter the due date Year:\nYear: ")
            
            add_task.write("\n" + ntask_user_name + ", " + ntask_title + ", " 
                           + ntask_desc + ", " + formatted_date + ", " 
                           + ntask_due_day + " " + ntask_due_month + " " 
                           + ntask_due_year + ", " + "No")
            print("New task created successful and save to file.")

        add_task.close


    elif menu == 'va':

        """setup that only Admin, managers, and HR can see all task, all other
          will not be able to all task"""
        # creat dictionary to check the user role
        user_role_c = open("user.txt", "r")
        user_n = []
        user_p = []  
        user_r = []      
        for idata in user_role_c:
            a,b,c = idata.split(", ") 
            c = c.strip()
            user_n.append(a)
            user_p.append(b)
            user_r.append(c)

        user_roledata = dict(zip(user_n, user_r))
        
        user_role = user_roledata[login_user_name]
                
        if user_role == "admin" or user_role == "manag" or user_role == "hradm":
            print(f"\n\n\n\t\t{login_user_name} All the task for Blaauwboch:\n\n")
            print("________________________________________________________\n")
            
            view_all = open("tasks.txt", "r")
            lines = view_all.readlines()

            for line in lines:
                temp = line.strip()
                temp = temp.split(", ")
                
                task = temp[1] 
                assigned_to = temp[0]
                date_assigned = temp[3]
                due_date = temp[4]
                task_complete = temp[5]
                task_description = temp[2]

            
                print(f'''Task:\t\t\t{task}
                      Assigned to:\t\t{assigned_to}
                      Date assigned:\t\t{date_assigned}
                      Due date:\t\t{due_date}
                      Task Complete?\t\t{task_complete}
                      Task Description:\n  {task_description}\n
                      ''')
                print("____________________________________________________\n")
                
            view_all.close()

        else:
            print('''\nYou are not able to view all the Task for Company. 
                  Please go to view my Task\n\n''')


    elif menu == 'vm':
        
        print(f"\n\n\n\t\t{login_user_name} your tasks for Blaauwboch:\n\n")
        print("____________________________________________________________\n")

        # create dictionary to check for the tas that are assign to user_name
        with open("tasks.txt", 'r') as user_task:
            lines = user_task.readlines()

            # create empty list for user task
            user_tasks = []
            ut_task = []        # Task:
            ut_assig = []       # Assigned to:
            ut_d_ass = []       # Date Assigned:
            ut_due = []         # Due date
            ut_com = []         # Task Complete?
            ut_desc = []         # Task Description

            for utdata in user_task:
                u,v,w,x,y,z = utdata.split(", ")
                z = z.strip()

                ut_task.append(v)
                ut_assig.append(u)
                ut_d_ass.append(x)
                ut_due.append(y)
                ut_com.append(z)
                ut_desc.append(w)

            user_tdata = dict (zip(ut_assig,ut_task))

            for line in lines:
                try:
                    temp = line.strip()
                    temp = temp.split(", ")
                    if temp[0] == login_user_name.strip():
                        user_tasks.append(temp)
                
                except IndexError:
                    continue        

            for temp in user_tasks:
                    task = temp[1] 
                    assigned_to = temp[0]
                    date_assigned = temp[3]
                    due_date = temp[4]
                    task_complete = temp[5]
                    task_description = temp[2]

                    print(f'''Task:\t\t\t{task}
                          Assigned to:\t\t{assigned_to}
                          Date assigned:\t\t{date_assigned}
                          Due date:\t\t{due_date}
                          Task Complete?\t\t{task_complete}
                          Task Description:\n  {task_description}\n''')
                    print("________________________________________________\n")
                    break
            
            user_task.close()


    elif menu == 's':
       
        while True:
             # creat a new statistics menu for user to choose what to display
            menu_s = input('''Select one of the following options:
                u - The total number of the users
                t - The total number of task
                as - all above stats
                e - exit
                : ''').lower()
            
            # creat data for the stats
            user_count = 0
            task_count = 0
            
            # open user file to count user, also strip blank lines.
            with open("user.txt", 'r') as count_u:
                for line in count_u:
                    if line.strip():
                        user_count += 1

            count_u.close()

            #open task file to count tasks, and also strip blank lines 
            with open("tasks.txt", 'r') as count_t:
                for line in count_t:
                    if line.strip():
                        task_count += 1

            count_t.close()

            if menu_s == 'u':
                print(f"\nThe total users: {user_count}\n")

            elif menu_s == 't':
                print(f"\nThe total tasks: {task_count}\n")
                      
            elif menu_s == 'as':
                print(f"\nThe total users: {user_count}")
                print(f"The total tasks: {task_count}\n")
                
            elif menu_s == 'e':
                exit()
            
            else:
                print("You have entered an invalid input. Please try again")


    elif menu == 'e':
        print('Goodbye!!!')
        exit()


    else:
        print("You have entered an invalid input. Please try again")
