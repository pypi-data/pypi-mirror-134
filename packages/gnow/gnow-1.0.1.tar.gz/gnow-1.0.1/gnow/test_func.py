# Import main class.
from .check import CheckClass
Check = CheckClass()

def create_dir():
    Check.do_command('mkdir git_test')

def delete_dir():
    Check.do_command('rm -rf git_test')

def test_do_command():
    command = 'echo $(( 1 + 1))'
    result  = Check.do_command(command).replace('\n', '')
    assert int(result) == 2

def test_no_repository_exists():
    Check.do_command('mkdir /tmp/gnow_test')
    result = Check.repository_exists('/tmp/gnow_test')
    Check.do_command('rm -rf /tmp/gnow_test')
    assert result == 0

def test_yes_repository_exists():
    Check.do_command('mkdir /tmp/gnow_test')
    Check.do_command('git init /tmp/gnow_test')
    result = Check.repository_exists('/tmp/gnow_test')
    Check.do_command('rm -rf /tmp/gnow_test')
    assert result == 1




#def test_stage_exists():
#    result = Check.stage_exists()
#    assert result == True

#def test_get_git_status():
#def test_is_change(area=''):
#def test_get_git_branch():
#def test_branch_exists():
#def test_commit_exists():
#def test_get_latest_tag():
#def test_do_git_tag(tag = 0):
#def test_do_git_add():
#def test_do_git_commit(message = ''):
#def test_do_git_push(branch = 'main'):
#def test_status(status = ''):
#def test_format_status(status = ''):
