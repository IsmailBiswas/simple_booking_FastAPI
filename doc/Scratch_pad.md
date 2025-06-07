## Models

**Classes**
- id
- class_name
- datetime
- instructor (str field)
- total_slot
- available_slots

**Booking**
- id
- class_id
- client_name
- client_email
- booking_date


## Booking process

make a booking post request -> validate data -> check if requested class exists
-> check if there is availble slot -> update available slot number ->
create new booking entry -> reutrn booked entry
