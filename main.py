from lib_used import *

#trouve le répertoire /home de l'utilisateur
dirusr = os.path.expanduser('~')

#def qui cherche un fichier dans tout les dossiers et sous dossier du repertoire /home de l'utilisateur
#prend en argument le nom du fichier et l'extention
def search(nom,ext):
    files = glob.glob(dirusr + '*/**/'+ nom +'.'+ ext, recursive = True)
    for file in files:
        print(file)


#nom = str(input('Nom du fichier (mettre ''*'' si nom inconnu ou au début/fin si partiellement connu) : '))
#ext = str(input('Extention du ficher (mettre ''*'' si inconnu) :'))
#search(nom,ext)

class MyWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("File Finder")
        self.setWindowIcon(QIcon("icons/file.png"))
        #largeur de la fenetre
        self.resize(300, 150)

        # Le type QWidget reprÃ©sente un conteneur de widgets (et il est lui-mÃªme un widget).
        # On crÃ©e une instance que l'on va mettre a centre de la fenÃªtre.
        centralArea = QWidget()
        # On injecte ce widget en tant que zone centrale.
        self.setCentralWidget(centralArea)
        #position par rapport a gauche, position verticale, taille de la case en longeur, taille de la case en horizontale
        label = QLabel("Nom du fichier : ", centralArea)
        label.setGeometry(10, 10, 100, 30)
        self.filetxt = QLineEdit("", centralArea)
        self.filetxt.setGeometry(160, 10, 120, 30)


        label = QLabel("Extention : ", centralArea)
        label.setGeometry(10, 50, 135, 30)
        self.exttxt = QLineEdit("", centralArea)
        self.exttxt.setGeometry(160, 50, 50, 30)



        button = QPushButton("Fermer",centralArea)
        button.setGeometry(10, 100, 60, 30)
        button.clicked.connect(self.bouton_fermer)

        button2 = QPushButton("Chercher",centralArea)
        button2.setGeometry(150, 100, 80, 30)
        button2.clicked.connect(self.bouton_chercher)
    def bouton_fermer(self):
        sys.exit()

    def bouton_chercher(self):
        file = self.filetxt.text()
        ext = self.exttxt.text()

        search(file,ext)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec())