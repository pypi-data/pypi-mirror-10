#!/bin/bash

find $PWD/* -type d | xargs rm -rv

while read line; do
  modline=`echo $line | awk -F"#" -v OFS="#" '{print $1, $2, $10}'`
  modline=`echo $modline | sed 's:"::g' | sed 's:7/1/::g' | sed 's:,::g'`
  country=`echo $modline | cut -d'#' -f1 | sed 's: :_:g' | sed 's:_and_::g' | sed 's:-::g'`
  country=`echo $country | sed 's:\.::g' | sed 's:(::g' | sed 's:)::g' | sed 's:_::g'`
  initial=`echo $country | head -c 1`
  [ ! -d $initial ] && mkdir -v $initial
  x=`echo $modline | cut -d'#' -f2`
  y=`echo $modline | cut -d'#' -f3`
  xerr=0.3
  yerr=`echo "$y*0.3" | bc -l`
  [[ "$initial" =~ [A-E] ]] && data="$x $y"
  [[ "$initial" =~ [F-J] ]] && data="$x $y 0. 0."
  [[ "$initial" =~ [K-O] ]] && data="$x $y 0. $yerr"
  [[ "$initial" =~ [P-T] ]] && data="$x $y $xerr 0."
  [[ "$initial" =~ [U-Z] ]] && data="$x $y $xerr $yerr"
  echo $data >> $initial/${country}.dat
done < WorldBankIndicators.csv
