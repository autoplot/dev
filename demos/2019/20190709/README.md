Autoplot v2019a_6 has a bug where trim doesn't work because DEPEND_1 is rank 2.  I put in code to loop over each record 
in this case, but JoinDataSet.join doesn't create the DEPEND_1 dataset.  I need to decide if this is a bug or something people
just need to know.

