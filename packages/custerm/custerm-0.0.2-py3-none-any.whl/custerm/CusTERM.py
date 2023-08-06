import tkinter as tk
import re

def fetchroot():
    return root

def show():
    global root, frame, oFrame, canvas
    root = tk.Tk()
    root.title("CusTERM")
    root.geometry("1000x500")

    root.configure(bg='#111111')
    try:
        root.iconbitmap("winicon.ico")
    except:
        pass
    root.resizable(0, 0)
    oFrame = tk.Frame(root,height=500,width=1000,highlightthickness=0)
    oFrame.pack()
    canvas = tk.Canvas(oFrame,height=500,width=1000,highlightthickness=0)
    frame = tk.Frame(canvas,height=500,width=1000,highlightthickness=0)
    canvas.pack(side="left")
    canvas.create_window((0,0),window=frame,anchor='nw')
    canvas.configure(bg='#111111')
    oFrame.configure(bg='#111111')
    frame.configure(bg='#111111')

    root.bind('<Return>', exeline)
    nl()

def hide():
    root.destroy()

def widget(master,width=1000,height=500):
    global root, frame, oFrame, canvas
    root = tk.Frame(master,height=height,width=width)
    root.configure(bg='#111111')
    oFrame = tk.Frame(root,height=height,width=width,highlightthickness=0)
    oFrame.pack()
    canvas = tk.Canvas(oFrame,height=height,width=width,highlightthickness=0)
    frame = tk.Frame(canvas,height=height,width=width,highlightthickness=0)
    canvas.pack(side="left")
    canvas.create_window((0,0),window=frame,anchor='nw')
    canvas.configure(bg='#111111')
    oFrame.configure(bg='#111111')
    frame.configure(bg='#111111')

    master.bind('<Return>', exeline)
    nl()

    return root

cmds = {}

# EXAMPLE
# regcmd("help",helpcmd)
def regcmd(command,callback):
    cmds[command] = callback

# EXAMPLE    
# log("Help: command1 - do a thing \n command2 - do another \n help - this command")
def log(content,style="normal",size=24,font="Source Code Pro",fg="#11ff11",bg="#111111"):
    fontref = (font, size, style)
    res = tk.Label(frame,text=content,fg=fg,bg=bg,font=fontref,anchor="w")
    res.pack(fill="both")

# EXAMPLE
# error("Error","This is an error")
def error(type,message):
    log(type+": "+message,style="italic",fg="#ff8381",bg="#2c0100")

# EXAMPLE
# warn("This is a warning")
def warn(message):
    log(message,style="italic",fg="#f9ad3d",bg="#342b05")

# EXAMPLE
# assertion(0==1,"This is a test assertion")
def assertion(condition,message,hard=False):
    if not condition:
        error("Assertion failed",message)
        if hard:
            raise AssertionError(message)
    return condition

def chk(sv):
    txt = sv.get().replace(">","")
    sv.set(">"+txt)
    line.focus()
    line.icursor("end")
    canvas.configure(scrollregion=canvas.bbox('all'))
    canvas.update_idletasks()
    canvas.yview_moveto("1.0")

def nl():
    global sv
    global line
    try:
        line.configure(state="disabled")
    except:
        pass
    sv = tk.StringVar()
    sv.trace("w", lambda name, index, mode, sv=sv: chk(sv))
    line = tk.Entry(frame,textvariable=sv,fg='#11ff11',bg="#111111",font=scpron,width=1000)
    line.pack(fill="both")
    line.configure(state="normal")
    chk(sv)

def exeline(dummy):
    txt = sv.get().replace(">","")
    for i in cmds.keys():
        match = re.search("^"+i+" ",txt)
        if txt in cmds:
            if not assertion(cmds[txt].__code__.co_argcount == 0, "The command takes an argument."):
                return
            cmds[txt]()
            break
        elif match is None:
            pass
        else:
            inp = match.string.replace(i+" ","")
            if not assertion(cmds[txt.replace(" "+inp,"")].__code__.co_argcount == 1, "The command takes 1 argument and 1 argument only."):
                return
            cmds[txt.replace(" "+inp,"")](inp)
            break
    nl()


scpron = ("Source Code Pro", 24, "normal")
scprob = ("Source Code Pro", 24, "bold")
scproi = ("Source Code Pro", 24, "italic")

if __name__ == "__main__":
    show()
    root.mainloop()
