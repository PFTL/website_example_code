import random
import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView, QPushButton, QTableWidgetItem, QTableWidget
from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex, QAbstractItemModel

df = pd.DataFrame({'a': [random.random() for i in range(500)],
                   'b': [random.random() for i in range(500)],
                   'c': [random.random() for i in range(500)]})

class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


class MyWidget(QTableWidget):
    def __init__(self, model):
        super(MyWidget, self).__init__(parent=None)
        super().setModel(model)

def update_df():
    df['a'][0] = 'Aquiles'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = pandasModel(df)
    view = MyWidget(model)
    view.resize(800, 600)
    btn = QPushButton('Click Me')
    element = QTableWidgetItem("50, 1")
    btn.clicked.connect(lambda: view.scrollToItem(element))
    btn.show()
    view.show()
    sys.exit(app.exec_())