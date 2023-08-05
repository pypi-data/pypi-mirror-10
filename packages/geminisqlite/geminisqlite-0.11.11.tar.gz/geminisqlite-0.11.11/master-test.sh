check()
{
	if diff $1 $2; then
    	echo ok
	else
    	echo fail
	fi
}
export -f check

cd test
rm ./*.db

# setup the testing databases from the testing VCF files
bash data-setup.sh

# Test query tool
bash test-query.sh

# Test basic functionality
bash test-columns.sh

# Test loading functionality
bash test-load.sh

# Test genotype BLOB functionality
bash test-genotypes.sh

# Test ClinVar attributes
bash test-clinvar.sh

# Test Exac
bash test-exac.sh

# Test genome annotations
bash test-genome.sh

# Test wildcards
bash test-wildcards.sh

# cleanup
rm ./*.db
rm ./file.dot

