python -m pytest -v -s -m "smoke" testCases\ --html=Reports\report.html --browser Chrome


rem python -m pytest -v -s -m "smoke and/or sanity" testCases\ --html=Reports\report.html --browser Chrome


rem python -m pytest -v -s -m "regression" testCases\ --html=Reports\report.html --browser Chrome