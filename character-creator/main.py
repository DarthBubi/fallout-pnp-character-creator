import os
import pickle
import sys

from PyQt5 import QtWidgets, QtCore

import about_dialogue
import character
import config
import import_dialogue
import main_view
import new_character_dialogue

__author__ = "Johannes Hackbarth"


class CharacterCreator(QtWidgets.QMainWindow, main_view.Ui_MainWindow):
    def __init__(self, parent=None):
        self.character_dict = {}
        self.changes = False
        super(CharacterCreator, self).__init__(parent)
        self.setupUi(self)
        self.quitAction.triggered.connect(self.close)
        self.aboutAction.triggered.connect(self.about)
        self.openCharacterAction.triggered.connect(self.file_open)
        self.newCharacterAction.triggered.connect(self.new_character)
        self.saveCharacterAction.triggered.connect(self.file_save)
        self.importCharacterAction.triggered.connect(self.import_character)
        self.exportCharacterAction.triggered.connect(self.export_character)
        self.databaseImportAction.triggered.connect(self.import_from_db)
        self.deleteCharacterAction.triggered.connect(self.delete_character)
        self.characterListWidget.currentItemChanged.connect(self.show_fields)
        self.characterListWidget.currentItemChanged.connect(self.list_traits)
        self.traitListWidget.currentItemChanged.connect(self.show_trait_description)

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
        self.show_fields()
        self.list_traits()
        self.show_trait_description()
        self.tabWidget.setCurrentIndex(0)

    def list_characters(self):
        for name in self.character_dict:
            item = QtWidgets.QListWidgetItem(name)
            self.characterListWidget.addItem(item)

    def get_character_dict(self):
        return self.character_dict

    def add_character_to_dict(self, char):
        char_item = QtWidgets.QListWidgetItem(char.name)
        self.character_dict.update({char_item.text(): char})
        self.characterListWidget.addItem(char_item)

    def list_traits(self):
        if self.characterListWidget.currentItem() is not None:
            char = self.character_dict.get(self.characterListWidget.currentItem().text())
            if char.traits:
                for trait in char.traits:
                    self.traitListWidget.addItem(trait.name)
            else:
                self.traitListWidget.clear()

    def show_trait_description(self):
        if self.characterListWidget.currentItem() is not None:
            char = self.character_dict.get(self.characterListWidget.currentItem().text())
            if char.traits:
                for trait in char.traits:
                    if trait.name == self.traitListWidget.currentItem().text():
                        self.traitDescriptionBox.setText(trait.description)
            else:
                self.traitDescriptionBox.clear()

    def show_fields(self):
        if self.characterListWidget.currentItem() is not None:
            char = self.character_dict.get(self.characterListWidget.currentItem().text())
        else:
            char = character.HumanCharacter()

        self.strengthSpinBox.setValue(char.strength[0])
        self.perceptionBox.setValue(char.perception[0])
        self.enduranceBox.setValue(char.endurance[0])
        self.charismaBox.setValue(char.charisma[0])
        self.intelligenceBox.setValue(char.intelligence[0])
        self.agilityBox.setValue(char.agility[0])
        self.luckBox.setValue(char.luck[0])

        self.nameField.setText(char.name)
        self.ageField.setText(char.age.__str__())
        self.sexField.setText(char.sex)
        self.raceField.setText(char.__str__())
        self.eyesField.setText(char.eyes)
        self.hairField.setText(char.hair)
        self.heightField.setText(char.height.__str__())
        self.weightField.setText(char.weight.__str__())
        self.appearanceField.setText(char.appearance)

        self.smallGunsBox.setValue(char.small_guns)
        self.bigGunsBox.setValue(char.big_guns)
        self.energyWeaponsBox.setValue(char.energy_weapons)
        self.unarmedBox.setValue(char.unarmed)
        self.meleeWeaponsBox.setValue(char.melee_weapons)
        self.throwingBox.setValue(char.throwing)
        self.explosivesBox.setValue(char.explosives)
        self.doctorBox.setValue(char.doctor)
        self.sneakBox.setValue(char.sneak)
        self.lockpickBox.setValue(char.lockpick)
        self.trapsBox.setValue(char.traps)
        self.scienceBox.setValue(char.science)
        self.repairBox.setValue(char.repair)
        self.pilotBox.setValue(char.pilot)
        self.speechBox.setValue(char.speech)
        self.barterBox.setValue(char.barter)
        self.gamblingBox.setValue(char.gambling)
        self.survivalBox.setValue(char.survival)

    def new_character(self):
        self.changes = True
        new_character = NewCharacterDialogue()
        if new_character.exec_():
            self.add_character_to_dict(new_character.get_character())

    def delete_character(self):
        self.changes = True
        choice = QtWidgets.QMessageBox.question(self, 'Delete Character',
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                "Do you want to delete the current character?")
        if choice == QtWidgets.QMessageBox.Yes:
            del self.character_dict[self.characterListWidget.currentItem().text()]
            self.characterListWidget.takeItem(self.characterListWidget.row(self.characterListWidget.currentItem()))
        else:
            pass

    def import_character(self):
        self.changes = True
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', ".", "*.fcf")
        if name[0] != "":
            with open(name[0], 'rb') as file:
                character = pickle.load(file)
                self.character_dict[character.name] = character
                self.characterListWidget.blockSignals(True)
                self.characterListWidget.clear()
                self.characterListWidget.blockSignals(False)
                self.list_characters()
        self.statusBar().showMessage("Import successful", 1000)

    def import_from_db(self):
        self.changes = True
        import_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', ".", "*.fcd")

        if import_path[0] is not "":
            with open(import_path[0], "rb") as import_file:
                import_db = pickle.load(import_file)

            import_dialog = ImportFromDatabase(import_db, self)

            if import_dialog.exec_():
                for name in import_dialog.get_characters():
                    self.add_character_to_dict(import_db.get(name))

    def export_character(self):
        if self.characterListWidget.currentItem() is not None:
            character = self.character_dict.get(self.characterListWidget.currentItem().text())
            filename = character.name.replace(" ", "").lower() + ".fcf"
            with open(filename, 'wb') as file:
                pickle.dump(character, file)
            self.statusBar().showMessage("Export successful", 1000)

    def file_save(self):
        with open(self.dbpath, "wb") as file:
            pickle.dump(self.character_dict, file)

        with open(os.path.expanduser("~") + "/.fcdbpath", "wb") as dbfile:
            pickle.dump(self.dbpath, dbfile)

        self.changes = False
        self.statusBar().showMessage("Save successful", 1000)

    def file_open(self):
        self.changes = True

        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', ".", "*.fcd")

        if path[0] is not "":
            self.dbpath = path[0]
            with open(path[0], "rb") as file:
                self.character_dict = pickle.load(file)
                self.characterListWidget.blockSignals(True)
                self.characterListWidget.clear()
                self.characterListWidget.blockSignals(False)
                self.list_characters()

    def closeEvent(self, event):
        if self.changes is False:
            choice = QtWidgets.QMessageBox.question(self, 'Quit Application', "Do you want to quit the application?",
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            choice = QtWidgets.QMessageBox.question(self, 'Quit without saving?', "Do you want to quit without saving?",
                                                    QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard
                                                    | QtWidgets.QMessageBox.Cancel)
            if choice == QtWidgets.QMessageBox.Save:
                self.file_save()
                event.accept()
            elif choice == QtWidgets.QMessageBox.Discard:
                event.accept()
            elif choice == QtWidgets.QMessageBox.Cancel:
                event.ignore()

    @staticmethod
    def about():
        dialogue = AboutDialogue()
        dialogue.exec_()


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


# TODO: Add items to character generation
class NewCharacterDialogue(QtWidgets.QDialog, new_character_dialogue.Ui_Dialog):
    def __init__(self, parent=None):
        super(NewCharacterDialogue, self).__init__(parent)
        self.setupUi(self)

        self.available_skill_points = 5  # magic number

        self.sexPicker.clear()
        self.sexPicker.addItems(["male", "female"])

        race_list = sorted(["Human", "Dog", "Super Mutant", "Half Mutant", "Ghoul", "Deathclaw", "Robot"])
        self.racePicker.clear()
        self.racePicker.addItems(race_list)
        self.racePicker.currentIndexChanged.connect(self.handle_race_change)
        self.handle_race_change()
        self.availablePointsBox.setText(str(self.available_skill_points))

        self.strengthBox.valueChanged.connect(lambda: self.handle_attribute_value_change(self.strengthLabel.text()))
        self.perceptionBox.valueChanged.connect(lambda: self.handle_attribute_value_change(self.perceptionLabel.text()))
        self.enduranceBox.valueChanged.connect(lambda: self.handle_attribute_value_change(self.enduranceLabel.text()))
        self.charismaBox.valueChanged.connect(lambda: self.handle_attribute_value_change(self.charismaLabel.text()))
        self.intelligenceBox.valueChanged.connect(
            lambda: self.handle_attribute_value_change(self.intelligenceLabel.text()))
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

        self.traitListWidget.currentItemChanged.connect(self.show_trait_description)
        self.traitListWidget.itemChanged.connect(self.handle_trait_check)
        self.traitListWidget.itemChanged.connect(lambda: self.handle_attribute_value_change(self.strengthLabel.text()))
        self.traitListWidget.itemChanged.connect(lambda: self.handle_attribute_value_change(self.perceptionLabel.text()))
        self.traitListWidget.itemChanged.connect(lambda: self.handle_attribute_value_change(self.enduranceLabel.text()))
        self.traitListWidget.itemChanged.connect(lambda: self.handle_attribute_value_change(self.charismaLabel.text()))
        self.traitListWidget.itemChanged.connect(lambda: self.handle_attribute_value_change(self.intelligenceLabel.text()))
        self.traitListWidget.itemChanged.connect(lambda: self.handle_attribute_value_change(self.agilityLabel.text()))
        self.traitListWidget.itemChanged.connect(lambda: self.handle_attribute_value_change(self.luckLabel.text()))

        self.nextButton = QtWidgets.QPushButton("Next")
        self.nextButton.clicked.connect(self.next_page)
        self.backButton = QtWidgets.QPushButton("Back")
        self.backButton.clicked.connect(self.previous_page)
        self.buttonBox.addButton(self.backButton, QtWidgets.QDialogButtonBox.ActionRole)
        self.backButton.setDisabled(True)
        self.buttonBox.addButton(self.nextButton, QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.finish_character_creation)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.close)
        self.stackedWidget.setCurrentIndex(0)

    def handle_race_change(self):
        self.selected_race()
        self.set_attribute_limits()
        self.set_default_attribute_values()
        self.available_skill_points = 5
        self.availablePointsBox.setText(str(self.available_skill_points))
        self.set_skill_values()
        self.list_traits()

    # TODO: Check total value against maximum/minimum value
    def handle_attribute_value_change(self, attribute):
        attr = attribute.lower()
        box = attr + "Box"
        mod_box = attr + "ModBox"
        total_box = attr + "TotalBox"

        for label in self.findChildren(QtWidgets.QLabel):
            if isinstance(label.buddy(), QtWidgets.QSpinBox):
                if attribute == label.text() and self.available_skill_points >= 0:
                    attr_vals = getattr(self.character, attr)
                    if getattr(self.character, attr)[0] > getattr(self, box).value():
                        self.available_skill_points += 1
                    elif getattr(self.character, attr)[0] < getattr(self, box).value() and \
                                    self.available_skill_points > 0:
                        self.available_skill_points -= 1
                    else:
                        getattr(self, box).setValue(getattr(self.character, attr)[0])

                    setattr(self.character, attr, (getattr(self, box).value(), attr_vals[1]))
                    getattr(self, mod_box).setValue(sum(getattr(self.character, attr)[1].values()))
                    getattr(self, total_box).setValue(self.character.total_value(getattr(self.character, attr)))

                self.availablePointsBox.setText(str(self.available_skill_points))

    def handle_skill_tag_change(self, skill):
        attr = skill.replace(" ", "_").lower()
        components = attr.split('_')
        box = components[0] + "".join(x.title() for x in components[1:]) + "Box"

        for label in self.findChildren(QtWidgets.QLabel):
            if isinstance(label.buddy(), QtWidgets.QCheckBox) and skill == label.text():

                if label.buddy().isChecked() and len(self.character.tagged_skills) < self.character.taggable_skills():
                    setattr(self.character, attr, getattr(self.character, attr) + 20)
                    getattr(self, box).setValue(getattr(self.character, attr))
                    self.character.tagged_skills.append(skill)
                    break

                elif skill in self.character.tagged_skills:
                    setattr(self.character, attr, getattr(self.character, attr) - 20)
                    getattr(self, box).setValue(getattr(self.character, attr))
                    self.character.tagged_skills.remove(skill)
                    break

                else:
                    label.buddy().setCheckState(QtCore.Qt.Unchecked)
                    break

    def next_page(self):
        if self.stackedWidget.currentIndex() < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)
            if self.stackedWidget.currentIndex() == 2:
                self.set_skill_values()
            self.backButton.setEnabled(True)
        if self.stackedWidget.currentIndex() == self.stackedWidget.count() - 1:
            self.nextButton.setDisabled(True)

    def previous_page(self):
        if self.stackedWidget.currentIndex() > 0:
            self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1)
            self.nextButton.setEnabled(True)
        if self.stackedWidget.currentIndex() == 0:
            self.backButton.setDisabled(True)

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
        self.strengthBox.setValue(self.character.strength[0])
        self.perceptionBox.setValue(self.character.perception[0])
        self.enduranceBox.setValue(self.character.endurance[0])
        self.charismaBox.setValue(self.character.charisma[0])
        self.intelligenceBox.setValue(self.character.intelligence[0])
        self.agilityBox.setValue(self.character.agility[0])
        self.luckBox.setValue(self.character.luck[0])
        self.strengthModBox.setValue(sum(self.character.strength[1]))
        self.perceptionModBox.setValue(sum(self.character.perception[1]))
        self.enduranceModBox.setValue(sum(self.character.endurance[1]))
        self.charismaModBox.setValue(sum(self.character.charisma[1]))
        self.intelligenceModBox.setValue(sum(self.character.intelligence[1]))
        self.agilityModBox.setValue(sum(self.character.agility[1]))
        self.luckModBox.setValue(sum(self.character.luck[1]))
        self.strengthTotalBox.setValue(self.character.total_value(self.character.strength))
        self.perceptionTotalBox.setValue(self.character.total_value(self.character.perception))
        self.enduranceTotalBox.setValue(self.character.total_value(self.character.endurance))
        self.charismaTotalBox.setValue(self.character.total_value(self.character.charisma))
        self.intelligenceTotalBox.setValue(self.character.total_value(self.character.intelligence))
        self.agilityTotalBox.setValue(self.character.total_value(self.character.agility))
        self.luckTotalBox.setValue(self.character.total_value(self.character.luck))

    def set_attribute_limits(self):
        self.strengthBox.setMinimum(self.character.MIN_STRENGTH)
        self.strengthBox.setMaximum(self.character.MAX_STRENGTH)
        self.perceptionBox.setMinimum(self.character.MIN_PERCEPTION)
        self.perceptionBox.setMaximum(self.character.MAX_PERCEPTION)
        self.enduranceBox.setMinimum(self.character.MIN_ENDURANCE)
        self.enduranceBox.setMaximum(self.character.MAX_ENDURANCE)
        self.charismaBox.setMinimum(self.character.MIN_CHARISMA)
        self.charismaBox.setMaximum(self.character.MAX_CHARISMA)
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

    def list_traits(self):
        self.traitListWidget.clear()
        for trait in config.TRAIT_LIST:
            if str(self.character) in trait.races:
                item = QtWidgets.QListWidgetItem(str(trait))
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.traitListWidget.addItem(item)

        self.traitListWidget.sortItems(QtCore.Qt.AscendingOrder)

    def show_trait_description(self):
        for trait in config.TRAIT_LIST:
            if trait.name == self.traitListWidget.currentItem().text():
                self.descriptionBox.setText(trait.description)
                break

    def handle_trait_check(self):

        list_items = [self.traitListWidget.item(i).text() for i in range(self.traitListWidget.count())]
        traits_available = sorted([trait for trait in config.TRAIT_LIST if trait.name in list_items],
                                  key=lambda trait: trait.name)

        for i, trait in enumerate(traits_available):
            if self.traitListWidget.item(i).checkState() and str(trait) not in self.character.traits:
                if len(self.character.traits) < 2:
                    attr_name = trait.attribute_mod[1].lower()
                    attr = getattr(self.character, attr_name)
                    mod = attr[1]
                    mod.update({trait.name: trait.attribute_mod[0]})
                    setattr(self.character, attr_name, (attr[0], mod))
                    self.character.add_trait(trait)
                    break
                elif len(self.character.traits) == 2 and str(trait) not in self.character.traits:
                    self.traitListWidget.item(i).setCheckState(QtCore.Qt.Unchecked)

            elif not self.traitListWidget.item(i).checkState() and str(trait) in self.character.traits:
                attr_name = trait.attribute_mod[1].lower()
                attr = getattr(self.character, attr_name)
                mod = attr[1]
                del mod[trait.name]
                setattr(self.character, attr_name, (attr[0], mod))
                self.character.remove_trait(trait)
                break

    def validate_fields(self):
        return self.nameField.text() and self.ageField.text() and self.eyesField.text() and self.hairField.text() and \
               self.heightField.text() and self.weightField.text()

    def finish_character_creation(self):
        if self.validate_fields() and len(self.tagged_skills) == 3 and self.available_skill_points == 0:
            self.character.name = self.nameField.text()
            self.character.age = self.ageField.text()
            self.character.sex = self.sexPicker.currentText()
            self.character.eyes = self.eyesField.text()
            self.character.hair = self.hairField.text()
            self.character.height = self.heightField.text()
            self.character.weight = self.weightField.text()
            self.character.appearance = self.appearanceField.toPlainText()
            self.accept()

    def get_character(self):
        return self.character


class AboutDialogue(QtWidgets.QDialog, about_dialogue.Ui_Dialog):
    def __init__(self, parent=None):
        super(AboutDialogue, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.close)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = CharacterCreator()
    form.show()
    sys.exit(app.exec_())
