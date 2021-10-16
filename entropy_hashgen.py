"""
Entropy Hashgen
Written by: N.M.
Version: 1.0
https://hashgen.n3p.xyz
"""

import hashlib, string, tkinter as tk, sys, os, base64
from datetime import date
from tkinter import filedialog, messagebox, ttk
from tkinter.constants import DISABLED, NORMAL, END

class AppValuesClass:
    def __init__(self):
        # op1
        self.filename = ''
        self.path = ''
        self.md5 = ''
        self.sha1 = ''
        self.sha256 = ''
        # op2
        self.checksum = ''
        self.checksum_type = ''
        self.analysis = ''
        self.comparison = ''

    def clear_op1(self):
        """ Clear op1 text boxes """
        self.filename = ''
        self.path = ''
        self.md5 = ''
        self.sha1 = ''
        self.sha256 = ''

    def clear_op2(self):
        """ Clear op1 text boxes """
        self.checksum = ''
        self.checksum_type = ''
        self.analysis = ''
        self.comparison = ''

def populate_main_window(frm_main):
    """Populate the main window of this program.
    Parameter
        frm_main: the main window
    Return: nothing
    """

    # object where values will be stored
    AppValues = AppValuesClass()

    class TextStyle:
        def __init__(self):
            self.font = 'Tahoma'
            self.size = 16
            self.style = 'normal'
            self.color = '#000000'
        def apply(self):
            return self.font, self.size, self.style

    # define styles
    LABEL_Style = TextStyle()
    LABEL_Style.font = 'Tahoma'
    LABEL_Style.size = 10
    LABEL_Style.style = 'normal'

    TEXT_FIELD_Style = TextStyle()
    TEXT_FIELD_Style.font = 'Courier New'
    TEXT_FIELD_Style.size = 10
    TEXT_FIELD_Style.style = 'bold'   
    # end styles

    # op1 widgets
    btn_op1_select_file = tk.Button(frm_main, text="Select File", height=1)
    btn_op1_clear = tk.Button(frm_main, text="Clear", height=1)

    lbl_op1_filename = tk.Label(frm_main, text="Filename:", font=LABEL_Style.apply())
    lbl_op1_path = tk.Label(frm_main, text="Path:", font=LABEL_Style.apply())
    lbl_op1_md5 = tk.Label(frm_main, text="MD5:", font=LABEL_Style.apply())
    lbl_op1_sha1 = tk.Label(frm_main, text="SHA-1:", font=LABEL_Style.apply())
    lbl_op1_sha256 = tk.Label(frm_main, text="SHA-256:", font=LABEL_Style.apply())

    txt_op1_filename = tk.Text(frm_main, height=1, bg="#dddeee", font=TEXT_FIELD_Style.apply(), state=DISABLED)
    txt_op1_path = tk.Text(frm_main, height=1, bg="#dddeee", font=TEXT_FIELD_Style.apply(), state=DISABLED)    
    txt_op1_md5 = tk.Text(frm_main, height=1, bg="#dddeee", font=TEXT_FIELD_Style.apply(), state=DISABLED)
    txt_op1_sha1 = tk.Text(frm_main, height=1, bg="#dddeee", font=TEXT_FIELD_Style.apply(), state=DISABLED)
    txt_op1_sha256 = tk.Text(frm_main, height = 1, bg="#dddeee", font=TEXT_FIELD_Style.apply(), state=DISABLED)

    # op1 grid
    lbl_op1_path.grid(row=3, column=1, padx=3, pady=3, columnspan=2, sticky="W")
    txt_op1_path.grid(row=3, column=3, padx=3, pady=3, columnspan=6, sticky="W")

    btn_op1_select_file.grid(row=4, column=3, padx=3, pady=8, columnspan=2, sticky="EW")
    btn_op1_clear.grid(row=4, column=5, padx=3, pady=8, columnspan=2, sticky="EW")

    lbl_op1_filename.grid(row=5, column=1, padx=3, pady=3, columnspan=2, sticky="W")
    lbl_op1_md5.grid(row=6, column=1, padx=3, pady=3, columnspan=2, sticky="W")
    lbl_op1_sha1.grid(row=7, column=1, padx=3, pady=3, columnspan=2, sticky="W")
    lbl_op1_sha256.grid(row=8, column=1, padx=3, pady=3, columnspan=2, sticky="W")

    txt_op1_filename.grid(row=5, column=3, padx=3, pady=3, columnspan=6, sticky="W")    
    txt_op1_md5.grid(row=6, column=3, padx=3, pady=3, columnspan=6, sticky="W")
    txt_op1_sha1.grid(row=7, column=3, padx=3, pady=3, columnspan=6, sticky="W")
    txt_op1_sha256.grid(row=8, column=3, padx=3, pady=3, columnspan=6, sticky="W")

    # separator    
    sep_1 = ttk.Separator(frm_main, orient='horizontal')
    sep_1.grid(row=9, column=1, padx=3, pady=8, columnspan=9, sticky="EW")

    # op2 widgets
    lbl_op2_enter_checksum = tk.Label(frm_main, text="Enter Checksum:", font=LABEL_Style.apply())
    txt_op2_input = tk.Text(frm_main, height=1, font=TEXT_FIELD_Style.apply(), state=NORMAL)

    btn_op2_analyze = tk.Button(frm_main, text="Analyze & Compare", height=1)
    btn_op2_clear = tk.Button(frm_main, text = "Clear", height=1)
    btn_op2_clear_all = tk.Button(frm_main, text = "Clear All", height=1)

    lbl_op2_checksum = tk.Label(frm_main, text="Checksum:", font=LABEL_Style.apply())
    lbl_op2_analysis = tk.Label(frm_main, text="Analysis:", font=LABEL_Style.apply())
    lbl_op2_comparison = tk.Label(frm_main, text="Comparison:", font=LABEL_Style.apply())

    txt_op2_checksum = tk.Text(frm_main, height=1, bg="#dddeee", font=TEXT_FIELD_Style.apply(), state=DISABLED)
    txt_op2_analysis = tk.Text(frm_main, height=1, bg="#dddeee", font=TEXT_FIELD_Style.apply(), state=DISABLED)
    txt_op2_comparison = tk.Text(frm_main, height=1, bg="#dddeee", font=TEXT_FIELD_Style.apply(), state=DISABLED)

    # op2 grid
    lbl_op2_enter_checksum.grid(row=11, column=1, padx=3, pady=3, columnspan=2, sticky="W")
    txt_op2_input.grid(row=11, column=3, padx=3, pady=3, columnspan=6, sticky="W")

    btn_op2_analyze.grid(row=12, column=3, padx=3, pady=3, columnspan=2, sticky="EW")
    btn_op2_clear.grid(row=12, column=5, padx=3, pady=3, columnspan=2, sticky="EW")
    btn_op2_clear_all.grid(row=12, column=7, padx=3, pady=3, columnspan=2, sticky="EW")

    lbl_op2_checksum.grid(row=13, column=1, padx=3, pady=3, columnspan=2, sticky="W")
    lbl_op2_analysis.grid(row=14, column=1, padx=3, pady=3, columnspan=2, sticky="W")
    lbl_op2_comparison.grid(row=15, column=1, padx=3, pady=3, columnspan=2, sticky="W")

    txt_op2_checksum.grid(row=13, column=3, padx=3, pady=3, columnspan=6, sticky="W")
    txt_op2_analysis.grid(row=14, column=3, padx=3, pady=3, columnspan=6, sticky="EW")
    txt_op2_comparison.grid(row=15, column=3, padx=3, pady=3, columnspan=6, sticky="EW")

    # separator    
    sep_2 = ttk.Separator(frm_main, orient='horizontal')
    sep_2.grid(row=16, column=1, padx=3, pady=8, columnspan=9, sticky="EW")

    # about
    #lbl_credits = tk.Label(frm_main, text="Written by: Nephi Malit, CSE-111, Section 18")
    btn_about = tk.Button(frm_main, text="About", height=1)
    btn_exit = tk.Button(frm_main, text="Exit", height=1)

    #lbl_credits.grid(row=17, column=1, padx=3, pady=3, columnspan=3, sticky="W")
    btn_about.grid(row=17, column=5, padx=3, pady=3, columnspan=2, sticky="EW")
    btn_exit.grid(row=17, column=7, padx=3, pady=3, columnspan=2, sticky="EW")

    def CLICK_about():

        version = 'v1.0'

        current_date = date.today()
        copyright_year = int(current_date.year)

        if copyright_year > 2021:
            copyright_year = "2021-" + str(copyright_year)    

        about_title = "About"
        about_info = f"Entropy Hashgen {version} \n\nCopyright © {copyright_year} N.M.\nhashgen.n3p.xyz"

        messagebox.showinfo(about_title, about_info)       
    btn_about.configure(command=CLICK_about)

    def CLICK_exit():

        sys.exit()
    btn_exit.configure(command=CLICK_exit)

    def GUI_refresh_op1_text_widgets():
        """Refreshes the values for text widgets in op1"""
        
        op1_text_widgets = [ txt_op1_filename, txt_op1_path, txt_op1_md5, txt_op1_sha1, txt_op1_sha256 ]

        # unlock text widgets
        for widget in op1_text_widgets:
            widget.configure(state=NORMAL)
        
        # clear previous values:
        for widget in op1_text_widgets:
            widget.delete(1.0, END)

        # display new values
        txt_op1_filename.insert(1.0, AppValues.filename)
        txt_op1_path.insert(1.0, AppValues.path)
        txt_op1_md5.insert(1.0, AppValues.md5)
        txt_op1_sha1.insert(1.0, AppValues.sha1)
        txt_op1_sha256.insert(1.0, AppValues.sha256)

        # re-lock text widgets
        for widget in op1_text_widgets:
            widget.configure(state=DISABLED)

    def CLICK_op1_select_file():
        """Executes when the user clicks the "Select File" Button in Option 1"""

        # Select File dialog        
        selected_file = GUI_select_file("Select File")
        if selected_file != '':
            try:
                # update path and filename
                AppValues.path = selected_file

                split_path = AppValues.path.split(sep="/")
                AppValues.filename = split_path[-1]
                
                # display message to be shown while working
                AppValues.md5 = "Working, please wait..."     
                AppValues.sha1 = "Working, please wait..."
                AppValues.sha256 = "Working, please wait..."
                
                GUI_refresh_op1_text_widgets()
                frm_main.update_idletasks()
                
            except FileNotFoundError:
                messagebox.showerror("Error", "File Not Found")
                return
        
        else: # elif new_path == ''
            return

        # clear checksum, analysis, and comparison
        # to avoid confusion with previous results
        CLICK_op2_clear()

        # do calculations and display new values
        AppValues.md5 = get_md5_hash(AppValues.path)
        GUI_update_text_widget(txt_op1_md5, AppValues.md5)
        #GUI_refresh_op1_text_widgets()
        frm_main.update_idletasks()

        AppValues.sha1 = get_sha1_hash(AppValues.path)
        GUI_update_text_widget(txt_op1_sha1, AppValues.sha1)
        #GUI_refresh_op1_text_widgets()
        frm_main.update_idletasks()

        AppValues.sha256 = get_sha256_hash(AppValues.path)
        GUI_update_text_widget(txt_op1_sha256, AppValues.sha256)
        #GUI_refresh_op1_text_widgets()
        frm_main.update_idletasks()
    btn_op1_select_file.configure(command=CLICK_op1_select_file)

    def CLICK_op1_clear():
        """Executes when the "Clear" Button is clicked in Option 1"""

        # clear all values
        AppValues.clear_op1()
        AppValues.clear_op2()

        # display new values
        GUI_refresh_op1_text_widgets()
        GUI_refresh_op2_text_widgets()
    btn_op1_clear.configure(command=CLICK_op1_clear)

    def CLICK_op2_analyze():
        """Called when the "Analyze and Compare" button is clicked in op2

        calls the following functions:
            analyze_checksum()
            compare_hash()
        """

        # take the input
        user_input_checksum = txt_op2_input.get(1.0, END)
        user_input_checksum = user_input_checksum.lower()
        user_input_checksum = user_input_checksum.strip()
        user_input_checksum = user_input_checksum.replace('\n', '')

        # update Checksum
        AppValues.checksum = user_input_checksum
        
        # update 
        GUI_update_text_widget(txt_op2_checksum, AppValues.checksum)

        # analyze checksum
        AppValues.checksum_type = analyze_checksum(AppValues.checksum)

        if AppValues.checksum_type in ["MD5", "SHA-1", "SHA-256"]:

            txt_op2_analysis.config(fg="black")
            AppValues.analysis = (AppValues.checksum_type + " detected.")
            
            # 
            if AppValues.checksum_type == 'MD5':
                file_hash = AppValues.md5
            elif AppValues.checksum_type == 'SHA-1':
                file_hash = AppValues.sha1
            elif AppValues.checksum_type == 'SHA-256':
                file_hash = AppValues.sha256

            # compare hash
            is_checksum_match = compare_hash(file_hash, AppValues.checksum)

            if is_checksum_match:

                AppValues.comparison = (f"OK: The {AppValues.checksum_type} checksum and the {AppValues.checksum_type} hash of the file match.")
                txt_op2_comparison.configure(fg="green")

            elif AppValues.path == "": # no file selected
                AppValues.comparison = (f"No file selected.")
                txt_op2_comparison.configure(fg="black")

            else:
                AppValues.comparison = (f"WARNING: The {AppValues.checksum_type} checksum and the {AppValues.checksum_type} hash of the file DO NOT match.")
                txt_op2_comparison.configure(fg="red")
        
        else:
            AppValues.analysis = ("Invalid checksum.")
            txt_op2_analysis.configure(fg="red")
            AppValues.comparison = "Please enter a valid MD5, SHA-1, or SHA-256 checksum."
            txt_op2_comparison.configure(fg="red")

        # update Analysis Text Box
        GUI_update_text_widget(txt_op2_analysis, AppValues.analysis)
        GUI_update_text_widget(txt_op2_comparison, AppValues.comparison)
    btn_op2_analyze.configure(command=CLICK_op2_analyze)

    def CLICK_op2_clear():
        """ Executes when "Clear" button in Option 2 is clicked."""

        AppValues.clear_op2
        GUI_refresh_op2_text_widgets() # refresh GUI
    btn_op2_clear.configure(command=CLICK_op2_clear)

    def CLICK_op2_clear_all():
        """Clears all the Checksum text entry boxes"""
        
        # clear the checksum entry box
        txt_op2_input.delete(1.0, END)
        
        # clear the rest of the fields
        AppValues.clear_op2
        GUI_refresh_op2_text_widgets()
    btn_op2_clear_all.configure(command=CLICK_op2_clear_all)

    def GUI_select_file(window_title):
        """
        Opens a dialog box to select a file
        PARAMETTERS:
            window_title:   a string
        RETURNS:
            file_path   :   the path to the file
        """
        file_path = filedialog.askopenfilename(initialdir="C:\\",
                                            title=window_title,
                                            filetypes= (
                                                ("All files","*.*"),
                                                ("Executable", "*.exe"),
                                                ("Text files","*.txt")
                                                ))
        return file_path

    def GUI_refresh_op2_text_widgets():
        op2_output_widgets = [ txt_op2_checksum, txt_op2_analysis, txt_op2_comparison ]
        
        # unlock widgets
        for widget in op2_output_widgets:
            widget.configure(state=NORMAL)

        # clear widgets
        for widget in op2_output_widgets:
            widget.delete(1.0, END)

        # re-lock
        for widget in op2_output_widgets:
            widget.configure(state=DISABLED)       

    def GUI_update_text_widget(txt_widget, new_content):
        txt_widget.configure(state=NORMAL)
        txt_widget.delete(1.0, END)
        txt_widget.insert(1.0, new_content)
        txt_widget.configure(state=DISABLED)

