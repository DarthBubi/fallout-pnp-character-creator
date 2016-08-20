import sys

from PyQt5 import QtWidgets
import pickle
import os

import character
import main_view
import about_dialogue
import new_character_dialogue

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
        self.newCharacterAction.triggered.connect(self.new_character)
        self.saveCharacterAction.triggered.connect(self.save_characters_to_file)
        self.importCharacterAction.triggered.connect(self.import_character)
        self.exportCharacterAction.triggered.connect(self.export_character)
        self.characterListWidget.currentItemChanged.connect(self.show_attributes)
        self.characterListWidget.currentItemChanged.connect(self.show_general)
        self.characterListWidget.currentItemChanged.connect(self.show_skills)

        if os.path.exists(os.path.expanduser("~") + "/.fcdbpath"):
            with open(os.path.expanduser("~") + "/.fcdbpath", "rb") as dbfile:
                self.dbpath = pickle.load(dbfile)
        else:
            path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Database File', os.path.expanduser("~"))
            if path is not "":
                self.dbpath = path + "/database.fcd"
                with open(os.path.expanduser("~") + "/.fcdbpath", "wb") as dbfile:
                    pickle.dump(self.dbpath, dbfile)
            else:
                sys.exit(0)

        if os.path.exists(self.dbpath):
            with open(self.dbpath, 'rb') as db:
                self.character_dict = pickle.load(db)

        self.list_characters()

    def new_character(self):
        new_character = NewCharacterDialogue()
        if new_character.exec_():
            self.add_character_to_dict(new_character.get_character())

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

    def export_character(self):
        character = self.character_dict.get(self.characterListWidget.currentItem().text())
        filename = character.name.replace(" ", "").lower() + ".fcf"
        with open(filename, 'wb') as file:
            pickle.dump(character, file)
        self.statusBar().showMessage("Export erfolgreich", 1000)

    def import_character(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', ".", "*.fcf")
        if name[0] != "":
            with open(name[0], 'rb') as file:
                character = pickle.load(file)
                self.character_dict[character.name] = character
                self.characterListWidget.blockSignals(True)
                self.characterListWidget.clear()
                self.characterListWidget.blockSignals(False)
                self.list_characters()
        self.statusBar().showMessage("Import erfolgreich", 1000)

    def save_characters_to_file(self):
        with open(self.dbpath, 'wb') as file:
            pickle.dump(self.character_dict, file)
        self.statusBar().showMessage("Speichern erfolgreich", 1000)

    # TODO: Read single character from file and add to character database
    def file_open(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', ".", "*.fcd")
        if name[0] != "":
            with open(name[0], 'rb') as file:
                self.character_dict = pickle.load(file)
                self.characterListWidget.blockSignals(True)
                self.characterListWidget.clear()
                self.characterListWidget.blockSignals(False)
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

    def get_character_dict(self):
        return self.character_dict

    def add_character_to_dict(self, char):
        char_item = QtWidgets.QListWidgetItem(char.name)
        self.character_dict.update({char_item.text(): char})
        self.characterListWidget.addItem(char_item)


# TODO: Add traits and items to character generation
class NewCharacterDialogue(QtWidgets.QDialog, new_character_dialogue.Ui_Dialog):

    def __init__(self, parent=None):
        super(NewCharacterDialogue, self).__init__(parent)
        self.setupUi(self)

        self.available_skill_points = 5  # magic number
        self.tagged_skills = ([], 0)

        self.sexPicker.clear()
        self.sexPicker.addItems(["male", "female"])

        race_list = sorted(["Human", "Dog", "Super Mutant", "Half Mutant", "Ghoul", "Deathclaw", "Robot"])
        self.racePicker.clear()
        self.racePicker.addItems(race_list)
        self.racePicker.currentIndexChanged.connect(self.handle_race_change)
        self.handle_race_change()
        self.availablePointsBox.setText(str(self.available_skill_points))

        self.strengthSpinBox.valueChanged.connect(self.handle_attribute_value_change)
        self.perceptionBox.valueChanged.connect(self.handle_attribute_value_change)
        self.enduranceBox.valueChanged.connect(self.handle_attribute_value_change)
        self.charismaBox.valueChanged.connect(self.handle_attribute_value_change)
        self.intelligenceBox.valueChanged.connect(self.handle_attribute_value_change)
        self.agilityBox.valueChanged.connect(self.handle_attribute_value_change)
        self.luckBox.valueChanged.connect(self.handle_attribute_value_change)

        self.smallGunsTag.clicked.connect(self.handle_strength_tag)
        self.bigGunsTag.clicked.connect(self.handle_skill_tags)
        self.energyWeaponsTag.clicked.connect(self.handle_skill_tags)
        self.unarmedTag.clicked.connect(self.handle_skill_tags)
        self.meleeWeaponsTag.clicked.connect(self.handle_skill_tags)
        self.throwingTag.clicked.connect(self.handle_skill_tags)
        self.explosivesTag.clicked.connect(self.handle_skill_tags)
        self.doctorTag.clicked.connect(self.handle_skill_tags)
        self.sneakTag.clicked.connect(self.handle_skill_tags)
        self.lockpickTag.clicked.connect(self.handle_skill_tags)
        self.trapsTag.clicked.connect(self.handle_skill_tags)
        self.scienceTag.clicked.connect(self.handle_skill_tags)
        self.repairTag.clicked.connect(self.handle_skill_tags)
        self.pilotTag.clicked.connect(self.handle_skill_tags)
        self.speechTag.clicked.connect(self.handle_skill_tags)
        self.barterTag.clicked.connect(self.handle_skill_tags)
        self.gamblingTag.clicked.connect(self.handle_skill_tags)
        self.survivalTag.clicked.connect(self.handle_skill_tags)

        self.nextButton = QtWidgets.QPushButton("Next")
        self.nextButton.clicked.connect(self.next_page)
        self.backButton = QtWidgets.QPushButton("Back")
        self.backButton.clicked.connect(self.previous_page)
        self.buttonBox.addButton(self.backButton, QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(self.nextButton, QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.finish_character_creation)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.close)
        self.stackedWidget.setCurrentIndex(0)

    def handle_race_change(self):
        self.selected_race()
        self.set_attribute_limits()
        # self.strengthSpinBox.blockSignals(True)
        # self.perceptionBox.blockSignals(True)
        # self.enduranceBox.blockSignals(True)
        # self.charismaBox.blockSignals(True)
        # self.intelligenceBox.blockSignals(True)
        # self.agilityBox.blockSignals(True)
        # self.luckBox.blockSignals(True)
        self.set_default_attribute_values()
        self.available_skill_points = 5
        self.set_skill_values()

    def handle_attribute_value_change(self):
        if self.available_skill_points > 0:
            if self.character.strength != self.strengthSpinBox.value():
                if self.character.strength > self.strengthSpinBox.value():
                    self.available_skill_points += 1
                else:
                    self.available_skill_points -= 1
                self.character.strength = self.strengthSpinBox.value()

            elif self.character.perception != self.perceptionBox.value():
                if self.character.perception > self.perceptionBox.value():
                    self.available_skill_points += 1
                else:
                    self.available_skill_points -= 1
                self.character.perception = self.perceptionBox.value()

            elif self.character.endurance != self.enduranceBox.value():
                if self.character.endurance > self.enduranceBox.value():
                    self.available_skill_points += 1
                else:
                    self.available_skill_points -= 1
                self.character.endurance = self.enduranceBox.value()

            elif self.character.charisma != self.charismaBox.value():
                if self.character.charisma > self.charismaBox.value():
                    self.available_skill_points += 1
                else:
                    self.available_skill_points -= 1
                self.character.charisma = self.charismaBox.value()

            elif self.character.intelligence != self.intelligenceBox.value():
                if self.character.intelligence > self.intelligenceBox.value():
                    self.available_skill_points += 1
                else:
                    self.available_skill_points -= 1
                self.character.intelligence = self.intelligenceBox.value()

            elif self.character.agility != self.agilityBox.value():
                if self.character.agility > self.agilityBox.value():
                    self.available_skill_points += 1
                else:
                    self.available_skill_points -= 1
                self.character.agility = self.agilityBox.value()

            elif self.character.luck != self.luckBox.value():
                if self.character.luck > self.luckBox.value():
                    self.available_skill_points += 1
                else:
                    self.available_skill_points -= 1
                self.character.luck = self.luckBox.value()

            self.availablePointsBox.setText(str(self.available_skill_points))

        elif self.available_skill_points == 0:
            if self.character.strength != self.strengthSpinBox.value():
                if self.character.strength > self.strengthSpinBox.value():
                    self.available_skill_points += 1
                else:
                    self.strengthSpinBox.setValue(self.character.strength)
                self.character.strength = self.strengthSpinBox.value()

            elif self.character.perception != self.perceptionBox.value():
                if self.character.perception > self.perceptionBox.value():
                    self.available_skill_points += 1
                else:
                    self.perceptionBox.setValue(self.character.perception)
                self.character.perception = self.perceptionBox.value()

            elif self.character.endurance != self.enduranceBox.value():
                if self.character.endurance > self.enduranceBox.value():
                    self.available_skill_points += 1
                else:
                    self.enduranceBox.setValue(self.character.endurance)
                self.character.endurance = self.enduranceBox.value()

            elif self.character.charisma != self.charismaBox.value():
                if self.character.charisma > self.charismaBox.value():
                    self.available_skill_points += 1
                else:
                    self.charismaBox.setValue(self.character.charisma)
                self.character.charisma = self.charismaBox.value()

            elif self.character.intelligence != self.intelligenceBox.value():
                if self.character.intelligence > self.intelligenceBox.value():
                    self.available_skill_points += 1
                else:
                    self.intelligenceBox.setValue(self.character.intelligence)
                self.character.intelligence = self.intelligenceBox.value()

            elif self.character.agility != self.agilityBox.value():
                if self.character.agility > self.agilityBox.value():
                    self.available_skill_points += 1
                else:
                    self.agilityBox.setValue(self.character.agility)
                self.character.agility = self.agilityBox.value()

            elif self.character.luck != self.luckBox.value():
                if self.character.luck > self.luckBox.value():
                    self.available_skill_points += 1
                else:
                    self.luckBox.setValue(self.character.luck)
                self.character.luck = self.luckBox.value()

            self.availablePointsBox.setText(str(self.available_skill_points))

    # test method
    def handle_strength_tag(self):
        if self.smallGunsTag.isChecked() and self.tagged_skills[1] < 3:
            self.character.small_guns += 20
            self.smallGunsBox.setValue(self.character.small_guns)
        elif self.tagged_skills[0].__contains__("small_guns"):
            self.character.small_guns -= 20
            self.smallGunsBox.setValue(self.character.small_guns)

    # TODO: Handle skill tagging
    def handle_skill_tags(self):
        pass

    def next_page(self):
        if self.stackedWidget.currentIndex() < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()+1)
            if self.stackedWidget.currentIndex() == 2:
                self.set_skill_values()

    def previous_page(self):
        if self.stackedWidget.currentIndex() > 0:
            self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()-1)

    def selected_race(self):
        if self.racePicker.currentText() == "Deathclaw":
            self.character = character.DeathclawCharacter()
        elif self.racePicker.currentText() == "Dog":
            self.character = character.DogCharacter()
        elif self.racePicker.currentText() == "Ghoul":
            self.character = character.GhoulCharacter()
        elif self.racePicker.currentText() == "Half Mutant":
            self.character = character.HalfMutantCharacter()
        elif self.racePicker.currentText() == "Human":
            self.character = character.HumanCharacter()
        elif self.racePicker.currentText() == "Robot":
            self.character = character.RobotCharacter()
        elif self.racePicker.currentText() == "Super Mutant":
            self.character = character.SuperMutantCharacter()

    def set_default_attribute_values(self):
        self.strengthSpinBox.blockSignals(True)
        self.strengthSpinBox.setValue(self.character.strength)
        self.strengthSpinBox.blockSignals(False)
        self.perceptionBox.blockSignals(True)
        self.perceptionBox.setValue(self.character.perception)
        self.perceptionBox.blockSignals(False)
        self.enduranceBox.blockSignals(True)
        self.enduranceBox.setValue(self.character.endurance)
        self.enduranceBox.blockSignals(False)
        self.charismaBox.blockSignals(True)
        self.charismaBox.setValue(self.character.charisma)
        self.charismaBox.blockSignals(False)
        self.intelligenceBox.blockSignals(True)
        self.intelligenceBox.setValue(self.character.intelligence)
        self.intelligenceBox.blockSignals(False)
        self.agilityBox.blockSignals(True)
        self.agilityBox.setValue(self.character.agility)
        self.agilityBox.blockSignals(False)
        self.luckBox.blockSignals(True)
        self.luckBox.setValue(self.character.luck)
        self.luckBox.blockSignals(False)

    def set_attribute_limits(self):
        self.strengthSpinBox.setMinimum(self.character.MIN_STRENGTH)
        self.strengthSpinBox.setMaximum(self.character.MAX_STRENGTH)
        self.perceptionBox.setMinimum(self.character.MIN_PERCEPTION)
        self.perceptionBox.setMaximum(self.character.MAX_PERCEPTION)
        self.enduranceBox.setMinimum(self.character.MIN_ENDURANCE)
        self.enduranceBox.setMaximum(self.character.MAX_ENDURANCE)
        self.charismaBox.setMinimum(self.character.MIN_CHARISMA)
        self.charismaBox.setMaximum( self.character.MAX_CHARISMA)
        self.intelligenceBox.setMinimum(self.character.MIN_INTELLIGENCE)
        self.intelligenceBox.setMaximum(self.character.MAX_INTELLIGENCE)
        self.agilityBox.setMinimum(self.character.MIN_AGILITY)
        self.agilityBox.setMaximum(self.character.MAX_AGILITY)
        self.luckBox.setMinimum(self.character.MIN_LUCK)
        self.luckBox.setMaximum(self.character.MAX_LUCK)

    def set_skill_values(self):
        self.character.calculate_base_skills()

        self.smallGunsBox.setValue(self.character.small_guns)
        self.bigGunsBox.setValue(self.character.big_guns)
        self.energyWeaponsBox.setValue(self.character.energy_weapons)
        self.unarmedBox.setValue(self.character.unarmed)
        self.meleeWeaponsBox.setValue(self.character.melee_weapons)
        self.throwingBox.setValue(self.character.throwing)
        self.explosivesBox.setValue(self.character.explosives)
        self.doctorBox.setValue(self.character.doctor)
        self.sneakBox.setValue(self.character.sneak)
        self.lockpickBox.setValue(self.character.lockpick)
        self.trapsBox.setValue(self.character.traps)
        self.scienceBox.setValue(self.character.science)
        self.repairBox.setValue(self.character.repair)
        self.pilotBox.setValue(self.character.pilot)
        self.speechBox.setValue(self.character.speech)
        self.barterBox.setValue(self.character.barter)
        self.gamblingBox.setValue(self.character.gambling)
        self.survivalBox.setValue(self.character.survival)

    # TODO: Check if all fields are filled with valid values
    def finish_character_creation(self):
        self.character.name = self.nameField.text()
        self.character.age = self.ageField.text()
        self.character.sex = self.sexPicker.currentText()
        self.character.calculate_base_skills()
        self.accept()

    def get_character(self):
        return self.character


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
