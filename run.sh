for i in {17..18} {22..25}
do
  pinctrl set $i ip
  GPIO[$i]=2
done