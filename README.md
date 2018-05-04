#

Generate test data

```sh
scripts/make_fake_genome.py 0.5 50000 0.73 30000 100 > data/fake_genome.fasta
wgsim -e 0.001 -d 500 -s 20 -1 101 -2 101 -r 0 data/fake_genome.fasta data/fake_reads1.fq data/fake_reads2.fq
```
