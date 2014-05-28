help:
	@clear
	@echo Execute um alvo make!
	@echo Exemplo: make deps 

clear:
	@clear
	@rm -rf venv

create_venv:
	@echo --- criando virtualenv ---
	@virtualenv venv --no-site-package --clear

deps_prod:
	@clear
	@echo --- instalando dependencias para ambiente de producao ---
	@TODO...

deps_dev:
	@clear
	@echo --- instalando dependencias para  ambiente de desenvolvimento ---
	@venv/bin/pip install -r requirements/local.txt

setup_dev: clear create_venv deps_dev
	@echo --- preparando ambiente de desenvolvimento ---

deploy:
	@clear
	@echo --- executando deploy da aplicaÃ§Ã£o ---
	@cd scripts && fab deploy_update
