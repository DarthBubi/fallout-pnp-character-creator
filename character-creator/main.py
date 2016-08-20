import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore
import pickle
import os

import character
import main_view
import about_dialogue
import new_character_dialogue
import import_dialogue

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
        self.importFromDatabaseAction.triggered.connect(self.import_from_db)
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

    def import_from_db(self):
        import_path =  QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', ".", "*.fcd")

        if import_path[0] is not "":
            with open(import_path[0], "rb") as import_file:
                import_db = pickle.load(import_file)

            import_dialog = ImportFromDatabase(import_db, self)

            if import_dialog.exec_():
                for name in import_dialog.get_characters():
                    self.add_character_to_dict(import_db.get(name))

    def list_characters(self):
        for name in self.character_dict:
            item = QtWidgets.QListWidgetItem(name)
            self.characterListWidget.addItem(item)

    def show_attributes(self):
        self.strengthSpinBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).strength)
        self.perceptionBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).perception)
        self.enduranceBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).endurance)
        self.charismaBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).charisma)
        self.intelligenceBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).intelligence)
        self.agilityBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).agility)
        self.luckBox.setValue(self.character_dict.get(self.characterListWidget.currentItem().text()).luck)

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

class ImportFromDatabase(QtWidgets.QDialog, import_dialogue.Ui_Dialog):

    def __init__(self, import_db, parent=None):
        super(ImportFromDatabase, self).__init__(parent)
        self.setupUi(self)

        for character in import_db:
            item = QtWidgets.QListWidgetItem(character)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.characterListWidget.addItem(item)

        self.characters = []
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.finish_import)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.close)

    def finish_import(self):
        for index in range(self.characterListWidget.count()):
            item = self.characterListWidget.item(index)
            if item.checkState() == QtCore.Qt.Checked:
                self.characters.append(item.text())
        self.accept()

    def get_characters(self):
        return self.characters


