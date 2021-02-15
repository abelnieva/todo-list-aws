localTest: 
	docker-compose  -f test/docker-compose.yml  up   --abort-on-container-exit
setupLocalEnv:
	sudo pip3 install -r requirements.txt 
startLocalDB:
	docker-compose  -f docker-compose-dynamo.yml   up  -d
stopLocalDB:
	docker-compose -f docker-compose-dynamo.yml down
sartSamLocal:
	sam local start-api --port 8080