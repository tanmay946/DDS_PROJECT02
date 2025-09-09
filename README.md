# 🅿️ Parking Lot Management System (Python)

This is a simple command-line-based Parking Lot Management System written in Python. It tracks cars using a linked list and a slot array, supports dynamic entry/exit, and tags Maharashtra-registered vehicles.

---

## 🚗 Features

- Add (park) a car in the next available slot
- Remove (exit) a car by license plate
- Display currently parked cars
- Detect and tag **Maharashtra** cars (`MH` plates)
- Fixed capacity management
- Linked list used for efficient insert/delete

---

## 📦 Requirements

- Python 3.x
- No third-party packages required

---

## 🧪 How to Run

```bash
python parking_lot.py


✅ Car KA01AB1234 parked at slot 0
✅ Car MH02CD5678 (Maharashtra) parked at slot 1
✅ Car DL03EF9012 parked at slot 2
🚫 Parking Full: Cannot park car MH04GH3456
🚗 Car MH02CD5678 exited from slot 1
✅ Car MH04GH3456 (Maharashtra) parked at slot 1


🧩 Future Improvements

#Add GUI with Tkinter or PyQt

#Slot reservation system

#Vehicle type categorization (2-wheeler, 4-wheeler)

#Save data to file
