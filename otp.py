import base64, string, secrets
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk, messagebox, filedialog
from itertools import cycle

KEY_LETTERS = tuple(string.ascii_letters + string.punctuation + string.digits)
APP_TITLE = 'OTP'

input_empty = True
key_empty = True

ICON_BYTES = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x1e\x00\x00\x00\x1e\x08\x06\x00\x00\x00;0\xae\xa2\x00\x00\x00 cHRM\x00\x00z&\x00\x00\x80\x84\x00\x00\xfa\x00\x00\x00\x80\xe8\x00\x00u0\x00\x00\xea`\x00\x00:\x98\x00\x00\x17p\x9c\xbaQ<\x00\x00\x00\x06bKGD\x00\xff\x00\xff\x00\xff\xa0\xbd\xa7\x93\x00\x00\x00\x07tIME\x07\xe9\n\x1e\x07\x0e\x0b\x0b\xf7:d\x00\x00\x05\x05IDATH\xc7\xed\x94]\x88]W\x15\xc7\x7fk\xeds\xce\x9d\xb9g\xee\x9d\x1b3CZ\x9a\x8f\xa6M3\xa6\x9dAc#\xb6\xb4M\x1b\x13\x12\x82\xc6\x1ae@DTP\x04\xdfD\x10T4(V\x0b\x01\x0b>(T\xf0E,H\xf5A\xa4\x824\xb6\xc6\xd6B\x85\xc4\x9a\x86\x94\xda\xd1\xd6\x8f\xb6c\x92\x99df\xee\xe7\xb9g\xef\xbd|\xb8\xf9\xa8\x9dd:\xc1\xc7\xf6\xff\xb4\xd9\xeb\x9c\xfd\xdbk\xad\xff^\xf0\x8e\xde\xderk\xb9~\xff\xe713p\x1b\xb8\xe9\xde\x8f\xeb\xe8\xd4\xee\xb4\xbemg22q\x8fB\x03\xd6Nr\xfd\x1d\x1f\xbe\xe6\xa3\xe5j\x81\x18#k\xde\xff!4I\xe9\x97\xa5\xac\xdf\xb2\x99\xf2\xf4i\x9b\x9b?\x8f\x05\x0f\x06E\xbb\xed6\x8d\xe6a\xa1\xd7G+\x15N\x9f\xfa\xc3\xaa\xc1z\xb5@\xbe\xf5nbQ\x10\xfb}\xf1\xe2\x8c\xb2o\xce\xb9\x9d\xc0\x03\x98}\xc5b\xdc""a\xe6\x95\xff\xc8\xb6\xb1\x06\x8f|\xf1\xb3\xbc\xeb}\xfbV\rN\xae\x16\xe8\xcc<C\xfd\xb6\xfb\xc4\xb7\x16-sZ{\xed\xc5\xa5_\xba4\xdb\x8b\x80$\t \x87+N\xbf^\xac\xdf\xf8\xe0\xb3y.k\xda\xe7\xac\x9c\x9b\xfb\xff3\xbey\xd74\xd1%j\xd9\x10\xb8\xf4\'\xe2\x92\xbd\xc0\xa1\x0f\xbcgr||l\xedV\x8b\xf1W\xb8\xe4{\xeb\xca\xde\xc7\x1a\xe7\xce\xda\xfeG\x8f8\xbb\x86\x1e_\x15<\xfb\xeak\x1a\xbb\xdd`\xbd\xee\x84\xc1\xb4\xf9\xf2[V\x16\xdf\xb9n\xfd\xa69\x8c\x99\xd6+/\x1f\xcc\xb2\xf4\xf9N\xa7\xfb\xd0\x99\xe3\xbfe\xfdx#$\x8d\xc6\xaa\xc1\xcb\xcc5r\xdb\x07\t\xadE\\\xad\xae \x11\x8b\x07@~m\xb0\xa7\x8c\xf1\x89<\xcb\x86C\x08\xae\xefC+K\x93C\x16\xe3\xb7\x9dh\xbd\xec\x97MTp\x95\x94\x85\xe7\x1eGUW\x04/\x8f\x9a!*\xe0\xbdR\xf6\x11\xe4u\x11\x88h3s\x0e\xef}7\x9a\xb5\xd2\xc4\x11c,\x01\\\x9a4\x87j9\xd5|X\xd7\x8d\xad\xd5\xea\xd6\xbb\xdd\r\xb7\xef\x13\xa8Ae\x13\x13{?\xb1\x0c\xe3\xde\xbc\x91\x8do\xc6|_cY\x04\x0baJ\xb3\xcaW\x11\x99\x14\xa8\x88\xb0\r\x91="\xb2\xcb`\x87\x08\xfb\x81\x1bU\xb5\x18\xae\x8d<?4\x94\xf5T\xd5\x96\x16\x97l\xc7\xe4M\xcc\xfa\x8a\xc6<\xb7\xc5f\x87\xedw\xeeb\xf6\xa5\xbf\\\xe2,w\xb5\x88\xd8\xe8x44M\xcb\xf6\xe3\x08\xd7\x01A\xc4>\x8d]n\x8e\\^{\xef\xfd\x83K\xf3\xe7\xb65\x9b\x9d\xcf\xdc\xbce\xd3{\xcdl\xac\x91\xb9\xa3\x02\x1eD\x81x\xfc\x8f\xcf\xae\\j\x11\xc3\xf9\x82\xc4w\x87\x10\xa9\tD05\xb3RT\x8dh\x0bfV \x04\xc0#\x10\xcd\x88\xbe<[\xafW\xbf\x7f\xf6\xec\xdcs\xe9P\xe5\xc8\xefN\xfe\xe3\xe5\xbc^\x9b\xaa\xd5k\xb1\x92\xa5\xca\x9bz~E\x07(\xa0\x88a\x043\x14#\x00i\xc5\xe9\x89\xe9\x9d;6\xb6\x97\xda\xbb1T\x105#I\x13\xf7\xb7$q\xaf\x9b\xf1e1^R\xd5o\xf6\x8b\xfe\xbaP\x96?^<q\x92\xd6\xc9gl\xc3\xbboy+s1\x98\xcdf\x97]/\x98 \x04\xb3\x99G\x9f>\xd6\xfc\xdc\'\x0f\x9c\x10\xace\x98\x08\x86\x88\x9e\xc8\x86\xab\xa9a\x88\xeaO\xcdx@U\x0f\x97\xde\xdfQ\x9f\xba\xb5Z\x9f\xba\xcb\x16\x96\x9a\xff\xf3\x82\xae\xd0c\x10\x91\xc1\xc2\x0c\xec\x82\t\x05+}\x98.\xfa\xc5\xc4c\xbf\xff\xd3nTkD\xeb!:\x04\x9c\xea\xb5;\x93\xa2J\x88\xe1\x0b\x82d&\xf2%\xf3\xfe\xef\xcd\x17\x9f\xea\x00\xe4[\xee\xb4\x953\x06,\x1a\x16\xe3\xc0B2\xa8\x02\x06*\xc2\xe6F=..,V-\x1a\x08C\xc4\xf8\x83\xf6\xf9\xf9\x86\xa9|\xea\xc2\xbd7"\x1c\x02\x0b\x9a\xb8\xe9\xc6\xf6}4\xb6\xef\xd3\x1b\xf6\x1c`\xc5\x8c/\xd6V@\x0cs\x06\x01\x08\x08\x98\xa0\xb3\xad\xde\xc3\xaa:\x86\x08\x82=\x94\x98\xef0R\xfb\x06\xa2f\xd1\xfe\x95\xa5\xe9\xd7\xf2|h\xa1W\x94\xc7;\xad\xf6\x99\xac\xa2Z\xf8\x10\xb3\x91\xfa\xca`C0u\x18R\xa8\xf9%\xccr\x04w\xa9\xf7Nw)\x82\xc5\xf8\xc3\xe1D\xe6{d\xdf\xbd0x~\x93\xd7\xd7|4\x14\xed\x10b\x1c|+\xa21\x84\x18\xbcg\xe6\x91\x87W\x06\x0foXg\xbd\x7f\x9fQ\x84>\xce}\xc4\x82?hF!\x17\x8ba\xe6\xc4\xe9,\xfd>]\xa9\xfc\x08\x0c\x83\xc7\x8aJ\xe5\xa0\xef,\x85\xaa\xaa\x1b\xb4+\xc64qq4\x1f\xa6\x8a\xf1\xea\xa9\'W\x06\xc7\x10\x00\x8b\x18"p\xcc\x8cco\x8c\xbb\xc4\xd1\xed\x16\x8cTG\x0e\x17eIh-\x1e\xe9\xfe\xf3\xcf\xf7\x031\xb9\xf1v\x99\xefYHGs2\xe7h\xbfp\x94\xf3\\Y\xcb\xc0\xfd\xd3\xe7Ae\x90\x9b\x99\x0e\xca\xfc\x861Uz\xa1\xb9\xd8\xef\x04\xff33A\xcc~\x9e\xdfrWDE\xeb\xbfx:&\xf7\xdf\x0bYJ\xf3\xe4\x13\xac$\xe1\x1a\xe4\x83\xa7>q\xcf\xc5\xff\x06\xc6\xee\xf7pyM1b\xeb\xafO1r\xeb}\xb4^8\xfa\x96g%\xab\x01^\xba\xa5\x08q0X\xcc\xa9*f\x0e\x91`!D\x00\xb4\xbe*\xe8;z{\xe8\xbft\x98d\x14\xa3\x02\xe8\xe2\x00\x00\x00%tEXtdate:create\x002025-10-30T07:12:49+00:00\xd82\xb3|\x00\x00\x00%tEXtdate:modify\x002025-10-30T07:10:54+00:00\x00\xe7\xba\xa3\x00\x00\x00(tEXtdate:timestamp\x002025-10-30T07:14:11+00:00\x88k\x1a[\x00\x00\x00 tEXtsoftware\x00https://imagemagick.org\xbc\xcf\x1d\x9d\x00\x00\x00\x18tEXtThumb::Document::Pages\x001\xa7\xff\xbb/\x00\x00\x00\x19tEXtThumb::Image::Height\x001024\xe7&\xd8\xbd\x00\x00\x00\x18tEXtThumb::Image::Width\x001024\xf2o\x04\xa4\x00\x00\x00\x17tEXtThumb::MTime\x001761808254%\x15\'\xa3\x00\x00\x00\x12tEXtThumb::Size\x00141874y+\x00\xea\x00\x00\x00\x15tEXtThumb::URI\x00./icon.png\x85D\xfel\x00\x00\x00\x00IEND\xaeB`\x82'

def set_status(widget, value):
    global input_empty,key_empty
    if isinstance(widget, Text):
        if widget == input_text:
            input_empty = value
    else:
        key_empty = value

class Entry(tk.Entry):

    def __init__(self,master = None ,defaulttext = '', defaultfg='#3e3e3e', *args, **kwargs):
        super().__init__(master,*args, **kwargs)
        self.defaultfg = defaultfg
        self.mainfg = self['fg']
        self.defaulttext = defaulttext
        if not self['textvariable']:
            self.insert(0, defaulttext)
            self.config(fg=defaultfg)

        self.bind('<FocusIn>', self._focus_in_handler)
        self.bind('<FocusOut>', self._focus_out_handler)

    def _focus_in_handler(self, event=None):
        if self.get() == self.defaulttext and self['fg'] == self.defaultfg:
            self.delete(0, 'end')
            self.config(fg=self.mainfg)

    def _focus_out_handler(self, event=None):
        if not self.get():
            self.insert(0, self.defaulttext)
            self.config(fg=self.defaultfg)
            set_status(self, True)
        else:
            set_status(self, False)

class Text(ScrolledText):

    def __init__(self,master = None ,defaulttext = '', defaultfg='#3e3e3e', *args, **kwargs):
        super().__init__(master,*args, **kwargs)
        self.defaultfg = defaultfg
        self.mainfg = self['fg']
        self.defaulttext = defaulttext
        self.insert('1.0', defaulttext)
        self.config(fg=defaultfg)

        self.bind('<FocusIn>', self._focus_in_handler)
        self.bind('<FocusOut>', self._focus_out_handler)

    def _focus_in_handler(self, event=None):
        if self.get('0.0', 'end')[:-1] == self.defaulttext and self['fg'] == self.defaultfg:
            self.delete('0.0', 'end')
            self.config(fg=self.mainfg)

    def _focus_out_handler(self, event=None):
        if not self.get('0.0', 'end')[:-1]:
            self.insert('1.0', self.defaulttext)
            self.config(fg=self.defaultfg)
            set_status(self, True)
        else:
            set_status(self, False)

def show_error(message):
    messagebox.showerror(title=APP_TITLE,message=message)

def save_output(binary):
    if binary:
        file_mode = 'wb'
    else:
        file_mode = 'w'

    try:
        file_obj = filedialog.asksaveasfile(mode=file_mode)

        if file_obj:
            if var.get():
                if binary:
                    data = base64.b64decode(output_text.get('1.0','end'))
                else:
                    data = output_text.get('1.0','end')

            else:
                if binary:
                    data = output_text.get('1.0','end').encode()
                else:
                    data = base64.b64encode(output_text.get('1.0','end').encode()).decode()

            file_obj.write(data)
    except PermissionError as err:
        show_error(err)
    
def clear_widget(widget):
    if isinstance(widget, Entry):
        widget.delete(0,'end')
    else:
        widget.delete('1.0','end')
    if window.focus_get() != widget:
        widget.insert('end', widget.defaulttext)
        widget.config(fg = widget.defaultfg)
        set_status(widget, True)

def decode_text(encrypted_text):
    try:
        return base64.b64decode(encrypted_text).decode()
    except:
        show_error('You should enter a base64 text to decrypt it')
        return

def convert_hex(key):
    try:
        return bytes.fromhex(key)
    except:
        show_error('Your key is not hexadecimal')
        return

def encrypt(text,key):
    if use_hex_var.get():
        key = convert_hex(key)
        if not key:
            return
    key = cycle(key)
    encrypted_text = ''
    if use_hex_var.get():
        for char in text:
            encrypted_text += chr(ord(char)+next(key))
    else:
        for char in text:
            encrypted_text += chr(ord(char)+ord(next(key)))
    return base64.b64encode(encrypted_text.encode())

def decrypt(encrypted_text,key):
    if use_hex_var.get():
        key = convert_hex(key)
        if not key:
            return
    encrypted_text = decode_text(encrypted_text)
    if not encrypted_text:
        return
    
    key = cycle(key)
    decrypted_text = ''
    if use_hex_var.get():
        for char in encrypted_text:
            decrypted_text += chr(ord(char)-next(key))
    else:
        for char in encrypted_text:
            decrypted_text += chr(ord(char)-ord(next(key)))
    return decrypted_text

def check():
    if not key_empty and not input_empty:
        try:
            if var.get():
                data = encrypt(input_text.get('1.0','end'), key_entry.get())
            else:
                data = decrypt(input_text.get('1.0','end'), key_entry.get())
            if data:
                output_text.delete('1.0','end')
                output_text.insert('1.0', data)
        except:
            show_error('An error occured while decrypting. Your key is probably wrong')
    else:
        messagebox.showwarning(title=APP_TITLE, message='You should enter both key and input text to encrypt or decrypt it.')

def create_random_key():
    global key_empty
    if not input_empty:
        key_entry.delete(0, 'end')
        key = ''
        text_length = len(input_text.get('1.0', 'end'))
        if not use_hex_var.get():
            for i in range(text_length):
                key += secrets.choice(KEY_LETTERS)
        else:
            key = secrets.token_hex(text_length)
        key_entry.insert(0, key)
        key_empty = False
    else:
        messagebox.showwarning(title=APP_TITLE, message='You should enter an input text to make a random key for it')

def copy_entry():
    window.clipboard_clear()
    window.clipboard_append(key_entry.get())

def copy_text(widget):
    window.clipboard_clear()
    window.clipboard_append(widget.get('1.0', 'end'))

def create_context_menu(is_entry,output_text=False):
    context_menu = tk.Menu(tearoff=0)
    context_menu.add_command(label='Select All', accelerator='Ctrl+A')
    context_menu.add_command(label='Copy', accelerator='Ctrl+C')
    context_menu.add_command(label='Paste', accelerator='Ctrl+V')
    context_menu.add_command(label='Cut', accelerator='Ctrl+X')
    context_menu.add_separator()
    if is_entry:
        context_menu.add_command(label='Copy Key', command=lambda : copy_entry(),accelerator='Ctrl+C')
        context_menu.add_command(label='Delete Key', command=lambda : clear_widget(key_entry),accelerator='Ctrl+D')
    if not is_entry:
        context_menu.add_command(accelerator='Ctrl+C')
        context_menu.add_command(accelerator='Ctrl+D')

        if output_text:
            context_menu.add_separator()
            context_menu.add_command(label='Save as binary',command=lambda : save_output(True),accelerator='Ctrl+S')
            context_menu.add_command(label='Save as base64',command=lambda : save_output(False),accelerator='Ctrl+Shift+S')
    return context_menu

def configure_menu(event, context_menu):
    if isinstance(event.widget, Text):
        if event.widget == input_text:
            context_menu.entryconfigure(5, label='Copy Input',command=lambda: copy_text(event.widget))
            context_menu.entryconfigure(6, label='Clear Input', command=lambda: clear_widget(event.widget))

        elif event.widget == output_text:
            context_menu.entryconfigure(5, label='Copy Output', command=lambda: copy_text(event.widget))
            context_menu.entryconfigure(6, label='Clear Output', command=lambda: clear_widget(event.widget))

    if window.focus_get() == event.widget:
        for i in range(4):
            context_menu.entryconfigure(i, state='normal')
        if isinstance(event.widget, Text):
            context_menu.entryconfigure(0, command=lambda: event.widget.tag_add('sel', '1.0', 'end'))
        else:
            context_menu.entryconfigure(0, command=lambda: event.widget.select_range(0, 'end'))

        context_menu.entryconfigure(1, command=lambda: event.widget.event_generate('<<Copy>>'))
        context_menu.entryconfigure(2, command=lambda: event.widget.event_generate('<<Paste>>'))
        context_menu.entryconfigure(3, command=lambda: event.widget.event_generate('<<Cut>>'))
    else:
        for i in range(4):
            context_menu.entryconfigure(i, state='disabled')

    return context_menu

def show_menu(event, context_menu):
    context_menu = configure_menu(event, context_menu)
    context_menu.tk_popup(event.x_root, event.y_root)

window = None
try:
    from ttkthemes import ThemedTk
    window = ThemedTk(theme='yaru')
except ModuleNotFoundError:
    window = tk.Tk()

input_text_menu = create_context_menu(False)
output_text_menu = create_context_menu(False,True)
key_entry_menu = create_context_menu(True)

window.title(APP_TITLE)

icon = tk.PhotoImage(data=ICON_BYTES)
window.iconphoto(True, icon)

root_frm = ttk.Frame()
rb_frm = ttk.Frame(root_frm,padding = 5)
text_frm = ttk.Frame(root_frm,padding = 5)
key_frm = ttk.Frame(root_frm,padding = 5)

var = tk.IntVar(value=1)
encrypt_rb = ttk.Radiobutton(rb_frm,text='Encrypt', variable=var, value=1, command = lambda : btn_convert.config(text='Encrypt'))
decrypt_rb = ttk.Radiobutton(rb_frm,text='Decrypt', variable=var, value=0, command = lambda : btn_convert.config(text='Decrypt'))

input_text = Text(text_frm,width=45, height=13, defaulttext='Enter the text here', font = 'TkTextFont', 
                  defaultfg='#3a3a3a', wrap = 'word',insertwidth=1)
output_text = Text(text_frm,width=45, height=13, defaulttext='The output will be shown here', font = 'TkTextFont', 
                   defaultfg='#3a3a3a', wrap = 'word',insertwidth=1)
btn_convert = ttk.Button(text_frm,text='Encrypt', command=check)

use_hex_var = tk.IntVar()
key_entry = Entry(key_frm, defaulttext='Enter the key here',insertwidth=1)
random_btn = ttk.Button(key_frm,text='random', command=create_random_key)
use_hex_cb = ttk.Checkbutton(key_frm,text='Use hex key', variable=use_hex_var)

input_text.bind('<Button-3>', lambda event : show_menu(event,input_text_menu))
output_text.bind('<Button-3>', lambda event : show_menu(event,output_text_menu))
key_entry.bind('<Button-3>', lambda event : show_menu(event, key_entry_menu))

output_text.bind('<Control-c>',lambda event : copy_text(output_text))
output_text.bind('<Control-d>',lambda event : clear_widget(output_text))
output_text.bind('<Control-s>',lambda event : save_output(True))
output_text.bind('<Control-S>',lambda event : save_output(False))

input_text.bind('<Control-c>',lambda event : copy_text(input_text))
input_text.bind('<Control-d>',lambda event : clear_widget(input_text))

key_entry.bind('<Control-c>',lambda event : copy_entry())
key_entry.bind('<Control-d>',lambda event : clear_widget(key_entry))

root_frm.pack(fill='both',expand=1)
rb_frm.pack()
key_frm.pack(anchor='w',fill='x')
text_frm.pack(fill='both', expand=1)

encrypt_rb.pack(side='left',padx=(0,10))
decrypt_rb.pack(side='left',padx=(10,0))

use_hex_cb.grid(row = 0,column = 0)
key_entry.grid(row=1, column=0, sticky='e', pady=5,ipady=1)
random_btn.grid(row=1,column=1, padx=5)

input_text.pack(side='left', fill='both', expand=1)
btn_convert.pack(side='left', padx=10)
output_text.pack(side='left',fill='both', expand=1)

window.mainloop()
