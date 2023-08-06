import math
import itertools

from .utils import (_no_separate_nan_version, aliasing_purepy, get_func,
                    _doc_str, isstr)

        
# min - builtin
# max - builtin
# sum - builtin
# all - builtin
# any - builtin


def _last(x):
    return x[-1]


def _first(x):
    return x[0]


def _array(x):
    return x


def _sort(x):
    return sorted(x)


def _rsort(x):
    return sorted(x, reverse=True)


def _mean(x):
    return sum(x) / len(x)


def _var(x, ddof=0):
    mean = _mean(x)
    return sum((xx - mean) ** 2 for xx in x) / (len(x) - ddof)


def _std(x, ddof=0):
    return math.sqrt(_var(x, ddof=ddof))


def _prod(x):
    r = x[0]
    for xx in x[1:]:
        r *= xx
    return r


def _anynan(x):
    return any(math.isnan(xx) for xx in x)


def _allnan(x):
    return all(math.isnan(xx) for xx in x)


_impl_dict = dict(min=min, max=max, sum=sum, prod=_prod, last=_last,
                  first=_first, all=all, any=any, mean=_mean, std=_std,
                  var=_var, anynan=_anynan, allnan=_allnan, sort=_sort,
                  rsort=_rsort, array=_array)
_impl_dict.update(('nan' + k, v) for k, v in list(_impl_dict.items())
                  if k not in _no_separate_nan_version)


def aggregate(group_idx, a, func='sum', size=None, fill_value=0, order=None,
              dtype=None, **kwargs):
    # Check for 2d group_idx
    if size is None:
        size = 1 + max(group_idx)

    for i in group_idx:
        if isinstance(i, int):
            if i < 0:
                raise ValueError("group_idx contains negative value")
        elif isinstance(i, (list, tuple)):
            raise NotImplementedError("pure python implementation doesn't"
                                      " accept ndim idx input.")
        else:
            try:
                len(i)
            except TypeError:
                raise ValueError("invalid value found in group_idx: %s" % i)
            else:
                raise NotImplementedError("pure python implementation doesn't "
                                          "accept ndim indexed input.")

    if isinstance(a, (int, float)):
        if func not in ("sum", "prod"):
            raise ValueError("scalar inputs are supported only for 'sum' and "
                             "'prod'")
        a = [a] * len(group_idx)
    elif len(group_idx) != len(a):
        raise ValueError("group_idx and a must be of the same length")

    func = get_func(func, aliasing_purepy, _impl_dict)
    if isstr(func):
        if func.startswith('nan'):
            func = func[3:]
            # remove nans
            group_idx, a = zip(*((ix, val) for ix, val in zip(group_idx, a)
                                 if not math.isnan(val)))

        func = _impl_dict[func]

    # sort data and evaluate function on groups
    data = sorted(zip(group_idx, a), key=lambda tp: tp[0])
    ret = [fill_value] * size
    for ix, group in itertools.groupby(data, key=lambda tp: tp[0]):
        ret[ix] = func(tuple(val for _, val in group), **kwargs)

    return ret

aggregate.__doc__ = """
    This is the pure python implementation of aggregate. It is terribly slow.
    Using the numpy version is highly recommended.
    """ + _doc_str
