init:
	test -n "$(name)"
	rm -rf ./.git
	find ./ -type f -exec perl -pi -e 's/parque_automotor/$(name)/g' *.* {} \;
	mv ./parque_automotor ./$(name)

superuser:
	docker exec -it parque_automotor ./manage.py createsuperuser

shell:
	docker exec -it parque_automotor ./manage.py shell

makemigrations:
	docker exec -it parque_automotor ./manage.py makemigrations

migrate:
	docker exec -it parque_automotor ./manage.py migrate

initialfixture:
	docker exec -it parque_automotor ./manage.py loaddata initial

testfixture:
	docker exec -it parque_automotor ./manage.py loaddata test

test:
	docker exec -it parque_automotor ./manage.py test

statics:
	docker exec -it parque_automotor ./manage.py collectstatic --noinput

makemessages:
	docker exec -it parque_automotor django-admin makemessages

compilemessages:
	docker exec -it parque_automotor django-admin compilemessages
