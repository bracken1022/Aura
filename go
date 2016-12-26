#!/usr/bin/env bash


set -e
VIRTUAL_ENV_PATH=aura_env/bin/activate

function main {
    source ${VIRTUAL_ENV_PATH}
    case "$1" in
      "ut" )
        run_unit_test;;

      "sh" )
        run_shell;;

      "sr" )
        run_server;;

    esac
}

function run_server {
    cd aura
    python manage.py runserver

}

function run_shell {
    cd aura
    python manage.py shell
    cd ../
}

function run_unit_test {
  cd aura

  if [ "$1" = "--prod" ]; then
    python manage.py test -v 2 --noinput --settings=aura.settings
  elif [ "$1" = "--ci" ]; then
    python manage.py test -v 2 --noinput --settings=aura.settings
  else
    python manage.py test -v 2 --noinput --settings=aura.settings
  fi

  cd ../
}

main $@
exit 0
