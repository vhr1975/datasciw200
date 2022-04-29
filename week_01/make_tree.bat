:: 
::     File name: make_tree.py
::     Author: Victor Ramirez
::     Date created: 8/26/2021
::     Date last modified: 8/26/2021
::     Python Version: 3.6
::     Class: DATASCI W200
::     HW: 1
:: 
:: # script to automate sections 1.2 of hw1
:: # create the dir structure
mkdir "s1"
mkdir "s1\s2"
mkdir "s1\s2\Advanced"
mkdir "s1\s3"

Rem Turns the echo on so that each command will be shown as executed 
echo on 
:: # create the required files
echo Virtual (conda) environments are my favorite new technology > "s1\s3\conf.txt"
echo Virtual environments are good for lib conflicts > "s1\s2\text_chunk1.txt"
copy "s1\s2\text_chunk1.txt" "s1\s2\Advanced\text_chunk2.txt"
echo I like them because they are great! >> "s1\s2\Advanced\text_chunk2.txt"

echo off
