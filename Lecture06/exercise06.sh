#!/usr/bin/bash
inputfile="./blastoutput2.out"
goodlines=$(grep -v "#" ${inputfile} | wc -l | cut -d ' ' -f1) # Counts number of non-comment lines (not starting with #) in blastoutput2.out
unset IFS # Clears any custom input field separator (ensures default whitespace splitting
unset dataline # Resets line counter (dataline is not explicitly initiated, but it
shorthsp=0 # Initialise counter for short alignments (shorthsp)
hspcounter=0 # Initialise counters for mismatches (hspcounter)
echo -e "We have ${goodlines} data lines for processing...\n"
dupS_acc=() # Initialise an array (dupS_acc) to track duplicate subject accessions (S_acc)
group1cut=150
group2cut=250
group3cut=350
outfile1="HSPscore.${group1cut}.exercise.out"
outfile2="HSPscore.${group2cut}.exercise.out"
outfile3="HSPscore.${group3cut}.exercise.out"
outfile4="HSPscore.morethan.${group3cut}.exercise.out"
rm -f ${outfile1} ${outfile2} ${outfile3} ${outfile4} # Removes old versions of outputfiles so results start afresh
# Reads each line (wholeline variable initialised by "read" coommand in BASH) in blastoutput2.out, skipping comment lines
while read wholeline; do
  echo "Line is ${wholeline}"
  if test ${wholeline:0:1} != "#"; then
# Increments counter for dataline. Splits the line into BLAST output columns (Q_acc, S_acc, etc.)
    dataline=$((dataline+1)) # dataline is an empty variable, so it gets initiated here
    echo "Line ${dataline} starts with ${wholeline:0:1}"
    read Q_acc S_acc pc_identity alignment_length mismatches gap_opens Q_start Q_end S_start S_end evalue bitscore <<< ${wholeline}
    bitscore=$(printf "%.0f\n" ${bitscore}) # Converts bitscore to float (%f), rounded to 0 dp, ending with \n
    echo -e "${dataline}\t${Q_acc}\t${S_acc}" >> Subject_accessions.exercise.out
    echo -e "${dataline}\t${alignment_length}\t${pc_identity}" >> al_leng_pcID.exercise.out
# Report lines with >20 mismatches, and lines with >20 mismatches and HSPs (<100 amino acids in length)
    if test ${mismatches} -gt 20 ; then
      echo -e "${dataline}\tmore than 20 mismatches:\t${Q_acc} ${S_acc} ${mismatches}"
    fi
    if test ${alignment_length} -lt 100 && test ${mismatches} -gt 20; then
      echo -e "${dataline}\tHSP shorter than 100aa, more than 20 mismatches:\t${alignment_length}\t${mismatches}"
    fi
# Increments hspcount to count lines with <20 mismatches, stores the lines in another array (hsp_array), and saves the first 20 lines in an output file
    if test ${mismatches} -lt 20 ; then
      hspcounter=$((hspcounter+1)) 
      if test ${hspcounter} -le 20; then
        hsp_array+=${wholeline}
        echo -e "${dataline}\t${hspcounter}\t${wholeline}" >> Fewer.than20MM.exercise.out
      fi
    fi
# Increments shorthsp to count lines with <100aa length, and saves the first 10 lines in an output file
    if test ${alignment_length} -lt 100; then
      shorthsp=$((shorthsp+1))
    fi
    if test ${dataline} -le 10; then
      echo -e "${dataline}\t${wholeline}" >> Top10.HSPs.exercise.out
    fi
# If S_acc contains "AEI", saves lines with echo in an output file
    if [[ ${S_acc} == *"AEI"* ]]; then
      echo -e "${dataline}\t${S_acc} contains AEI: Subject starts at ${S_start}, Query starts at ${Q_start}" >> AEIinSubjectAcc.starts.exercise.out
    fi
# Tracks duplicate S_acc
    if test ${S_acc} == ${pre_acc}; then
      dupecount=$((dupecount+1)) # If current S_acc = previous S_acc, increment dupecount (this counter becomes useless after first entry)
      if [[ dupecount == 1 ]]; then
        dupS_acc=${S_acc} # Enter first duplicate in dupS_acc array
      fi
# Subsequently, if current S_acc = previous S_acc, check if dupS_acc already contain current S_acc, then do nothing, else add to dupS_acc array
      if [[ $dupS_acc == *${S_acc}* ]]; then
        echo ""
      else
        dupS_acc+=(${S_acc})
      fi  
    fi    
    pre_acc=${S_acc} # Current S_acc becomes previous S_acc
# Calculates mismatch percentage and logs results per line
    MMpercent=$((100*${mismatches}/${alignment_length}))
    echo -e "${dataline}\t${alignment_length}\t${mismatches}\t${MMpercent}" >> Mismatchpercent.exercise.out
# Classify into scorebins = 1,2,3,4 by bitscore
    scorebin=1
    if [ ${bitscore} -gt ${group3cut} ]; then
      scorebin=4
    fi
    if [ ${bitscore} -le ${group3cut} ] && [ ${bitscore} -gt ${group2cut} ]; then
      scorebin=3
    fi
    if [ ${bitscore} -le ${group2cut} ] && [ ${bitscore} -gt ${group1cut} ]; then 
      scorebin=2
    fi
# Case block to append each line to respective output file based on scorebin classification
    scoregroupdetails=$(echo -e "${dataline}\t${Q_acc}\t${S_acc}\t${bitscore}") 
    case $scorebin in
      4)
      echo -e "${scoregroupdetails}" >> ${outfile4}
      ;;
      3)
      echo -e "${scoregroupdetails}" >> ${outfile3}
      ;;
      2)
      echo -e "${scoregroupdetails}" >> ${outfile2}
      ;; 
      1)
      echo -e "${scoregroupdetails}" >> ${outfile1} 
      ;;
    esac
# End-of-file summary
    if test ${dataline} -eq ${goodlines}; then
      echo -e "\n\nENDBLOCK\n\nThere were ${shorthsp} HSPs shorter than 100 amino acids" 
      echo -e "There were ${#dupS_acc[@]} Subjects with multiple HSPs"
    fi
  fi
done < ${inputfile}
