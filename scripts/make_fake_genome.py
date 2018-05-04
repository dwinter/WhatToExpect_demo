#!/usr/bin/env python3
import argparse
import numpy as np
import sys

def sim_one_seq(GC_p, length):
    """Simulate a single isochore with given GC percentage (GC_p) and length"""
    bases = ['A','C','G','T']
    AT_p = (1 - GC_p)/2
    wt = [AT_p, GC_p/2, GC_p/2, AT_p]
    return("".join(np.random.choice(bases, replace=True, p = wt, size=length)))



def fake_genome(comp_1, len_1, comp_2, len_2, n):
    """
    Generate a single chromosome sequence with 2-component isochore-like structure
    comp1: tuple with (GC%, mean-length) for first component 
    comp2: tuple with (GC%, mean-length) for second component     
    n: Number of isochors for each component
    """ 
    A_lens = np.random.negative_binomial(1, 1/len_1, n)
    B_lens = np.random.negative_binomial(1, 1/len_2, n)
    #make the sequences
    A_seqs = [sim_one_seq(comp_1, L) for L in A_lens]    
    B_seqs = [sim_one_seq(comp_2, L) for L in B_lens]    
    fake_ref = "".join([a+b for a,b in zip(B_seqs, A_seqs)])
    return(fake_ref)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Genearate a fake genome')
    parser.add_argument("comp_1", 
                        help="nucleotide composition of first component", 
                        type=float)
    parser.add_argument("len_1", 
                        help="mean length of first component", type=int)
    parser.add_argument("comp_2", 
                        help="nucleotide composition of second component", 
                        type=float)
    parser.add_argument("len_2", help="mean length of second component", type=int)
    parser.add_argument("n", help="Number of isochores ", type=int)
    args = parser.parse_args()
    seq= fake_genome(args.comp_1, args.len_1, args.comp_2, args.len_2, args.n)
    header= ">fake_genome comp1={},{} comp2={},{}\n".format(args.comp_1, args.len_1, args.comp_2, args.len_2)
    sys.stdout.write(header)
    sys.stdout.write(seq)
    sys.exit(0) 
    

    

    
