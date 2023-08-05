###############################################################################
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program. If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
###############################################################################

__author__ = 'Donovan Parks'
__copyright__ = 'Copyright 2014'
__credits__ = ['Donovan Parks']
__license__ = 'GPL3'
__maintainer__ = 'Donovan Parks'
__email__ = 'donovan.parks@gmail.com'

import logging
from collections import defaultdict

"""
To do:
 1. There is a serious hack in taxonomic_consistency which should be resolved, but
     requires the viral and plasmid phylogenies to be taxonomically consistent.
"""


class Taxonomy(object):
    """Manipulation of Greengenes-style taxonomy files and strings.

    This class currently assumes a Greengenes-style taxonomy
    string with the following 7 taxonomic ranks:
      d__; c__; o__; f__; g__; s__

    Spaces after the semi-colons are optional.
    """

    rank_prefixes = ('d__', 'p__', 'c__', 'o__', 'f__', 'g__', 's__')
    rank_labels = ('domain', 'phylum', 'class', 'order', 'family', 'genus', 'species')
    rank_index = {'d__': 0, 'p__': 1, 'c__': 2, 'o__': 3, 'f__': 4, 'g__': 5, 's__': 6}

    unclassified_rank = 'unclassified'

    unclassified_taxon = []
    for p in rank_prefixes:
        unclassified_taxon.append(p + unclassified_rank)
    unclassified_taxon = ';'.join(unclassified_taxon)

    def __init__(self):
        """Initialization."""

        self.logger = logging.getLogger()

    def taxa(self, tax_str):
        """Taxa specified by taxonomy string.

        Parameters
        ----------
        tax_str : str
            Greengenes-style taxonomy string.

        Returns
        -------
        list : [<domain>, <phylum>, ..., <species>]
            Rank order list of taxa.
        """

        taxa = [x.strip() for x in tax_str.split(';')]

        return taxa

    def taxa_at_ranks(self, tax_str):
        """Taxon at each taxonomic rank.

        Parameters
        ----------
        tax_str : str
            Greengenes-style taxonomy string.

        Returns
        -------
        dict : d[rank_label] -> taxon
            Taxon at each taxonomic rank.
        """

        taxa = self.taxa(tax_str)

        d = {}
        for rank, taxon in enumerate(taxa):
            d[Taxonomy.rank_labels[rank]] = taxon

    def check_full(self, tax_str):
        """Check if taxonomy string specifies all expected ranks.

        Parameters
        ----------
        tax_str : str
            Greengenes-style taxonomy string.

        Returns
        -------
        boolean
            True if string contains all expected ranks, else False.
        """

        taxa = [x.strip() for x in tax_str.split(';')]
        if len(taxa) != len(Taxonomy.rank_prefixes):
            self.logger.error('[Error] Taxonomy string contains too few ranks:')
            self.logger.error('[Error] %s' % str(taxa))
            return False

        for r, taxon in enumerate(taxa):
            if taxon[0:3] != Taxonomy.rank_prefixes[r]:
                self.logger.error('[Error] Taxon is not prefixed with the expected rank, %s.:' % Taxonomy.rank_prefixes[r])
                self.logger.error('[Error] %s' % str(taxa))
                return False

        return True

    def fill_missing_ranks(self, tax_str):
        """Fill in any missing ranks in a taxonomy string.

        This function assumes the taxonomy string lists
        taxa in proper rank order, but that some ranks
        may be missing.

        Parameters
        ----------
        tax_str : str
            Greengenes-style taxonomy string.

        Returns
        -------
        str
            Taxonomy string with prefixes for all ranks.
        """

        taxa = [x.strip() for x in tax_str.split(';')]

        new_tax = []
        cur_taxa_index = 0
        for rank_prefix in Taxonomy.rank_prefixes:
            if taxa[cur_taxa_index][0:3] == rank_prefix:
                cur_taxa_index.append(taxa[cur_taxa_index])
                cur_taxa_index += 1
            else:
                new_tax.append(rank_prefix)

        return ';'.join(new_tax)

    def taxonomic_consistency(self, taxonomy):
        """Determine taxonomically consistent classification for taxa at each rank.

        Parameters
        ----------
        taxonomy : d[unique_id] -> [d__<taxon>; ...; s__<taxon>]
            Taxonomy strings indexed by unique ids.

        Returns
        -------
        dict : d[taxa] -> expected parent
            Expected parent taxon for taxa at all taxonomic ranks, or
            None if the taxonomy is consistent.
        """

        expected_parent = defaultdict(lambda: dict)
        for genome_id, taxa in taxonomy.iteritems():
            if taxa[0] == 'd__Viruses' or '[P]' in taxa[0]:
                # *** This is a HACK. It would be far better to enforce
                # a taxonomically consistent taxonomy, but
                # the viral taxonomy at IMG is currently not consistent
                continue

            for r in xrange(1, len(taxa)):
                if taxa[r] == Taxonomy.rank_prefixes[r]:
                    break

                if taxa[r] in expected_parent:
                    if taxa[r - 1] != expected_parent[taxa[r]]:
                        self.logger.error('[Error] Provided taxonomy is not taxonomically consistent.')
                        self.logger.error('[Error] Genome %s indicates the parent of %s is %s.' % (genome_id, taxa[r], taxa[r - 1]))
                        self.logger.error('[Error] The parent of this taxa was previously indicated as %s.' % (expected_parent[taxa[r]]))
                        return None

                expected_parent[taxa[r]] = taxa[r - 1]

        return expected_parent

    def validate(self, taxonomy):
        """Check if taxonomy forms a strict hierarhcy.

        Parameters
        ----------
        taxonomy : d[unique_id] -> [d__<taxon>; ...; s__<taxon>]
            Taxonomy strings indexed by unique ids.

        Returns
        -------
        boolean
            True is taxonomy is valid, otherwise False
        """

        for unique_id, taxa in taxonomy.iteritems():
            if len(taxa) != len(Taxonomy.rank_prefixes):
                self.logger.error('[Error] Taxonomy contains too few ranks:')
                self.logger.error('[Error] %s\t%s' % (unique_id, taxa))
                return False

            for r, taxon in enumerate(taxa):
                if taxon[0:3] != Taxonomy.rank_prefixes[r]:
                    self.logger.error('[Error] Taxon is not prefixed with the expected rank, %s.:' % Taxonomy.rank_prefixes[r])
                    self.logger.error('[Error] %s\t%s' % (unique_id, taxon))
                    return False

        if not self.taxonomic_consistency(taxonomy):
            return False

        return True

    def read(self, taxonomy_file):
        """Read Greengenes-style taxonomy file.

        Expected format is:
            <id>\t<taxonomy string>

        where the taxonomy string has the formats:
            d__; c__; o__; f__; g__; s__

        Parameters
        ----------
        taxonomy_file : str
            Greengenes-style taxonomy file.

        Returns
        -------
        dict : d[unique_id] -> [d__<taxon>; ...; s__<taxon>]
            Taxonomy strings indexed by unique ids.
        """

        d = {}
        for line in open(taxonomy_file):
            line_split = line.split('\t')
            unique_id = line_split[0]

            tax_str = line_split[1].rstrip()
            if tax_str[-1] == ';':
                # remove trailing semicolons which sometimes
                # appear in Greengenes-style taxonomy files
                tax_str = tax_str[0:-1]

            d[unique_id] = tax_str.split(';')

        return d

    def write(self, taxonomy, output_file):
        """Write Greengenes-style taxonomy file.

        Parameters
        ----------
        taxonomy : d[unique_id] -> [d__<taxon>; ...; s__<taxon>]
            Taxonomy strings indexed by unique ids.
        output_file : str
            Name of output file.
        """

        fout = open(output_file, 'w')
        for genome_id, taxa in taxonomy.iteritems():
            fout.write(genome_id + '\t' + ';'.join(taxa) + '\n')
        fout.close()
