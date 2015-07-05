from PyQt4.QtGui import *
from PyQt4.QtCore import *

from my_gui import Ui_MainWindow
from iron_rich_foods import foods

class MyMainGui(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainGui, self).__init__(parent)
        self.setupUi(self)
        self.rowcount = 1
        self.isCollapsed = True
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setHeaderLabels(['Food', 'Amount of iron (mg)'])

        self.spinBox_hgb_level.valueChanged.connect(self.cal_conversion_and_diagnosis)
        self.comboBox_age_group_tab1.currentIndexChanged.connect(self.cal_conversion_and_diagnosis)
        self.comboBox_HgB_units.currentIndexChanged.connect(self.cal_conversion_and_diagnosis)
        self.spinBox_quantity_of_food.valueChanged.connect(self.update_tree)
        self.pushButton_expand_collapse_tree.clicked.connect(self.expand_or_collapse_tree)
        self.comboBox_anemia_type_tab3.currentIndexChanged.connect(self.anemia_type)

        app.setStyle(QStyleFactory.create('plastique'))

    def expand_or_collapse_tree(self):
        """Expands and collapses tree widget of iron rich foods.
        Also changes the buttons text and icon."""

        icon = QIcon()
        if self.isCollapsed:
            self.treeWidget.expandAll()
            self.isCollapsed = False
            self.pushButton_expand_collapse_tree.setText('Collapse Categories')
            icon.addPixmap(QPixmap(':/icons/collapse.png'))
        else:
            self.treeWidget.collapseAll()
            self.isCollapsed = True
            self.pushButton_expand_collapse_tree.setText('Expand Categories')
            icon.addPixmap(QPixmap(':/icons/expand.png'))
        self.pushButton_expand_collapse_tree.setIcon(icon)


    def update_tree(self):
        '''Updates the amount of iron in each food item in the tree
        whenever the quantity of food is changed through the spinbox'''

        self.treeWidget.clear()
        food_quantity = self.spinBox_quantity_of_food.value()
        plist, clist, clist_iron = foods()

        for idx1, parent in enumerate(plist):
            pitems = QTreeWidgetItem(self.treeWidget) # set tree widget class as the top level item
            pitems.setText(0, parent)
            child_list = clist[idx1]
            child_iron_list = clist_iron[idx1]

            for idx2, child in enumerate(child_list):
                citems = QTreeWidgetItem(pitems) # set the category as the top level item for each food in a category
                citems.setText(0, child)
                iron_value = child_iron_list[idx2]*food_quantity
                iron_value = '{0:.1f}'.format(iron_value)
                citems.setText(1, iron_value)

        if self.isCollapsed:
            self.treeWidget.collapseAll()
        else:
            self.treeWidget.expandAll()

        self.treeWidget.resizeColumnToContents(0)
        self.treeWidget.resizeColumnToContents(1)

    def cal_conversion_and_diagnosis(self):
        """Diagnoses anemia based on the level of hemoglobin. It also changes
        the input units into standard g/dl unit"""

        self.hgb_level = self.spinBox_hgb_level.value()
        self.hgb_unit = self.comboBox_HgB_units.currentText()
        self.age_group_tab1 = self.comboBox_age_group_tab1.currentText()

        if self.hgb_unit == 'g/L':
            # convert g\L into g\dL
            self.hgb_level = self.hgb_level / 10
            hgb_level_str = '{0:.2f}'.format(self.hgb_level)
            self.lineEdit_conversion.setText('The selected g/L contains ' + hgb_level_str + ' g/dl.')
        if self.hgb_unit == 'mmol/L':
            # convert mmol/L into g/dL
            self.hgb_level = self.hgb_level / 18
            hgb_level_str = '{0:.2f}'.format(self.hgb_level)
            self.lineEdit_conversion.setText('The selected mmol/L contains ' + hgb_level_str + ' g/dl.')

        if self.hgb_unit =='g/dl':
            self.lineEdit_conversion.setText('')

        if self.age_group_tab1 == 'Males > 15-years' or self.age_group_tab1 == 'Females > 15-years':
            # shows level of anemia for males and females above 15-years.
            if self.hgb_level >= 0 and self.hgb_level <= 5:
                self.lineEdit_diagnosis.setText('Severe anemia!')
                self._show_anemia_icon('Severe anemia!')
            elif self.hgb_level >= 6 and self.hgb_level <= 8:
                self.lineEdit_diagnosis.setText('Mild anemia!')
                self._show_anemia_icon('Mild anemia!')
            elif self.hgb_level >= 9 and self.hgb_level <= 13:
                self.lineEdit_diagnosis.setText('Normal!')
                self._show_anemia_icon('Normal!')
            elif self.hgb_level >= 14 and self.hgb_level <= 100:
                self.lineEdit_diagnosis.setText('High level of hemoglobin!')
                self._show_anemia_icon('High level of hemoglobin!')

        if self.age_group_tab1 == 'Males < 15-years' or self.age_group_tab1 == 'Females < 15-years':
            # shows level of anemia for males and females below 15-years.
            if self.hgb_level >= 0 and self.hgb_level <= 8:
                self.lineEdit_diagnosis.setText('Severe anemia!')
                self._show_anemia_icon('Severe anemia!')
            elif self.hgb_level >= 9 and self.hgb_level <= 11:
                self.lineEdit_diagnosis.setText('Mild anemia!')
                self._show_anemia_icon('Mild anemia!')
            elif self.hgb_level >= 12 and self.hgb_level <= 13:
                self.lineEdit_diagnosis.setText('Normal!')
                self._show_anemia_icon('Normal!')
            elif self.hgb_level >= 14 and self.hgb_level <= 100:
                self.lineEdit_diagnosis.setText('High level of hemoglobin!')
                self._show_anemia_icon('High level of hemoglobin!')

        if self.age_group_tab1 == 'Females pregnant' or self.age_group_tab1 == 'Children < 8-years':
            # shows level of anemia for pregnant females and children below 8-years.
            if self.hgb_level >= 0 and self.hgb_level <= 9:
                self.lineEdit_diagnosis.setText('Severe anemia!')
                self._show_anemia_icon('Severe anemia!')
            elif self.hgb_level >= 10 and self.hgb_level <= 13:
                self.lineEdit_diagnosis.setText('Mild anemia!')
                self._show_anemia_icon('Mild anemia!')
            elif self.hgb_level >= 13 and self.hgb_level <= 16:
                self.lineEdit_diagnosis.setText('Normal!')
                self._show_anemia_icon('Normal!')
            elif self.hgb_level >= 16 and self.hgb_level <= 100:
                self.lineEdit_diagnosis.setText('High level of hemoglobin!')
                self._show_anemia_icon('High level of hemoglobin!')

    def _show_anemia_icon(self, ane_type):
        """Convenience function to change anemia icon according to the diagnosis."""

        icon = QIcon()
        if ane_type == 'Severe anemia!':
            icon.addPixmap(QPixmap(':icons/severe-anemia.png'))
        elif ane_type == 'Mild anemia!':
            icon.addPixmap(QPixmap(':icons/mild-anemia.png'))
        elif ane_type == 'Normal!':
            icon.addPixmap(QPixmap(':icons/normal.png'))
        elif ane_type == 'High level of hemoglobin!':
            icon.addPixmap(QPixmap(':icons/high-hemoglobin.png'))

        self.toolButton_anemia_icon.setIcon(icon)


    def anemia_type(self):
        """Displays symptoms of anemia according to its severity."""

        self.anemia_type = self.comboBox_anemia_type_tab3.currentText()
        if self.anemia_type == 'Severe anemia':
            self.textEdit_anemia_symptoms.setText('1. Leg cramps.\n'
                                                  '2. Tingling (pins and needle sensation in hands and feet\n'
                                                  '3. Heart palpitation\n'
                                                  '4. Insomnia\n'
                                                  '5. Loss of sense of touch\n'
                                                  '6. Stiffness of arms and legs')
        else:
            self.anemia_type == 'Mild anemia'
            self.textEdit_anemia_symptoms.setText('1. Dizziness\n'
                                                  '2. Pale skin\n'
                                                  '3. Pica i.e., hunger or craving for strange substances such '
                                                  'as paper, ice, or dirt\n'
                                                  '4. Sourness of mouth\n'
                                                  '5. Cracking of lip corners\n'
                                                  '6. Vomiting\n'
                                                  '7. Headache')


if __name__ == '__main__':
    app = QApplication([])
    my_gui = MyMainGui()
    my_gui.show()
    app.exit(app.exec_())