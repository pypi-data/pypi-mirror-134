import datetime
import time

from .color import ColorClass
from .check import CheckClass
Color = ColorClass()
Check = CheckClass()

class MainClass:
    #def __init(selft):

    #------------------------------
    # Add
    #------------------------------
    def fast_add(self):
        Color.set('ADD ', 'purple', '', 'bold', '')
        try:
            read = input('files to the index? [n/Y or Enter]')
            if read == 'no' or read == 'NO' or read == 'n' or read == 'N':
                exit()
            elif read == 'yes' or read == 'YES' or read == 'y' or read == 'Y':
                Check.do_git_add()
                Color.set('STAGING done. ✔', 'green')
                print()
            else:
                Check.do_git_add()
                Color.set('STAGING done. ✔', 'green')
                print()
        except (KeyboardInterrupt) as e:
            Color.set('Process aborted.', 'red')
            exit()

    #------------------------------
    # Commit
    #------------------------------
    def fast_commit(self, input_message = ''):

        if Check.is_change('workingtree') == True:
            self.fast_add()

        # If there is no commit message argument, the date and status will be used as the message.
        if input_message == '':
            now     = str(datetime.datetime.today())
            message = Check.format_status(Check.get_git_status())
        else:
            message = input_message

        # Push to main if it appears to be the first push where no local branch exists.
        if Check.branch_exists() == '':
            branch = 'main'
            Color.set('Initial commit.', 'yellow')
        else:
            branch = Check.get_git_branch()

        Color.set('COMMIT MESSAGE: ', 'yellow', '', '', '')
        print (message)
        Color.set('BRANCH: ', 'yellow', '', '', '')
        print (branch)

        try:
            Color.set('COMMIT ', 'purple', '', 'bold', '')
            read = input('the index contents? [n/Y or Enter]')
            if read == 'no' or read == 'NO' or read == 'n' or read == 'N':
                exit()
            elif read == 'yes' or read == 'YES' or read == 'y' or read == 'Y':
                Check.do_git_commit(message)
                Color.set('COMMIT done. ✔', 'green')
                print()
            else:
                Check.do_git_commit(message)
                Color.set('COMMIT done. ✔', 'green')
                print()
        except (KeyboardInterrupt) as e:
            Color.set('Process aborted.', 'red')
            exit()

    #------------------------------
    # Push
    #------------------------------
    def fast_push(self, input_message = ''):
        Check.status()
        # Check any file exists in the working tree.
        if Check.is_change('workingtree') == True:
            self.fast_add()
        # Check any file exists in the index. 
        if Check.is_change('index') == True:
            self.fast_commit(input_message)

        # コミット済みファイルが存在するか
        # Check any file exists in the index. 
        if Check.commit_exists() == False:
            exit()

        # ローカルのブランチが存在しない初回pushとみられる場合はmainにpushする
        if Check.branch_exists == 0:
            branch = 'main'
            Color.set('Initial commit', 'yellow')
        else:
            branch = Check.get_git_branch() 

        try:
            Color.set('BRANCH: ', 'yellow', '', '', '')
            print (branch)
            Color.set('PUSH ', 'purple', '', 'bold', '')
            read = input('local commits? [n/Y or Enter]')
            if read == 'no' or read == 'NO' or read == 'n' or read == 'N':
                exit()
            elif read == 'yes' or read == 'YES' or read == 'y' or read == 'Y':
                push = Check.do_git_push(branch)
                Color.set('PUSH done. ✔', 'green')
            else:
                push = Check.do_git_push(branch)
                Color.set('PUSH done. ✔', 'green')
                exit()
        except (KeyboardInterrupt) as e:
            Color.set('Process aborted.', 'red')
            exit()

    #------------------------------
    # Tags
    #------------------------------
    def fast_tag(self, new_tag = ''):
        latest_tag = Check.get_latest_tag()
        if latest_tag == '':
            latest = '0.0.0'
        else:
            latest = Check.get_latest_tag()
        try:
            latest_list  = latest.split('.')
            latest_major = latest_list[0]
            latest_minor = latest_list[1]
            latest_patch = latest_list[2]
            patch_increment = int(latest_patch) + 1
            patch_ver       = latest_major + '.' + latest_minor + '.' + str(patch_increment)
        except:
            Color.set('Latest tag ', 'red', '', '', '')
            Color.set(latest_tag, 'red', '', 'bold', '')
            Color.set(' is not an auto-incrementable version notation.', 'red')
            Color.set('Supports tags in X.Y.Z format.', 'red')
            patch_ver = '0.0.1'
        if new_tag == '':
            if Check.get_latest_tag() == '':
                Color.set('No tags are currently.', 'green')
            else:
                Color.set('Latest tag is ' + latest, 'green')
            Color.set('Auto incremented version is ' + patch_ver, 'green')
            try:
                Color.set('TAG ', 'purple', '', 'bold', '')
                read = input('the latest commit? [n/Y or Enter]')
                if read == 'no' or read == 'NO' or read == 'n' or read == 'N':
                    exit()
                elif read == 'yes' or read == 'YES' or read == 'y' or read == 'Y':
                    Check.do_git_tag(patch_ver)
                    Check.do_command('git push origin --tag')
                else:
                    Check.do_git_tag(patch_ver)
                    Check.do_command('git push origin --tag')
            except (KeyboardInterrupt) as e:
                Color.set('Process aborted.', 'red')
                exit()
        else: # user add a tag
            if Check.get_latest_tag() == '':
                Color.set('No tags are currently.', 'green')
            else:
                Color.set('Latest tag is ' + latest, 'green')
            Color.set('New tag is ' + new_tag, 'green')
            try:
                read = input('Tagging? [n/Y or Enter]')
                if read == 'no' or read == 'NO' or read == 'n' or read == 'N':
                    exit()
                elif read == 'yes' or read == 'YES' or read == 'y' or read == 'Y':
                    Check.do_git_tag(new_tag)
                    Check.do_command('git push origin --tag')
                else:
                    Check.do_git_tag(new_tag)
                    Check.do_command('git push origin --tag')
            except (KeyboardInterrupt) as e:
                Color.set('Process aborted.', 'red')
                exit()

    #------------------------------
    # How to use
    #------------------------------
    def usage(self):
        Color.set(' HELP ', 'green', 'white')
        Color.set('gnow command :: Git commit for NOW', 'green')
        print("This is the 'gnow' command to do a quick git commit and git push.")
        print('')
        print("Options:")
        print("  (no args): Run git add -> commit -> push")
        print("  -h, --help :Show helps.")
        print("  -v, -V, --version :Show version.")
        print("  -c, --commit [ARG] :Commit only.")
        print("  -t, --tag [ARG] :Add tag. If no argument, current version will be automatically incremented.")

