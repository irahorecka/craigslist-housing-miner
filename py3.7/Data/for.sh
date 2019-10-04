for f in *csv;
do sed -i '' 1d $f | tr '-' '_';
done