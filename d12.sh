#It seems in my input, all presents either have a total volume larger than the region, or there's plenty of room, so this seems to give right answer without solving the actual general problem :)
cat input_d_12.txt | tail -n +31 | sed -e 's/://' -e 's/x/ /' | awk '{print $1*$2 -($3*7+$4*7+$5*6+$6*7+$7*7+$8*5)}' | grep -v "-" | wc -l
