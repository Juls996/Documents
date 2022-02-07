import os
import shutil

patha = "C:\\Users\\taskin\\Desktop\\TestDev\\5.2"
phatb = "C:\\Users\\taskin\\Desktop\\TestDev\\"


def look_for_folder_in_patches():
    patch_folder = ""
    install_folder = "C:\\"
    filename = "jiveXRVViewer.jar"
    new_version = "5.3.0.9"


    # Patch-mtime auslesen
    full_patch_path = patch_folder + new_version + "\\"
    patch_mtime = os.path.getmtime(full_patch_path + filename)


    if not os.path.exists(install_folder + new_version):
        os.mkdir(install_folder + new_version)





print("Datei vom", jxA)

    previous_version = new_version.split(".")
    previous_version[2] = str(int(previous_version[2]) - 1)
    previous_version = ".".join(previous_version)

    # und mtime auslesen
    previous_patch_mtime = os.path.getmtime(install_folder + previous_version + "\\" + filename)

    # variable setzen, die angibt, ob die mtime der patchdatei größer ist (die datei ist also jünger (neu erstellt))
    patch_is_new = previous_patch_mtime < patch_mtime

    if patch_is_new:
        print(shutil.copy(full_patch_path + filename, install_folder + new_version + "\\"))


look_for_folder_in_patches()
