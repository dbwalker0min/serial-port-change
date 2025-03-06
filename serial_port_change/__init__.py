import serial.tools.list_ports
import time

def get_serial_ports() -> set[str]:
    """Get a set of serial ports available on the system."""
    return {port.device for port in serial.tools.list_ports.comports()}

def monitor_serial_ports() -> None:
    """Monitor changes in the serial ports added or removed from the system."""
    print("Monitoring serial ports...")
    previous_ports = get_serial_ports()

    while True:
        try:
            time.sleep(0.5)
            current_ports = get_serial_ports()

            # determine if any ports were added or removed. This uses set operations.
            added_ports = current_ports - previous_ports
            removed_ports = previous_ports - current_ports

            for port in added_ports:
                print(f"New serial port detected: {port}")

            for port in removed_ports:
                print(f"Serial port removed: {port}")

            # establish the new baseline
            previous_ports = current_ports

        except KeyboardInterrupt:
            # user exits with control-C
            break

if __name__ == "__main__":
    monitor_serial_ports()
