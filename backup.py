import shutil
import datetime
import os

def backup_files(source,destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination,f"backup_{today}.tar.gz")
    shutil.make_archieve(backup_file_name,'gztar',source)

source = r"C:\Users\VISHAL\Desktop\Python_practice"      
destination = r"C:\Users\VISHAL\Desktop\Python_practice\backups"
backup_files(source,destination)