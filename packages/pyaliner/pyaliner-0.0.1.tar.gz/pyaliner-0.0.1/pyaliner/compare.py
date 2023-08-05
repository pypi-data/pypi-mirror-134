"""
API for rich sequence comparisons
"""
from typing import Tuple, Iterable, Sequence

from pypey import pype, px, Fn

from pyaliner import GAP, JOIN
from pyaliner.align import align, COMPACT, CLASSIC, Seq
from pyaliner.display import rich_paired_in_true_pred, rich_paired_true_pred, in_terminal, rich_inlined_true_pred, FILL

compact_align = px(align, kind=COMPACT)

PAIRED = 'paired'
INLINED = 'inlined'


def compare_in_true_pred_from_file(path: str, alignment: str = COMPACT):
    """
    Visually compares triplets of inputs, ground-truths and predictions in the given file.

    :param path: path to file with a collection of three lines, each an input followed by a ground-truth
        followed by a prediction
    :param alignment: the type of alignment to apply to the triplet
    :return: nothing, but displays comparison in terminal
    """
    compare_in_true_pred(pype.file(path).map(str.strip).select(bool).map(str.split), alignment)


def compare_in_true_pred_from_files(in_path: str, true_path: str, pred_path: str, alignment: str = COMPACT):
    """
    Visually compares triplets of inputs, ground-truths and predictions in the given filse.

    :param in_path: path to file with with a line per input sequence
    :param true_path: path to file with with a line per target sequence
    :param pred_path: path to file with with a line per predicted sequence
    :param alignment: the type of alignment to apply to the triplet
    :return: nothing, but displays comparison in terminal
    """
    in_lines, true_lines, pred_lines = \
        (pype.file(path).map(str.strip).select(bool) for path in [in_path, true_path, pred_path])

    compare_in_true_pred(in_lines.interleave(true_lines).interleave(pred_lines, n=2).map(str.split), alignment)


def compare_true_pred_from_file(path: str, alignment: str, view: str = PAIRED):
    """
    Visually compares pairs of ground-truths and predictions in the given file.

    :param path: path to file with an even number of lines, each being a ground-truth or a prediction, in that order
    :param alignment: the type of alignment to apply to the triplet
    :param view: the view to display in the terminal
    :return: nothing, but displays comparison in terminal
    """
    compare_true_pred(pype.file(path).map(str.strip).select(bool).map(str.split), alignment, view)


def compare_true_pred_from_files(true_path: str, pred_path: str, alignment: str, view: str = PAIRED):
    """
    Visually compares pairs of ground-truths and predictions in the given files.

    :param true_path: path to file with with a line per target sequence
    :param pred_path: path to file with with a line per predicted sequence
    :param alignment: the type of alignment to apply to the triplet
    :param view: the view to display in the terminal
    :return: nothing, but displays comparison in terminal
    """
    true_lines, pred_lines = (pype.file(path).map(str.strip).select(bool) for path in [true_path, pred_path])

    compare_true_pred(true_lines.interleave(pred_lines).map(str.split), alignment, view)


def compare_in_true_pred(triplets: Iterable[Iterable[str]], alignment: str = COMPACT):
    """
    Visually compares triplets of inputs, ground-truths and predictions in the collection.

    :param triplets: collection of three strings, each being an input, a ground-truth or a prediction, in that order
    :param alignment: the type of alignment to apply to the triplet
    :return: nothing, but displays comparison in terminal
    """
    align_fn = align if alignment == CLASSIC else compact_align

    alignments = pype(triplets).chunk(size=3).map(lambda in_seq, true, pred: _3way_align(in_seq, true, pred, align_fn))

    in_terminal(rich_paired_in_true_pred(alignments))


def compare_true_pred(pairs: Iterable[Iterable[str]], alignment: str, view: str = PAIRED):
    """
    Visually compares pairs of ground-truths and predictions in the given file.

    :param pairs: collection of even number of strings, each ground-truth followed by a prediction
    :param alignment: the type of alignment to apply to the triplet
    :param view: the view to display in the terminal
    :return: nothing, but displays comparison in terminal
    """

    alignments = pype(pairs).chunk(size=2).map(compact_align if alignment == COMPACT else align)

    in_terminal(rich_inlined_true_pred(alignments) if view == INLINED else rich_paired_true_pred(alignments))


def _3way_align(in_seq: Sequence[str], true: Sequence[str], pred: Sequence[str], align_fn: Fn) -> Tuple[Seq, Seq, Seq]:
    # TODO THIS IS A SLOW HEURISTIC METHOD, NEEDS REPLACING WITH MORE PERFORMANT BETTER THOUGHT-THROUGH ALGORITHM

    true_ali, pred_ali = align_fn(true, pred)

    input_ali, true_ali = align_fn(in_seq, true_ali)
    input_ali, pred_ali = align_fn(input_ali, pred_ali)

    if len(input_ali) != len(true_ali) or len(true_ali) != len(pred_ali):
        true_ali, pred_ali = align_fn(true_ali, pred_ali)

        input_ali, true_ali = align_fn(input_ali, true_ali)
        input_ali, pred_ali = align_fn(input_ali, pred_ali)

    if len(input_ali) != len(true_ali) or len(true_ali) != len(pred_ali):
        true_ali, pred_ali = align_fn(true_ali, pred_ali)

        input_ali, true_ali = align_fn(input_ali, true_ali)
        input_ali, pred_ali = align_fn(input_ali, pred_ali)

    return (pype([input_ali, true_ali, pred_ali])
            .zip(trunc=False, pad=FILL)
            .reject(lambda _in, true, pred: _in == GAP and true == GAP and pred == GAP)
            .map(lambda _in, true, pred: (_in.strip(GAP + JOIN) if len(_in) > 2 else _in, true, pred))
            .unzip()
            .map(tuple)
            .to(tuple))