def get_md5_hash(filename):
    """
    Get the MD5 Hash of a file
    """
    md5_hash = hashlib.md5()

    with open(filename,"rb") as file:

        # divide file into chunks to avoid loading the entire file in memory
        for chunk in iter(lambda: file.read(4096),b""):
            md5_hash.update(chunk)

    return md5_hash.hexdigest()

def get_sha1_hash(filename):
    """
    Get the SHA-1 Hash of a file
    """
    sha1_hash = hashlib.sha1()

    with open(filename,"rb") as file:

        # divide file into chunks to avoid loading the entire file in memory
        for chunk in iter(lambda: file.read(4096),b""):
            sha1_hash.update(chunk)

    return sha1_hash.hexdigest()

def get_sha256_hash(filename):
    """
    Get the SHA-256 Hash of a file
    """
    sha256_hash = hashlib.sha256()

    with open(filename,"rb") as file:

        # divide file into chunks to avoid loading the entire file in memory
        for chunk in iter(lambda: file.read(4096),b""):
            sha256_hash.update(chunk)

    return sha256_hash.hexdigest()

def analyze_checksum(hash):
    """
    Analyzes a secure hash:
        checks whether it is contains only hexadecimal chracters,
        measures length to determine if it is MD5, SHA-1, or SHA-256
    PARAMETERS:
        hash
    RETURNS:
        hash_type:  'MD5', 'SHA-1', 'SHA-256' or 'INVALID_HASH'    
    """
    allowed_characters = string.hexdigits

    for _ in hash:
        if _ not in allowed_characters:
            is_valid_checksum = False
            return 'INVALID'

    if len(hash) == 32: # MD5
        hash_type = 'MD5'
    elif len(hash) == 40: # SHA-1
        hash_type = 'SHA-1'
    elif len(hash) == 64: # SHA-256
        hash_type = 'SHA-256'
    else:
        #return [False, 'INVALID']
        return 'INVALID'

    return hash_type

