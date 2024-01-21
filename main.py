from mysql.connector import connect, Error
from getpass import getpass

def main():
    # connect to database
    try:
        conn = connect(
            host = 'localhost',
            user = input('Enter Username: '),
            password = getpass('Enter Password: '),
            database = 'artmuseum'
        )
    except Error as e:
        print(e)

    print('Welcome to the Art Museum database!')
    
    # handle user input
    running = True
    possibleinputs = ['q', 'p', 'u', 'x']
    while running:
        print('q - run a query')
        print('p - run a stored procedure')
        print('u - update database')
        print('x - close program')

        userinput = str(input())

        # handle q input
        if userinput == 'q':
            print('Select query:')
            print('1 - artists in exhibit')
            print('2 - employees in department')
            print('3 - number of visits on date')
            print('4 - employee schedule')
            print('5 - most popular days to visit')
            print('b - back')

            qinput = str(input())

            # handle 1 input
            if qinput == '1':
                print('Enter exhibit id:')
                exhibit_id = str(input())

                values = (exhibit_id,)
                query = """
                        SELECT a.last_name, a.first_name
                        FROM artist AS a
                        JOIN piece AS p
                        ON a.artist_id = p.artist_id
                        JOIN exhibit AS e
                        ON e.exhibit_id = p.exhibit_id
                        WHERE e.exhibit_id = %s
                        """
                try:
                    with conn.cursor() as cursor:
                        cursor.execute(query, values)
                        for row in cursor:
                            print(row)
                except Error as e:
                    print('Invalid input, returned to main menu')
            
            # handle 2 input
            if qinput == '2':
                print('Enter department id:')
                dept_id = str(input())

                values = (dept_id,)
                query = """
                        SELECT e.last_name, e.first_name
                        FROM employee AS e
                        JOIN department AS d
                        ON e.dept_id = d.dept_id
                        WHERE d.dept_id = %s
                        """
                try:
                    with conn.cursor() as cursor:
                        cursor.execute(query, values)
                        for row in cursor:
                            print(row)
                except Error as e:
                    print('Invalid input, returned to main menu')

            # handle 3 input
            if qinput == '3':
                print('Enter date (yyyy-mm-dd):')
                date = str(input())

                values = (date,)
                query = """
                        SELECT COUNT(*)
                        FROM visit
                        WHERE date = %s
                        """
                try:
                    with conn.cursor() as cursor:
                        cursor.execute(query, values)
                        for row in cursor:
                            print(row)
                except Error as e:
                    print('Invalid input, returned to main menu')

            # handle 4 input
            if qinput == '4':
                print('Enter employee last name:')
                last_name = str(input())
                print('Enter employee first name:')
                first_name = str(input())

                values = (last_name, first_name,)
                query = """
                        SELECT ws.start_time, ws.end_time, ws.day
                        FROM work_slot AS ws
                        JOIN employee_work_slot AS ews
                        ON ews.slot_id = ws.slot_id
                        JOIN employee AS e
                        ON e.employee_id = ews.employee_id
                        WHERE e.last_name = %s
                        AND e.first_name = %s
                        """
                try:
                    with conn.cursor() as cursor:
                        cursor.execute(query, values)
                        for row in cursor:
                            print(row)
                except Error as e:
                    print('Invalid input, returned to main menu')

            # handle 5 input
            if qinput == '5':
                query = """
                        SELECT date, COUNT(*)
                        FROM visit
                        GROUP BY date
                        ORDER BY COUNT(*) DESC
                        LIMIT 5
                        """
                try:
                    with conn.cursor() as cursor:
                        cursor.execute(query)
                        for row in cursor:
                            print(row)
                except Error as e:
                    print('Invalid input, returned to main menu')

            # handle b input
            if qinput == 'b':
                print('Welcome the the Art Museum database!')
            
            # handle invalid inputs
            possibleqinputs = ['1', '2', '3', 'b']
            validqinput = False
            for i in possibleqinputs:
                if qinput == i:
                    validqinput = True
            if not validqinput:
                print('Invalid input, returned to menu')

        # handle p input
        if userinput == 'p':
            print('Select procedure:')
            print('1 - get_visits_by_day')
            print('2 - get_employee_work_day')
            print('3 - get_art_by_artist')
            print('b - back to menu')

            selectinput = str(input())

            # handle first procedure
            if selectinput == '1':
                print('Enter date (yyyy-mm-dd):')
                pinput = str(input())

                with conn.cursor() as cursor:
                    cursor.callproc('get_visits_by_day', (pinput,))
                    results = cursor._stored_results
                    for result in results:
                        for visitor in result.fetchall():
                            print(visitor)

            # handle second procedure
            if selectinput == '2':
                print('Enter date (yyyy-mm-dd):')
                pinput = str(input())

                with conn.cursor() as cursor:
                    cursor.callproc('get_employee_work_day', (pinput,))
                    results = cursor._stored_results
                    for result in results:
                        for employee in result.fetchall():
                            print(employee)

            # handle third procedure
            if selectinput == '3':
                print('Enter artist last name:')
                pinput1 = str(input())
                print('Enter artist first name')
                pinput2 = str(input())

                with conn.cursor() as cursor:
                    cursor.callproc('get_art_by_artist', (pinput1, pinput2,))
                    results = cursor._stored_results
                    for result in results:
                        for artist in result.fetchall():
                            print(artist)

            # handle b input
            if selectinput == 'b':
                print('Welcome the the Art Museum database!')


            # handle invalid inputs
            possiblefinputs = ['1', '2', '3', 'b']
            validsinput = False
            for i in possiblefinputs:
                if selectinput == i:
                    validsinput = True
            if not validsinput:
                print('Invalid input, returned to menu')

        # handle u input
        if userinput == 'u':
            print('Select update function:')
            print('u - update')
            print('i - insert')
            print('d - delete')
            print('b - back')
            
            updateinput = str(input())

            # handle u input
            if updateinput == 'u':
                print('Table to update:')
                print('1 - department')
                print('2 - employee')
                print('3 - exhibit')
                print('4 - artist')
                print('5 - piece')
                print('6 - visitor')
                print('7 - visit')
                print('b - back')

                uinput = str(input())

                # handle 1 input
                if uinput == '1':
                    print('Enter field to set:')
                    field = str(input())
                    print('Enter value to set to:')
                    value1 = str(input())
                    print('Enter where field:')
                    wheref = str(input())
                    print('Enter where parameter:')
                    wherep = str(input())

                    statement = f'UPDATE department SET {field} = %s WHERE {wheref} = %s'
                    values = (value1, wherep)

                    try:
                        with conn.cursor() as cursor:
                            cursor.execute(statement, values)
                            conn.commit()
                            print('Update successful')
                    except Error as e:
                        print(e)
                
                # handle 2 input
                if uinput == '2':
                    print('Enter field to set:')
                    field = str(input())
                    print('Enter value to set to:')
                    value1 = str(input())
                    print('Enter where field:')
                    wheref = str(input())
                    print('Enter where parameter:')
                    wherep = str(input())

                    statement = f'UPDATE employee SET {field} = %s WHERE {wheref} = %s'
                    values = (value1, wherep)

                    try:
                        with conn.cursor() as cursor:
                            cursor.execute(statement, values)
                            conn.commit()
                            print('Update successful')
                    except Error as e:
                        print(e)

                # handle 3 input
                if uinput == '3':
                    print('Enter field to set:')
                    field = str(input())
                    print('Enter value to set to:')
                    value1 = str(input())
                    print('Enter where field:')
                    wheref = str(input())
                    print('Enter where parameter:')
                    wherep = str(input())

                    statement = f'UPDATE exhibit SET {field} = %s WHERE {wheref} = %s'
                    values = (value1, wherep)

                    try:
                        with conn.cursor() as cursor:
                            cursor.execute(statement, values)
                            conn.commit()
                            print('Update successful')
                    except Error as e:
                        print(e)

                # handle 4 input
                if uinput == '4':
                    print('Enter field to set:')
                    field = str(input())
                    print('Enter value to set to:')
                    value1 = str(input())
                    print('Enter where field:')
                    wheref = str(input())
                    print('Enter where parameter:')
                    wherep = str(input())

                    statement = f'UPDATE artist SET {field} = %s WHERE {wheref} = %s'
                    values = (value1, wherep)

                    try:
                        with conn.cursor() as cursor:
                            cursor.execute(statement, values)
                            conn.commit()
                            print('Update successful')
                    except Error as e:
                        print(e)

                # handle 5 input
                if uinput == '5':
                    print('Enter field to set:')
                    field = str(input())
                    print('Enter value to set to:')
                    value1 = str(input())
                    print('Enter where field:')
                    wheref = str(input())
                    print('Enter where parameter:')
                    wherep = str(input())

                    statement = f'UPDATE piece SET {field} = %s WHERE {wheref} = %s'
                    values = (value1, wherep)

                    try:
                        with conn.cursor() as cursor:
                            cursor.execute(statement, values)
                            conn.commit()
                            print('Update successful')
                    except Error as e:
                        print(e)

                # handle 6 input
                if uinput == '6':
                    print('Enter field to set:')
                    field = str(input())
                    print('Enter value to set to:')
                    value1 = str(input())
                    print('Enter where field:')
                    wheref = str(input())
                    print('Enter where parameter:')
                    wherep = str(input())

                    statement = f'UPDATE visitor SET {field} = %s WHERE {wheref} = %s'
                    values = (value1, wherep)

                    try:
                        with conn.cursor() as cursor:
                            cursor.execute(statement, values)
                            conn.commit()
                            print('Update successful')
                    except Error as e:
                        print(e)

                # handle 7 input
                if uinput == '7':
                    print('Enter field to set:')
                    field = str(input())
                    print('Enter value to set to:')
                    value1 = str(input())
                    print('Enter where field:')
                    wheref = str(input())
                    print('Enter where parameter:')
                    wherep = str(input())

                    statement = f'UPDATE visit SET {field} = %s WHERE {wheref} = %s'
                    values = (value1, wherep)

                    try:
                        with conn.cursor() as cursor:
                            cursor.execute(statement, values)
                            conn.commit()
                            print('Update successful')
                    except Error as e:
                        print(e)

                # handle b input
                if uinput == 'b':
                    print('Welcome the the Art Museum database!')
                
                # handle invalid inputs
                possibleuinputs = ['1', '2', '3', '4', '5', '6', '7', 'o', 'b']
                validuinput = False
                for i in possibleuinputs:
                    if uinput == i:
                        validuinput = True
                if not validuinput:
                    print('Invalid input, returned to menu')

            # handle i input
            if updateinput == 'i':
                print('Table to insert into:')
                print('1 - department')
                print('2 - employee')
                print('3 - exhibit')
                print('4 - artist')
                print('5 - piece')
                print('6 - visitor')
                print('7 - visit')
                print('b - back')
                
                sinput = str(input())

                # handle 1 input
                if sinput == '1':
                    print('Number of rows to insert:')
                    rinput = str(input())
                    
                    statement = 'INSERT INTO department (dept_name, description) VALUES (%s, %s)'
                    values = []

                    try:
                        i = 0
                        while i < int(rinput):
                            print('Enter dept_name:')
                            dept_name = str(input())
                            print('Enter description:')
                            description = str(input())

                            values.append((dept_name, description))

                            i += 1

                        with conn.cursor() as cursor:
                            cursor.executemany(statement, values)
                            conn.commit()
                            print('Insert successful')
                    
                    except ValueError:
                        print('Invalid input, returned to main menu')
                    except Error as e:
                        print(e)
                
                # handle 2 input
                if sinput == '2':
                    print('Number of rows to insert:')
                    rinput = str(input())
                    
                    statement = 'INSERT INTO employee (dept_id, last_name, first_name, birth_date, wage) VALUES (%s, %s, %s, %s, %s)'
                    values = []

                    try:
                        i = 0
                        while i < int(rinput):
                            print('Enter dept_id:')
                            dept_id = str(input())
                            print('Enter last_name:')
                            last_name = str(input())
                            print('Enter first_name:')
                            first_name = str(input())
                            print('Enter birth date (yyyy-mm-dd)')
                            birth_date = str(input())
                            print('Enter wage:')
                            wage = str(input())

                            values.append((dept_id, last_name, first_name, birth_date, wage))

                            i += 1

                        with conn.cursor() as cursor:
                            cursor.executemany(statement, values)
                            conn.commit()
                            print('Insert successful')
                    
                    except ValueError:
                        print('Invalid input, returned to main menu')
                    except Error as e:
                        print(e)
                
                # handle 3 input
                if sinput == '3':
                    print('Number of rows to insert:')
                    rinput = str(input())
                    
                    statement = 'INSERT INTO exhibit (manager_id, theme, description) VALUES (%s, %s, %s)'
                    values = []

                    try:
                        i = 0
                        while i < int(rinput):
                            print('Enter manager_id:')
                            manager_id = str(input())
                            print('Enter theme:')
                            theme = str(input())
                            print('Enter description:')
                            description = str(input())

                            values.append((manager_id, theme, description))

                            i += 1

                        with conn.cursor() as cursor:
                            cursor.executemany(statement, values)
                            conn.commit()
                            print('Insert successful')
                    
                    except ValueError:
                        print('Invalid input, returned to main menu')
                    except Error as e:
                        print(e)

                # handle 4 input
                if sinput == '4':
                    print('Number of rows to insert:')
                    rinput = str(input())
                    
                    statement = 'INSERT INTO artist (last_name, first_name, birth_date, death_date, nationality, biography) VALUES (%s, %s, %s, %s, %s, %s)'
                    values = []

                    try:
                        i = 0
                        while i < int(rinput):
                            print('Enter last_name')
                            last_name = str(input())
                            print('Enter first_name')
                            first_name = str(input())
                            print('Enter birth_date (yyyy-mm-dd)')
                            birth_date = str(input())
                            print('Enter death_date (yyyy-mm-dd)')
                            death_date = str(input())
                            print('Enter nationality')
                            nationality = str(input())
                            print('Enter biography')
                            biography = str(input())

                            values.append((last_name, first_name, birth_date, death_date, nationality, biography))

                            i += 1

                        with conn.cursor() as cursor:
                            cursor.executemany(statement, values)
                            conn.commit()
                            print('Insert successful')

                    except ValueError:
                        print('Invalid input, returned to main menu')
                    except Error as e:
                        print(e)

                # handle 5 input
                if sinput == '5':
                    print('Number of rows to insert:')
                    rinput = str(input())
                    
                    statement = 'INSERT INTO piece (artist_id, exhibit_id, name, description, year) VALUES (%s, %s, %s, %s, %s)'
                    values = []

                    try:
                        i = 0
                        while i < int(rinput):
                            print('Enter artist_id')
                            artist_id = str(input())
                            print('Enter exhibit_id')
                            exhibit_id = str(input())
                            print('Enter name')
                            name = str(input())
                            print('Enter description')
                            description = str(input())
                            print('Enter year')
                            year = str(input())

                            values.append((artist_id, exhibit_id, name, description, year))

                            i += 1

                        with conn.cursor() as cursor:
                            cursor.executemany(statement, values)
                            conn.commit()
                            print('Insert successful')

                    except ValueError:
                        print('Invalid input, returned to main menu')
                    except Error as e:
                        print(e)

                # handle 6 input
                if sinput == '6':
                    print('Number of rows to insert:')
                    rinput = str(input())
                    
                    statement = 'INSERT INTO visitor (last_name, first_name, email, phone_num, birth_date) VALUES (%s, %s, %s, %s, %s)'
                    values = []

                    try:
                        i = 0
                        while i < int(rinput):
                            print('Enter last_name')
                            last_name = str(input())
                            print('Enter first_name')
                            first_name = str(input())
                            print('Enter email')
                            email = str(input())
                            print('Enter phone_num')
                            phone_num = str(input())
                            print('Enter birth_date')
                            birth_date = str(input())

                            values.append((last_name, first_name, email, phone_num, birth_date))

                            i += 1

                        with conn.cursor() as cursor:
                            cursor.execute(statement, values)
                            conn.commit()
                            print('Insert successful')

                    except ValueError:
                        print('Invalid input, returned to main menu')
                    except Error as e:
                        print(e)

                # handle 7 input
                if sinput == '7':
                    print('Number of rows to insert:')
                    rinput = str(input())
                    
                    statement = 'INSERT INTO visit (ticket_id, visitor_id, receptionist_id, check_in, date) VALUES (%s, %s, %s, %s, %s)'
                    values = []

                    try:
                        i = 0
                        while i < int(rinput):
                            print('Enter ticket_id')
                            ticket_id = str(input())
                            print('Enter visitor_id')
                            visitor_id = str(input())
                            print('Enter receptionist_id')
                            receptionist_id = str(input())
                            print('Enter check_in (hh:mm:ss)')
                            check_in = str(input())
                            print('Enter date (myyyy-mm-dd)')
                            date = str(input())

                            values.append((ticket_id, visitor_id, receptionist_id, check_in, date))

                            i += 1

                        with conn.cursor() as cursor:
                            cursor.execute(statement, values)
                            conn.commit()
                            print('Insert successful')

                    except ValueError:
                        print('Invalid input, returned to main menu')
                    except Error as e:
                        print(e)

                # handle b input
                if sinput == 'b':
                    print('Welcome the the Art Museum database!')
                
                # handle invalid inputs
                possibleiinputs = ['1', '2', '3', '4', '5', '6', '7', 'o', 'b']
                validiinput = False
                for i in possibleiinputs:
                    if sinput == i:
                        validiinput = True
                if not validiinput:
                    print('Invalid input, returned to menu')

            # handle d input
            if updateinput == 'd':
                print('Table to delete from:')
                print('1 - department')
                print('2 - employee')
                print('3 - exhibit')
                print('4 - artist')
                print('5 - piece')
                print('6 - visitor')
                print('7 - visit')
                print('b - back')

                dinput = str(input())

                # handle 1 input
                if dinput == '1':
                    print('ID to delete:')
                    idinput = str(input())
                    value = (idinput,)

                    try:
                        statement = 'DELETE FROM department WHERE dept_id = %s'
                        with conn.cursor() as cursor:
                            cursor.execute(statement, value)
                            conn.commit()
                            print('Delete successful')
                    
                    except ValueError:
                        print('Invalid input, returned to main menu')
                    except Error as e:
                        print(e)
                
                # handle 2 input
                if dinput == '2':
                    print('ID to delete:')
                    idinput = str(input())

                    value = (idinput,)
                    try:
                        statement = 'DELETE FROM employee WHERE employee_id = %s'
                        with conn.cursor() as cursor:
                            cursor.execute(statement, value)
                            conn.commit()
                            print('Delete successful')
                    
                    except ValueError:
                        print('Invalid input, returned to main menu')
                    except Error as e:
                        print(e)

                # handle 3 input
                if dinput == '3':
                    print('ID to delete:')
                    idinput = str(input())
                    value = (idinput,)

                    try:
                        statement = 'DELETE FROM exhibit WHERE exhibit_id = %s'
                        with conn.cursor() as cursor:
                            cursor.execute(statement, value)
                            conn.commit()
                            print('Delete successful')
                    
                    except ValueError:
                        print('Invalid input, returned to main menu')
                    except Error as e:
                        print(e)
                
                # handle 4 input
                if dinput == '4':
                    print('ID to delete:')
                    idinput = str(input())
                    value = (idinput,)

                    try:
                        statement = 'DELETE FROM artist WHERE artist = %s'
                        with conn.cursor() as cursor:
                            cursor.execute(statement, value)
                            conn.commit()
                            print('Delete successful')
                    
                    except ValueError:
                        print('Invalid input, returned to main menu')
                    except Error as e:
                        print(e)

                # handle 5 input
                if dinput == '5':
                    print('ID to delete:')
                    idinput = str(input())
                    value = (idinput,)

                    try:
                        statement = 'DELETE FROM piece WHERE piece_id = %s'
                        with conn.cursor() as cursor:
                            cursor.execute(statement, value)
                            conn.commit()
                            print('Delete successful')
                    
                    except ValueError:
                        print('Invalid input, returned to main menu')
                    except Error as e:
                        print(e)

                # handle 6 input
                if dinput == '6':
                    print('ID to delete:')
                    idinput = str(input())
                    value = (idinput,)

                    try:
                        statement = 'DELETE FROM visitor WHERE visitor_id = %s'
                        with conn.cursor() as cursor:
                            cursor.execute(statement, value)
                            conn.commit()
                            print('Delete successful')
                    
                    except ValueError:
                        print('Invalid input, returned to main menu')
                    except Error as e:
                        print(e)

                # handle 7 input
                if dinput == '7':
                    print('ID to delete:')
                    idinput = str(input())
                    value = (idinput,)

                    try:
                        statement = 'DELETE FROM visit WHERE visit_id = %s'
                        with conn.cursor() as cursor:
                            cursor.execute(statement, value)
                            conn.commit()
                            print('Delete successful')
                    
                    except ValueError:
                        print('Invalid input, returned to main menu')
                    except Error as e:
                        print(e)

                # handle b input
                if dinput == 'b':
                    print('Welcome the the Art Museum database!')

                # handle invalid inputs
                possibledinputs = ['1', '2', '3', '4', '5', '6', '7', 'o', 'b']
                validdinput = False
                for i in possibledinputs:
                    if dinput == i:
                        validdinput = True
                if not validdinput:
                    print('Invalid input, returned to menu')


            # handle invalid inputs
            possibleuinputs = ['u', 'i', 'd', 'b']
            validuinput = False
            for i in possibleuinputs:
                if updateinput == i:
                    validuinput = True
            if not validuinput:
                print('Invalid input, returned to menu')

        # handle x input
        if userinput == 'x':
            running = False

        # handle invalid inputs
        validinput = False
        for i in possibleinputs:
            if userinput == i:
                validinput = True
        if not validinput:
            print('Invalid input, try again')

    conn.close()

if __name__ == '__main__':
    main()