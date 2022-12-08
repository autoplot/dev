echo 'stdout'
timeout /t 1 /nobreak
echo 'stderr' 1>&2
timeout /t 1 /nobreak
echo 'stdout'
timeout /t 1 /nobreak
echo 'done'

