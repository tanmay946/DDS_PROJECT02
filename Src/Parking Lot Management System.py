class CarNode:
    """
    Node to represent each parked car in the linked list.
    """
    def __init__(self, license_plate, slot_number):
        self.license_plate = license_plate
        self.slot_number = slot_number
        self.next = None


class ParkingLot:
    """
    A linked list and slot-array-based Parking Lot system.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None] * capacity  # List to track slot occupancy
        self.head = None  # Head of linked list
        self.tail = None  # Tail of linked list
        self.active_cars = 0  # Count of currently parked cars

    def is_full(self):
        return self.active_cars == self.capacity

    def is_empty(self):
        return self.active_cars == 0

    def allocate_slot(self):
        """
        Find the first free slot index.
        """
        for i in range(self.capacity):
            if self.slots[i] is None:
                return i
        return -1  # No free slot found

    def park_car(self, license_plate):
        """
        Parks a car in the first available slot.
        """
        if self.is_full():
            print(f"🚫 Parking Full: Cannot park car {license_plate}")
            return

        slot = self.allocate_slot()
        if slot == -1:
            print(f"⚠ Error: No available slot for {license_plate}")
            return

        # Mark slot as occupied
        self.slots[slot] = license_plate
        new_car = CarNode(license_plate, slot)

        # Add to linked list
        if not self.head:
            self.head = self.tail = new_car
        else:
            self.tail.next = new_car
            self.tail = new_car

        self.active_cars += 1
        region = " (Maharashtra)" if license_plate.startswith("MH") else ""
        print(f"✅ Car {license_plate}{region} parked at slot {slot}")

    def exit_car(self, license_plate):
        """
        Removes the car with the given license plate from the lot.
        """
        if self.is_empty():
            print("⚠ Parking lot is empty.")
            return

        prev = None
        current = self.head

        while current:
            if current.license_plate == license_plate:
                # Free the slot
                self.slots[current.slot_number] = None
                print(f"🚗 Car {license_plate} exited from slot {current.slot_number}")

                # Update linked list pointers
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next

                if current == self.tail:
                    self.tail = prev

                self.active_cars -= 1
                return
            prev = current
            current = current.next

        print(f"⚠ Car {license_plate} not found in the lot.")

    def display_parked_cars(self):
        """
        Displays all currently parked cars with slot and region info.
        """
        if self.is_empty():
            print("🚫 No cars parked.")
            return

        print("🚘 Currently parked cars:")
        current = self.head
        while current:
            region = " (Maharashtra)" if current.license_plate.startswith("MH") else ""
            print(f" - Car {current.license_plate}{region} at slot {current.slot_number}")
            current = current.next


# Entry point
if __name__ == "__main__":
    lot = ParkingLot(capacity=3)

    # Park 3 cars
    lot.park_car("KA01AB1234")  # Karnataka
    lot.park_car("MH02CD5678")  # Maharashtra
    lot.park_car("DL03EF9012")  # Delhi

    lot.display_parked_cars()

    # Try to park when full
    lot.park_car("MH04GH3456")

    # Exit a car
    lot.exit_car("MH02CD5678")
    lot.display_parked_cars()

    # Park again (should now have a free slot)
    lot.park_car("MH04GH3456")
    lot.display_parked_ca
