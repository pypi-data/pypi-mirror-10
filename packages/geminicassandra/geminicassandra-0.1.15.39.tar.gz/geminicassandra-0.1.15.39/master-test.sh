#!/bin/bash

check()
{
        if diff $1 $2; then
        echo ok
        else
        echo fail
        fi
}
export -f check

export cassandra_ips="127.0.0.1"

cd test

#bash cassandra-test-setup.sh

bash cassandra-test-query.sh

bash test-load.sh

bash test-wildcards.sh

bash test-wildcards-multicore.sh

bash test-genotypes.sh

bash test-exac.sh

bash test-genome.sh

bash test-columns.sh

bash test-clinvar.sh
