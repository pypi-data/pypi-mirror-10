psql -h postgres-dev -c 'create database tweeply;' -U postgres
psql -h postgres-dev -c "create role tweeply with password 'tweeply' login;" -U postgres -d tweeply
