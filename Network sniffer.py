from PyQt5 import QtWidgets, QtCore
from scapy.all import sniff
import pandas as pd
import threading

class NetworkSniffer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.packet_data = []
        self.sniffing = False
        self.thread = None

    def initUI(self):
        self.setWindowTitle("Network Sniffer")
        self.setGeometry(100, 100, 800, 600)

        # Table to display packets
        self.table = QtWidgets.QTableWidget(self)
        self.table.setGeometry(20, 20, 760, 500)
        self.table.setColumnCount(5)  # Columns: Time, Source, Destination, Protocol, Length
        self.table.setHorizontalHeaderLabels(["Time", "Source", "Destination", "Protocol", "Length"])

        # Buttons
        self.start_button = QtWidgets.QPushButton("Start", self)
        self.start_button.setGeometry(20, 540, 100, 40)
        self.start_button.clicked.connect(self.start_sniffing)

        self.stop_button = QtWidgets.QPushButton("Stop", self)
        self.stop_button.setGeometry(140, 540, 100, 40)
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.stop_sniffing)

        self.export_button = QtWidgets.QPushButton("Export", self)
        self.export_button.setGeometry(260, 540, 100, 40)
        self.export_button.clicked.connect(self.export_data)

    def start_sniffing(self):
        self.sniffing = True
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.thread = threading.Thread(target=self.sniff_packets)
        self.thread.start()

    def stop_sniffing(self):
        self.sniffing = False
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def sniff_packets(self):
        sniff(prn=self.process_packet, stop_filter=lambda x: not self.sniffing)

    def process_packet(self, packet):
        # Extract packet details
        details = [
            str(packet.time),
            getattr(packet, "src", "N/A"),
            getattr(packet, "dst", "N/A"),
            packet.summary(),
            len(packet)
        ]
        self.packet_data.append(details)
        self.update_table(details)

    def update_table(self, details):
        QtCore.QMetaObject.invokeMethod(self, "_update_table", QtCore.Qt.QueuedConnection, 
                                        QtCore.Q_ARG(list, details))

    @QtCore.pyqtSlot(list)
    def _update_table(self, details):
        row = self.table.rowCount()
        self.table.insertRow(row)
        for col, detail in enumerate(details):
            self.table.setItem(row, col, QtWidgets.QTableWidgetItem(str(detail)))

    def export_data(self):
        if not self.packet_data:
            QtWidgets.QMessageBox.warning(self, "No Data", "No packets captured to export.")
            return
        path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "", "CSV Files (*.csv)")
        if path:
            df = pd.DataFrame(self.packet_data, columns=["Time", "Source", "Destination", "Protocol", "Length"])
            df.to_csv(path, index=False)
            QtWidgets.QMessageBox.information(self, "Export Successful", f"Data exported to {path}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = NetworkSniffer()
    window.show()
    sys.exit(app.exec_())
