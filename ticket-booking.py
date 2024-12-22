def book_seat(total_seats, booked_seats, seat_number):
    if seat_number in booked_seats:
        return "Seat is already booked."
    elif seat_number < 1 or seat_number > total_seats:
        return "Invalid seat number."
    else:
        booked_seats.append(seat_number)
        return "Seat successfully booked."
def cancel_seat(booked_seats, seat_number):
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
        return "Seat successfully cancelled."
    else:
        return "Seat is not booked."
def get_available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
total_seats = 10
booked_seats = [2, 5, 7]
book_seat = 3
cancel_seat = 5
available_seats = get_available_seats(total_seats, booked_seats)
print(f"Available seats: {available_seats}")
