heroku login:
	HEROKU_API_KEY=${HEROKU_API_KEY} heroku container:login

build-ml-api-heroku:
	docker build -t registry.heroku.com/${HEROKU_APP_NAME}/web .

push-ml-api-heroku:
	docker push registry.heroku.com/${HEROKU_APP_NAME}/web

release-heroku:
	heroku container:release web --app ${HEROKU_APP_NAME}



