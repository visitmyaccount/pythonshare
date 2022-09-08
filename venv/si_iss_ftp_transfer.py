import os
import sys
import yaml
import argparse
import logging
import paramiko

from datetime import datetime as dt

log = logging.getLogger()

def rename_incoming_files(incoming_folder):
    input_files = os.listdir(incoming_folder)
    for filename in input_files:
        original_filename = os.path.join(incoming_folder, filename)
        file_data = dt.fromtimestamp(os.path.getctime(original_filename)).strftime("%Y-%m-%d")
        new_filename = os.path.join(incoming_folder, file_data+ " - ") + filename.lower())
        if len(new_filename) >= 255:
            renamed_newfile = new_filename.split(' - ')
            new_filename = renamed_newfile[0] + ' - ' + renamed_newfile[-1]
        log.info("File {0} has been renamed {1}".format(original_filename, new_filename))
        os.rename(original_filename, new_filename)


def copy_from_iss_ftp(sftp_host, sftp_user, sftp_pass, input_folder, cleanup):
    log.info("Copying from ftp host{0} with user{1}".format(sftp_host, sftp_user))

    if not os.path.isdir(input_folder):
        log.info("INPUT Folder {0} doesn't exist creating it now".format(input_folder ))
        os.makedir(input_folder)

    transport = paramiko.Transport((sftp_host, 22))
    transport.connect(None, sftp_user, sftp_pass)

    sftp = paramiko.SFTPClient.from_transport(transport)

    log.info("Copy from reports dir")
    sftp.chdir("reports")
    log.info("current working directory:" + sftp.getcwd())
    if not sftp.listdir():
        msg = "No Post or Pre Meeting files to process please contact the ISS team"
        log.error(msg)
        raise RuntimeError(msg)

    for reports_file in sftp.listdir():
        incoming_filename = os.path.join(input_folder, reports_file)
        log.info("Copying file from :{0}/reports/{1} to:{2}".format(sftp_host, reports_file, incoming_filename))
        sftp.get(reports_file, incoming_filename)


    sftp.chdir("..")


def parse_args():
    parser