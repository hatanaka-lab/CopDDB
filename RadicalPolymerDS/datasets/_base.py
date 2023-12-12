from ..utils import Bunch


def load_testset(*, N=10):
    data = list(range(N))
    target = list(range(N))
    return Bunch(
        data=data,
        target=target
    )
