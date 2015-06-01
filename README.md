
#W205_CommonCrawl

Hank Mushinski's submission for Assignment 1

ANSWERS
==

3.
--
The local process of test-1.warc took 1m33.681s.
The EMR process of test-1.warc took 27m6.799s

I did not run a local version of test-100.warc, but the ~90 second runtime was fairly consistent on multiple trials across multiple machines.
Assuming a consistent filesize for each WARC chunk, we might expect:
	90 seconds * 100 files ~= 9000 seconds ~= 150 minutes.

When running test-100.warc on EMR, the result was 47m32.239s with 4 instances of m1.xlarge. The time taken by provisioning and boostrapping should be easily accounted for by the speed boost from parallelization.

4.
--

There were 5140 unique address tags.

5.
--

Local and EMR runs of test-1.warc both returned 5140 unique keywords with the same counts. Run included script "python check_all_sums.py out/ emr-out/" to confirm this result.