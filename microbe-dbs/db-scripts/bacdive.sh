#!/bin/bash
# -*- coding: utf-8 -*-
# author:  	maxime déraspe
# email:	maximilien1er@gmail.com


# download files from web site
function rep_download_files() {

    out_dir=""
    if [ -z $1 ]
    then
        outdir=bacdive_ #тут заменить на нужную дату
    else
        outdir=$1/bacdive_
    fi
    # mkdir -p $outdir &&
    cd $outdir
	outdir=$(pwd -P)

	echo -ne "Enter BacDive username : "
	read user
	echo -ne "Enter BacDive password : "
	read -s password

    echo -e "\n\nDownloading BacDive $release [$outdir].."
	dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
	python3 $dir/bacdive.py $user $password $outdir

}

function download_files() {

    release=$(date +%Y-%m-%d)

    out_dir=""
    if [ -z $1 ]
    then
        outdir=bacdive_$release
    else
        outdir=$1/bacdive_$release
    fi
    mkdir -p $outdir && cd $outdir
	outdir=$(pwd -P)
	
	echo -ne "Enter BacDive username : "
	read user
	echo -ne "Enter BacDive password : "
	read -s password

    echo -e "\n\nDownloading BacDive $release [$outdir].."
	dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
	python $dir/bacdive.py $user $password $outdir

}

# gunzip files
function organize_files() {
    for i in *.tar.gz
    do
        mkdir ${i%.tar.gz}
        tar xvf $i -C ${i%.tar.gz}
    done
    rm *.tar.gz
}


download_files $1
# organize_files

