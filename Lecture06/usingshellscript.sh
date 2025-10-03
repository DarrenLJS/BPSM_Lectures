wc -l first_seq_character.txt

sort first_seq_character.txt | uniq -c | sort -k1,1nr