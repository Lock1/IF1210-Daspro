############################## Informasi Modul ##############################
# Modul __init__ digunakan ketika program utama mengimport package,
# Package akan berfungsi sebagai modul dengan membaca dan melaksanakan __init__
# terlebih dahulu ketika importing

def notExistPrint(module):
    print("Module {} tidak ada.".format(module))

from package.base import *

try:
    from package.load import *
except ModuleNotFoundError:
    notExistPrint("load")

try:
    from package.login import *
except ModuleNotFoundError:
    notExistPrint("login")

try:
    from package.cariwahana import *
except ModuleNotFoundError:
    notExistPrint("cariwahana")

try:
    from package.usetiket import *
except ModuleNotFoundError:
    notExistPrint("usetiket")

try:
    from package.addwahana import *
except ModuleNotFoundError:
    notExistPrint("addwahana")

try:
    from package.kehilangan import *
except ModuleNotFoundError:
    notExistPrint("kehilangan")

try:
    from package.bestwahana import *
except ModuleNotFoundError:
    notExistPrint("bestwahana")

try:
    from package.upgradegold import *
except ModuleNotFoundError:
    notExistPrint("upgradegold")

try:
    from package.signup import *
except ModuleNotFoundError:
    notExistPrint("signup")
