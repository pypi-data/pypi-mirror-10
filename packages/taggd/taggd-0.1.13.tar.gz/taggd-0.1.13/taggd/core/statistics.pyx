class Statistics(object):
    """
    Shorthand for a statistics object. Not cdef-cythonized so as to keep threading compatible.
    """

    def __init__(self):
        self.total_reads = 0
        self.total_reads_wr = 0
        self.unmatched = 0
        self.perfect_matches = 0
        self.imperfect_unambiguous_matches = 0
        self.imperfect_ambiguous_matches = 0   # Non-unique
        self.edit_distance_counts = 0
