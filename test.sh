echo "\n----- naive -----\n"
for i in {1..3}
do
    time ./naive_search.py english "svwscgwmvtikpiqhskbtxwdak" > /dev/null
done

echo "\n----- set -----\n"
for i in {1..3}
do
    time ./set_search.py english "svwscgwmvtikpiqhskbtxwdak" > /dev/null
done
