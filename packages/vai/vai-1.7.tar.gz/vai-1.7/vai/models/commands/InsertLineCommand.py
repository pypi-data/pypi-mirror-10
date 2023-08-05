from .BufferCommand import BufferCommand
from .CommandResult import CommandResult

class InsertLineCommand(BufferCommand):
    def __init__(self, buffer, text):
        super().__init__(buffer)
        self._text = text

    def execute(self):
        document = self._document
        cursor = self._cursor

        if self.savedCursorPos() is None:
            self.saveCursorPos()

        self.saveModifiedState()
        pos = self.savedCursorPos()

        document.insertLine(pos[0], self._text)
        document.lineMetaInfo("Change").setData("added", pos[0])
        cursor.toCharFirstNonBlankForLine(pos[0])
        document.documentMetaInfo("Modified").setData(True)
        return CommandResult(True,  None)

    def undo(self):
        self._document.deleteLine(self.savedCursorPos()[0])
        self.restoreCursorPos()
        self.restoreModifiedState()