def compare_hash(hash, checksum):
    """Compares hash, returns values 
    PARAMETERS:
        hash:       string
        checksum:   string
    RETURNS:
        boolean
    """
    if hash.lower() == checksum.lower():
        return True
    else:
        return False

def main():
    # Create the Tk root object.
    root = tk.Tk() 

    frm_main = tk.Frame(root)
    root.resizable(False, False)

    # icon
    icon = "AAABAAEAAAAAAAEAIAD3KQAAFgAAAIlQTkcNChoKAAAADUlIRFIAAAEAAAABAAgGAAAAXHKoZgAAKb5JREFUeNrtnXuUXFWd7z+7ujtPSLqbtyFd1VUFhOGiQkICiToMzBIdRdDxiVddVwfGx6iIep2Zte443rl3Zu6MouNVR2VgLXCJL0ZFxBHvgFyHBExIfMRcEujqVHcMECDp7phnP2rfP37nVJ2qru6u16mz96n9WSsr1V3V5+xzav++57d/+7d/W+HoODLJlP/yeu//7wPkRvJRN83RZlTUDXC0l4Dx9+MZPiIEh8CJQKeRiLoBjvYxODAAuqj5bwc2ef9ukF8p0oODUTfT0UacAHQQCZUApQEywAeQ7z8B/Jn8TqMKOupmOtqIE4AOIZv0n+xKAe8HLgi8fQHwPu25B+kB5wV0Ck4AOgSN/2TXVwDvrPKRdyrU5QBKOS+gU+iKugGO8AkE/pYC/wCsq/Kx5cBK4IfAdP/KXsYmxqNuuiNknAfQWVwLvHae919bfN/1jI7AeQAxJ/D0PxP4JyA1z8e7gXOBHwDH+nudFxB3nM7HmPPKp/TeCWyo4c8uB97l/5BNpaK+DEeIOAGIMYXSlN4a4H3UlvilvM+uAdAuHhhrnADElIDr78/zp+v48zSlPIHAFKIjbjgBiD+voJjpVxdv9/42MIXoiBsuCBhDAk//5cBngJc0cJilyHqB+4ApFxCMJ84DiCOqONR/A3BNE0d6FfB6AOW8gFjiBCBmZJIpP3J3DvBhYFETh1sE3Ayco1FBz8IRE5wAxIh0+ZTde4C1LTjsWuDd/g8Zt1owVjgBiBGBFP6LgZtaeOibvGOCWy0YK5wAxISAe94NfAhY3cLDD3jH7JZzJaO+XEeLcAIQP64C3hzCcd/sHRtXSCo+uGnAGBB4+q8APgv8XginWYysJ/gBcNJNC8YD5wFYzrmrVtE9VXwiB57SoXA18CaAGX2CQbdOwHqcAFjO4u4epns0yJi/OE4PiWJ8oUstIeHigdbjBMBisqvLpuRKkfpweTFwU8HrOS4gaDdOACxGlx7Ba5F5/3bx7kSBS+WlCwjajBMAS8kOpPyXi5CMv3PaePoXIRmCi8B5ATbjBMBSSuX9uQbJ+W83bwBeKS+dF2ArTgAsJDDt1wfcgqz6azfLvXP3VbTJYRFOACyjokTXDcDLI2zOK4C3yUtFeqCemiMOE3ACYBmBEl1ppNJPlMlcXcAHpS0apQrR3hxH3TgBsIi052ZrEgp4L17dvohZA7xXe0UIMim3WtAmnABYhCr+X9hAoHKvAbxLoaXisKsiahVOACwhU9qvbwnwESQv3xTO9Nq0BNy0oE04AbCF0vj6NcgOP6Zxrdc23LSgPbjVgBYgU2wK4HTg89RX4rtd9OB2FbIO46T6Sq4s+/lhHo66SZEyMDBAjyo6arcAn8bA781DAx8DbgWN7upieHg46jZFSiqVoru7m66uLhYvXszOnTvRBsVJjOpIG5Zu4IUzD1R5RwMJciN7o25i2wkk2JwP/AjIRN2mBRhChgJPAuRG8lG3p+1kBlJzWlbv6aexffv2qJtYJMylo3Vz5JQj/ss1wCpgF/CcDIB1WbaZ6kowFPOnS5XdfUw3foAssqvQR4BCJpmKvQicd26WQtd0tbe6kADpRcBvgd1Rt7USowRgqmfKf3ku8A3gBWAHsBnYBjyFZhwFeqZAJplCI2Ib8072MmSnHlv4z8C/Aj+LuiFhEex7BcT4FaAlNToLrAc2ApcisZu34gRgfiYXTdIlw6NdiPGv8f7dAIwBQyi2IYLwC2BEwTEoPS0LBUUioa0XhExptd8yZOzfH3Wb6qDfa/PjwLE4eAGZZIpCQZNIlHx779UyIAlcqsXg1yMC0Bv4891InzYOo2IAUDTkLuAu5t7TrgAcAJ4AHvX+7QSeAaaq/YFtHTCTSvpL/m4A7kBq8tnESWQ/gbtRmlx+JOr21EU6mURVN48eZOn1xYjBX47UYDyTuafV7wbeARRM64dGeQCCAvQMsIW5BSCBfAnnIDXwTgL7gV95f/dzRHVfQCKIZfGDGV0gPzoa9YXOiezuA8DZyFjaNuPHa/PNwENo9azpXkA2nUZPF6o9EhXiwq8BNgCbkKpIq6j9e9mMPLSMwzgB0BR85d0KjFPuSs3FYmRuPI3sZXcE2AtsR27+48AwcBigSyW8MZxCYdZwIbt6MLgb738B1kXdpia4TK5B/x0osgODDI2aM5OTSSYldVkl0DNlxr8C6UvrEINfCwwCpzRwmnEkfmXk7orGDQGg+LTuA35CawzgILAH8Qy2AL9EorInZn9UkxuJzl0NeCoXAfcj40ubGUGmBXdBtEOx4r6Jala3X4IUVX0JYvDrgQuA01pw2m1I4ZRxkx40PsZ5AEUUY2i20hoBOA0Zr21Elq8+C/yGUvxgFxJTmKFiE0yNZrhNgpBNpfy1NH71XduNH+8aPoRMDU5nB1IMjebbcuKqRUrE+LuQ4dVFyBh+o/f6bFpvE9sUalwb+fw3VQBK92oLsuy1lWsWupFpxnOR7a+PA/uQWYUtyNDjySOjiUOnDMhwpDgmV6AKXQzty4Vz2aXrvhJ4SygniYa3AN8B/l2H6HNmBger7l24+HfHOXnq0n4kmWo98pR/KfLUXxridReAzaYaPxgqAKqnCz09A5ID8ByizGGxFOkY5yMddQLInTJQ2IYIwnYgj+IogE7MkEmm6D2hGVuiGG69W7cSSaddGeI1txv/mrYh97dlZAaSTPetpHv8cKXxLwdSwNqTpy7dhHiSGdp7Xw8gDxYKRg62DY0BQNF9WwbcR7i73cxHAXgemVF4DBGEXwNPA5OzPq0gl883e81nAdfjVdyto50Z4P2EP2NwEvgSkKM+z+wkcC9woJmxcDqZIkHVgNoiJDIfnJ67EIngR7Xq9SFkleQxE8f/YKgHADL2VqhjiOFFJQAJxCDPAn4fMfqnkZyDLV7bnkBEooAuH3f2TE+xe//+es95APhKA23dANxI+AIwBXwLCaiGzgUvOp/pnnKt9Yw/AZyBGLk/jr8YKVlej3iGyaPAMWOfshgsAIEkjC2I4ZnwpS5C3MoUouxHgTyldOXHkWzFCTRMdfeUCcJCT4FGnxLeOdr5XXY3096Fr2fQS6vVTJc7WiuRLLvLEINfiwQZo6iKvBAnEQEwOAJgsADkRvJ+x96JTNmZuAZ+ORI9vgjJ9DqErFfYigjXL4BRJNCI6ckwJiDfeTFsthQYAC6hlGZ7HnakRe9H+q7R37mxAhDgGWTcbaIAVNKPuOIbkPG4n678U+DLSD6CY2FOQ2Z//gBx8c/CvuI1v0L6rtEYXRJMzRRAxpxbom5LA3Qh49GrkMyyY1E3yCKOIffsKuQe2mb8IH12ioTJEQDDBUB3FZv3GJLeaxvTwN+D+iTeMMBRE8e9e/b3wHSzB4uAI/hB0oLJEQDDBSAwdtqN5PbbxDTwj6D+O+gTAKrHhhFXtJTukT4h945/xD4R2Iu39t/k8T8YLgAl9AtIQo4tVDX+oaGhqNtlPENDQ3EQge3ISlTjsUQAlEam2WzAGX+TxEAENiN7pUXdjgUxXgACedSPY34U3Rl/i7BYBA4ifRUKRpYAKMN4AQisxBvGqzRrKM74W4ylIrAH6avkRs2vgmS8AAQ4TJvSTxvAGX9IWCgCW/EKz9iATQIAMrdq2hc/iTP+UJlHBCabOGwYTGNPrAqwRQBK+QC/RIp5mMQ9oD7ljD9cqojAp4B7om5XBc8ifZQZC8b/YIkA5EobgOzDvPLK60FvAkApv46BIwT09EygnJf2S3eZxG+QdSvk95lbdDaIFQIAoERRT+CtsDKILHAbcLVf0ieTGmzqgI7ZFO+p3OOrkXuejbpdFTwKnNDK7Oy/INYIgC7lVD+KeWm1aeCrOBEIhSrG/1XMWxx2HO/hpMKse9ZirBGAQKXeXchQwDScCISAJcYPgeGp6em/QawRgADFQIuBOBFoIRYZP0jthwNNH6XNWCUAnmM1g9lTLU4EWoBlxg8yRW1dBNgqAQiEVrbS4uqyLcaJQBNYaPwTSJ80u/5XFawSgMDY6kmkKq3JOBFoAAuNH6QvPgmQa9OmJ63CKgHw6RqbPIS/4MJsnAjUgaXGD/D4kaO/OxR1IxrBSgGY6VsEBu+4WoETgRqw2PgLwOZTlp8adTsawj4BKI2xdmBJ0QVKInCVE4HZVBj/Vdhj/CB7QkixGsvG/2ChAATGWHuRiru2kEay15wIBKhi/Ldhj/GDlP7Kg33jf7BQAAIcRYqF2oQTgQAxMH6QPng06kY0is0CAKVdg2zCiQCxMf5J7CxZX8ROASitC9iJ7NVnG74IdGRgcI6FPbYZP0jf+zXItvE2YqUA5PYWK4QXt1+ykI6cHbA42l+N4gNoaJ/paSnVsVIAAI6eqcB+F6yjRCBmxg/eEHTFpGlFqmrHWgFYfqA452J1EIYOEYEYGn8xCD2xyN4NX6wVgMCUyxNAPeVXJ4G7AZPqdsVaBCww/iGkT9QTUM7jTUMPW7T8txJrBSBAKRFjYaaBz4B6N/CneOWbDSGWImCB8Q8Df+r1ic9Qe9HZHUjfsxqrBcCbCyhQWxwgWLr7JPAQcBNOBELDEuO/CXhI+kRdJcdtSUWfF6sFIHD3twHzLcaYVbffKy75IE4EQsEi438wUGi01n0HSovR7Kn+VRWrBSAw9hoCnprjY3Pv0mu+CFiZLGRBbv8s469z85Gn8GJIuXw+6mtpCqsFIECpIEM5c+7Yk8t7uQRmi4B1GYMWZPjNMv5cfm+9OxBtBWVyQZqaiYsAwOySTAtu1+VEoLXYavw+NYrADLDFyqV/VbBeALqnFvkvg0UZa96rz4lAa7Dd+H1qEIEDSF+jZ3oq6mtqGusFYM/TxQ2DR5F5WU2de/U5EWiOuBi/zzwioJE+Ngqwe//+qK+raawXAAAlodjjwE9pcKNOi0TAqNkBCxb21GX8PvOIwE+B48r28L9HLK4ikxzEG5OdBhzD2zmokY06rZy+krZuAn4MnBLy+Y8ArwI2V5zfintVi/EHyWaz6KliCGApsAw4CHZtADIXsfAAciPFL/UgTRg/VPUEbsQ8T6AsTyBSzDb+G2nC+KHSE+A4MTJ+iIkHEAZWjWuF9nsAgsnG/1Azxt8JxMIDCIMKT+AhTPYESrRD0IPncMZvOc4DWABLPIEbgd8B30Q8gLDGBgrxAN4KnGrwvXDGXyNOAGrAgsDgN4APAGcQvldXQFbBfRF4W9QXHqDpgF8n4gSgRgwWgUeQjt/uEukXevfgZVHfAJzxN4wTgDowUAQ2A+8B9qA1JBKhd/xMahAKBT82cgFwOxKAjApn/E1gZynTiBgbH6e/t8/v/HuBXcgTsC+C5rTd+Iv3oK9fRFCpg147LgEGIrgHzvibxDoPIJtMzYpwtXtO1gBPIBLjn3UPovUEIjf+TDJV9rPSMGTZ7kDWeADZ1YP09fUGf7US6AWOjk2Mt7UtEXsCkRt/8R5E5wlEbvwA/b29AGcB3cBJlPzutBV9HDo83vb2NIIVeQCZZAqdKD73u4E/BL4FXB9VmyJaO2CE8Zfdg0TC94T2eG3b3NxRF8QI4w9wPdIX/xDpm+iEnuUdmIrRApBNpkinUsFfXYRMP90DXAMsauCwLaPNImCU8Zfdg/aJgGnGD9IHr0H65BeRPgpAOpUiM5CKun3zYqQApJMpeeoj4yrgbOAvgPuRDrAy6jb6tGntgJHGX3YPwheBluT2h8hKpG/ej/TVs5UGlHiwpnoERglAKiU3KhCZXAbcAPwA+FsgGXUbqxFy2rDRxl92D8ITAZsy/JJIX70P6bvL/DcyyRSpco82cowRgEwyRVcpvJ8AXoFs1nAHcFnU7VuIkETACuMvuwetFwGbjD/IOqTv3g28AiW21qUxyhuIXAAyA0lvPX+R84HPAd8DrgMWR93GWmmxCFhl/GX3oHUiYKvx+yxG+vD30HwO6dsAZJJJMgPRF3SJTACK4yKl8NaunA7cAvwI+CDQH/XNaYQWiYCVxl92D5oXAduNP0g/0qd/hPTx00GBktmCdIQeQdsFID2QrnSBlgB/DNwLfBrIRHY3WkQVEahndsBq4y+7B42LQGnHHvuNP0gG6eP3In1+CUg2XiaZIhtBfKCtApBJplBK9vPR8s1eDtwJfA3YiIWZiXPR4BRhLIy/7B7ULwImTvW1EoX09a8hff9yzxYo6PbnD7RFAKpMg6QV+n8hSvhmpNZa7KhTBGJl/GX3oHYRiLvxB1mK9P17PVtI+4VGM8kU2TblD4SaCpxOJiVltkQf0gH+CQmOLG/yFP8GbG13KnA91Jg2HEvjL7sHC6cNW2f8XirwBuDVTRxmObKG4hrv5yHgRLvSikPxAAaL8/lFj34RcC3wXcT414R2RQaygCfwCDE2/rJ7MNsTeMR72zrjD4E1iG18F7GVRVBKKz531apQTtryMXcmmURPnUT1LKGQ0CQK6lLgZuANNP/Er+TPkPRLG7kK+BPgb4An4mz8QSpWEV4I/DfgX5BgqY18APhCi495FBGCzynYoYGe6S6mumdavvK1ZQKQSSYrD7caUfV3Ay9q8Q3y+SyyEKO72QNFwCTi7o11ivH7VIhAH5Al4nUdDTINvAX4SEjHfwZZZv1VYF/wjVYJQdMCkBkchELZCv0VwJuADwEvDunG+JwEbNygTSF7zL0aeBKlOsb4fTKpQX84cD4SyzkLO3fc7CH8ZLWdwOeBbwOH/V9qYLhJIWhKACoi+92IW3sLUiTDxqdyO3kO+H1gd1w2magXr/+sAf4vcGbU7TGcaSR+dCsyXCpuV9RM/2nISP0FOwG5vhh54r8Z8QAcC2Pj0y4s3L1YmG5kpuAKxBP4POIZkE1l0Hqa3MhIQwetmWxqEO1tR+V9Y+cgY/ybiKYmnMPRaaxAgsevRPZluF3rmWdAFT3yejyCmgQgm0yiUUXjR6L5r0ei+2ujviMORwcygMwgXU9p+vAoiIeeSCie2rtwXGnBPAApzKGCn78S2YjidpzxOxxRsxaZRv0GYpsJgEKhtrTiOT2AKn+8BpnzfDvRlMF2OBzV8RPtXobUH/gCsBtYcFgwSwCC43yPM4B3Ae/DjJ1wHA5HdfqQh/SrgX8G7kJmmzwhUORGyocFRQHIDg6iCzpo/EuB1yJJDpcTo5V6DkfMSQP/gCw5/ixSnuw4aG9Irxn2ZgwSIOpQKPjRfe0vV7zL+3cFzvgdDtsILre/i8ByexWYMej2X3gWnlGo9wHvRFx/h8NhN0uANyJJZ18DvgTkwJst8D7UjyysuR/4KM74HY64cQaSpXs/gZJ73cg84i3ImuTIi4Q6HI5QuQApuvsm4FZn8A5HB5MAvo94ATcjhRocDkd82QN8GLH57/sewCHgfwOvQVYbPR91Kx0OR0t5HvgMYuNfQGyeRDFDSGYBc8DHEHW4BzgRdasdDkdTnEBs+Trg43gzACDZgQn/xUwpAUgDW5CpwHcBj+GWazoctqGBRxE7fqf3WssbqpgaXMwEzO+TzCDZpksDHEfWHT/sHcClAjscdjCMpALfSWA4r7VieHSOVGAfP1e4uD235BJ/GvghkitwA24xkMNhImPA15FCubuLv9WQG81X/YM5VwP6LkJgVeBupOrPPUjewDXYWcjR4Ygbk8CPgc8q+JmGgv/GQsVBFswDyI3kSSSKSwEKyJDgbUhVku1RX7nD0eFsR/ZYuAF42Dd+pWqrDFRTRSC/skjAGziK5BX/u3fyG3ElwRyOdjKKlAu/Aykf7jF7ye981FUTsDQsSKJUN1KLTP8PUPfiioI6HO3gMBVFQRW6LLJfDw1VBfarj/pFBryGvA/4Dq4seK24JdYl3L1YmDnLgg81UA3Yp+kbn/ZKhAdYgXgCH0LKhYeJ2xjEUtzGIHXxa+SJ/x0CG4OQUORqKPw5Hy3cGixV+St/a7D3IOXDw8BtDWYhbmuwmnkaGeObuzVYJZlkCqZ7oHsKpQtolXCbg1bHbQ7qNgedi+LmoFqpHUprZhIn6CosafnmoC1/cuZG8py7ahWL6UGrBMAOpKP78YGXA10tOl0xldl0MqlBeSFu79WIqqcRT+lPUGoPhQKZ1GBsRaDC+C/w7sHLgA1YuD245/W2ckn9DPAzZJz/E2BSeSn6Srfe+Fvd+CK/3b+f3EgepYsOxiRSmPANyFLE3Y0e20bmMX4QA7gduACl8EUgblQx/tu9a8e7F18FrvbuUSzvwQL4iXZ/jGTdTsqvNbmRPHvz+VBO2qoncVUOTYwzNjFO/8pef7BxAtiGBH0mgfNobljwb8DWsYnxMC+jKRYwfp8B4BJgM0odRGv6+/oZGzf3uuq+B7ONf1PFx/oQQdgF7EUp+nv7jL4H/b29IN7Lq5s4zHNInb5bkKe+twJXkxsZYWxiItRraEtFoNxovui+aAn0DmvUJ5Alit9GFh7FjhqN32cTMfQEajR+n07yBPzFdtdprT4BDPtPydxIvqGNPhuhrSXBciN5uhJySiXf8GPIkuN3IEuQbZwGqkqdxu8TKxGo0/h94i4C/nL7d+Att1feQF/rxpJ5mqHtNQGf2ruX3Eg+aOkngH9FvIGPEShYYCsVxn8VtRm/TyxEoEHj9/FF4KqYicAQ0sevQ/q8uPtKDH94dLjtDQo1BjAfY358QMZRAMeQogU/9n4+D9mdaD6MiwFUMf7bqL+OgtUxgSaN36cPmTH6DYbGBOqIARxC+sHNSIDvmPzaG+dHeE2RVwWW8U4++KsnUdyMbD9+L5LtZwUtMn4fKz2BFhm/Txq5h7Z6AieRPvx6JFnoyWLtvTaO8+cjcgHwyY3kmfFnDTUFZD70BuDdwONRt28hWmz8PlaJQIuN38dWEdiG9N0bkL5cANBdXUblrRgjAAD5/Cxv4Biy3fG1wF8C0UtmFUIyfh8rRCAk4/exSQRGkL76OqTvHvPfyI3kGR5u/zh/PiKLAczHWCB/QCdAwRHgEeD/INmLWWTPs8hjAFWi/a00fh+jYwIhG7+PHxMwJk+gIgYwgWzC+WEkjfeIl9RIbiSPSXGqIEYKgM/YxDhj42WBwueRIOFWZPXYLmB7VDe3wam+RjFSBNpk/D5GJQt5/fKlyEKmm5GEngP++yYbvo8167CzqwfRibI0gZWIF3AgijFVm40/yGZkheWeqBcQtdn4gwxjwNoBby3AWch0XjFlT2nF0Kj5axnAcA8gyKHDMiw4reQNnERWTbVdZSM0fjDEE4jQ+MEQT8DzAI7izVQprciN5jlk+FM/iDUegClEbPxBIvMEIjb+IEZ4AjZjjQdgAgYZP0TkCRhk/GCIJ2AzzgOoEcOMP8gjyFPwiTaf90JK6/mjxnkCDeIEoAYMNn6fbyCVac4g/NyOAjIb80VkfwhTcCLQAE4AFiDkJJ9WMIzsy/A74JvAKYS3qlIhORlvBU41+F485ESgNpwAzIMlxi9PPRmHP0Dr6y5WchTZFm4zZnpDTgTqwKhUYJOwzPh92lFPIXiOB702mJTfalPacOTExgOoLEuueroZGhpq7Fg2Gb9Sfjs3IVmSp4R87iPAq5DZB5PjIi3zBLLZLHpquux3Ji3oaYZYeACZZFHhT8OrIaCnpslms/Ufqz25/c0wK9gVKdIGkz2BpioLVRj/UqSPVdsHw0piIQABM3gv8NeglkD9ImBBtN+oSHfx3GaLQMPlxcqNXy0B/hrpY6iYOM+xEACv0OhS4A+Aj4P+q3pFwBLjvxFDjN+nigjcSAxEYLbx678CPo70saU6JuUrrReANatW+S8HkOQURZ0iYJHxGxnZrhCBh7BcBOYxfoX0sQEo63vWYr0ATHX3+C8vQVZmgdQMqEkEnPG3hriIwDzG7++idRbS14J9z1qsFwDADwJspHxtw4Ii4Iy/tdguAjUYP0gf22hEALYFxEMANCuB9VXemVMEnPGHg60iUKPx+6xH65VRX0grsFoA0iX1ziJlxKtRVQQA043/Jiwzfp8qImD87EAdxg/S17JQ1getxGoBULrgv1wH9M/z0VkiYIHxGxXtrxcbpwhrNH6QvrYOQGm7ZwOsFgBv8J+gtvXoQRFYTP079rSDWBi/j0UicJX0iZqM32cT1ttPDC4AWQJ7aY2f7QY+CvoO4Cs44w8dS0TgK16f+Ci1GT9Inzsj6sY3i7UCkC6lYl4IpOr400XIZg315wmHRyyN38cCEcgifWJRHX+TQvoemWQy6vY3jLUCsHKymJ99OeEvgQ2TWBu/jwUiUC/Lkb4HS1ZE3ZaGsVYADi/qBlHsjVG3pQk6wvh9YigCG4FFnPhd1O1oGCsFILs64798EXBx1O1pkI4yfp+YicDFSB8kmzYpnFQ7VgqATsz4L1+M9wVYhpELe9qFBQuIauVFSB9ETxeaPFQ0WCkAAcQFswsrM/xajQUZg7Vg+xDUagEoBWHswRl/gJiIgAShLV0aYJ0ApEtTLilgTdTtqQNn/FWIgQgUp6HTFk4HWicAgUosa7EnEcPq3P6wsWDtwHycjvRFK6sEWScAAEdGzgAZe9nQ/o6M9teLxbMDCWDTzJLjUbej4cZbxynJ5/uBy6JuRw04468Di0VgXdeJpf3NH6b9WCUAgZTL84FME4dqB874G8BSEcggfZJMKhV1W+rCKgEI1P9dD5hckMEZfxNYKAKlgjSWrQ62TAAAvySTuTjjbwEWisAmykvSWYGNAlAsymggzvhbiGUi8FLg7KgbUS/WCEBgJ5aLgNVRt6cKzvhDwCIRWI30Tat2DbJGAHRp/H8F3vZfBuGMP0QsEYGleJmpBYvSAawRACXRlSWIAJjEEB28sKddzLGAqLHdX8NjI7AkYVEg0AoBSA0M+C/PBf5T1O2pYCuozQBojeq2Lg5kDaq7i0ABz83A1qjbVEFxeHreatNnqQUrBKBLFZv5UswLtLwR9Ccb3ZDUURtV6vZ/Enhj1O2q4GzgJQCF0pJ1o7FCAAJspPaije1iEQ1uSOqojXk27TBtKXg3tVWoNgabBGAFsCHqRsxBzXsROuqjzh17TGA90letwHgBCEyppIELom7PPDgRaDEWGj9IH00DZAZSUbdlQYwXgADrgNOibsQCOBFoEZYaP0gfXSfNjropC2OLACjsGVs5EWgSi43fZ5O2wvztEYBi0QVLcCLQIDEwfoC1Svqs8RgtAIHx/xrAtm1Y596V2DEnMTB+kL66BiCTNLvbGi0A6KIXtQE4JermNEA38OegP4V56csms9S7Z3+OfcYP0lc3AKgus8uFmy0ASgP0YPby37mYAZ5GatwdBpZF3SCLWIbcs4eQe2hHVk05m4AePWN2KMAGdT0HL7vKAg4BTyEpqluAXwCjgJ0F46LjIPA/gVuBAWT590Zkjv08wIbyWy9G+u5o1A2ZD2MFIDD+vxhYFXV75uAokAd2AJuBx4EhlJoo5axLtViNJjeSj7q9xpMbyZNJplBaoZU+DuyRf+qboFciO/muQ56wlyIluU3cHHYV0ndHM8mUsd+9sQKg0X6Z5SuAxVG3x2MScUl3Ik/4x4AngOeB0mDPM/6e6Sl2799f88GbXEfezgjjdDPtXcgYgu+vWbWKqe4evFpbE8B2799tSFn4C5FluBsp7dVnQorwYq9N90fdkPkwVgA8419GtMt/C8ALiJE/hhj9rxERmKz8sFaK4eaXAp8FXE99nbiAFKbsacM96QHegjyF64khnQTuBQ7Uc7JKAc2kUn7dvYJ3rAPAw9798vfq24iIwhpEJKKKdV2O9OFjEZ1/QYyMUGTTafRMAUTdH0TGUu1iAsgh7vxm5GmTR9z9Ij3LVjJ1bJzcyEjLTuw9UVcC3wKuaeM1t4MHEOGYaKU7nE6m6J2cZmLRrGfZcmR4sBYZLqxDRLKdxWSfBa4CnuiemWHPb/e18dS1YaQH4Bk/SPDnrJBPdxzYB/wSMfitwJOT0wcPLeoOZB77Q/ruBLnhUIvRTACfRp4eJlc+buSaJlp94OGAmGRXZ4I7Rx8FdgG7ciNX35VJPtiPlO5ej3gIlyBr98Ocnj3TO88T011m1okwUgAAMTjFJlrvvk0jyryL0jh+l/e7Yu/xjV+jGW7hU34+FEWdeRjxAm5qy4nD51veNaF0eE7n0L5c2c/pgRRKQSb5IMgMzWPevy8iD5aLkCHmFUihmbNprU0kgE0o7ja1XLiRQwDPFe4FfkJrdgA6iESTtyJP+V8hT/0T5R8T1YkyYltR/PR+wL4dJ8sZAV6DiGy093YgNVePX4JUm3opMlxYj6zqa8Xis8eBVwJjJs4EGCcAkjqpQQz/AaCvgcMcAfYi43d/em4YSS4JEL3BV5JdPYguFZX7C+Bvo25Tk/wl8HcgT/+hUXPqJWaSKbTS1bySFciSXn+6cS2S3ttINuo4IgDbtIbh0XzUl12GgQKQ9Jv1fsRVq4WTwH4kQr8Z+DmwG4ngz3K+VFeCoXDH8U3eg5T/8mzgB9ixD2I1tgGvQ4ZXRgltJanVA3Qlqo42FbKwZw2S3rsRSUxbRe3T0x8AvqSAIcPugYExAAX+2GluCsBzwP+jND23E3gGmJr1aQ05w5R3PnIjedKpFErzLPA54A7MyYWolZNe25/VCobz+ajbMy/5feUJe5mBJCQSoLVG8jyeB/4DmQY9B8k58Kcbfw8J+M0Vr9oEfEUbmNJslAdwJVeyL5kHefL9FG9Flcc4UgbaT7PdgYwvy+dYCxoSCXIj5riajZBNpnzXZRlwN3Bd1G2qk3uBG4BjJj756iWTTEFXAmZmLe5ZhsRpLkEM/TIkXbk38JndyHTgM6qnm6Ehc6qZG+gBABIAOx25cTsQg98KDIEeC+qWjOLNdi8bYchLiUUE7lbg5diRAw8Scb/Va7v1xg+z+1cmmfJnbY4hiWJPIELdiwjAZZTSlU9HvIRnek62I1erdkwVgP3A25DI8XOUuU5i/ImZbp76rTlKGga+uAGPAF8HPhh1m2rk616bTZ39apqgIAymUgQ2AxlHYh/bgC8jQ4OLkD5Nz6RZAmDqEGA2lo3jW0UgIHg+8CMkm81kcsAfAU9C/DyzWkgnUySoLn5nPncOjx5/NOomFjEqPSlPnvMnL6CgZC/A6e4Z9o7kGZsYZ2xiPOrmRcLKvl4/snQQ8dheiWHCHUAjy3h/CDCjYHx8POo2tZ2xiXEOeX02nc2wfOZUTp1cwcqDfWw+vjnq5pVhakdyBAh4AacjwTVTC6RsQYKVL0BnPv1twygPwFGdsYlx+nv7QAJOE8C1tGflXz0cB/4rsN205CrH3JhdEswRoDj9dD9wX9StqcJ9+Gvftdl18BwlnABYQmDZ8Qngs8jsiCk857XpBEButD2LpxzN4wTAQjTq58CdUbcjwJ1K2hTbab+44gTAIvxxtZKaY19GEqWiZjfwZe3VQRt2Y3+rcAJgGVoXv7Jh4AtEm18+47VhGDSJhJtUsg0nAJYxPFq2ivFuZIFKVPyH1wZA8dReu9dfdCJOACwkMMU2huTcH234YI1z1Dv3WEWbHBbhBMB+HgC+G8F5v+ud20X+LMYJgKUEnriTyLr7p9t4+me8c05CZ67RiAtOACxG+wXyE3oHUjSkXdyO1jsg3CKfjvBx357lBNYJrEYW4bw45FPuRIp87gM39rcd5wFYTkGBnjoBYpCfJ9wtwqa9c+xjOsFUwbgKV446cQJgOXvzeVRPsVzgd5CdlMLiQeDbAHQXGN1n3k43jvpwAhADAusEDiNTc4cbP9qclB3buf7xwAlAbCjOxT2E/5RuLd/2jh3c+dxhOU4AYkLAC/DH6aONH20WowTiC6ZtbuFoHCcAcaKUi78T+GoLj3ybd0yX8xMznADEiFx5Lv4dyNZozbIduN3/wa32ixdOAGJGbiTvJ3eUZes1iJ9l+IxSXS7wF0OcAMSQgJv+Pfx8/cZ4wDsGWoeZXuCICicAMSTwpC5bsVcnZSsNA0FGR4xwAhBTlCoGBH+G7NRTL3d7f+uIMU4AYspQvhgQLCDbrNezH7pfbagALuknzjgBiDElJ4DdwD9T2yye9j67G6BQcOvF4owTgBgzlM8Hf7wTeKyGPyurOLx3nyvzFWfczkAxR3YV6gXZVegwsqvQXLtCnwA+AWzTaIZd4C/2OA+gs/ih92++9+8DSLiu0RE4D6ADCHgB08g+9a8Dlld87HngZmAvuMBfp+BkvkPwpwU1+lHgriof+RrgbVzvAn+dghOADsGfFlQoP8q/J/D2HuBLeLMEuREX+OsUnAB0ECqh/HnAHKV5fj9PIAcwU3Dr/ToJ5+t1GIEiov3A973X1wOHwI39Ow0XBOwwAgHB40i+/6PAL8AZfyfy/wGiFTVRiqNIvQAAAABJRU5ErkJggg=="

    icondata= base64.b64decode(icon)
    
    # The temp file is icon.ico
    tempFile= "icon.ico"
    iconfile= open(tempFile,"wb")

    # Extract the icon
    iconfile.write(icondata)
    iconfile.close()
    root.iconbitmap(tempFile)

    # delete tempFile
    os.remove(tempFile)

    frm_main.master.title("Entropy Hashgen")
    frm_main.pack(padx=15, pady=15, fill=tk.BOTH, expand=1)
    
    populate_main_window(frm_main)

    
    root.mainloop()

#def decode_base64()


if __name__ == "__main__":
    main()