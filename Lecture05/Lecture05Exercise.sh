#!/usr/bin/bash

#Go through the file showing an index counter and the country, but with header and blank lines
IFS=$'\t'
count=0
while read name	email	city	birthday_day	birthday_month	birthday_year	country
do
count=$((count+1))
echo -e "${count}\t${country}"
done < example_people_data.tsv

#Go through the file showing an index counter and the country, but also identify blank lines and header
count=0
IFS=$'\t'
while read name	email	city	birthday_day	birthday_month	birthday_year	country
do
if test -z ${name}
  then
  echo -e "X\tBlank line found"
  else
  if test ${country} == "country"
    then
    echo -e "X\tHeader line found"
    else
    count=$((count+1))
    echo -e "${count}\t${country}"
  fi
fi
done < example_people_data.tsv

#Generates output files, putting people of the same country into a different file
count=0
IFS=$'\t'
while read name	email	city	birthday_day	birthday_month	birthday_year	country
do
if test -z ${name} || test ${country} == "country"
  then
  echo "Ignoring"
  else
  count=$((count+1))
  echo -e "${count}\t${name}\t${city}\t${country}" >> ${country// /}.details
fi
done < example_people_data.tsv

#Separate people into different files by country and birth year (<1980 considered older)
count=0
IFS=$'\t'
while read name	email	city	birthday_day	birthday_month	birthday_year	country
do
if test -z ${name} || test ${country} == "country"
  then
  continue
  else
  count=$((count+1))
  outputfile=${country// /}.younger.details
  if test ${birth_year} -le 1980
    then
    outputfile=${country// /}.older.details
  fi
echo -e "${count}\t${name}\t${birthday_year}\t${country}" >> ${outputfile}
fi
done < example_people_data.tsv

#Filters for rows with birthday_month=10 and saves them to another file
month=10
outputfile="Month.${month}.details"
count=0
IFS=$'\t'
while read name	email	city	birthday_day	birthday_month	birthday_year	country
do
if test -z ${name} || test ${country} == "country"
  then
  echo "Ignoring"
  else
  count=$((count+1))
  if test ${birthday_month} -eq ${month}
    then
    echo -e "${count}\t${name}\t${birthday_month}\t${country}" >> ${outputfile}
  fi
fi
done < example_people_data.tsv

#Filters for Mozambique details, and stores details in an array while process is running. Once process is done, look through array and save all contents into output file
count=0
fnr=0
IFS=$'\t'
wantedcountry="Mozambique"
inputfile="example_people_data.tsv"
inputfilelength=$(wc -l ${inputfile} | cut -d ' ' -f1)
outputfile="Country.${wantedcountry}.details"

unset my_array
declare -A my_array

while read name	email	city	birthday_day	birthday_month	birthday_year	country
do
fnr=$((fnr+1))
echo -e "Line number: ${fnr}"
if test -z ${name} || test ${country} == "country"
  then
  echo "" > /dev/null
  else
  if test ${country} == ${wantedcountry}
    then
    count=$((count+1))
    my_array[${count}]="${fnr}\t${name}\t${country}"
    echo -e "${my_array[${count}]}"
  fi
fi

if test ${fnr} -eq ${inputfilelength}
  then
  echo -e "\n###Here are the end of file results for ${wantedcountry}:" > ${outputfile}
  for i in "${my_array[@]}"
  do
  echo -e "${i}" >> ${outputfile}
  done
fi
done < ${inputfile}
