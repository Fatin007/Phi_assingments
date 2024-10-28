class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        Star_Cinema.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().entry_hall(self)
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        
        seats = []
        for i in range(self.__rows):
            seats.append([0] * self.__cols)

        self.__seats[id] = seats

    def book_seats(self, id, row, col):
        row -= 1
        col -= 1
        if id not in self.__seats:
            raise ValueError("Invalid show ID.")
        
        seats = self.__seats[id]
        
        if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
            raise IndexError(f"Invalid seat position: ({row+1}, {col+1}).")
        if seats[row][col] == 1:
            raise ValueError(f"Seat ({row+1}, {col+1}) is already booked.")
        
        seats[row][col] = 1
        print(f"Seat ({row+1},{col+1}) is successfully booked.")

    def view_show_list(self):
        for show in self.__show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, id):
        if id not in self.__seats:
            raise ValueError("Invalid show ID.")
        
        seats = self.__seats[id]

        print("\n\Availabile Seat(s):")

        for i in range(self.__rows):
            for j in range(self.__cols):
                if seats[i][j] == 0:
                    print(f"Seat ({i+1},{j+1})")

        print("\n\nMatrix:")

        for i in seats:
            print(i)


cinema = Star_Cinema()
hall1 = Hall(rows=10, cols=10, hall_no=1)
hall1.entry_show(id="111", movie_name="JAVA", time="06:00 PM")
hall2 = Hall(rows=5, cols=5, hall_no=2)
hall2.entry_show(id="222", movie_name="CPP", time="8:00 PM")

def main():
    while True:
        print("\n----- Star Cinema -----")
        print("1. View all shows today")
        print("2. View available seats")
        print("3. Book ticket")
        print("4. Exit")
        print("-----------------------")
        op = input("Enter your option: ")

        if op == '1':
            print("Today's Shows:")
            for hall in Star_Cinema.hall_list:
                hall.view_show_list()

        elif op == '2':
            show_id = input("Enter the show ID: ")
            for hall in Star_Cinema.hall_list:
                try:
                    hall.view_available_seats(show_id)
                    break
                except ValueError as e:
                    print(e)

        elif op == '3':
            show_id = input("Enter the show ID: ")
            try:
                nun_of_seats = int(input("Enter the number of seats: "))
            except ValueError:
                print("Invalid input format. Enter a number for number of seats.")
                continue

            for i in range(nun_of_seats):
                try:
                    row = int(input(f"Enter the row for seat {i+1}: "))
                    col = int(input(f"Enter the col for seat {i+1}: "))
                except ValueError:
                    print("Invalid input format. Enter a number for row and col.")
                    break
                
                bool = False
                for hall in Star_Cinema.hall_list:
                    try:
                        hall.book_seats(show_id, row, col)
                        bool = True
                        break
                    except ValueError as e:
                        print(e)
                    except IndexError as e:
                        print(e)
                
                if bool==False:
                    i-=1


        elif op == '4':
            print("Thank you for visiting Star Cinema!")
            break

        else:
            print("Invalid option. Please try again.")

main()
