#!/bin/bash

#~ java -jar bfg-1.12.3.jar --delete-folders BASIC* cpu6809
#~ java -jar bfg-1.12.3.jar --delete-folders PyDC cpu6809
#~ java -jar bfg-1.12.3.jar --delete-folders basic_editor cpu6809
#~ java -jar bfg-1.12.3.jar --delete-folders dev_startup_scripts cpu6809
#~ java -jar bfg-1.12.3.jar --delete-folders misc cpu6809
#~ java -jar bfg-1.12.3.jar --delete-folders requirements cpu6809

#~ java -jar bfg-1.12.3.jar --delete-files dragon* cpu6809
#~ java -jar bfg-1.12.3.jar --delete-files coco* cpu6809
#~ java -jar bfg-1.12.3.jar --delete-files *.wav cpu6809
#java -jar bfg-1.12.3.jar --delete-files basic* cpu6809
#java -jar bfg-1.12.3.jar --delete-files *.bas cpu6809

#~ git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch BASIC*' --prune-empty --tag-name-filter cat -- --all
#~ git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch PyDC' --prune-empty --tag-name-filter cat -- --all
#~ git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch basic_editor' --prune-empty --tag-name-filter cat -- --all
#~ git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch dev_startup_scripts' --prune-empty --tag-name-filter cat -- --all
#~ git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch misc' --prune-empty --tag-name-filter cat -- --all
#~ git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch requirements' --prune-empty --tag-name-filter cat -- --all
#~ git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch *.sh' --prune-empty --tag-name-filter cat -- --all
#~ git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch *.cmd' --prune-empty --tag-name-filter cat -- --all
#~ git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch dragonpy/CoCo' --prune-empty --tag-name-filter cat -- --all
#~ git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch CoCo' --prune-empty --tag-name-filter cat -- --all
#~ git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch Dragon*' --prune-empty --tag-name-filter cat -- --all
#~ git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch vectrex' --prune-empty --tag-name-filter cat -- --all
#~ git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch dragonpy/Dragon32' --prune-empty --tag-name-filter cat -- --all
#~ git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch dragonpy/Dragon64' --prune-empty --tag-name-filter cat -- --all
#~ git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch dragonpy/vectrex' --prune-empty --tag-name-filter cat -- --all
#~ git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch bootstrap' --prune-empty --tag-name-filter cat -- --all
#~ git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch dragonpy/core/gui.py' --prune-empty --tag-name-filter cat -- --all
#~ git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch dragon32_CAS_decode.py' --prune-empty --tag-name-filter cat -- --all
#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch Multicomp6809' --prune-empty --tag-name-filter cat -- --all
#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch Simple6809' --prune-empty --tag-name-filter cat -- --all
#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch sbc09' --prune-empty --tag-name-filter cat -- --all

#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch dragonpy/Multicomp6809' --prune-empty --tag-name-filter cat -- --all
#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch dragonpy/Simple6809' --prune-empty --tag-name-filter cat -- --all
#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch dragonpy/sbc09' --prune-empty --tag-name-filter cat -- --all

#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch MC6809/Multicomp6809' --prune-empty --tag-name-filter cat -- --all
#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch MC6809/Simple6809' --prune-empty --tag-name-filter cat -- --all
#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch MC6809/sbc09' --prune-empty --tag-name-filter cat -- --all

#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch MC6809/tests/test_BASIC*' --prune-empty --tag-name-filter cat -- --all
#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch dragonpy/tests/test_BASIC*' --prune-empty --tag-name-filter cat -- --all

#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch MC6809/tests/test_sbc09.py' --prune-empty --tag-name-filter cat -- --all
#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch dragonpy/tests/test_sbc09.py' --prune-empty --tag-name-filter cat -- --all

#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch MC6809/tests/test_cli.py' --prune-empty --tag-name-filter cat -- --all
#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch dragonpy/tests/test_cli.py' --prune-empty --tag-name-filter cat -- --all

#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch *cli.py' --prune-empty --tag-name-filter cat -- --all
#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch boot*.py' --prune-empty --tag-name-filter cat -- --all
#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch dragonpy/core/cli.py' --prune-empty --tag-name-filter cat -- --all
#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch */srecord*' --prune-empty --tag-name-filter cat -- --all
#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch */BASIC09*' --prune-empty --tag-name-filter cat -- --all
#git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch */pager*' --prune-empty --tag-name-filter cat -- --all
git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch */periphery*' --prune-empty --tag-name-filter cat -- --all
git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch */rom*' --prune-empty --tag-name-filter cat -- --all

rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now --aggressive