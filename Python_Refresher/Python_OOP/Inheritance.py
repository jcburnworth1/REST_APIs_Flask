##### Inheritance Example #####
class Device: ## Basic object that we will inherit from - Knows nothing about inherited classes
    def __init__(self, name: str, connected_by: str):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})" # !r - Calls repr method of self.name

    def disconnect(self):
        self.connected = False
        print("Disconnected.")

# printer = Device("Printer", "USB") ## Device is not a printer but we need printer functionality
# print(printer)
# printer.disconnect()

##### Inherit Devices to Printer object #####
class Printer(Device):
    def __init__(self, name: str, connected_by: str, capactiy: int):
        super().__init__(name, connected_by)
        self.capacity = capactiy ## Maximum Capacity
        self.remaining_pages = capactiy ## Current Capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining.)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected.")
            return

        print(f"Printing {pages} pages.")

        self.remaining_pages -= pages

printer = Printer("Printer", "USB", 50)
printer.print(10)
printer.disconnect()