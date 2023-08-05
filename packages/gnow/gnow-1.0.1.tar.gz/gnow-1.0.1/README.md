[![Python 3.9](https://github.com/addshlab/gnow/actions/workflows/python39.yml/badge.svg)](https://github.com/addshlab/gnow/actions/workflows/python39.yml)
[![Python 3.8](https://github.com/addshlab/gnow/actions/workflows/python38.yml/badge.svg)](https://github.com/addshlab/gnow/actions/workflows/python38.yml)
[![Python 3.7](https://github.com/addshlab/gnow/actions/workflows/python37.yml/badge.svg)](https://github.com/addshlab/gnow/actions/workflows/python37.yml)
[![Python 3.6](https://github.com/addshlab/gnow/actions/workflows/python36.yml/badge.svg)](https://github.com/addshlab/gnow/actions/workflows/python36.yml)
[![Python 3.5](https://github.com/addshlab/gnow/actions/workflows/python35.yml/badge.svg)](https://github.com/addshlab/gnow/actions/workflows/python35.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# gnow

A wrapper command to make git add/commit/push and tagging easier.

## Installation

```
$ pip install gnow
```

## Usage

### Status

```
$ gnow -s

{CURRENT_BRANCH} ({CURRENT_TAG})
-----------------
 Working tree
 - No files.
 Index
 - No files.
 Unpushed commit
 - No commits.
-----------------
```

### git add -> git commit -> git push

```
# Auto commit message
$ gnow

# Manual commit message
$ gnow 'YOUR COMMIT MESSAGE'

main (1.1.1)
---------------------
 Working tree
 - Updated README.md
 Index
 - No files.
 Unpushed commit
 - No commits.
---------------------
ADD files to the index? [n/Y or Enter]
STAGING done. ✔

COMMIT MESSAGE: Updated README.md
BRANCH: main
COMMIT the index contents? [n/Y or Enter]
COMMIT done. ✔

BRANCH: main
PUSH local commits? [n/Y or Enter]
PUSH done. ✔
```

### git commit

This operation is the same as `git commit`.

```
# Auto input (Make the commit message the status of the file)
$ gnow -c

# Manual input
$ gnow -c 'YOUR COMMIT MESSAGE'

ADD files to the index? [n/Y or Enter]
STAGING done. ✔

COMMIT MESSAGE: Updated README.md
BRANCH: main
COMMIT the index contents? [n/Y or Enter]
COMMIT done. ✔
```

### Tagging

This command supports tags in vX.Y.Z format. The leading v is auto-filled. You only have to specify X.Y.Z.

```
# Auto input (Automatically increments the patch version)
$ gnow -t
Latest tag is 1.0.1
New tag is 1.0.2
TAG the latest commit? [n/Y or Enter]

# Manual input
$ gnow -t 1.0.0
Latest tag is 0.0.6
New tag is 1.0.0
TAG the latest commit? [n/Y or Enter]

# When there are no tag settings
$ gnow -t
No tags are currently.
Auto incremented version is 0.0.1
TAG the latest commit? [n/Y or Enter]
```

## Changelog

- 2022-01-10 Minor fix
- 2021-07-09 Start porting to Python
- 2020-07-09 Published a bash script version on Github
