import subprocess

from .color import ColorClass

Color = ColorClass()

#------------------------------
# Confirm the existence of the Git repository.
#------------------------------

class CheckClass:
    #def __init__(self):

    def do_command(self,command):
        proc = subprocess.Popen(
            command,
            shell  = True,
            stdin  = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE)
        stdout_data, stderr_data = proc.communicate()
        return stdout_data.decode()

    def repository_exists(self, path = '.'):
        command = "git -C %s status -s 2>&1 > /dev/null | awk '{print $1}'" % path
        if self.do_command(command) == '':
            return True
        else:
            return False

    def stage_exists(self, path = '.'):
        command = "git -C %s status -s" % path
        if self.do_command(command) == '':
            return False
        else:
            return True

    def get_git_status(self, path = '.'):
        command = "git -C %s status -s" % path
        status  = self.do_command(command)
        if not status:
            return ''
        else:
            return status

    def is_change(self, area=''):
        workingtree = ''
        index       = ''
        if self.get_git_status() == False:
            return False
        status = self.get_git_status().split('\n')
        for item in status:
            if item:
                index       = index + item.rsplit(' ')[0]
                workingtree = workingtree + item.rsplit(' ')[1]

        if area == 'index':
            if index:
                return True
            else:
                return False
        elif area == 'workingtree':
            if workingtree:
                return True
            else:
                return False
        else:
            return False

    def get_git_branch(self, path = '.'):
        command = "git -C %s rev-parse --abbrev-ref HEAD" % path
        branch  = self.do_command(command).replace('\n', '')
        return branch

    def branch_exists(self, path = '.'):
        command = "git -C %s branch" % path
        branch  = self.do_command(command).replace('\n', '')
        return branch

    def commit_exists(self, path = '.'):
        branch = self.get_git_branch().rstrip('\r\n')
        command = 'git -C %s log --pretty=format:"%%H" origin/%s..HEAD' % (path, branch)
        commit  = self.do_command(command)
        if not commit:
            return False
        else:
            return commit

    def get_unpushed_list(self, path = '.'):
        branch = self.get_git_branch().rstrip('\r\n')
        command1 = 'git -C %s log --pretty=format:"%%h" origin/%s..HEAD' % (path, branch)
        command2 = 'git -C %s log --pretty=format:"%%d" origin/%s..HEAD' % (path, branch)
        short_hash = self.do_command(command1)
        ref_name   = self.do_command(command2)
        if not short_hash:
            return False
        else:
            return short_hash + ref_name

    def get_latest_tag(self, path = '.'):
        command = 'git -C %s tag | sed s/^v//g | sort -t . -n -k1,1 -k2,2 -k3,3 | tail -n1' % path
        tag     = self.do_command(command).replace('\n','')
        return tag

    def do_git_tag(self, tag = 0, path = '.'):
        command = 'git -C %s tag -a v%s -m "%s"' % (path, tag, tag)
        tag     = self.do_command(command)
        return tag

    def do_git_add(self, path = '.'):
        command = 'git -C %s add -A' % path
        result  = self.do_command(command)
        return result

    def do_git_commit(self, message = '', path = '.'):
        message = message.replace('\n','')
        command = 'git -C %s commit -m "%s"' % (path, message)
        result  = self.do_command(command)
        return result

    def do_git_push(self, branch = 'main', path = '.'):
        command = 'git -C %s push origin %s' % (path, branch)
        push    = self.do_command(command)
        return push

    """
    see also: https://git-scm.com/docs/git-status
    """
    def status(self, status = ''):
        index_i       = 0
        workingtree_i = 0
        status = self.get_git_status()
        status_dict = {
            'M  ':'i.Modified ',
            'MM ':'i.Modified*',
            'MD ':'i.Modified* ',
            'A  ':'i.Added ',
            'AM ':'i.Added* ',
            'AD ':'i.Added* ',
            'D  ':'i.Deleted ',
            'R  ':'i.Renamed ',
            'RM ':'i.Renamed* ',
            'RD ':'i.Renamed* ',
            'C  ':'i.Copied ',
            'CM ':'i.Copied* ',
            'CD ':'i.Copied* ',
            ' M ':'w.Updated ',
            'MM ':'w.Updated* ',
            'AM ':'w.Updated* ',
            'RM ':'w.Updated* ',
            'CM ':'w.Updated* ',
            ' D ':'w.Deleted ',
            'MD ':'w.Deleted* ',
            'AD ':'w.Deleted* ',
            'RD ':'w.Deleted* ',
            'CD ':'w.Deleted* ',
            ' R ':'w.Renamed ',
            'DR ':'w.Renamed* ',
            ' C ':'w.Copied ',
            'DC ':'w.Copied* ',
            'DD ':'o.Unmerged ',
            'AU ':'o.Unmerged ',
            'UD ':'o.Unmerged ',
            'UA ':'o.Unmerged ',
            'DU ':'o.Unmerged ',
            'AA ':'o.Unmerged ',
            'UU ':'o.Unmerged ',
            '?? ':'o.Untracked ',
            '!! ':'o.Ignored ',
        }
        for word, read in status_dict.items():
            status = status.replace(word, read)
        status_list = status.split('\n')
        del status_list[-1]
        # Border between status display.
        if not status_list:
            max_file_name = 1
        else:
            max_file_name = len(max((x for x in status_list), key=len))
        if max_file_name <= 14:
            border = '-' * 17
        else:
            border = '-' * (max_file_name + 2)

        Color.set(self.get_git_branch(), 'green', '', 'bold', '')

        if self.get_latest_tag() == '':
            Color.set(' (no tags)', 'white', '', 'em')
        else:
            Color.set(' (' + self.get_latest_tag() + ')', 'white', '', 'em')

        print(border)

        Color.set(' Working tree ', 'purple', '', 'bold')
        for item in status_list:
            if item.startswith('w.') or item.startswith('o.'):
                if item.startswith('w.'):
                    print(' - ' + item.strip('w.'))
                    workingtree_i += 1
                if item.startswith('o.'):
                    print(' - ', end='')
                    Color.set(item.strip('o.'), 'red')
                    workingtree_i += 1
        if workingtree_i == 0:
            Color.set(' - No files.', 'white', '', 'em')

        Color.set(' Index ', 'purple', '', 'bold')
        it = iter(status_list)
        for item in status_list:
            if item.startswith('i.'):
                print(' - ' + item.strip('i.'))
                index_i += 1
        if index_i == 0:
            Color.set(' - No files.', 'white', '', 'em')

        Color.set(' Unpushed commit ', 'purple', '', 'bold')
        if self.get_unpushed_list():
            print(self.get_unpushed_list())
        else:
            Color.set(' - No commits.', 'white', '', 'em')

        print(border)

    def format_status(self, status = ''):
        format_dict = {
            'M  ':'Updated ',
            'A  ':'Added ',
            'D  ':'Deleted ',
            'R  ':'Renamed ',
            'C  ':'Copied '
        }
        for word, read in format_dict.items():
            status = status.replace(word, read)
        return status.replace('\n', ', ').strip(', ')
