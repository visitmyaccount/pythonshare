import os
import logging
import paramiko

log = logging.getLogger()


def copy_from_iss_ftp(sftp_host, sftp_user, sftp_pass, input_folder, cleanup):
    log.info("Copying from ftp host{0} with user{1}".format(sftp_host, sftp_user))

    if not os.path.isdir(input_folder):
        log.info("INPUT Folder {0} doesn't exist creating it now".format(input_folder))
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
