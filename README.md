This project is a Python-based network sniffer with a graphical user interface (GUI) built using PyQt5. It allows users to capture network packets in real-time, display detailed packet information in an interactive table, and export the captured data to a CSV file for further analysis.

Features
Real-Time Packet Sniffing: Capture network packets using Scapy and display them instantly in the GUI.
Interactive Packet Display: View packet details (timestamp, source, destination, protocol, length) in a table.
Start/Stop Sniffing: Control packet capturing with start and stop buttons.
Export to CSV: Save captured packets to a CSV file for offline analysis.
Multi-threading: Ensures the GUI remains responsive during packet sniffing.
Requirements
To run this project, you need the following dependencies:

Python 3.7 or higher
PyQt5
Scapy
Pandas
Install the required libraries using pip:

pip install pyqt5 scapy pandas
How to Use
Clone the repository:

git clone <repository_url>
cd <repository_directory>
Run the application:

python network_sniffer_gui.py
Use the following controls in the GUI:

Start Button: Begin capturing network packets.
Stop Button: Stop capturing packets.
Export Button: Save the captured packet data to a CSV file.
View packet details in the table as they are captured.

Project Structure
network sniffer.py: The main script that implements the GUI and packet sniffing logic.
Preview
Real-Time Packet Table: Displays captured packet details such as time, source, destination, protocol, and length.
Control Buttons: Start, stop, and export captured packets easily.
Notes
Root/admin permissions may be required to capture packets on some systems.
Ensure that Scapy is correctly installed and configured for your operating system.
License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the terms of the license.

Acknowledgments
PyQt5 Documentation
Scapy Documentation
