echo -e  "\nFinding hall python files in p3 directory not recursively"
find ../p3 -maxdepth 1 -name "*.py*" -not -name "*.pyc" -exec wc -l {} \;

echo -e "\nFinding all python files in parent directory recursively and printing line counts"
find ../ -name "*.py*" -not -name "*.pyc" -exec wc -l {} \;

echo -e "\nFinding all python files in parent directory and just printing total count"
find ../ -name "*.py*" -not -name "*.pyc"  -print0 | xargs -0 cat | wc -l
