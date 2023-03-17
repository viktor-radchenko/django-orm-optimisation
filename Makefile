init:
	python3 -m virtualenv .venv
	git remote remove origin
	@echo "\n \n "
	@echo "PLEASE ADD NEW REMOTE ORIGIN TO THE PROJECT"
	@echo "git remote add origin <url-to-your-git-repo> \n"
	@echo "CREATE A CLEAN FIRST COMMIT"
	@echo "git checkout --orphan develop \n"
	@echo "ACTIVATE YOUR VIRTUAL ENV AND RUN"
	@echo "pip install -r requirements.txt"
