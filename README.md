https://www.markdownguide.org/cheat-sheet/







*********************** as we worked  **********************


so our file knows what exact python to use    #!/usr/bin/env python3.12

used a match case for our cli.py file 

show our usere to run the following lines 


we ran 

'''
pip install ipdb

pipenv install sqlalchemy

pipenv install sqlalchemy alembic 


git add Pipfile Pipfile.lock
git commit -m 'add sqlalchemy and alembic to pipenv'
git push

'''

and to set up our file to be ran correctly


'''
chmod +x cli.py
./cli.py 
'''




Library/
├── .git
├── .gitignore
├── .python-version
├── .venv
├── company.db
├── lib/
│   ├── __pycache__/
│   ├── alembic.ini
│   ├── cli.py
│   ├── company.db
│   ├── debug.py
│   ├── helpers.py
│   ├── migrations/
│   │   ├── env.py
│   │   ├── README
│   │   ├── script.py.mako
│   │   └── versions/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   ├── model_1.py
│   │   ├── campus.py        <-- Focus
│   │   └── book.py          <-- Focus
│   └── seed.py
├── Pipfile
├── Pipfile.lock
└── README.md