# TODO: Add traits and items to character generation
class NewCharacterDialogue(QtWidgets.QDialog, new_character_dialogue.Ui_Dialog):
    def __init__(self, parent=None):
        super(NewCharacterDialogue, self).__init__(parent)
        self.setupUi(self)

        self.available_skill_points = 5  # magic number
        self.tagged_skills = []

        self.sexPicker.clear()
        self.sexPicker.addItems(["male", "female"])

        race_list = sorted(["Human", "Dog", "Super Mutant", "Half Mutant", "Ghoul", "Deathclaw", "Robot"])
        self.racePicker.clear()
        self.racePicker.addItems(race_list)
        self.racePicker.currentIndexChanged.connect(self.handle_race_change)
        self.handle_race_change()
        self.availablePointsBox.setText(str(self.available_skill_points))

        self.strengthSpinBox.valueChanged.connect(lambda: self.handle_attribute_value_change(self.strengthLabel.text()))
        self.perceptionBox.valueChanged.connect(lambda: self.handle_attribute_value_change(self.perceptionLabel.text()))
        self.enduranceBox.valueChanged.connect(lambda: self.handle_attribute_value_change(self.enduranceLabel.text()))
        self.charismaBox.valueChanged.connect(lambda: self.handle_attribute_value_change(self.charismaLabel.text()))
        self.intelligenceBox.valueChanged.connect(lambda: self.handle_attribute_value_change(self.intelligenceLabel.text()))
        self.agilityBox.valueChanged.connect(lambda: self.handle_attribute_value_change(self.agilityLabel.text()))
        self.luckBox.valueChanged.connect(lambda: self.handle_attribute_value_change(self.luckLabel.text()))

        self.smallGunsTag.clicked.connect(lambda: self.handle_skill_tag_change(self.smallGunsLabel.text()))
        self.bigGunsTag.clicked.connect(lambda: self.handle_skill_tag_change(self.bigGunsLabel.text()))
        self.energyWeaponsTag.clicked.connect(lambda: self.handle_skill_tag_change(self.energyWeaponsLabel.text()))
        self.unarmedTag.clicked.connect(lambda: self.handle_skill_tag_change(self.unarmedLabel.text()))
        self.meleeWeaponsTag.clicked.connect(lambda: self.handle_skill_tag_change(self.meleeWeaponsLabel.text()))
        self.throwingTag.clicked.connect(lambda: self.handle_skill_tag_change(self.throwingLabel.text()))
        self.explosivesTag.clicked.connect(lambda: self.handle_skill_tag_change(self.explosivesLabel.text()))
        self.doctorTag.clicked.connect(lambda: self.handle_skill_tag_change(self.doctorLabel.text()))
        self.sneakTag.clicked.connect(lambda: self.handle_skill_tag_change(self.sneakLabel.text()))
        self.lockpickTag.clicked.connect(lambda: self.handle_skill_tag_change(self.lockpickLabel.text()))
        self.trapsTag.clicked.connect(lambda: self.handle_skill_tag_change(self.trapsLabel.text()))
        self.scienceTag.clicked.connect(lambda: self.handle_skill_tag_change(self.scienceLabel.text()))
        self.repairTag.clicked.connect(lambda: self.handle_skill_tag_change(self.repairLabel.text()))
        self.pilotTag.clicked.connect(lambda: self.handle_skill_tag_change(self.pilotLabel.text()))
        self.speechTag.clicked.connect(lambda: self.handle_skill_tag_change(self.speechLabel.text()))
        self.barterTag.clicked.connect(lambda: self.handle_skill_tag_change(self.barterLabel.text()))
        self.gamblingTag.clicked.connect(lambda: self.handle_skill_tag_change(self.gamblingLabel.text()))
        self.survivalTag.clicked.connect(lambda: self.handle_skill_tag_change(self.survivalLabel.text()))

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
        self.strengthSpinBox.blockSignals(True)
        self.perceptionBox.blockSignals(True)
        self.enduranceBox.blockSignals(True)
        self.charismaBox.blockSignals(True)
        self.intelligenceBox.blockSignals(True)
        self.agilityBox.blockSignals(True)
        self.luckBox.blockSignals(True)
        self.set_default_attribute_values()
        self.available_skill_points = 5
        self.availablePointsBox.setText(self.available_skill_points.__str__())
        self.set_skill_values()

    def handle_attribute_value_change(self, attribute):
        if attribute == self.strengthLabel.text() and self.available_skill_points >= 0:
            if self.character.strength > self.strengthSpinBox.value():
                self.available_skill_points += 1
            elif self.character.strength < self.strengthSpinBox.value() and self.available_skill_points > 0:
                self.available_skill_points -= 1
            else:
                self.strengthSpinBox.setValue(self.character.strength)
            self.character.strength = self.strengthSpinBox.value()

        elif attribute == self.perceptionLabel.text() and self.available_skill_points >= 0:
            if self.character.perception > self.perceptionBox.value():
                self.available_skill_points += 1
            elif self.character.perception < self.perceptionBox.value() and self.available_skill_points > 0:
                self.available_skill_points -= 1
            else:
                self.perceptionBox.setValue(self.character.perception)
            self.character.perception = self.perceptionBox.value()

        elif attribute == self.enduranceLabel.text() and self.available_skill_points >= 0:
            if self.character.endurance > self.enduranceBox.value():
                self.available_skill_points += 1
            elif self.character.endurance < self.enduranceBox.value() and self.available_skill_points > 0:
                self.available_skill_points -= 1
            else:
                self.enduranceBox.setValue(self.character.endurance)
            self.character.endurance = self.enduranceBox.value()

        elif attribute == self.charismaLabel.text() and self.available_skill_points >= 0:
            if self.character.charisma > self.charismaBox.value():
                self.available_skill_points += 1
            elif self.character.charisma < self.charismaBox.value() and self.available_skill_points > 0:
                self.available_skill_points -= 1
            else:
                self.charismaBox.setValue(self.character.charisma)
            self.character.charisma = self.charismaBox.value()

        elif attribute == self.intelligenceLabel.text() and self.available_skill_points >= 0:
            if self.character.intelligence > self.intelligenceBox.value():
                self.available_skill_points += 1
            elif self.character.intelligence < self.intelligenceBox.value() and self.available_skill_points > 0:
                self.available_skill_points -= 1
            else:
                self.intelligenceBox.setValue(self.character.intelligence)
            self.character.intelligence = self.intelligenceBox.value()

        elif attribute == self.agilityLabel.text() and self.available_skill_points >= 0:
            if self.character.agility > self.agilityBox.value():
                self.available_skill_points += 1
            elif self.character.agility < self.agilityBox.value() and self.available_skill_points > 0:
                self.available_skill_points -= 1
            else:
                self.agilityBox.setValue(self.character.agility)
            self.character.agility = self.agilityBox.value()

        elif attribute == self.luckLabel.text() and self.available_skill_points >= 0:
            if self.character.luck > self.luckBox.value():
                self.available_skill_points += 1
            elif self.character.luck < self.luckBox.value() and self.available_skill_points > 0:
                self.available_skill_points -= 1
            else:
                self.luckBox.setValue(self.character.luck)
            self.character.luck = self.luckBox.value()

        self.availablePointsBox.setText(str(self.available_skill_points))

    # TODO: Make all not checked tags uncheckable if limit is reached
    def handle_skill_tag_change(self, skill):
        if skill == self.smallGunsLabel.text() and self.smallGunsTag.isChecked() and self.tagged_skills.__len__() < 3:
            self.character.small_guns += 20
            self.smallGunsBox.setValue(self.character.small_guns)
            self.tagged_skills.append(skill)
        elif skill == self.smallGunsLabel.text() and self.tagged_skills.__contains__(skill):
            self.character.small_guns -= 20
            self.smallGunsBox.setValue(self.character.small_guns)
            self.tagged_skills.remove(skill)

        elif skill == self.bigGunsLabel.text() and self.bigGunsTag.isChecked() and self.tagged_skills.__len__() < 3:
            self.character.big_guns += 20
            self.bigGunsBox.setValue(self.character.big_guns)
            self.tagged_skills.append(skill)
        elif skill == self.bigGunsLabel.text() and self.tagged_skills.__contains__(skill):
            self.character.big_guns -= 20
            self.bigGunsBox.setValue(self.character.big_guns)
            self.tagged_skills.remove(skill)

        elif skill == self.energyWeaponsLabel.text() and self.energyWeaponsTag.isChecked() and self.tagged_skills.__len__() < 3:
            self.character.energy_weapons += 20
            self.energyWeaponsBox.setValue(self.character.energy_weapons)
            self.tagged_skills.append(skill)
        elif skill == self.energyWeaponsLabel.text() and self.tagged_skills.__contains__(skill):
            self.character.energy_weapons -= 20
            self.energyWeaponsBox.setValue(self.character.energy_weapons)
            self.tagged_skills.remove(skill)

        elif skill == self.unarmedLabel.text() and self.unarmedTag.isChecked() and self.tagged_skills.__len__() < 3:
            self.character.unarmed += 20
            self.unarmedBox.setValue(self.character.unarmed)
            self.tagged_skills.append(skill)
        elif skill == self.unarmedLabel.text() and self.tagged_skills.__contains__(skill):
            self.character.unarmed -= 20
            self.unarmedBox.setValue(self.character.unarmed)
            self.tagged_skills.remove(skill)

        elif skill == self.meleeWeaponsLabel.text() and self.meleeWeaponsTag.isChecked() and self.tagged_skills.__len__() < 3:
            self.character.melee_weapons += 20
            self.meleeWeaponsBox.setValue(self.character.melee_weapons)
            self.tagged_skills.append(skill)
        elif skill == self.meleeWeaponsLabel.text() and self.tagged_skills.__contains__(skill):
            self.character.melee_weapons -= 20
            self.meleeWeaponsBox.setValue(self.character.melee_weapons)
            self.tagged_skills.remove(skill)

        elif skill == self.throwingLabel.text() and self.throwingTag.isChecked() and self.tagged_skills.__len__() < 3:
            self.character.throwing += 20
            self.throwingBox.setValue(self.character.throwing)
            self.tagged_skills.append(skill)
        elif skill == self.throwingLabel.text() and self.tagged_skills.__contains__(skill):
            self.character.throwing -= 20
            self.throwingBox.setValue(self.character.throwing)
            self.tagged_skills.remove(skill)

        elif skill == self.explosivesLabel.text() and self.explosivesTag.isChecked() and self.tagged_skills.__len__() < 3:
            self.character.explosives += 20
            self.explosivesBox.setValue(self.character.explosives)
            self.tagged_skills.append(skill)
        elif skill == self.explosivesLabel.text() and self.tagged_skills.__contains__(skill):
            self.character.explosives -= 20
            self.explosivesBox.setValue(self.character.explosives)
            self.tagged_skills.remove(skill)

        elif skill == self.doctorLabel.text() and self.doctorTag.isChecked() and self.tagged_skills.__len__() < 3:
            self.character.doctor += 20
            self.doctorBox.setValue(self.character.doctor)
            self.tagged_skills.append(skill)
        elif skill == self.doctorLabel.text() and self.tagged_skills.__contains__(skill):
            self.character.doctor -= 20
            self.doctorBox.setValue(self.character.doctor)
            self.tagged_skills.remove(skill)

        elif skill == self.sneakLabel.text() and self.sneakTag.isChecked() and self.tagged_skills.__len__() < 3:
            self.character.sneak += 20
            self.sneakBox.setValue(self.character.sneak)
            self.tagged_skills.append(skill)
        elif skill == self.sneakLabel.text() and self.tagged_skills.__contains__(skill):
            self.character.sneak -= 20
            self.sneakBox.setValue(self.character.sneak)
            self.tagged_skills.remove(skill)

        elif skill == self.lockpickLabel.text() and self.lockpickTag.isChecked() and self.tagged_skills.__len__() < 3:
            self.character.lockpick += 20
            self.lockpickBox.setValue(self.character.lockpick)
            self.tagged_skills.append(skill)
        elif skill == self.lockpickLabel.text() and self.tagged_skills.__contains__(skill):
            self.character.lockpick -= 20
            self.lockpickBox.setValue(self.character.lockpick)
            self.tagged_skills.remove(skill)

        elif skill == self.trapsLabel.text() and self.trapsTag.isChecked() and self.tagged_skills.__len__() < 3:
            self.character.traps += 20
            self.trapsBox.setValue(self.character.traps)
            self.tagged_skills.append(skill)
        elif skill == self.trapsLabel.text() and self.tagged_skills.__contains__(skill):
            self.character.traps -= 20
            self.trapsBox.setValue(self.character.traps)
            self.tagged_skills.remove(skill)

        elif skill == self.scienceLabel.text() and self.scienceTag.isChecked() and self.tagged_skills.__len__() < 3:
            self.character.science += 20
            self.scienceBox.setValue(self.character.science)
            self.tagged_skills.append(skill)
        elif skill == self.scienceLabel.text() and self.tagged_skills.__contains__(skill):
            self.character.science -= 20
            self.scienceBox.setValue(self.character.science)
            self.tagged_skills.remove(skill)

        elif skill == self.repairLabel.text() and self.repairTag.isChecked() and self.tagged_skills.__len__() < 3:
            self.character.repair += 20
            self.repairBox.setValue(self.character.repair)
            self.tagged_skills.append(skill)
        elif skill == self.repairLabel.text() and self.tagged_skills.__contains__(skill):
            self.character.repair -= 20
            self.repairBox.setValue(self.character.repair)
            self.tagged_skills.remove(skill)

        elif skill == self.pilotLabel.text() and self.pilotTag.isChecked() and self.tagged_skills.__len__() < 3:
            self.character.pilot += 20
            self.pilotBox.setValue(self.character.pilot)
            self.tagged_skills.append(skill)
        elif skill == self.pilotLabel.text() and self.tagged_skills.__contains__(skill):
            self.character.pilot -= 20
            self.pilotBox.setValue(self.character.pilot)
            self.tagged_skills.remove(skill)

        elif skill == self.speechLabel.text() and self.speechTag.isChecked() and self.tagged_skills.__len__() < 3:
            self.character.speech += 20
            self.speechBox.setValue(self.character.speech)
            self.tagged_skills.append(skill)
        elif skill == self.speechLabel.text() and self.tagged_skills.__contains__(skill):
            self.character.speech -= 20
            self.speechBox.setValue(self.character.speech)
            self.tagged_skills.remove(skill)

        elif skill == self.barterLabel.text() and self.barterTag.isChecked() and self.tagged_skills.__len__() < 3:
            self.character.barter += 20
            self.barterBox.setValue(self.character.barter)
            self.tagged_skills.append(skill)
        elif skill == self.barterLabel.text() and self.tagged_skills.__contains__(skill):
            self.character.barter -= 20
            self.barterBox.setValue(self.character.barter)
            self.tagged_skills.remove(skill)

        elif skill == self.gamblingLabel.text() and self.gamblingTag.isChecked() and self.tagged_skills.__len__() < 3:
            self.character.gambling += 20
            self.gamblingBox.setValue(self.character.gambling)
            self.tagged_skills.append(skill)
        elif skill == self.gamblingLabel.text() and self.tagged_skills.__contains__(skill):
            self.character.gambling -= 20
            self.gamblingBox.setValue(self.character.gambling)
            self.tagged_skills.remove(skill)

        elif skill == self.survivalLabel.text() and self.survivalTag.isChecked() and self.tagged_skills.__len__() < 3:
            self.character.survival += 20
            self.survivalBox.setValue(self.character.survival)
            self.tagged_skills.append(skill)
        elif skill == self.survivalLabel.text() and self.tagged_skills.__contains__(skill):
            self.character.survival -= 20
            self.survivalBox.setValue(self.character.survival)
            self.tagged_skills.remove(skill)

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
