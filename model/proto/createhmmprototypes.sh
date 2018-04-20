protofile='hmmproto_5_1_49'

activities=(1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16)

hmm_prefix="Activity"
for i in "${activities[@]}"
do
  cp $protofile $hmm_prefix$i
  sed -i -e "s/proto/$hmm_prefix$i/g" $hmm_prefix$i
done

