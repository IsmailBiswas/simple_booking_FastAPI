## **🧪 Python Developer Assignment (1+ Years Experience)**

### **Objective:**

Build a simple **Booking API** for a fictional fitness studio using Python. The
goal is to evaluate your coding skills, design thinking, and understanding of
backend development principles.

### **📌 Requirements:**

#### **Scenario:**

A fitness studio offers classes like Yoga, Zumba, and HIIT. Clients should be able to view available classes and book a spot.

---

### **🎯 Tasks:**

#### **1\. API Endpoints to Implement:**

* `GET /classes`

  * Returns a list of all upcoming fitness classes (name, date/time, instructor, available slots)

* `POST /book`

  * Accepts a booking request (class\_id, client\_name, client\_email)

  * Validates if slots are available, and reduces available slots upon successful booking

* `GET /bookings`

  * Returns all bookings made by a specific email address

### 

### 

### 

### **🛠️ Technical Expectations:**

* Use **Python** with any backend framework of your choice (**Django**, **Flask**, or **FastAPI** preferred)

* Use an in-memory DB like SQLite or store data in a file (no need to set up a full DB)

* Write **clean, modular, and well-documented code**

* Timezone management: Classes created in IST and on change of timezone all the slots should be changed accordingly

* Handle **errors and edge cases** (e.g., overbooking, missing fields)

* Add basic **input validation**, logging, or unit tests

---

### **📦 Deliverables:**

* A public GitHub repo or zip file containing:

  * Source code

  * Sample input data or seed data

  * README with setup instructions and sample cURL or Postman requests

Submit a Loom Video with a walkthrough of the entire assignment (Mandatory)  
Timeline: Submit within 3 working days 

---

### **✅ Evaluation Criteria:**

* Code readability and structure

* API design and functionality

* Error handling and validation

* Use of good practices (DRY, modularity, naming, etc.)

* Bonus: Basic tests, thoughtful documentation, creativity

