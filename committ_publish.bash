#!/bin/bash
# git
git add .
git commit -m "something"
git push origin
# publish online
cd Chemistry_Lessons_Jupyter_Notebooks/
ghp-import -n -p -f _build/html
