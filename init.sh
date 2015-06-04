#!/bin/bash

work_dir=/usr/src/myapp
cd ${work_dir} || exit
[ -d .ssh ] && cp -a .ssh ~
[ -f requirements.txt ] && pip install -r requirements.txt

chmod +x ${work_dir}/app.py; ${work_dir}/app.py
