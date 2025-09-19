import os
import shutil
import datetime

def backup_files (source,destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination,f"backup_{today}")
    shutil.make_archive(backup_file_name,'gztar',source)
source = "/home/shubhi_11/devops/shubhi-devops/python-for-devops"
destination = "/home/shubhi_11/devops/shubhi-devops/python-for-devops/backups"
backup_files(source,destination)