# Review this code, taking into account good practices for software development and design patterns.
# If you are familiar with Python, also feel free to suggest a more 'pythonic' solution.
# Assume that the code works as is, there is no need to review functionality, only syntax/style/reusability/etc.

# -------------------------------------------------------------------------------------------------

# For the sake of brevity in this test, pretend that all magic* functions works exactly as expected.
import magic_install
import requests
import magic_git_config
import sys

class CommandRunner():
    def __init__(self, command, tool):
        self.command = command
        self.tool = tool

    def ex(self):
        result = self.command.execute()

        message = result ? 'successfully' : 'failed'

        self.print_message(tool, message)


    def print_message(self, tool, message):
        print "%s install %s" % (tool, message)


class InstallGit():

    self.user = 'aaa'
    self.email = 'sss'
    self.eol = 'teste'
    self.pack_limit = ''
    self.post_buffer = ''

    def execute(self):

        response = requests.get(
            'https://esss.com.br/site/dev/downloads/tools/git',
            auth=('download_user', 'my_secret_password'),
            timeout=100,
            allow_redirects=True,  # Must be enabled for our server,
            verify=False,  # Server is not signed,
            stream=True  # For downloading files
        )

        if(response.status_code != '200'):
            return False

        file_path = 'D:/downloads/git'
        download_file = open(file_path, 'wb')

        with download_file as write_file:

            for chunk in response.iter_content(chunk_size=1024):
                # write chunk in file
                write_file.write(chunk)

            write_file.close()

        try:
            magic_install(download_file)
        except:
            return False

        self.configure_git()

        return True


    def configure_git(self):
        
        magic_git_config('user.name', self.user)
        magic_git_config('user.email', self.email)
        magic_git_config('core.eol', self.eol)
        magic_git_config('pack.packsizelimit', self.pack_limit)
        magic_git_config('http.postbuffer', self.post_buffer)

        return True

    class ConfigureGit(InstallGit):
        # Override from superclass (install_and_configure_git_command) since we only want to config
        def __init__(self):
            InstallGit.__init__(self)

        def execute(self):
            self.configure_git(self.user, self.email, self.eol, self.pack_limit, self.post_buffer)
            return True


class InstallSvn():
    '''
    Command to install SVN in a user's machine
    '''
    def execute(self):
        response = requests.get(
            'https://esss.com.br/site/dev/downloads/tools/svn',
            auth=('download_user', 'my_secret_password'),
            timeout=100,
            allow_redirects=True,  # Must be enabled for our server,
            verify=False,  # Server is not signed,
            stream=True  # For downloading files
        )

        if(response.status_code != '200'):
            return False

        file_path = 'D:/downloads/svn'
        download_file = open(file_path, 'wb')

        with download_file as write_file:

            for chunk in res.iter_content(chunk_size=1024):
                # write chunk in file
                write_file.write(chunk)

            write_file.close()

        try:
            magic_install(download_file)
        except:
            return False

        return True



#===================================================================================================
# Main
#===================================================================================================
if __name__ == '__main__':

    if sys.argv[1] == 'install':
        if sys.argv[2] == 'git':
            cmd = command_runner(InstallGit(), sys.argv[2])
        elif sys.argv[2] == 'svn':
            cmd = command_runner(InstallSVN(), sys.argv[2])
    elif sys.argv[1] == 'configure_git':
        cmd = command_runner(ConfigureGit(), sys.argv[2])

    result = cmd.ex()
    sys.exit(result)
