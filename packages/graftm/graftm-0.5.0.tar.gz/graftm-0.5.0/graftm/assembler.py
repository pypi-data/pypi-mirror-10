import subprocess
import tempfile
import os
import shutil

from Bio import SeqIO

from graftm.messenger import Messenger

class TaxoGroup:

    def __init__(self): pass

    def main(self, args):
        ## Split the lists of graftM runs

        # Define a list to contain the paths to all of the guppy files that will be used
        guppy_list= []

        # Define a list to contan the paths to all of the sequence files that will be used
        f_sequence_list = []

        # Split the comma separated input files
        file_list = args.graft_run.split(',')

        #
        for run in file_list:
            guppy_list.append(run + '/' + run + '_placements.guppy')
            f_sequence_list.append(run + '/' + run + '_hits.fa')

        ## Creates a list of sequences and their taxonomic classification from all the guppy files
        Messenger().header("Preparing reads")
        split_guppys = TaxoGroup().guppy_splitter(guppy_list)

        ## Grabs the sequences from the forward reads, and grabs the corresponding reverse reads as well.
        grouped_sequences = TaxoGroup().rank_grouper(split_guppys, f_sequence_list)

        Messenger().header("Assembling")
        TaxoGroup().assembler(grouped_sequences, 'graftM_assemble', args.assembly_type, args)

        exit(1)

    def guppy_splitter(self, guppy_file, cutoff):
        ## Split a gupyp file, and return the placement information in hash
        ## format, and also the placement confidence at each rank

        # Send the message that the guppy file is being split
        Messenger().message("Parsing the guppy file(s)")
        read_tax_dict = {} # Define an empty output hash
        
        # Split each line in the guppy, check that it meets the cutoff, and
        # Return a hash with the placements, and rank placements
        for lst in [x.replace('Candidatus ', 'Candidatus_').split() for x in open(guppy_file,'r')]: # for each entry in the guppy file
            if lst[0] != 'name': # ignore the title entry of the guppy
                lst[0] = '_'.join(lst[0].split('_')[:-1]) # Remove the unique identifier of this read name
                if lst[1] == lst[2] and float(lst[len(lst)-2]) > float(cutoff): # If the placements match, and the placement confidence meets the cutoff
                    if lst[0] not in read_tax_dict: # If the read name is not already in the list
                        read_tax_dict[lst[0]] = {}
                        read_tax_dict[lst[0]]['placement'] = [lst[3]] # Add a placement entry for this read
                        read_tax_dict[lst[0]]['confidence'] = [lst[len(lst)-2]] # Add a confidence entry for this read
                    else: # else, if there is already an entry for this read
                        if len(read_tax_dict[lst[0]]['placement']) < 7: # Ensure that the rank of placement isn't already full
                            read_tax_dict[lst[0]]['placement'].append(lst[3]) # And append the rank to the list.
                            read_tax_dict[lst[0]]['confidence'].append(lst[len(lst)-2]) # And append the confidence to the list
                        else:
                            # Go out on a limb here, and assume that the full placement has been given. Sometimes placements are duplicated for the same read in the guppy file.
                            # raise Exception('Programming Error: Guppy file not formatted correctly: %s' % (guppy_file)) # If its full, and there are too many placements for a given read, fail.
                            pass
        # Return the hash.
        return read_tax_dict

    def rank_grouper(self, split_guppy, f_sequences_list):
        '''Gathers the sequences that correspond to each id, and taxonomic rank within the split guppy'''
        n_misses = 0
        tax_list = [{}, {}, {}, {}, {}, {}]

        f_sequences = {}


        for f in f_sequences_list:
            records = SeqIO.to_dict(SeqIO.parse(open(f, 'r'), "fasta"))
            f_sequences.update(records)
            Messenger().message( "%s reads found in %s" % (len( records.keys() ), os.path.basename(f) ) )

        Messenger().message("Using %s forward reads in total." % (len(f_sequences.keys())))
        Messenger().message("Sorting 16S forward sequences into taxonomic groups")

        for read_name, classification in split_guppy.iteritems():
            taxonomic_group = classification[len(classification) - 1]

            tax_dict = tax_list[len(classification) - 2]

            if taxonomic_group not in tax_dict:
                tax_dict[taxonomic_group] = []
            tax_dict[taxonomic_group].append(f_sequences[read_name[:-2]])

        return tax_list

    def assembler(self, tax_rank_list, output_directory, assembly_type, args):

        rank = ['K','P','C','O','F','G']
        p_rank= ['Kingdom','Phylum','Class','Order','Family','Genus']
        cmd = 'mkdir %s 2>/dev/null' % output_directory

        try:
            subprocess.check_call(cmd, shell = True)

        except:
            Messenger().message("A folder with the name '%s' already exists... This is awkward... \n" % output_directory)
            exit(1)


        for idx, taxonomic_rank in enumerate(tax_rank_list):
            r = p_rank.pop(0)
            if r == 'Genus':
                Messenger().message("Using %s to assemble reads classified at the %s level." % (assembly_type, r))
            else:
                Messenger().message("Using %s to assemble reads classified at the %s level. -WARNING- These assemblies are likely to be rubbish." % (assembly_type, r))

            for tax_name, sequences in taxonomic_rank.iteritems():
                number_of_sequences = len(list(sequences))
                if number_of_sequences > 1:
                    output_assembly_file_path = os.path.join(output_directory, '%s_%s_%s_assembly.fa' % (rank[idx], tax_name, str(number_of_sequences)))
                    output_reads_file_path = os.path.join(output_directory, '%s_%s_%s_reads.fa' % (rank[idx], tax_name, str(number_of_sequences)))
                    velvet_assembly_path = os.path.join(output_directory, '%s_%s_velvet_assembly' % (rank[idx],tax_name))

                    if assembly_type == "phrap":

                        with tempfile.NamedTemporaryFile() as tmp:

                            SeqIO.write(sequences, output_reads_file_path, "fasta")
                            cmd = 'phrap -minscore 40 -minmatch 45 -revise_greedy -forcelevel 0 -repeat_stringency 0.99 %s >/dev/null' % (output_reads_file_path)

                            subprocess.check_call(cmd, shell = True)

                            cmd = 'mv %s.contigs %s' % (output_reads_file_path, output_assembly_file_path)
                            subprocess.check_call(cmd, shell = True)

                    elif assembly_type == "finishm":

                        # Write out the sequences to this file
                        SeqIO.write(sequences, output_reads_file_path, "fasta")


                        # Run finishm visualise on the clustered sequences
                        cmd = 'finishm visualise --quiet --assembly-coverage-cutoff 3.5 --assembly-kmer %s --velvet-directory %s --fasta %s --assembly-svg %s' % (args.kmer, velvet_assembly_path, output_reads_file_path, output_assembly_file_path.replace('.fa', '.svg'))
                        subprocess.check_call(cmd, shell = True)

                        # Move the output picture to the output directory
                        cmd = 'mv *.svg %s' % (output_directory)
                        subprocess.check_call(cmd, shell = True)

                        # Move the clustered sequence files to the output directory
                        cmd = 'mv %s %s' % (output_sequence_file_path.replace('_assembly.fa', ''), output_directory)
                        subprocess.check_call(cmd, shell = True)

                        # Assemble the reads, as best as finishm can
                        cmd = 'finishm assemble --quiet --already-assembled-velvet-directory %s/%s --output-contigs %s --output-pathspec --bubbly --no-progressbar --max-bubble-size 999999999 --post-assembly-coverage-cutoff 10.5' % (output_directory, output_sequence_file_path, output_sequence_file_path.replace('_assembly.fa', '.fa'), )
                        subprocess.check_call(cmd, shell = True)

                        # Move the resulting assembly to the output directory
                        cmd = 'mv %s %s' % (output_sequence_file_path.replace('_assembly.fa', ''), output_directory)
                        subprocess.check_call(cmd, shell = True)

                    elif assembly_type == "velvet":

                        # Write out the sequences to this file
                        SeqIO.write(sequences, output_reads_file_path, "fasta")

                        # Run a velvet assembly
                        cmd = 'velveth %s %s -fasta -short %s 1>/dev/null' % (velvet_assembly_path, args.kmer, output_reads_file_path)
                        subprocess.check_call(cmd, shell = True)
                        cmd = 'velvetg %s -cov_cutoff 3.5 1>/dev/null' % (velvet_assembly_path)
                        subprocess.check_call(cmd, shell = True)



                        if args.finish:

                            if len([x for x in open(os.path.join(velvet_assembly_path, 'contigs.fa'), 'r').readlines() if x.startswith('>')]) > 1:
                                # Finish off fragments
                                cmd = 'phrap -minscore 40 -minmatch 45 -revise_greedy -forcelevel 0 -repeat_stringency 0.99 %s > /dev/null 2>&1' % (os.path.join(velvet_assembly_path, 'contigs.fa'))
                                subprocess.check_call(cmd, shell = True)

                                # Move the resulting assembly to the output directory
                                shutil.move(os.path.join(velvet_assembly_path, 'contigs.fa.contigs'),  output_assembly_file_path)

                            elif len([x for x in open(os.path.join(velvet_assembly_path, 'contigs.fa'), 'r').readlines() if x.startswith('>')]) == 1:
                                # Move the resulting assembly to the output directory
                                shutil.move(os.path.join(velvet_assembly_path, 'contigs.fa'),  output_assembly_file_path)

                            else:
                                pass
                        else:

                            # Move the resulting assembly to the output directory
                            shutil.move(os.path.join(velvet_assembly_path, 'contigs.fa'),  output_assembly_file_path)

        Messenger().message("Finished assembling\n")

