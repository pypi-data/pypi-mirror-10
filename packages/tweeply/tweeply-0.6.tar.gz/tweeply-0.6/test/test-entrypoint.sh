#!/bin/bash
pip install -r test-requirements.txt
sh /usr/src/app/test/create_db.sh
/bin/sh -c "$@"
