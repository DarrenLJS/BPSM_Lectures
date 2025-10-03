#!/usr/bin/awk -f

BEGIN{;}{
if (substr($1,1,1)==">")
{
print "this is a header line: " $0;
hline=FNR;
}
if (FNR==hline+1)
{
print "First line is: " $0;
first_seq_character=substr($0,1,1);
print "First character is: " first_seq_character;
print first_seq_character > "first_seq_character.txt"
}
}
