import urwid
from disassemble import *
from assembler import *
from statusbar import *
import signals

class DisassembleText(urwid.Text):

    def selectable(self):
        return False

    def keypress(self, size, key):
        return key

class DisassembleInstruction(urwid.WidgetWrap):
    def __init__(self, instr, da, view):
        urwid.WidgetWrap.__init__(self, None)
        self.address = urwid.Text(hex(instr.address).rstrip('L'))
        self.opcode = urwid.Text(' '.join(["%02x" % (j) for j in instr.bytes]))
        self.instr = urwid.Text(instr.mnemonic)
        self.operands = urwid.Text(instr.op_str)
        self.editMode = False
        self.da = da
        self.view = view
        self.mode4()

    def selectable(self):
        return True

    def mode4(self):
        self._w = urwid.Columns([
            ('fixed', 12, self.address),
            ('fixed', 25, self.opcode),
            ('fixed', 10, self.instr),
            ('fixed', 55, self.operands)
            ])

    def mode3(self):
        self._w = urwid.Columns([
            ('fixed', 12, self.address),
            ('fixed', 25, self.opcode),
            ('fixed', 65, self._editbox),
            ])

    def modifyOpcode(self, opcode):
        if opcode == "":
            self.mode4()
            return

        original_opcode_len = len(self.opcode.text.replace(' ','').decode('hex'))
        if len(opcode) < original_opcode_len:
            opcode = opcode.ljust(original_opcode_len, "\x90") # Fill with nop
        elif len(opcode) > original_opcode_len:
            safe_opcode_len = 0
            for i in self.da.disasm(int(self.address.text, 16), 0x20):
                if len(opcode) > safe_opcode_len:
                    safe_opcode_len += len(i.bytes)
            opcode = opcode.ljust(safe_opcode_len, "\x90") # Fill with nop

        self.da.writeMemory(int(self.address.text, 16), opcode)

        if original_opcode_len == len(opcode):
            self.opcode.set_text(' '.join(["%02x" % ord(i) for i in opcode]))
            code = [i for i in self.da.md.disasm(opcode, len(opcode))][0]
            self.instr.set_text(code.mnemonic)
            self.operands.set_text(code.op_str)
            self.mode4()
        else:
            self.view.updateList(self.view.disasmlist._w.focus_position)

    def keypress(self, size, key):
        if self.editMode:
            if key == "esc":
                self.editMode = False
                self.mode4()
            elif key == "enter":
                self.editMode = False
                asmcode = self._editbox.get_edit_text()
                opcode = assemble(asmcode, self.da.arch)
                self.modifyOpcode(opcode)
            elif isinstance(key, basestring):
                self._w.keypress(size, key)
            else:
                return key
        else:
            if key == "enter":
                self._editbox = urwid.Edit("", self.instr.text+" "+self.operands.text)
                self.mode3()
                self.editMode = True
            elif key == "d" or key == "D":
                def fillWithNop(yn, arg):
                    if yn == 'y':
                        self.modifyOpcode("\x90")
                signals.set_prompt_yn.send(self, text="Remove this line?", callback=fillWithNop, arg=None)
            else:
                if key == "j" or key == "J":
                    key = "down"
                elif key == "k" or key == "K":
                    key = "up"
                return key

class SymbolText(urwid.Text):

    def selectable(self):
        return False

    def keypress(self, size, key):
        return key

class DisassembleList(urwid.WidgetWrap):
    def __init__(self, dList):
        urwid.WidgetWrap.__init__(self, None)
        self.updateList(dList)

    def set_focus(self, idx):
        self._w.set_focus(idx)

    def updateList(self, dList, focus=0):
        self._w = urwid.ListBox(urwid.SimpleListWalker(dList))
        if focus:
            self._w.set_focus(focus)

    def selectable(self):
        return True

    def keypress(self, size, key):
        key = super(self.__class__, self).keypress(size, key)
        if key == "j":
            key = "down"
        elif key == "k":
            key = "up"
        return key

class DisassembleWindow(urwid.Frame):
    def __init__(self, view, body, header, footer):
        urwid.Frame.__init__(
                self, body,
                header if header else None,
                footer if footer else None
            )
        self.view = view
        signals.focus.connect(self.sig_focus)

    def sig_focus(self, sender, section):
        self.focus_position = section

    def keypress(self, size, key):
        key = super(self.__class__, self).keypress(size, key)
        return key

class DisassembleView:
    palette = [('header', 'white', 'black'),
            ('reveal focus', 'black', 'light gray', 'standout'),
            ('status', 'white', 'dark blue', 'standout')]

    def __init__(self, filename):
        self.header = urwid.Text(" BINCH: %s" % (filename))

        self.da = Disassembler(filename)

        items = self.setupList()
        self.disasmlist = DisassembleList(items)

        self.body = urwid.Padding(self.disasmlist, 'center', 105)
        self.body = urwid.Filler(self.body, ('fixed top',1), ('fixed bottom',1))

        self.footer = StatusBar("HotKeys -> g: Go to a address | s: Save | d: Remove | enter: Modify | q: Quit")
        self.view = DisassembleWindow(self,
                urwid.AttrWrap(self.body, 'body'),
                urwid.AttrWrap(self.header, 'head'),
                self.footer)

        signals.call_delay.connect(self.sig_call_delay)

    def setupList(self):
        body = self.da.disasm(self.da.entry)
        items = []
        idx = 0
        self.index_map = dict()
        for i in body:
            address = i.address
            if address in self.da.symtab:
                items.append(SymbolText(" "))
                items.append(SymbolText(" < "+self.da.symtab[address]+" >"))
                idx+=2
            items.append(DisassembleInstruction(i, self.da, self))
            self.index_map[address] = idx
            idx+=1

        items = map(lambda x: urwid.AttrMap(x, 'bg', 'reveal focus'), items)
        return items

    def updateList(self, focus=0):
        items = self.setupList()
        self.disasmlist.updateList(items, focus)

    def main(self):
        self.loop = urwid.MainLoop(self.view, self.palette,
                handle_mouse=False,
                unhandled_input=self.unhandled_input)
        self.loop.run()

    def unhandled_input(self, k):
        def goto(text):
            try:
                address = int(text, 16)
            except:
                return "It is not hexadecimal number: "+text

            if address in self.index_map:
                self.disasmlist.set_focus(self.index_map[address])
                return "Jump to "+hex(address)
            else:
                for i in range(1, 0x10):
                    if address - i in self.index_map:
                        self.disasmlist.set_focus(self.index_map[address - i])
                        return "Jump to "+hex(address - i)
                    elif address + i in self.index_map:
                        self.disasmlist.set_focus(self.index_map[address + i])
                        return "Jump to "+hex(address + i)

                return "Invalid address: "+hex(address)

        if k in ('q', 'Q'):
            def askQuit(yn, arg):
                if yn == 'y':
                    raise urwid.ExitMainLoop()
            signals.set_prompt_yn.send(self, text="Quit?", callback=askQuit, arg=None)
        elif k in ('g', 'G'):
            signals.set_prompt.send(self, text="Goto: ", callback=goto)
        elif k in ('s', 'S'):
            self.da.save()

    def sig_call_delay(self, sender, seconds, callback):
        def cb(*_):
            return callback()
        self.loop.set_alarm_in(seconds, cb)
