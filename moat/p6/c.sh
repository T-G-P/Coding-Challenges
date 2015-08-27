find . -name "*.py*" -not -name "*.pyc"  -print0 | xargs -0 cat | wc -l
