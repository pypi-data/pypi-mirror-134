from tshistory.api import timeseries as basetimeseries

from tshistory_refinery import helper, http


def timeseries(uri):
    if uri.startswith('postgres'):
        return helper.apimaker(helper.config())

    assert uri.startswith('http')

    return http.RefineryClient(uri)
