
install: requirements.txt
	pip install -r requirements.txt

run-dev-docker: Dockerfile.dev
	docker build . -f Dockerfile.dev -t linkedin-scraper-app
	docker run -i -t --rm linkedin-scraper-app