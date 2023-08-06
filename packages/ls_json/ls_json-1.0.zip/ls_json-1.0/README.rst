=======
ls_json
=======
ls_json traverses either the provided path or current dir and returns the file tree (with file sizes) in json format

by default it installs as a console application into the users path.

**Usage:**::

    ~/ls_json ## python setup.py install

    ~/ls_json ## ls_json
    {
      ".git": {
        ".COMMIT_EDITMSG.swp": 4096,
        "COMMIT_EDITMSG": 282,
        "FETCH_HEAD": 100,
        "HEAD": 23,
        "config": 360,
        "description": 73,
        "index": 474,
        "info": {
          "exclude": 240
        },
        "logs": {
          "HEAD": 700,
          "refs": {
            "heads": {
              "master": 700
            },
            "remotes": {
              "origin": {
                "HEAD": 197,
                "master": 304
              }
            }
          }
        },
        "objects": {
          "1d": {
            "9bb6e4f5debac1c7342d437a22ba8e41c35a10": 794
          },
          "2a": {
            "5e29c1271823cc2791203936cb97103d039133": 10073
          }
        },
        "sourcetreeconfig": 1034
      },
      ".gitignore": 24,
      "LICENSE.txt": 38578,
      "README.md": 228,
      "ls_json.py": 1695,
      "setup.cfg": 41,
      "setup.py": 1445
    }