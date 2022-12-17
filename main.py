from lib_used import *

#trouve le répertoire /home de l'utilisateur
dirusr = os.path.expanduser('~')

#def qui cherche un fichier dans tout les dossiers et sous dossier du repertoire /home de l'utilisateur
#prend en argument le nom du fichier et l'extention
def search(nom,ext):
    files = glob.glob(dirusr + '*/**/'+ nom +'.'+ ext, recursive = True)
    for file in files:
        print(file)


nom = str(input('Nom du fichier (mettre ''*'' si nom inconnu ou au début/fin si partiellement connu) : '))
ext = str(input('Extention du ficher (mettre ''*'' si inconnu) :'))
search(nom,ext)

'''
class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Calculateur de masque de sous-rÃ©seaux")
        self.setWindowIcon(QIcon("icons/file.png"))
        # largeur de la fenetre
        self.resize(300, 220)
        self.execute()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec())'''