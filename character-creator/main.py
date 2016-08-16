import sys

from PyQt5 import QtWidgets
import pickle

import character
import main_view
import about_dialogue

__author__ = "Johannes Hackbarth"


class CharacterCreator(QtWidgets.QMainWindow, main_view.Ui_MainWindow):

    # TODO: Read existing characters from file
    def __init__(self, parent=None):
        self.foo = character.DogCharacter()
        self.foo.name = "Foo"
        self.foo.appearance = "The path of the righteous man is beset on all sides by the iniquities of the selfish" \
                              " and the tyranny of evil men. Blessed is he who, in the name of charity and good will," \
                              " shepherds the weak through the valley of darkness, for he is truly his brother's" \
                              " keeper and the finder of lost children. And I will strike down upon thee with great" \
                              " vengeance and furious anger those who would attempt to poison and destroy My brothers." \
                              " And you will know My name is the Lord when I lay My vengeance upon thee."
        self.foo.calculate_base_skills()
        self.character_dict = {self.foo.name: self.foo}
        super(CharacterCreator, self).__init__(parent)
        self.setupUi(self)
        self.quitAction.triggered.connect(self.close)
        self.aboutAction.triggered.connect(self.about)
        self.openCharacterAction.triggered.connect(self.file_open)
        self.newCharacterAction.triggered.connect(self.new_character_dummy)
        self.saveCharacterAction.triggered.connect(self.save_characters_to_file)
        self.characterListWidget.currentItemChanged.connect(self.show_attributes)
        self.characterListWidget.currentItemChanged.connect(self.show_general)
        self.characterListWidget.currentItemChanged.connect(self.show_skills)
        self.list_characters()

    # TODO: Implement character generation dialogue
    def new_character(self):
        pass

    def list_characters(self):
        for name in self.character_dict:
            item = QtWidgets.QListWidgetItem(name)
            self.characterListWidget.addItem(item)

    def show_attributes(self):
        self.strengthSpinBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).strength)
        self.strengthSpinBox.setMinimum(self.character_dict.get(self.characterListWidget.currentItem().text()).MIN_STRENGTH)
        self.strengthSpinBox.setMaximum(self.character_dict.get(self.characterListWidget.currentItem().text()).MAX_STRENGTH)
        self.perceptionBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).perception)
        self.perceptionBox.setMinimum(self.character_dict.get(self.characterListWidget.currentItem().text()).MIN_PERCEPTION)
        self.perceptionBox.setMaximum(self.character_dict.get(self.characterListWidget.currentItem().text()).MAX_PERCEPTION)
        self.enduranceBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).endurance)
        self.enduranceBox.setMinimum(self.character_dict.get(self.characterListWidget.currentItem().text()).MIN_ENDURANCE)
        self.enduranceBox.setMaximum(self.character_dict.get(self.characterListWidget.currentItem().text()).MAX_ENDURANCE)
        self.charismaBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).charisma)
        self.charismaBox.setMinimum(self.character_dict.get(self.characterListWidget.currentItem().text()).MIN_CHARISMA)
        self.charismaBox.setMaximum(self.character_dict.get(self.characterListWidget.currentItem().text()).MAX_CHARISMA)
        self.intelligenceBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).intelligence)
        self.intelligenceBox.setMinimum(self.character_dict.get(self.characterListWidget.currentItem().text()).MIN_INTELLIGENCE)
        self.intelligenceBox.setMaximum(self.character_dict.get(self.characterListWidget.currentItem().text()).MAX_INTELLIGENCE)
        self.agilityBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).agility)
        self.agilityBox.setMinimum(self.character_dict.get(self.characterListWidget.currentItem().text()).MIN_AGILITY)
        self.agilityBox.setMaximum(self.character_dict.get(self.characterListWidget.currentItem().text()).MAX_AGILITY)
        self.luckBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).luck)
        self.luckBox.setMinimum(self.character_dict.get(self.characterListWidget.currentItem().text()).MIN_LUCK)
        self.luckBox.setMaximum(self.character_dict.get(self.characterListWidget.currentItem().text()).MAX_LUCK)

    def show_general(self):
        self.nameField.setText(self.character_dict.get(self.characterListWidget.currentItem().text()).name)
        self.ageField.setText(self.character_dict.get(self.characterListWidget.currentItem().text()).age.__str__())
        self.sexField.setText(self.character_dict.get(self.characterListWidget.currentItem().text()).sex)
        self.raceField.setText(self.character_dict.get(self.characterListWidget.currentItem().text()).__str__())
        self.eyesField.setText(self.character_dict.get(self.characterListWidget.currentItem().text()).eyes)
        self.hairField.setText(self.character_dict.get(self.characterListWidget.currentItem().text()).hair)
        self.heightField.setText(self.character_dict.get(self.characterListWidget.currentItem().text()).height.__str__())
        self.weightField.setText(self.character_dict.get(self.characterListWidget.currentItem().text()).weight.__str__())
        self.appearanceField.setText(self.character_dict.get(self.characterListWidget.currentItem().text()).appearance)

    def show_skills(self):
        self.smallGunsBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).small_guns)
        self.bigGunsBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).big_guns)
        self.energyWeaponsBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).energy_weapons)
        self.unarmedBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).unarmed)
        self.meleeWeaponsBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).melee_weapons)
        self.throwingBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).throwing)
        self.explosivesBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).explosives)
        self.doctorBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).doctor)
        self.sneakBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).sneak)
        self.lockpickBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).lockpick)
        self.trapsBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).traps)
        self.scienceBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).science)
        self.repairBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).repair)
        self.pilotBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).pilot)
        self.speechBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).speech)
        self.barterBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).barter)
        self.gamblingBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).gambling)
        self.survivalBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).survival)

    # TODO: Remove dummy function
    def new_character_dummy(self):
        dummy_char = character.HumanCharacter()
        dummy_char.name = "Dummy Char"
        dummy_char.calculate_base_skills()
        dummy_item = QtWidgets.QListWidgetItem(dummy_char.name)
        self.character_dict.update({dummy_item.text(): dummy_char})
        self.characterListWidget.addItem(dummy_item)

    def save_characters_to_file(self):
        with open('characters.pickle', 'wb') as file:
            pickle.dump(self.character_dict, file)

    # TODO: Read single character from file and add to character database
    def file_open(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', ".", "*.pickle")
        with open(name[0], 'rb') as file:
            self.characterListWidget.blockSignals(True)
            self.characterListWidget.clear()
            self.characterListWidget.blockSignals(False)
            self.character_dict = pickle.load(file)
            self.list_characters()

    def closeEvent(self, event):
        choice = QtWidgets.QMessageBox.question(self, 'Quit Application', "Do you want to quit the application?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    @staticmethod
    def about():
        dialogue = AboutDialogue()
        dialogue.exec_()


class AboutDialogue(QtWidgets.QDialog, about_dialogue.Ui_Dialog):

    def __init__(self, parent=None):
        super(AboutDialogue, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.close)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = CharacterCreator()
    form.show()
    sys.exit(app.exec_())

main()
