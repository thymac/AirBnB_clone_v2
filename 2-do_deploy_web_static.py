#!/usr/bin/python3
"""
A Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy
"""

from fabric.api import run, put, env
from os.path import exists
# Update with your server IP addresses
env.hosts = ['52.3.241.147', '100.25.163.229']
env.user = 'ubuntu'  # Update with your username
env.key_filename = '~/.ssh/school'  # Update with your SSH private key path


def do_deploy(archive_path):
    if not exists(archive_path):
        return False

    try:
        archive_filename = archive_path.split('/')[-1]
        archive_folder = '/data/web_static/releases/{}/'.format(
            archive_filename.split('.')[0])

        # Upload the archive to the /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Create the target directory on the web server
        run('mkdir -p {}'.format(archive_folder))

        # Extract the archive contents to the target directory
        run('tar -xzf /tmp/{} -C {} --strip-components=1'.format(archive_filename, archive_folder))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Move the contents of the extracted folder to the target directory
        run('mv {}web_static/* {}'.format(archive_folder, archive_folder))

        # Remove the empty web_static directory
        run('rm -rf {}web_static'.format(archive_folder))

        # Delete the existing symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link pointing to the deployed version
        run('ln -s {} /data/web_static/current'.format(archive_folder))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed:", str(e))
        return False

