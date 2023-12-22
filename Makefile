

start_pgadmin:
	docker-compose up pgadmin --build --force-recreate --remove-orphans -d


start_funnel: 
	docker-compose up postgres --build --force-recreate --remove-orphans -d 
	@echo "postgres started"
	docker-compose up funnel --build --force-recreate --remove-orphans -d 
	@echo "funnel started"


start_worker:
	docker-compose up alembic --build --force-recreate --remove-orphans -d
	echo "alembic started"
	docker-compose up worker --build --force-recreate --remove-orphans -d
	echo "worker started"


cluster_stop:
	docker-compose down

